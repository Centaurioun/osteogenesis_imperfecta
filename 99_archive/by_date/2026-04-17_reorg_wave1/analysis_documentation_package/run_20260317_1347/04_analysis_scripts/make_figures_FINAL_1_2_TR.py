#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import zipfile
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

SEED = 20260228
np.random.seed(SEED)

REQ_FILES = {
    "t1": "publication_table1_overall_FINAL.csv",
    "t2": "publication_table2_by_gene_group_FINAL.csv",
    "t3": "publication_table3_inferential_FINAL.csv",
    "rob": "robustness_panel_FINAL.csv",
    "cv": "cv_panel_FINAL.csv",
}

PRIMARY_ENDPOINTS = [
    "doku_anomalisi_var_rt",
    "gingivitis",
    "caries_any_rt",
    "caries_count",
]
BINARY_ENDPOINTS = ["doku_anomalisi_var_rt", "gingivitis", "caries_any_rt"]

EP_TR = {
    "doku_anomalisi_var_rt": "Doku anomalisi",
    "gingivitis": "Gingivit",
    "caries_any_rt": "Çürük varlığı",
    "caries_count": "Çürük sayısı",
}

METHOD_TR = {"LOO": "LOO", "RSKF": "RSKF"}
GENE_TR = {"Other": "Diğer"}

def fail(msg: str):
    raise RuntimeError(msg)

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def read_csv_from_zip(zf: zipfile.ZipFile, name: str) -> pd.DataFrame:
    with zf.open(name) as f:
        return pd.read_csv(f)

def read_csv_from_dir(input_dir: str, name: str) -> pd.DataFrame:
    return pd.read_csv(os.path.join(input_dir, name))

def load_required_tables(input_path: str):
    if os.path.isdir(input_path):
        for value in REQ_FILES.values():
            if not os.path.exists(os.path.join(input_path, value)):
                fail(f"Klasörde eksik dosya: {value}")
        return (
            read_csv_from_dir(input_path, REQ_FILES["t1"]),
            read_csv_from_dir(input_path, REQ_FILES["t2"]),
            read_csv_from_dir(input_path, REQ_FILES["t3"]),
            read_csv_from_dir(input_path, REQ_FILES["rob"]),
            read_csv_from_dir(input_path, REQ_FILES["cv"]),
        )

    if zipfile.is_zipfile(input_path):
        with zipfile.ZipFile(input_path) as zf:
            names = set(zf.namelist())
            for value in REQ_FILES.values():
                if value not in names:
                    fail(f"Zip içinde eksik dosya: {value}")
            return (
                read_csv_from_zip(zf, REQ_FILES["t1"]),
                read_csv_from_zip(zf, REQ_FILES["t2"]),
                read_csv_from_zip(zf, REQ_FILES["t3"]),
                read_csv_from_zip(zf, REQ_FILES["rob"]),
                read_csv_from_zip(zf, REQ_FILES["cv"]),
            )

    fail("Girdi, FINAL CSV dosyalarını içeren bir klasör veya geçerli bir zip arşivi olmalıdır.")

def setup_matplotlib():
    plt.rcParams.update({
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.titlesize": 12,
        "axes.labelsize": 10,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "legend.fontsize": 9,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    })

# ✅ Artık figürlere FINAL.1.2 etiketi BASMIYORUZ.
# (İstersen ileride tekrar isterseniz, bu fonksiyonu geri koyabiliriz.)
def add_tag(_tag: str):
    return

def parse_n_pct(value_str: str):
    s = str(value_str).strip()
    if "(" not in s or "%" not in s:
        fail(f"Beklenmeyen n(%) formatı: {s}")
    n_part = s.split("(")[0].strip()
    pct_part = s.split("(")[1].split("%")[0].strip()
    n = int(float(n_part))
    pct = float(pct_part)
    return n, pct

def parse_ci(ci_str: str):
    s = str(ci_str).strip().rstrip(",")
    if s in {"-", "", "nan", "NaN"}:
        return np.nan, np.nan
    parts = [p.strip().rstrip(",") for p in s.split(",") if p.strip()]
    if len(parts) != 2:
        fail(f"Beklenmeyen CI formatı: {ci_str}")
    return float(parts[0]), float(parts[1])

def qc_tables(t1: pd.DataFrame, t2: pd.DataFrame, t3: pd.DataFrame, rob: pd.DataFrame, cv: pd.DataFrame):
    for df, cols, name in [
        (t1, {"Variable", "Value", "95% CI (Wilson)"}, "Table1"),
        (t2, {"scenario", "gene_group", "N"}, "Table2"),
        (t3, {"scenario", "endpoint", "p_classic", "p_permutation", "effect_size_value",
              "epsilon2_primary", "epsilon2_alt", "p_holm_primary_family_classic", "p_holm_binary_family_perm"}, "Table3"),
        (rob, {"scenario", "endpoint", "p_base", "loo_p_min", "loo_p_max",
               "infra_exclusion_p", "infra_exclusion_delta_p"}, "Robustness"),
        (cv, {"scenario", "endpoint", "cv_method", "delta_auc", "delta_auc_ci_low", "delta_auc_ci_high"}, "CV"),
    ]:
        missing = cols - set(df.columns)
        if missing:
            fail(f"{name}: Eksik kolonlar: {sorted(missing)}")

    n_row = t1[t1["Variable"].astype(str).str.strip().eq("N")]
    if n_row.empty:
        fail("Table1: N satırı bulunamadı")
    if str(n_row.iloc[0]["Value"]).strip() != "34":
        fail(f"Table1: Beklenen N=34, bulunan={n_row.iloc[0]['Value']}")

    t3p = t3[t3["scenario"].eq("Primary")]
    if set(t3p["endpoint"]) != set(PRIMARY_ENDPOINTS):
        fail(f"Table3: Primary endpoint seti uyuşmuyor: {sorted(t3p['endpoint'].tolist())}")

    robp = rob[rob["scenario"].eq("Primary")]
    if set(robp["endpoint"]) != set(PRIMARY_ENDPOINTS):
        fail("Robustness: Primary endpoint seti uyuşmuyor")

    cvp = cv[cv["scenario"].eq("Primary")]
    if set(cvp["endpoint"]) != set(BINARY_ENDPOINTS):
        fail("CV: Primary binary endpoint seti uyuşmuyor")
    if not set(["LOO", "RSKF"]).issubset(set(cvp["cv_method"].unique())):
        fail("CV: Hem LOO hem RSKF bulunmalı (Primary)")
    if len(cvp) < 6:
        fail(f"CV: Primary satır sayısı beklenenden az. Satır={len(cvp)}")

# ✅ Yayın-hazır n etiketi: büyük barlarda içeri, küçük barlarda üste + beyaz bbox
def annotate_n(ax, x, height, n, inside_threshold=12):
    n = int(n)
    if height >= inside_threshold:
        y = height - 2.5
        va = "top"
    else:
        y = height + 2.0
        va = "bottom"

    ax.text(
        x, y, f"n={n}",
        ha="center", va=va, fontsize=9,
        bbox=dict(boxstyle="round,pad=0.20", facecolor="white", edgecolor="none", alpha=0.85)
    )

def figA_prevalans(t1: pd.DataFrame, outdir: str):
    rows = ["doku_anomalisi_var_rt", "gingivitis", "caries_any_rt", "Infraokluzyon (Total N)"]
    df = t1.set_index("Variable").loc[rows].reset_index()

    df[["n", "pct"]] = df["Value"].apply(lambda x: pd.Series(parse_n_pct(x)))
    df[["ci_l", "ci_h"]] = df["95% CI (Wilson)"].apply(lambda x: pd.Series(parse_ci(x)))

    labels = ["Doku anomalisi", "Gingivit", "Çürük varlığı", "İnfraoklüzyon"]
    x = np.arange(len(labels))
    y = df["pct"].values
    yerr = np.vstack([y - df["ci_l"].values, df["ci_h"].values - y])

    plt.figure(figsize=(7.2, 3.8))
    plt.title("Prevalans (Wilson %95 Güven Aralığı)")
    ax = plt.gca()
    bars = ax.bar(x, y)
    ax.errorbar(x, y, yerr=yerr, fmt="none", capsize=4)

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Prevalans (%)")
    ax.set_ylim(0, 100)

    for i, b in enumerate(bars):
        annotate_n(ax, b.get_x() + b.get_width()/2, b.get_height(), df["n"].iloc[i])

    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "FigA_prevalans_TR.png"))
    plt.close()

def figB_gen_grup(t2: pd.DataFrame, outdir: str):
    df = t2[t2["scenario"].eq("Primary")].copy()
    if df.empty:
        fail("Table2: Primary senaryo yok")

    df["gene_group_tr"] = df["gene_group"].apply(lambda g: GENE_TR.get(str(g), str(g)))
    df["N"] = df["N"].astype(int)
    df = df.sort_values("N", ascending=False)

    plt.figure(figsize=(7.2, 3.6))
    plt.title("Gen grubu dağılımı (Primary)")
    ax = plt.gca()
    bars = ax.bar(df["gene_group_tr"], df["N"])
    ax.set_xlabel("Gen grubu")
    ax.set_ylabel("N")

    # Daha temiz: barın hemen üstü + bbox
    for b in bars:
        h = b.get_height()
        ax.text(
            b.get_x() + b.get_width()/2, h + 0.15, f"{int(h)}",
            ha="center", va="bottom", fontsize=9,
            bbox=dict(boxstyle="round,pad=0.18", facecolor="white", edgecolor="none", alpha=0.85)
        )

    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "FigB_gen_grup_TR.png"))
    plt.close()

def figC_inferans_ozet(t3: pd.DataFrame, outdir: str):
    df = t3[t3["scenario"].eq("Primary")].set_index("endpoint").loc[PRIMARY_ENDPOINTS].reset_index()

    eff = []
    p_show = []
    holm_show = []
    names = []
    for _, r in df.iterrows():
        ep = r["endpoint"]
        names.append(EP_TR.get(ep, ep))

        if ep == "caries_count":
            eff.append(float(r["epsilon2_primary"]))
            p_show.append(float(r["p_classic"]))
            holm_show.append(float(r["p_holm_primary_family_classic"]))
        else:
            eff.append(float(r["effect_size_value"]))
            p_show.append(float(r["p_permutation"]))
            holm_show.append(float(r["p_holm_binary_family_perm"]))

    y = np.arange(len(names))
    x = np.array(eff, dtype=float)

    plt.figure(figsize=(7.6, 3.8))
    plt.title("İnferans özeti (Primary)")
    ax = plt.gca()
    ax.scatter(x, y)
    ax.set_yticks(y)
    ax.set_yticklabels(names)
    ax.set_xlabel("Etki büyüklüğü (V veya ε²)")
    ax.axvline(0, linewidth=1)

    for i in range(len(names)):
        if df.iloc[i]["endpoint"] == "caries_count":
            txt = f"p={p_show[i]:.3f} | Holm={holm_show[i]:.3f}"
        else:
            txt = f"p_perm={p_show[i]:.3f} | Holm={holm_show[i]:.3f}"
        ax.text(x[i] + 0.01, y[i], txt, va="center", fontsize=8)

    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "FigC_inferans_ozet_TR.png"))
    plt.close()

def figE_robustluk(rob: pd.DataFrame, outdir: str):
    df = rob[rob["scenario"].eq("Primary")].set_index("endpoint").loc[PRIMARY_ENDPOINTS].reset_index()

    names = [EP_TR.get(ep, ep) for ep in df["endpoint"].tolist()]
    y = np.arange(len(names))

    plt.figure(figsize=(8.0, 3.8))
    plt.title("Sağlamlık: LOO p aralığı ve infra hariç Δp")
    ax = plt.gca()

    ax.hlines(y, df["loo_p_min"].values, df["loo_p_max"].values)
    ax.scatter(df["p_base"].values, y, label="Baz p")
    ax.scatter(df["infra_exclusion_p"].values, y, marker="x", label="İnfra hariç p")

    for i in range(len(names)):
        dp = float(df["infra_exclusion_delta_p"].iloc[i])
        ax.text(float(df["loo_p_max"].iloc[i]) + 0.01, y[i], f"Δp_infra={dp:.3f}", va="center", fontsize=8)

    ax.set_yticks(y)
    ax.set_yticklabels(names)
    ax.set_xlabel("p-değeri")
    ax.set_xlim(0, 1)
    ax.legend(loc="lower right")

    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "FigE_robustluk_TR.png"))
    plt.close()

def figF_cv_delta_auc(cv: pd.DataFrame, outdir: str):
    df = cv[cv["scenario"].eq("Primary")].copy()

    order = ["doku_anomalisi_var_rt", "gingivitis", "caries_any_rt"]
    ytick = []
    y = []
    x = []
    lo_list = []
    hi_list = []

    # Üstte LOO olsun istiyorsan sırayı ['LOO','RSKF'] yap.
    for i, ep in enumerate(order):
        for j, meth in enumerate(["LOO", "RSKF"]):
            r = df[(df["endpoint"] == ep) & (df["cv_method"] == meth)]
            if r.empty:
                fail(f"CV: eksik satır: {ep} / {meth}")
            r = r.iloc[0]

            yi = i * 2 + j
            y.append(yi)
            ytick.append(f"{EP_TR.get(ep, ep)} — {METHOD_TR.get(meth, meth)}")

            xi = float(r["delta_auc"])
            lo = float(r["delta_auc_ci_low"])
            hi = float(r["delta_auc_ci_high"])
            lo, hi = (lo, hi) if lo <= hi else (hi, lo)

            x.append(xi); lo_list.append(lo); hi_list.append(hi)

    y = np.array(y)
    x = np.array(x)
    lo_list = np.array(lo_list)
    hi_list = np.array(hi_list)

    plt.figure(figsize=(8.2, 4.2))
    plt.title("Model doğrulama: ΔAUC ve %95 Güven Aralığı (Primary)")
    ax = plt.gca()

    cap = 0.12
    for yi, lo, hi in zip(y, lo_list, hi_list):
        ax.hlines(yi, lo, hi)
        ax.vlines([lo, hi], yi - cap, yi + cap)

    ax.scatter(x, y)
    ax.axvline(0, linewidth=1)
    ax.set_yticks(y)
    ax.set_yticklabels(ytick)
    ax.set_xlabel("ΔAUC (yaş+gen − yaş)")

    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "FigF_cv_delta_auc_TR.png"))
    plt.close()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="FINAL CSV dosyalarını içeren klasör yolu veya outputs_FINAL_1_2.zip yolu")
    ap.add_argument("--out", required=True, help="Figür çıkış klasörü")
    args = ap.parse_args()

    setup_matplotlib()
    ensure_dir(args.out)

    t1, t2, t3, rob, cv = load_required_tables(args.input)

    qc_tables(t1, t2, t3, rob, cv)

    figA_prevalans(t1, args.out)
    figB_gen_grup(t2, args.out)
    figC_inferans_ozet(t3, args.out)
    figE_robustluk(rob, args.out)
    figF_cv_delta_auc(cv, args.out)

    print("OK — Türkçe figürler üretildi (PNG).")

if __name__ == "__main__":
    main()
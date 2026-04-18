"""
Round 2 rule-constrained reruns for A03-A11.

Purpose:
    Perform real numerical reruns for A03-A11 endpoints under project-valid rules,
    instead of editorial-only supplementary labeling.

Inputs:
    - osteogenesis_imperfecta_camber_input_minimal_v1.csv (runtime-consistent gene groups / IDs)
    - archive/osteogenesis_imperfecta_original_data.csv (binary dental/ortho endpoints)

Outputs:
    - reanalysis_statistician_vs_project/09_round2_outputs/rule_constrained_rerun_A03_A11.csv

Notes:
    - Small-sample approach: chi-square + permutation p-value (10k) and Cramer's V.
    - Fixed seed for reproducibility (20260228).
"""

from __future__ import annotations

from pathlib import Path
import numpy as np
import pandas as pd
import scipy.stats as stats
from statsmodels.stats.multitest import multipletests

SEED = 20260228
N_PERM = 10000


def _project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _find_col(columns: list[str], candidates: list[str]) -> str:
    colset = {c.strip().upper(): c for c in columns}
    for cand in candidates:
        key = cand.strip().upper()
        if key in colset:
            return colset[key]
    raise KeyError(f"Column not found. Candidates: {candidates}")


def _cramers_v(chi2: float, n: int, r: int, c: int) -> float:
    if n <= 0:
        return float("nan")
    min_dim = min(r - 1, c - 1)
    if min_dim <= 0:
        return float("nan")
    return float(np.sqrt(chi2 / (n * min_dim)))


def _perm_pvalue(ct: pd.DataFrame, iters: int = N_PERM, seed: int = SEED) -> float:
    rng = np.random.default_rng(seed)
    chi2_obs = stats.chi2_contingency(ct, correction=False)[0]
    row_sums = ct.sum(axis=1).to_numpy(dtype=int)
    col_sums = ct.sum(axis=0).to_numpy(dtype=int)
    n = int(ct.to_numpy().sum())
    r_dim = len(row_sums)
    c_dim = len(col_sums)

    expected = np.outer(row_sums, col_sums) / n
    expected[expected == 0] = 1.0

    rows = np.repeat(np.arange(r_dim), row_sums)
    cols_template = np.repeat(np.arange(c_dim), col_sums)

    gte = 0
    for _ in range(iters):
        cols = rng.permutation(cols_template)
        flat_idx = rows * c_dim + cols
        perm_flat = np.bincount(flat_idx, minlength=r_dim * c_dim)
        perm = perm_flat.reshape((r_dim, c_dim))
        chi2_perm = np.sum((perm - expected) ** 2 / expected)
        if chi2_perm >= chi2_obs - 1e-12:
            gte += 1
    return gte / iters


def main() -> None:
    root = _project_root()
    minimal_fp = root / "osteogenesis_imperfecta_camber_input_minimal_v1.csv"
    original_fp = root / "archive" / "osteogenesis_imperfecta_original_data.csv"

    out_dir = root / "reanalysis_statistician_vs_project" / "09_round2_outputs"
    out_dir.mkdir(parents=True, exist_ok=True)

    minimal = pd.read_csv(minimal_fp)
    original = pd.read_csv(original_fp)

    id_min = _find_col(list(minimal.columns), ["hasta_kodu"])
    id_org = _find_col(list(original.columns), ["HASTA KODU", "HASTA_KODU", "HASTA KODU "])

    grp_col = _find_col(list(minimal.columns), ["gen_group"])  # runtime-consistent grouping

    endpoint_map = [
        ("A03", "OPEN BITE", "open_bite_rt"),
        ("A04", "CROSSBITE", "cross_bite_rt"),
        ("A05", "OVERBITE", "over_bite_rt"),
        ("A06", "TRANSPOZİSYON", "transpozisyon_rt"),
        ("A07", "DİŞ EKSİKLİĞİ", "dis_eksikligi_rt"),
        ("A08", "GÖMÜLÜ", "gomulu_dis_rt"),
        ("A09", "ARTI DİŞ", "arti_dis_rt"),
        ("A10", "TAURODONTİZM", "taurodontizm_rt"),
        ("A11", "KÖK ANOMALİSİ", "kok_anomalisi_rt"),
    ]

    records = []
    raw_ps = []

    for analysis_id, raw_name, endpoint in endpoint_map:
        raw_col = _find_col(list(original.columns), [raw_name, raw_name.replace("İ", "I")])

        sub_min = minimal[[id_min, grp_col]].copy()
        sub_org = original[[id_org, raw_col]].copy()
        sub_min[id_min] = pd.to_numeric(sub_min[id_min], errors="coerce")
        sub_org[id_org] = pd.to_numeric(sub_org[id_org], errors="coerce")

        merged = sub_min.merge(sub_org, left_on=id_min, right_on=id_org, how="inner")
        merged = merged.dropna(subset=[grp_col, raw_col])

        # Binary-only rule: any non-zero treated as presence.
        merged[endpoint] = (pd.to_numeric(merged[raw_col], errors="coerce").fillna(0) > 0).astype(int)

        usable_n = int(len(merged))

        ct = pd.crosstab(merged[grp_col], merged[endpoint])

        if ct.shape[0] < 2 or ct.shape[1] < 2:
            p_perm = float("nan")
            p_classic = float("nan")
            cramerv = float("nan")
            expected_min = float("nan")
            test_used = "Insufficient variability"
        else:
            chi2, p_classic, _, expected = stats.chi2_contingency(ct, correction=False)
            p_perm = _perm_pvalue(ct, iters=N_PERM, seed=SEED)
            cramerv = _cramers_v(chi2, int(ct.to_numpy().sum()), ct.shape[0], ct.shape[1])
            expected_min = float(np.min(expected))
            test_used = "Chi2_with_permutation_validation"

        raw_ps.append(p_perm)

        records.append(
            {
                "analysis_id": analysis_id,
                "endpoint": endpoint,
                "usable_n": usable_n,
                "coding_rule_used": "binary var/yok; runtime gene_group; small-sample permutation",
                "test_used": test_used,
                "p_value": p_perm,
                "effect_size": cramerv,
                "p_classic": p_classic,
                "expected_min": expected_min,
                "manuscript_status_recommendation": "supplementary-only",
                "why_not_primary_if_applicable": "Outside predefined primary inferential family; retained as secondary rerun for numerical support.",
            }
        )

    # Holm correction across A03-A11 reruns.
    p_series = pd.Series(raw_ps, dtype=float)
    valid_mask = p_series.notna()
    holm = np.full(len(records), np.nan)
    if valid_mask.any():
        _, p_holm, _, _ = multipletests(p_series[valid_mask].to_numpy(), method="holm")
        holm[np.where(valid_mask)[0]] = p_holm

    for i, rec in enumerate(records):
        rec["p_holm_round2_family"] = holm[i]
        if pd.notna(holm[i]) and holm[i] < 0.05:
            rec["manuscript_status_recommendation"] = "exploratory signal (supplement-first)"
            rec["why_not_primary_if_applicable"] = "Numerically notable but outside predefined primary inferential family and requires cautious secondary framing."
        elif pd.notna(rec["p_value"]) and rec["p_value"] < 0.10:
            rec["manuscript_status_recommendation"] = "supplementary-only (weak-signal)"

    out_df = pd.DataFrame(records)
    out_df.to_csv(out_dir / "rule_constrained_rerun_A03_A11.csv", index=False)


if __name__ == "__main__":
    main()

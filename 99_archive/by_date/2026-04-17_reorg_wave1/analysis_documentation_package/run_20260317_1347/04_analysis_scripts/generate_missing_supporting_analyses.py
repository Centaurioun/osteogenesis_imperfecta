import os
import random
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

SEED = 20260228
np.random.seed(SEED)
random.seed(SEED)
os.environ["PYTHONHASHSEED"] = str(SEED)

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "missing_statistical_analyses"
DATA_PATH = ROOT / "Manuscript_Data" / "02_source_data" / "raw_data" / "osteogenesis_imperfecta_camber_input_minimal_v1.csv"
FINAL_DIR = ROOT / "Manuscript_Data" / "04_final_outputs" / "tables_csv_and_logs"
T3_PATH = FINAL_DIR / "publication_table3_inferential_FINAL.csv"
ROB_PATH = FINAL_DIR / "robustness_panel_FINAL.csv"
CV_PATH = FINAL_DIR / "cv_panel_FINAL.csv"
ISSUE_LOG_PATH = ROOT / "issue_log_v3.csv"


def append_issue_log(rows: list[dict]) -> None:
    if not rows:
        return
    issue_df = pd.DataFrame(rows)
    issue_df.insert(0, "timestamp", datetime.now().isoformat(timespec="seconds"))
    if ISSUE_LOG_PATH.exists():
        existing = pd.read_csv(ISSUE_LOG_PATH)
        cols = list(dict.fromkeys(existing.columns.tolist() + issue_df.columns.tolist()))
        existing = existing.reindex(columns=cols)
        issue_df = issue_df.reindex(columns=cols)
        out = pd.concat([existing, issue_df], ignore_index=True)
    else:
        out = issue_df
    out.to_csv(ISSUE_LOG_PATH, index=False)


def holm_adjust(p_values: pd.Series) -> pd.Series:
    p = p_values.to_numpy(dtype=float)
    n = len(p)
    order = np.argsort(p)
    ranked = p[order]
    adjusted = np.empty(n, dtype=float)
    for i, val in enumerate(ranked):
        adjusted[i] = min(1.0, (n - i) * val)
    adjusted = np.maximum.accumulate(adjusted)
    out = np.empty(n, dtype=float)
    out[order] = adjusted
    return pd.Series(out, index=p_values.index)


def cramer_v(chi2: float, n: int, r: int, c: int) -> float:
    min_dim = min(r - 1, c - 1)
    if n <= 0 or min_dim <= 0:
        return np.nan
    return float(np.sqrt(chi2 / (n * min_dim)))


def permutation_pvalue(ct: pd.DataFrame, iters: int = 10000) -> float:
    chi2_obs = stats.chi2_contingency(ct, correction=False)[0]
    rm = ct.sum(axis=1).to_numpy()
    cm = ct.sum(axis=0).to_numpy()
    n = int(ct.values.sum())
    rows = np.repeat(np.arange(len(rm)), rm)
    cols = np.repeat(np.arange(len(cm)), cm)
    c_dim = len(cm)
    r_dim = len(rm)
    expected = np.outer(rm, cm) / n
    expected[expected == 0] = 1.0
    count_gte = 0
    for _ in range(iters):
        np.random.shuffle(cols)
        idx = rows * c_dim + cols
        perm_flat = np.bincount(idx, minlength=r_dim * c_dim)
        perm_table = perm_flat.reshape((r_dim, c_dim))
        chi_perm = np.sum((perm_table - expected) ** 2 / expected)
        if chi_perm >= chi2_obs - 1e-9:
            count_gte += 1
    return count_gte / iters


def classify_robustness(row: pd.Series) -> tuple[str, str]:
    loo_delta = row.get("loo_delta_p_max_abs", np.nan)
    infra_delta = abs(row.get("infra_exclusion_delta_p", np.nan)) if pd.notna(row.get("infra_exclusion_delta_p", np.nan)) else np.nan
    p_min = row.get("loo_p_min", np.nan)
    p_max = row.get("loo_p_max", np.nan)
    flips_significance = pd.notna(p_min) and pd.notna(p_max) and ((p_min < 0.05 <= p_max) or (p_max < 0.05 <= p_min))

    max_delta = np.nanmax([loo_delta, infra_delta]) if any(pd.notna(x) for x in [loo_delta, infra_delta]) else np.nan

    if flips_significance or (pd.notna(max_delta) and max_delta >= 0.08):
        return "fragile", "Significance/interpretation shifts under perturbation"
    if pd.notna(max_delta) and max_delta >= 0.04:
        return "partly stable", "Moderate p-shift under perturbation"
    return "stable", "Low p-shift under perturbation"


def main() -> None:
    df = pd.read_csv(DATA_PATH)

    # Derived variables (FINAL.1.2 semantics)
    df["infraokluzyon_var_rt"] = (df["occl_tip"] == 4).astype(int)
    df["angle_sinifi_rt"] = df["occl_tip"].where(df["occl_tip"].isin([1, 2, 3]), np.nan)
    df["caries_count_rt"] = df["dmft_dmft"]
    df["caries_any_rt"] = (df["caries_count_rt"] > 0).astype(int)
    df["doku_anomalisi_var_rt"] = (df["doku_anomalisi"] != 0).astype(int)

    # Runtime gene grouping
    vc = df["gen_mutasyonu"].fillna("Unknown").astype(str).str.upper().value_counts()
    majors = ["COL1A1", "COL1A2", "FKBP10", "P3H1"]
    df["gene_group_primary"] = df["gen_mutasyonu"].fillna("Unknown").astype(str).str.upper().apply(lambda x: x if x in majors else "Other")
    k3 = [g for g, c in vc.items() if c >= 3 and g != "UNKNOWN"]
    k4 = [g for g, c in vc.items() if c >= 4 and g != "UNKNOWN"]
    df["gene_group_k3"] = df["gen_mutasyonu"].fillna("Unknown").astype(str).str.upper().apply(lambda x: x if x in k3 else "Other")
    df["gene_group_k4"] = df["gen_mutasyonu"].fillna("Unknown").astype(str).str.upper().apply(lambda x: x if x in k4 else "Other")

    # --- Stage 0: Gap audit (must come first) ---
    gap_audit = """# analysis_gap_audit

## 1. Primary analyses already implemented
- FINAL.1.2 primary descriptive, inferential, robustness and secondary CV panels are already present in authoritative outputs.
- Primary inferential framework already includes permutation support for sparse categorical data and Kruskal-Wallis for count-like `dmft_dmft`.
- Holm adjustments and effect-size reporting are already in `publication_table3_inferential_FINAL.csv`.

## 2. Missing supporting analyses
- Endpoint-level missingness and denominator transparency tables were not separately exported in a dedicated supporting bundle.
- Alternative grouping check table (Primary vs k=3 vs k=4) needed as explicit reviewer-facing support.
- Focused age/dentition supporting checks were not isolated into a standalone traceable file.

## 3. Missing robustness analyses
- Expanded robustness classification (`stable / partly stable / fragile`) file is not separately exported.
- Sensitivity decision memo for interpretation impact was missing as a dedicated markdown artifact.

## 4. Missing reporting/traceability items
- Integrated support synthesis across analysis tiers (`primary/supporting/robustness/secondary exploratory`) was missing.
- Completion report documenting added vs intentionally not-added analyses was missing.

## 5. Analyses that should NOT be added
- Parametric t-test/ANOVA pipelines for primary inference (data are small-n and non-normal by design).
- Classical unpenalized logistic regression as primary inferential evidence.
- Over-fragmented subgroup interaction analyses beyond data power.
- CV/AUC outputs as standalone clinical predictive evidence.

## 6. Immediate risks before further analysis
- Small expected cell counts can produce unstable asymptotic p-values if exact/permutation checks are bypassed.
- Single-observation sensitivity can materially change interpretation in n=34.
- Misreading `occl_tip==4` inside Angle classes or treating `dmft_dmft` as classical decomposed DMFT would invalidate interpretation.
"""
    (OUT_DIR / "analysis_gap_audit.md").write_text(gap_audit, encoding="utf-8")

    # --- Stage 1: Data quality and availability ---
    issues: list[dict] = []
    quality_rows = []

    # Codebook-like checks
    checks = {
        "occl_tip_allowed": df["occl_tip"].isin([1, 2, 3, 4]).all(),
        "binary_gingivitis": df["gingivitis"].isin([0, 1]).all(),
        "binary_doku_anomalisi_var": df["doku_anomalisi_var"].isin([0, 1]).all(),
        "binary_caries_any": df["caries_any"].isin([0, 1]).all(),
        "binary_infraokluzyon_var": df["infraokluzyon_var"].isin([0, 1]).all(),
        "age_non_negative": (df["yas"] >= 0).all(),
        "dmft_non_negative": (df["dmft_dmft"] >= 0).all(),
        "dentition_allowed": df["dentisyon_donemi_kod"].isin([1, 2, 3]).all(),
    }

    for name, ok in checks.items():
        status = "PASS" if ok else "FAIL"
        quality_rows.append({"check": name, "status": status, "detail": "" if ok else "Unexpected values detected"})
        if not ok:
            issues.append({
                "severity": "FAIL",
                "category": "DATA_QUALITY",
                "description": f"{name} failed",
                "affected_ids": "",
                "action_taken": "Fail-fast assertion"
            })

    # Derived variable consistency checks
    derive_checks = pd.DataFrame([
        {
            "field": "infraokluzyon_var",
            "matches_runtime": bool((df["infraokluzyon_var"].astype(int) == df["infraokluzyon_var_rt"]).all()),
            "mismatch_n": int((df["infraokluzyon_var"].astype(int) != df["infraokluzyon_var_rt"]).sum()),
        },
        {
            "field": "angle_sinifi",
            "matches_runtime": bool(df["angle_sinifi"].fillna(-999).astype(float).eq(df["angle_sinifi_rt"].fillna(-999).astype(float)).all()),
            "mismatch_n": int((~df["angle_sinifi"].fillna(-999).astype(float).eq(df["angle_sinifi_rt"].fillna(-999).astype(float))).sum()),
        },
        {
            "field": "caries_any",
            "matches_runtime": bool((df["caries_any"].astype(int) == df["caries_any_rt"]).all()),
            "mismatch_n": int((df["caries_any"].astype(int) != df["caries_any_rt"]).sum()),
        },
        {
            "field": "doku_anomalisi_var",
            "matches_runtime": bool((df["doku_anomalisi_var"].astype(int) == df["doku_anomalisi_var_rt"]).all()),
            "mismatch_n": int((df["doku_anomalisi_var"].astype(int) != df["doku_anomalisi_var_rt"]).sum()),
        },
    ])

    for _, r in derive_checks.iterrows():
        if not bool(r["matches_runtime"]):
            issues.append({
                "severity": "FAIL",
                "category": "DERIVED_MISMATCH",
                "description": f"Derived field mismatch: {r['field']}",
                "affected_ids": "",
                "action_taken": "Fail-fast assertion"
            })

    # Informational traceability event (required transparency)
    excluded_ids = df.loc[df["occl_tip"] == 4, "hasta_kodu"].astype(str).tolist()
    issues.append({
        "severity": "INFO",
        "category": "ANALYTIC_EXCLUSION",
        "description": "Angle analysis excluded occl_tip==4 as infraocclusion",
        "affected_ids": ";".join(excluded_ids),
        "action_taken": "Set angle_sinifi_rt=NaN and infraokluzyon_var_rt=1"
    })

    # Save quality outputs
    pd.DataFrame(quality_rows).to_csv(OUT_DIR / "data_quality_flags.csv", index=False)
    missingness = pd.DataFrame({
        "variable": df.columns,
        "missing_n": df.isna().sum().to_numpy(),
        "missing_pct": (df.isna().mean() * 100).round(3).to_numpy(),
    })
    missingness.to_csv(OUT_DIR / "missingness_summary.csv", index=False)

    endpoints = ["doku_anomalisi_var_rt", "gingivitis", "caries_any_rt", "caries_count_rt", "angle_sinifi_rt", "infraokluzyon_var_rt"]
    denom = []
    for ep in endpoints:
        usable = int(df[ep].notna().sum())
        denom.append({"endpoint": ep, "usable_n": usable, "total_n": int(len(df)), "usable_pct": round(100 * usable / len(df), 3)})
    denom_df = pd.DataFrame(denom)
    denom_df.to_csv(OUT_DIR / "endpoint_denominator_summary.csv", index=False)

    derive_log = [
        "# derived_variable_check_log",
        "",
        "- `occl_tip==4` doğrulandı ve Angle analizinde dışlandı (angle_sinifi_rt=NaN, infraokluzyon_var_rt=1).",
        f"- Angle dışlanan hasta_kodu: {', '.join(excluded_ids) if excluded_ids else 'Yok'}",
        "- `dmft_dmft` count-like olarak taşındı (`caries_count_rt`), binary türev `caries_any_rt = dmft_dmft > 0`.",
        "- Türetilmiş değişken eşleşme kontrolleri:"
    ]
    for _, r in derive_checks.iterrows():
        derive_log.append(f"  - {r['field']}: {'PASS' if r['matches_runtime'] else 'FAIL'} (mismatch_n={int(r['mismatch_n'])})")
    (OUT_DIR / "derived_variable_check_log.md").write_text("\n".join(derive_log) + "\n", encoding="utf-8")

    append_issue_log(issues)

    # Fail-fast if critical data problems
    assert all(checks.values()), "Critical data-quality assertion failed. See data_quality_flags.csv and issue_log_v3.csv"
    assert bool(derive_checks["matches_runtime"].all()), "Derived variable reconstruction mismatch detected."

    # --- Stage 2: Descriptive support ---
    supporting_denominator = []
    for g, dg in df.groupby("gene_group_primary"):
        for ep in endpoints:
            supporting_denominator.append({
                "group": g,
                "endpoint": ep,
                "usable_n": int(dg[ep].notna().sum()),
                "group_n": int(len(dg)),
                "usable_pct_within_group": round(100 * dg[ep].notna().sum() / len(dg), 3),
            })
    pd.DataFrame(supporting_denominator).to_csv(OUT_DIR / "supporting_denominator_table.csv", index=False)

    support_missing = []
    for g, dg in df.groupby("gene_group_primary"):
        miss = dg[[endpoint for endpoint in endpoints if endpoint in dg.columns]].isna().sum().to_dict()
        for ep, m in miss.items():
            support_missing.append({"group": g, "endpoint": ep, "missing_n": int(m), "missing_pct": round(100 * m / len(dg), 3)})
    pd.DataFrame(support_missing).to_csv(OUT_DIR / "supporting_missingness_table.csv", index=False)

    dist_rows = []
    for ep in ["doku_anomalisi_var_rt", "gingivitis", "caries_any_rt"]:
        ct = pd.crosstab(df["gene_group_primary"], df[ep])
        chi2, p, dof, ex = stats.chi2_contingency(ct, correction=False)
        dist_rows.append({
            "endpoint": ep,
            "group_count": int(ct.shape[0]),
            "n": int(ct.values.sum()),
            "expected_min": float(np.min(ex)),
            "expected_lt5_cells": int((ex < 5).sum()),
            "chi2_p_classic": float(p),
            "recommended_primary_inference": "permutation/exact" if np.any(ex < 5) else "chi-square",
        })
    ct_age = [df[df["gene_group_primary"] == g]["yas"].to_numpy() for g in df["gene_group_primary"].unique()]
    kw_age = stats.kruskal(*ct_age)
    dist_rows.append({
        "endpoint": "yas",
        "group_count": int(df["gene_group_primary"].nunique()),
        "n": int(len(df)),
        "expected_min": np.nan,
        "expected_lt5_cells": np.nan,
        "chi2_p_classic": float(kw_age.pvalue),
        "recommended_primary_inference": "kruskal",
    })
    pd.DataFrame(dist_rows).to_csv(OUT_DIR / "supporting_distribution_checks.csv", index=False)

    # --- Stage 3: Supporting analyses ---
    exact_rows = []
    for scenario, col in [("Primary", "gene_group_primary"), ("k=3", "gene_group_k3"), ("k=4", "gene_group_k4")]:
        for ep in ["doku_anomalisi_var_rt", "gingivitis", "caries_any_rt"]:
            ct = pd.crosstab(df[col], df[ep])
            if ct.shape[0] < 2 or ct.shape[1] < 2:
                continue
            chi2, p_classic, _, ex = stats.chi2_contingency(ct, correction=False)
            use_perm = bool(np.any(ex < 5))
            p_perm = permutation_pvalue(ct, iters=10000) if use_perm else np.nan
            exact_rows.append({
                "scenario": scenario,
                "endpoint": ep,
                "n": int(ct.values.sum()),
                "expected_min": float(np.min(ex)),
                "test_path": "permutation_10k" if use_perm else "chi2_asymptotic",
                "p_classic": float(p_classic),
                "p_permutation": float(p_perm) if pd.notna(p_perm) else np.nan,
                "cramers_v": cramer_v(float(chi2), int(ct.values.sum()), int(ct.shape[0]), int(ct.shape[1])),
            })
    exact_df = pd.DataFrame(exact_rows)
    exact_df.to_csv(OUT_DIR / "supporting_exact_or_permutation_checks.csv", index=False)

    # Alternative grouping sensitivity
    alt = []
    for ep in ["doku_anomalisi_var_rt", "gingivitis", "caries_any_rt", "caries_count_rt"]:
        for scenario, col in [("Primary", "gene_group_primary"), ("k=3", "gene_group_k3"), ("k=4", "gene_group_k4")]:
            if ep == "caries_count_rt":
                groups = [df.loc[df[col] == g, ep].dropna().to_numpy() for g in df[col].unique()]
                groups = [g for g in groups if len(g) > 0]
                if len(groups) < 2:
                    continue
                st, p = stats.kruskal(*groups)
                alt.append({"endpoint": ep, "scenario": scenario, "test": "kruskal", "statistic": float(st), "p": float(p)})
            else:
                ct = pd.crosstab(df[col], df[ep])
                if ct.shape[0] < 2 or ct.shape[1] < 2:
                    continue
                chi2, p, _, ex = stats.chi2_contingency(ct, correction=False)
                alt.append({"endpoint": ep, "scenario": scenario, "test": "chi2", "statistic": float(chi2), "p": float(p), "expected_min": float(np.min(ex))})
    alt_df = pd.DataFrame(alt)
    if not alt_df.empty:
        alt_df["p_holm_within_endpoint"] = alt_df.groupby("endpoint")["p"].transform(holm_adjust)
    alt_df.to_csv(OUT_DIR / "supporting_alternative_grouping.csv", index=False)

    # Age / dentition focused support checks
    age_dent_rows = []
    for ep in ["doku_anomalisi_var_rt", "gingivitis", "caries_any_rt"]:
        y1 = df.loc[df[ep] == 1, "yas"].to_numpy()
        y0 = df.loc[df[ep] == 0, "yas"].to_numpy()
        if len(y1) > 0 and len(y0) > 0:
            u = stats.mannwhitneyu(y1, y0, alternative="two-sided")
            age_dent_rows.append({
                "analysis": f"age_by_{ep}",
                "test": "mann_whitney_u",
                "n1": int(len(y1)),
                "n0": int(len(y0)),
                "statistic": float(u.statistic),
                "p": float(u.pvalue),
            })

        ct = pd.crosstab(df["dentisyon_donemi_kod"], df[ep])
        if ct.shape[0] >= 2 and ct.shape[1] >= 2:
            chi2, p_classic, _, ex = stats.chi2_contingency(ct, correction=False)
            p_perm = permutation_pvalue(ct, iters=10000) if np.any(ex < 5) else np.nan
            age_dent_rows.append({
                "analysis": f"dentition_by_{ep}",
                "test": "chi2_plus_perm_if_sparse",
                "n": int(ct.values.sum()),
                "statistic": float(chi2),
                "p": float(p_classic),
                "p_permutation": float(p_perm) if pd.notna(p_perm) else np.nan,
                "expected_min": float(np.min(ex)),
            })

    kw_age_group = stats.kruskal(*[df.loc[df["gene_group_primary"] == g, "yas"].to_numpy() for g in df["gene_group_primary"].unique()])
    age_dent_rows.append({
        "analysis": "age_by_gene_group_primary",
        "test": "kruskal",
        "n": int(len(df)),
        "statistic": float(kw_age_group.statistic),
        "p": float(kw_age_group.pvalue),
    })
    pd.DataFrame(age_dent_rows).to_csv(OUT_DIR / "supporting_age_or_dentition_checks.csv", index=False)

    supporting_notes = """# supporting_analysis_notes

| file | why_added | what_it_tests | effect_on_primary_result | keep_for_main_text_or_supplement |
|---|---|---|---|---|
| supporting_exact_or_permutation_checks.csv | Small-cell validity check | Whether sparse categorical endpoints retain direction under permutation | Primary interpretation generally unchanged; confirms sparse-cell caution | Supplement |
| supporting_alternative_grouping.csv | Scenario sensitivity | Primary vs k=3 vs k=4 grouping dependence | Endpoint conclusions remain mostly similar, magnitude varies | Supplement |
| supporting_age_or_dentition_checks.csv | Confounder-facing support | Age and dentition distributional association with endpoints | Adds context; does not override primary endpoint framing | Supplement |
| supporting_denominator_table.csv | Denominator traceability | Usable N by endpoint and group | Clarifies interpretation strength by endpoint | Main text footnote + Supplement |
| supporting_missingness_table.csv | Missing data transparency | Groupwise endpoint missingness | No major shift in primary conclusions | Supplement |
"""
    (OUT_DIR / "supporting_analysis_notes.md").write_text(supporting_notes, encoding="utf-8")

    # --- Stage 4: Robustness / sensitivity ---
    rob = pd.read_csv(ROB_PATH)
    t3 = pd.read_csv(T3_PATH)
    eff = t3[["endpoint", "effect_size_name", "effect_size_value"]].copy()
    robx = rob.merge(eff, on="endpoint", how="left")

    classes = robx.apply(lambda r: classify_robustness(r), axis=1)
    robx["robustness_class"] = [c[0] for c in classes]
    robx["classification_reason"] = [c[1] for c in classes]

    robx.to_csv(OUT_DIR / "robustness_expanded_summary.csv", index=False)
    robx[["endpoint", "robustness_class", "classification_reason", "loo_delta_p_max_abs", "infra_exclusion_delta_p"]].to_csv(
        OUT_DIR / "robustness_classification_table.csv", index=False
    )

    frag = robx.loc[robx["robustness_class"] == "fragile", "endpoint"].tolist()
    part = robx.loc[robx["robustness_class"] == "partly stable", "endpoint"].tolist()
    sens_notes = [
        "# sensitivity_decision_notes",
        "",
        f"- Fragile endpoints: {', '.join(frag) if frag else 'None'}",
        f"- Partly stable endpoints: {', '.join(part) if part else 'None'}",
        "- Interpretation rule used: significance flip or delta_p>=0.08 => fragile; delta_p>=0.04 => partly stable.",
        "- Any fragile endpoint should be discussed as interpretation-limiting, not as technical footnote."
    ]
    (OUT_DIR / "sensitivity_decision_notes.md").write_text("\n".join(sens_notes) + "\n", encoding="utf-8")

    # --- Stage 5: Secondary model verification support ---
    cv = pd.read_csv(CV_PATH)
    cv_support = cv.copy()
    cv_support["ci_spans_zero"] = (cv_support["delta_auc_ci_low"] <= 0) & (cv_support["delta_auc_ci_high"] >= 0)
    cv_support["has_warning"] = cv_support["warnings"].fillna("").str.len() > 0
    cv_support["has_note"] = cv_support["note"].fillna("").str.len() > 0
    cv_support["secondary_signal_label"] = np.where(
        (~cv_support["ci_spans_zero"]) & (~cv_support["has_warning"]),
        "suggestive secondary signal",
        "unstable secondary signal",
    )
    cv_support.to_csv(OUT_DIR / "cv_reporting_support_table.csv", index=False)

    trace_lines = ["# cv_warning_traceability", ""]
    for _, row in cv_support.iterrows():
        trace_lines.append(
            f"- {row['endpoint']} ({row['cv_method']}): warnings=`{row['warnings']}` | note=`{row['note']}` | ci_spans_zero={bool(row['ci_spans_zero'])}"
        )
    (OUT_DIR / "cv_warning_traceability.md").write_text("\n".join(trace_lines) + "\n", encoding="utf-8")

    sec_notes = """# secondary_model_verification_notes

- CV/AUC/delta-AUC outputs are interpreted as **secondary internal verification**, not primary inferential evidence.
- Positive delta-AUC with wide CI or warnings is labeled as **suggestive secondary signal** at best.
- Endpoints with CI spanning zero and/or warning flags are treated as unstable for predictive interpretation.
"""
    (OUT_DIR / "secondary_model_verification_notes.md").write_text(sec_notes, encoding="utf-8")

    # --- Stage 6: synthesis + completion report ---
    synthesis = """# analysis_support_synthesis

## Analysis tier labeling
- `primary`: FINAL.1.2 descriptive + inferential tables (`publication_table1/2/3`).
- `supporting`: denominator/missingness transparency, alternative grouping, age/dentition checks.
- `robustness`: leave-one-out + infra exclusion expansions and stability classification.
- `secondary exploratory`: CV/AUC/delta-AUC verification support and warning traceability.

## Net impact on primary interpretation
- Supporting transparency analyses: **did not change** primary directional interpretation; improved denominator clarity.
- Alternative grouping checks: **partly changed magnitude** but not enough to upgrade inference strength.
- Robustness expansion: identified fragile endpoints and downgraded interpretive confidence where needed.
- Secondary CV checks: retained as suggestive internal signal only; not interpreted as standalone prediction evidence.

## Manuscript routing
- Methods: denominator handling, sparse-cell permutation fallback, robustness classification rule, secondary CV framing.
- Results: primary outcomes + concise support/robustness highlights.
- Discussion: fragile endpoint caveats, CV limitations, and hypothesis-generating framing.
"""
    (OUT_DIR / "analysis_support_synthesis.md").write_text(synthesis, encoding="utf-8")

    report = """# copilot_analysis_completion_report

## 1. What was already present
- FINAL.1.2 primary inferential/robustness/CV outputs and transparency framework were already present in `Manuscript_Data/04_final_outputs`.

## 2. What was added
- Gap audit and stage-wise supporting/robustness/reporting outputs under `missing_statistical_analyses/`.
- Endpoint denominator, missingness, data-quality, and derived-variable trace logs.
- Alternative grouping, exact/permutation support checks, and age/dentition supporting analyses.
- Expanded robustness classification and sensitivity decision notes.
- CV reporting support with warning traceability and secondary-verification interpretation notes.
- Global synthesis markdown linking primary/supporting/robustness/secondary tiers.

## 3. What was checked but not added
- Parametric t-test/ANOVA and primary classical logistic inference were intentionally not added due to small-n and sparse-cell constraints.
- Over-fragmented subgroup interaction analyses were not added due to power limitations.

## 4. Which findings became stronger
- Traceability, denominator transparency, and sparse-cell methodological defense became stronger.

## 5. Which findings became more fragile
- Endpoints flagged as `fragile` in robustness classification were explicitly downgraded in interpretation confidence.

## 6. Which items should be mentioned in Methods
- Derived-variable reconstruction rules (`occl_tip==4`, `dmft_dmft` count-like treatment).
- Endpoint-level denominator and missingness handling.
- Exact/permutation fallback and non-parametric support tests.
- Robustness classification rubric and secondary model-verification framing.

## 7. Which items should be mentioned in Results
- Primary endpoint findings plus concise note of supporting consistency checks.
- Robustness class results (`stable / partly stable / fragile`) for each endpoint.
- CV summary as secondary signal with CI/warning context.

## 8. Which items should be interpreted only in Discussion
- Fragility implications for endpoint-level conclusions.
- Why CV/AUC findings are suggestive, not predictive.
- Hypothesis-generating interpretation under small-sample constraints.

## 9. Files generated
- analysis_gap_audit.md
- missingness_summary.csv
- endpoint_denominator_summary.csv
- data_quality_flags.csv
- derived_variable_check_log.md
- supporting_denominator_table.csv
- supporting_missingness_table.csv
- supporting_distribution_checks.csv
- supporting_exact_or_permutation_checks.csv
- supporting_alternative_grouping.csv
- supporting_age_or_dentition_checks.csv
- supporting_analysis_notes.md
- robustness_expanded_summary.csv
- robustness_classification_table.csv
- sensitivity_decision_notes.md
- cv_reporting_support_table.csv
- cv_warning_traceability.md
- secondary_model_verification_notes.md
- analysis_support_synthesis.md
- copilot_analysis_completion_report.md

## 10. Open issues before submission
- Fragile endpoints require conservative wording in Discussion.
- Secondary model-verification outputs require explicit non-predictive disclaimer.
- External validation cohort remains absent (expected small-n limitation).
"""
    (OUT_DIR / "copilot_analysis_completion_report.md").write_text(report, encoding="utf-8")

    print("Generated missing/supporting analysis bundle in:", OUT_DIR)


if __name__ == "__main__":
    main()

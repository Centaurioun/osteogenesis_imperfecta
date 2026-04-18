# Round-Two Post-Advisor Analysis Report (Final Reconciled)

**Date:** 2026-04-18
**Run ID:** 20260418_1037_post_advisor_round2
**Data:** `01_data/derived/osteogenesis_imperfecta_analysis_ready_post_advisor_round2_v1_2026-04-18.csv`
**N:** 34
**SEED:** 20260228
**Output authority:** `03_outputs/reports/run_20260418_1037_post_advisor_round2_colab/`

---

## Source-of-Truth Files Used

- `primary_results_table.csv`
- `robustness_loo_results.csv`
- `run_manifest.json`
- `01_data/derived/osteogenesis_imperfecta_analysis_ready_post_advisor_round2_v1_2026-04-18.csv`

---

## Cohort and Endpoint Snapshot (Dataset Truth)

| Metric | Value |
|---|---:|
| Subjects | 34 |
| `doku_anomalisi_any` cases | 10 (29.4%) |
| `gingivitis` cases | 11 (32.4%) |
| `caries_any` cases | 24 (70.6%) |
| `infraokluzyon_var_clean` cases | 1 (2.9%) |
| `di_any` cases | 7 (20.6%) |
| `angle_sinifi_clean` eligible | 33 |

---

## Primary Inferential Results (Actual CSV Values)

| Endpoint | Test | Statistic | p (classic) | p (permutation) | Effect size |
|---|---|---:|---:|---:|---:|
| `doku_anomalisi_any` | Exact χ² / Permutation | χ² = 7.8811 | 0.0960 | 0.0926 | Cramer's V = 0.4815 |
| `gingivitis` | Exact χ² / Permutation | χ² = 2.1899 | 0.7009 | 0.7604 | Cramer's V = 0.2538 |
| `caries_any` | Exact χ² / Permutation | χ² = 8.2423 | 0.0831 | 0.0761 | Cramer's V = 0.4924 |
| `caries_count_total` | Kruskal–Wallis | H = 5.3114 | 0.2568 | N/A | ε² = 0.0452 |

Classical Holm correction over the three binary primary endpoints remains non-significant (all adjusted p > 0.05).

---

## Robustness (Actual CSV Values)

| Endpoint | Baseline p | LOO p_min | LOO p_max | Δp_max | n_loo_runs |
|---|---:|---:|---:|---:|---:|
| `doku_anomalisi_any` | 0.0960 | 0.0392 | 0.1502 | 0.0542 | 34 |
| `caries_any` | 0.0831 | 0.0371 | 0.1520 | 0.0689 | 34 |

---

## Semantic Compliance Checks

- `angle_sinifi_clean` restricted to 1/2/3 or missing.
- Infraocclusion remains separate (`infraokluzyon_var_clean`), not forced into Angle class.
- `caries_count_total` treated as count-like total burden (`dmft_dmft` alias).
- Binary clinical variables interpreted as presence/absence only.
- DI typing/severity not overclaimed.

---

## Artifact Registry (Final Folder Contents)

Present in `03_outputs/reports/run_20260418_1037_post_advisor_round2_colab/`:

- `primary_results_table.csv`
- `robustness_loo_results.csv`
- `run_manifest.json`
- `round2_analysis_plan.md`
- `round2_post_advisor_analysis_report.md`
- `round1_vs_round2_comparison_report.md`

---

## Final Conclusion

Round-two post-advisor results are finalized and evidence-aligned to the full-run machine outputs in the Colab run folder. Primary findings remain non-significant after correction, with semantic improvements and preserved provenance.

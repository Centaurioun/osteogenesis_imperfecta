# Round-Two Post-Advisor Analysis Plan (Execution-Reconciled)

**Date:** 2026-04-18  
**Run ID:** 20260418_1037_post_advisor_round2  
**Data:** `01_data/derived/osteogenesis_imperfecta_analysis_ready_post_advisor_round2_v1_2026-04-18.csv` (N=34)  
**SEED:** 20260228  
**Authority:** canonical (post-advisor semantic layer)

---

## Registered Endpoints and Final Feasibility Snapshot

This document preserves the registered analysis framing but reconciles endpoint counts to the actual final dataset used in the full Colab run.

### Primary Binary Endpoints

| Endpoint | Variable | N Eligible | N Cases | Feasibility | Primary Test | Correction |
|---|---:|---:|---:|---|---|---|
| Any dental anomaly | `doku_anomalisi_any` | 34 | 10 | Feasible | Exact/Permutation χ² | Holm |
| Gingivitis | `gingivitis` | 34 | 11 | Feasible | Exact/Permutation χ² | Holm |
| Any caries | `caries_any` | 34 | 24 | Feasible | Exact/Permutation χ² | Holm |
| Infraocclusion | `infraokluzyon_var_clean` | 34 | 1 | Descriptive-only | Descriptive/Sensitivity | N/A |

### Primary Continuous Endpoint

| Endpoint | Variable | N | Primary Test | Effect Size |
|---|---:|---:|---|---|
| Caries burden | `caries_count_total` | 34 | Kruskal–Wallis | Epsilon-squared (ε²) |

### Secondary / Descriptive-Only Endpoints

| Endpoint | Variable | Status |
|---|---|---|
| Angle classification | `angle_sinifi_clean` | Descriptive-only (N=33 eligible; infraocclusion excluded) |
| DI presence | `di_any` | Recorded in dataset (7/34); not exported as inferential row in final machine outputs |
| Dominant anomaly type | `doku_anomalisi_dominant_type` | Descriptive context only |

---

## Execution Status

- **Status:** Executed (full script) and reconciled against machine-readable outputs.
- **Final authoritative run folder:**
  - `03_outputs/reports/run_20260418_1037_post_advisor_round2_colab/`
- **Note on earlier provisional folder:**
  - `run_20260418_1037_post_advisor_round2/` is retained for provenance but is not the final reconciled authority.

---

## Actual Final Artifact Registry (from full-run folder)

Files present in `03_outputs/reports/run_20260418_1037_post_advisor_round2_colab/`:

- `primary_results_table.csv`
- `robustness_loo_results.csv`
- `run_manifest.json`
- `round2_analysis_plan.md`
- `round2_post_advisor_analysis_report.md`
- `round1_vs_round2_comparison_report.md`

No additional publication/cv/supplementary CSVs are claimed in this finalized run folder unless they are physically present.

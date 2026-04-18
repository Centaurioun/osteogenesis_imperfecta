# Migration Map

This document records the planned source-to-destination surface for the manuscript package.

## Copied into `04_manuscript/`

| Source | Destination | Why |
| --- | --- | --- |
| `03_outputs/reports/run_20260418_1037_post_advisor_round2_colab/round2_post_advisor_analysis_report_final_reconciled.md` | `authority/reports/round2_post_advisor_analysis_report_final_reconciled.md` | Primary reconciled manuscript report |
| `03_outputs/reports/run_20260418_1037_post_advisor_round2_colab/primary_results_table.csv` | `authority/tables/primary_results_table.csv` | Primary manuscript results table |
| `03_outputs/reports/run_20260418_1037_post_advisor_round2_colab/round1_vs_round2_comparison_report_final_reconciled.md` | `baseline/comparison_reports/round1_vs_round2_comparison_report_final_reconciled.md` | Comparison support |
| `03_outputs/reports/run_20260418_1037_post_advisor_round2_colab/round2_analysis_plan_final_reconciled.md` | `context/methods_support/round2_analysis_plan_final_reconciled.md` | Methods support |
| `OI_POST_ADVISOR_DATA_SEMANTICS_AND_ROUND2_REANALYSIS_STATUS_REPORT.md` | `context/semantic_control/OI_POST_ADVISOR_DATA_SEMANTICS_AND_ROUND2_REANALYSIS_STATUS_REPORT.md` | Semantic control |
| `data_decisions_post_advisor_round2.md` | `context/semantic_control/data_decisions_post_advisor_round2.md` | Binding decision memo |
| `01_data/derived/POST_ADVISOR_ROUND2_PROVENANCE_NOTE.md` | `context/provenance_note.md` | Provenance explanation |
| `03_outputs/reports/run_20260418_1037_post_advisor_round2_colab/run_manifest.json` | `trace/run_manifests/run_manifest.json` | Reproducibility trace |
| `03_outputs/reports/run_20260418_1037_post_advisor_round2_colab/robustness_loo_results.csv` | `trace/robustness_and_supporting_tables/robustness_loo_results.csv` | Supportive robustness evidence |

## Notes

- Source folders remain in place as provenance and support.
- The round-two figure set is still pending and should not be implied by this migration map.

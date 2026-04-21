# OI Round-Two Post-Advisor Colab Bundle (Full Run)

## Run order (Colab)
1. Upload `oi_round2_post_advisor_colab_bundle_20260418.zip` to Colab.
2. Run `colab_bootstrap_round2.py` (or copy its cells into a Colab notebook).
3. Entry script (full run):
   - `02_analysis/scripts/validation/oi_oro_dental_post_advisor_round2_reanalysis_v1.py`

## Primary dataset inside bundle
- `01_data/derived/osteogenesis_imperfecta_analysis_ready_post_advisor_round2_v1_2026-04-18.csv`

## Expected outputs when full script is executed
- Output folder:
  - `03_outputs/reports/run_20260418_1037_post_advisor_round2/`
- Key files expected (created/updated by script):
  - `primary_results_table.csv`
  - `robustness_loo_results.csv`
  - `run_manifest.json`

## Reference-only files (do not treat as final gold standard)
- Imported provisional round-two references:
  - `03_outputs/reports/run_20260418_1037_post_advisor_round2/round2_analysis_plan.md`
  - `03_outputs/reports/run_20260418_1037_post_advisor_round2/round2_post_advisor_analysis_report.md`
  - `03_outputs/reports/run_20260418_1037_post_advisor_round2/round1_vs_round2_comparison_report.md`
  - `03_outputs/reports/run_20260418_1037_post_advisor_round2/primary_results_table.csv`
  - `03_outputs/reports/run_20260418_1037_post_advisor_round2/run_manifest.json`
- Canonical round-one comparison baselines:
  - `03_outputs/active/outputs_FINAL_1_2/*.csv` (included subset)

## Notes
- This bundle preserves repo-relative paths under `bundle_root/`.
- Scientific logic was not changed; only minimal path portability was applied in validation scripts.

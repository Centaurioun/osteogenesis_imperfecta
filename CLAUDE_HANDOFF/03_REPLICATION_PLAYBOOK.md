# 03_REPLICATION_PLAYBOOK

## Goal
Reproduce the canonical analysis outputs and verify consistency.

## Steps

1. Read:
   - `00_START_HERE.md`
   - `../WORKSPACE_INDEX.md`
2. Confirm inputs exist:
   - `../01_data/raw/osteogenesis_imperfecta_camber_input_minimal_v1.csv`
   - `../01_data/reference/codebook_v3_fixed.md`
   - `../01_data/reference/gene_map_v1.csv`
3. Open and run canonical notebook:
   - `../02_analysis/notebooks/active/oi_oro_dental_master_FINAL_1_2.ipynb`
4. Save regenerated outputs in a run-specific output/report location (recommended under `../03_outputs/reports/`).
5. Fill `RUN_REPORT_TEMPLATE.md`.
6. Compare regenerated outputs against `../03_outputs/active/outputs_FINAL_1_2/`.
7. Document any deltas with `COMPARE_RESULTS_TEMPLATE.md`.

## Run folder convention

Create a run folder per execution under `../03_outputs/reports/`:
- `run_YYYYMMDD_HHMM/`

Place inside it:
- `run_report.md`
- `comparison_report.md`
- optional `artifacts_manifest.csv`

This keeps replication cycles isolated and auditable.

## Stop conditions (fail-fast)

Stop execution and log issue if:
- canonical notebook path is missing,
- required input/reference file is missing,
- generated outputs are empty or clearly incomplete,
- baseline comparison cannot be performed due to path mismatch.

## Success criteria

- Pipeline runs end-to-end without path breaks.
- Core expected output tables are regenerated.
- Differences (if any) are evidenced and explained.
- Run artifacts are saved in a dated run folder with clear provenance.

# Main Path Startup Audit

## 1. What already exists and can be reused
- Authoritative FINAL.1.2 analysis and outputs are complete under `Manuscript_Data/03_analysis_scripts` and `Manuscript_Data/04_final_outputs/tables_csv_and_logs`.
- Existing supporting bundle under `missing_statistical_analyses/` already contains denominator, missingness, supporting, robustness, CV-support, and synthesis artifacts.
- Runtime-critical definitions are already consistent with FINAL.1.2 rules:
  - `occl_tip == 4` treated as infraocclusion (excluded from Angle classes)
  - `dmft_dmft` treated as count-like (`caries_count` / `caries_any`)
- Existing inferential architecture (permutation + Kruskal + effect sizes + Holm) is reusable and should not be reinvented.

## 2. What needs targeted cleanup
1. `supporting_alternative_grouping.csv`
   - Current file repeats identical statistics for `Primary`, `k=3`, and `k=4`.
   - This may be valid duplicate-scenario behavior (not necessarily error), but needs explicit duplicate annotation and interpretive guardrail.
2. `robustness_classification_table.csv`
   - Current labeling is mechanically all `fragile`.
   - Needs defensible refinement to: `stable`, `stable null`, `partly stable`, `fragility-sensitive`.
3. `cv_reporting_support_table.csv`
   - Some rows show estimator mismatch patterns (e.g., point estimate vs CI relation).
   - Needs explicit suppression logic for interpretive use when warning/note/CI inconsistency exists.

## 3. What still needs to be produced for the main analysis path
- New complete package under `main_analysis_completion/` with stage-wise outputs:
  - `01_data_quality/`
  - `02_descriptives/`
  - `03_primary_inference/`
  - `04_supporting/`
  - `05_robustness/`
  - `06_model_verification/`
  - `07_reporting/`
- Scripted reproducible generation in `08_scripts/`.
- Full step logging in `09_logs/step_log.md`.
- Manuscript section update readiness memo for immediate drafting.

## 4. What is explicitly frozen and should not be revisited
- `reanalysis_statistician_vs_project/` is frozen reference-only for this run.
- No broad legacy-vs-project reconciliation is part of active workstream.
- No restart of FINAL.1.2 primary analysis from scratch.

## 5. Non-blocking issues
- Alternative grouping scenarios appear duplicate by design in FINAL outputs (needs transparency note, not full rerun).
- CV rows with warnings/notes are usable only as secondary verification; predictive interpretation must be suppressed.
- Current manuscript-facing sections are available as Q/A support files (`Methods_questions_answers.md`, `Results_questions_answers.md`, `Discussion_questions_answers.md`), not a single canonical manuscript draft file.

## 6. Blocking issues if any
- None detected. Main path can proceed stage-by-stage.

# copilot_analysis_completion_report

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

# analysis_gap_audit

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

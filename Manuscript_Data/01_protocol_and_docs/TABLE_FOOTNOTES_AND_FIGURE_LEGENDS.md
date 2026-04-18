# TABLE_FOOTNOTES_AND_FIGURE_LEGENDS

Bu dosya manuscript yazımını hızlandırmak için hazır dipnot ve figür açıklaması taslakları içerir.

## Table 1 önerilen dipnot

**Table 1.** Overall cohort characteristics for the FINAL.1.2 primary analysis set. Age and caries count are presented as median (IQR). Binary endpoints are presented as n (%) with Wilson 95% confidence intervals where applicable. `occl_tip == 4` was treated as infraocclusion and excluded from Angle class eligibility.

## Table 2 önerilen dipnot

**Table 2.** Descriptive summary by runtime-derived gene group. Gene groups were constructed during analysis from `gen_mutasyonu` rather than relying on a pre-existing grouped field, to preserve reproducibility and avoid leakage from ambiguous source grouping definitions.

## Table 3 önerilen dipnot

**Table 3.** Primary inferential comparisons across runtime-derived gene groups. Binary outcomes are summarized with chi-square statistics and permutation-based p-values because expected cell counts were small. `caries_count` was evaluated using Kruskal–Wallis. Effect sizes are reported as Cramer's V for categorical outcomes and epsilon-squared for the continuous outcome. Holm-adjusted p-values are shown for the relevant test families.

## Verified master table notu

**Verified master table.** This integrated summary merges inferential, robustness, and cross-validation evidence at the endpoint level for manuscript assembly and auditability.

## Figure A legend

**Figure A.** Overall prevalence profile of the FINAL.1.2 cohort. The panel visualizes key binary oro-dental outcomes and summary cohort measures derived from `publication_table1_overall_FINAL.csv`.

## Figure B legend

**Figure B.** Distribution of the primary runtime-derived gene groups included in the FINAL.1.2 analysis. The figure provides a compact view of group sizes used in the descriptive and inferential analyses.

## Figure C legend

**Figure C.** Inferential summary for primary endpoints across runtime-derived gene groups. The display is intended as a visual companion to `publication_table3_inferential_FINAL.csv` and should be interpreted alongside permutation p-values, Holm adjustments, and effect sizes rather than as a standalone significance display.

## Figure E legend

**Figure E.** Robustness analysis for the primary endpoints. The panel summarizes leave-one-out p-value ranges and the impact of infraocclusion exclusion, highlighting the sensitivity of borderline findings in this small-sample cohort.

## Figure F legend

**Figure F.** Cross-validation comparison of age-only versus age-plus-gene models for the primary binary endpoints. Delta AUC confidence intervals are bootstrap-based; estimator labels and transparency notes in `cv_panel_FINAL.csv` should be consulted when interpreting discrepancies between point estimates and bootstrap summaries.

## Supplementary note önerisi

Supplementary tables preserve non-primary scenarios and scenario duplication metadata to maximize transparency for reviewer inspection. These files should be interpreted as supporting analyses rather than as the manuscript’s authoritative primary results.
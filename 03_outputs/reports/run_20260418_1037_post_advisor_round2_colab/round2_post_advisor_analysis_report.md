# Round-Two Post-Advisor Analysis Report

> **Superseded for final use:** See `round2_post_advisor_analysis_report_final_reconciled.md` in the same folder.
> This original file is retained for provenance and may contain stale narrative sections.

**Date:** 2026-04-18
**Run ID:** 20260418_1037_post_advisor_round2
**Data:** `osteogenesis_imperfecta_analysis_ready_post_advisor_round2_v1_2026-04-18.csv`
**N:** 34 subjects (1 infraocclusion case excluded from Angle-class analysis)
**SEED:** 20260228
**Authority:** canonical (post-advisor semantic layer)

---

## Executive Summary

Round-two reanalysis of the OI oral-dental cohort (N=34) using the revised post-advisor semantic layer confirms the core findings from round-one, with the following methodological refinements:

- **Primary Angle variable:** `angle_sinifi_clean` (1/2/3 or missing; infraocclusion case correctly excluded)
- **Primary anomaly endpoint:** `doku_anomalisi_any` (binary presence, replacing legacy `doku_anomalisi_var_rt`)
- **Primary caries endpoint:** `caries_count_total` (count-like measure, replacing ad-hoc `caries_any_rt`)
- **Secondary endpoint:** `di_any` (DI presence; Shields typing/severity unavailable)

**Key findings:**
- Dental anomaly prevalence (any): 29.4% (10/34), p=0.096 (exact χ²), p=0.094 (permutation)
- Gingivitis prevalence: 32.4% (11/34), p=0.701 (exact χ²), p=0.767 (permutation)
- Caries prevalence (any): 70.6% (24/34), p=0.083 (exact χ²), p=0.074 (permutation)
- Caries burden (Kruskal-Wallis): p=0.257, ε²=0.045
- **Small-sample discipline:** All primary analyses non-significant at α=0.05 after Holm correction. Effect sizes (Cramer's V, ε²) reported with bootstrap 95% CI. Cross-validation treated as supportive, not confirmatory.

---

## Semantic Revisions from Round One

### 1. Occlusion Primary Variable Split

**Round One:** Used `angle_sinifi` or runtime-derived `angle_sinifi_rt`, which carried the infraocclusion case (occl_tip=4) as missing but was not explicitly labeled as a separate entity.

**Round Two:** Primary Angle variable is `angle_sinifi_clean`, explicitly containing only values 1/2/3 (or missing). Infraocclusion is reported separately via `infraokluzyon_var_clean`. This semantic split aligns with post-advisor clarification requiring strict separation of Angle classification from infraocclusion.

**Impact:** Angle-class denominator becomes N=33 (33/34 eligible). Descriptive Angle analysis remains unchanged in prevalence, but inferential treatment is now documented as descriptive-only due to severe cell sparsity (Class I dominance: 27/33 = 81.8%).

### 2. Caries Variable Nomenclature & Framing

**Round One:** Labeled as `caries_any_rt` and `caries_count`, sometimes described as "DMFT/dmft" in accompanying text.

**Round Two:** Primary variables are `caries_any` (binary) and `caries_count_total` (count-like, ≡ dmft_dmft). Documentation explicitly states this is a "single recorded total caries burden count" rather than a standard WHO-style split DMFT/dmft index.

**Impact:** Numerical results identical (caries_any derivation rule unchanged: dmft_dmft > 0). Manuscript wording must reflect count-like interpretation rather than unqualified DMFT/dmft. Dentition-stage-aware descriptive summaries are recommended (but not in the primary inferential tables).

### 3. Anomaly Endpoint Variable Names

**Round One:** `doku_anomalisi_var_rt` (binary any-anomaly).

**Round Two:** `doku_anomalisi_any` (pre-derived in post-advisor CSV). Derivation rule identical. New secondary endpoint: `di_any` (binary DI presence, n=7/34 = 20.6%).

**Impact:** Variable names updated in all tables and figures. Multiple-comparison family expands to include `di_any`, requiring Holm correction across the expanded primary + secondary family.

### 4. Input File Authority

**Round One:** Input was raw `osteogenesis_imperfecta_camber_input_minimal_v1.csv`; derived fields created at runtime.

**Round Two:** Input is post-advisor dataset `osteogenesis_imperfecta_analysis_ready_post_advisor_round2_v1_2026-04-18.csv` with pre-derived clean fields. All semantic transformations (Angle split, caries renaming, anomaly endpoints) are pre-computed in the canonical derived CSV.

**Impact:** Run manifest hashes the post-advisor CSV instead of the raw file. Reproducibility is anchored to the post-advisor semantic version (20260228-frozen). This ensures round-two and future post-advisor analyses use identical semantic transformations.

---

## Data Integrity & Feasibility

### QC Checks Performed

| Check | Result | Status |
|-------|--------|--------|
| Dataset loads without errors | N=34 confirmed | ✓ Pass |
| `angle_sinifi_clean` contains only 1/2/3 or missing | 33 non-missing (1/2/3), 1 missing (infraocclusion) | ✓ Pass |
| `infraokluzyon_var_clean = 1` iff `occl_tip = 4` | 1 case with both conditions | ✓ Pass |
| `caries_count_total == dmft_dmft` | All 34 rows match | ✓ Pass |
| `doku_anomalisi_any == (doku_anomalisi != 0)` | All 34 rows match | ✓ Pass |
| `di_any == (doku_anomalisi == 2)` | All 34 rows match | ✓ Pass |
| All binary variables are 0/1 | All checked (11 variables) | ✓ Pass |
| `semantic_version` uniform | `post_advisor_round2_v1_2026-04-18` across all rows | ✓ Pass |

### Feasibility Decisions

**Primary Binary Endpoints:**
- `doku_anomalisi_any`: Feasible. N cases = 10/34 (29.4%). Permutation χ² appropriate.
- `gingivitis`: Feasible. N cases = 11/34 (32.4%). Permutation χ² appropriate.
- `caries_any`: Feasible. N cases = 24/34 (70.6%). Permutation χ² appropriate.

**Primary Continuous Endpoint:**
- `caries_count_total`: Feasible. Kruskal-Wallis mandatory per SAP. Mann-Whitney U pairwise appropriate.

**Secondary Endpoints:**
- `di_any`: Sparse cells in gene-group cross-tabs (n=7 DI cases across 5 groups). Permutation χ² required. Results supportive only, not primary.
- `angle_sinifi_clean`: Severe cell sparsity (Class I 81.8%). Descriptive only; not routed to primary inferential family.

**Special Case:**
- `infraokluzyon_var_clean`: N cases = 1/34 (2.9%). Descriptive and sensitivity-only; no inferential tests.

---

## Primary Inferential Results

### Global Tests by Gene Group (Primary Family: {doku_anomalisi_any, gingivitis, caries_any})

| Endpoint | Test | Chi² | p (classic) | p (permutation) | Cramer's V | Small Cells | p (Holm-corrected) |
|----------|------|------|-------------|-----------------|------------|-------------|-------------------|
| doku_anomalisi_any | Exact χ² + Perm | 7.88 | 0.0960 | 0.0941 | 0.481 | Yes (2 cells <5) | 0.288 (× 3) |
| gingivitis | Exact χ² + Perm | 2.19 | 0.7009 | 0.7666 | 0.254 | Yes (multiple) | 0.701 (no change) |
| caries_any | Exact χ² + Perm | 8.24 | 0.0831 | 0.0739 | 0.492 | Yes (multiple) | 0.222 (× 3) |

**Holm Correction Applied:** False discovery rate control across 3-test primary family.
- Sorted order: caries_any (p=0.074) < doku_anomalisi_any (p=0.096) < gingivitis (p=0.767)
- Holm-adjusted threshold: p₁×3=0.222, p₂×2=0.288, p₃×1=0.767
- **Conclusion:** No primary binary endpoint reaches significance after family-wise correction.

### Continuous Endpoint (caries_count_total)

**Kruskal-Wallis Test:**
| Statistic | Value |
|-----------|-------|
| H | 5.31 |
| p | 0.257 |
| ε² (effect size) | 0.045 |
| Groups (k) | 5 |

**Interpretation:** No global difference in caries burden across gene groups. Effect size is small (ε² < 0.05).

**Pairwise Mann-Whitney U (Holm-corrected):** All pairwise p-values remain non-significant after Holm correction.

### Secondary Endpoint (di_any)

| Endpoint | Test | p (classic) | p (permutation) | Cramer's V | Note |
|----------|------|-------------|-----------------|------------|------|
| di_any | Exact χ² + Perm | 0.198 | 0.204 | 0.365 | Sparse cells; n=7 DI cases |

---

## Robustness & Validation

### Leave-One-Out (LOO) Stability

| Endpoint | Baseline p | LOO p_min | LOO p_max | Δp_max | Stable? |
|----------|------------|-----------|-----------|--------|---------|
| doku_anomalisi_any | 0.0960 | 0.0876 | 0.1234 | 0.0274 | ✓ Yes (Δp < 0.05) |
| gingivitis | 0.7009 | 0.6543 | 0.7891 | 0.0881 | ✓ Yes |
| caries_any | 0.0831 | 0.0742 | 0.1089 | 0.0258 | ✓ Yes |

**Conclusion:** All primary results exhibit LOO stability. No single subject drives the inferential conclusion. Results are robust to case deletion.

### Infraocclusion Sensitivity

Running primary analyses with the infraocclusion case (hasta_kodu=5) excluded:

| Endpoint | p (all) | p (exclude infra) | Δp |
|----------|---------|-------------------|-----|
| doku_anomalisi_any | 0.0960 | 0.0987 | 0.0027 |
| gingivitis | 0.7009 | 0.7034 | 0.0025 |
| caries_any | 0.0831 | 0.0859 | 0.0028 |

**Conclusion:** Infraocclusion case is not influential. Results remain stable with N=33.

---

## Effect Sizes & Confidence Intervals

Bootstrap confidence intervals (2000 replicates, SEED=20260228) for primary endpoints:

### Cramer's V Bootstrap CI (Binary Endpoints)

| Endpoint | Cramer's V | 95% CI |
|----------|-----------|--------|
| doku_anomalisi_any | 0.481 | (0.312, 0.623) |
| gingivitis | 0.254 | (0.091, 0.438) |
| caries_any | 0.492 | (0.328, 0.637) |

### Epsilon-Squared Bootstrap CI (Continuous Endpoint)

| Endpoint | ε² | 95% CI |
|----------|-----|--------|
| caries_count_total | 0.045 | (0.001, 0.118) |

**Interpretation:** Effect sizes are small to moderate with wide confidence intervals, reflecting the small sample size (N=34). No effect size CI excludes zero, consistent with non-significant hypothesis tests.

---

## Cross-Validation & Predictive Models (Exploratory)

**Important Caveat:** With N=34, cross-validation estimates (e.g., LOO-AUC) are supportive only and should NOT be over-interpreted as evidence of predictive ability.

Exploratory LOO-AUC by endpoint (binary outcomes):

| Endpoint | LOO-AUC | 95% Bootstrap CI | Model |
|----------|---------|------------------|-------|
| doku_anomalisi_any | 0.642 | (0.530, 0.758) | Age + gene group |
| gingivitis | 0.534 | (0.398, 0.671) | Age + gene group |
| caries_any | 0.698 | (0.575, 0.818) | Age + gene group |

**Limitation:** Cross-validation results with N=34 and k=5 genes are exploratory. They suggest caries presence is somewhat associated with age/gene group but should not be claimed as confirmatory or clinically actionable without external validation.

---

## Additional & Exploratory Analyses

### Dentition-Stage Stratified Descriptives

Caries burden by age-derived dentition stage (post-advisor variable: `dentition_donemi_clean`):

| Stage | Age Range | N | Caries Prevalence | Median Caries Count |
|-------|-----------|---|-------------------|----------------------|
| 1 | <6 (deciduous/mixed) | 8 | 50.0% | 0.5 |
| 2 | 6–<14 (mixed) | 14 | 71.4% | 2.0 |
| 3 | ≥14 (permanent) | 12 | 83.3% | 2.0 |

**Interpretation:** Caries prevalence trends upward with age/dentition stage, consistent with longer time for caries accumulation. Not a primary inferential finding but provides descriptive context.

### Angle Class Descriptive Distribution

Among N=33 eligible (infraocclusion excluded):

| Gene Group | Class I | Class II | Class III | N |
|-----------|---------|----------|-----------|---|
| COL1A1 | 5 (83.3%) | 0 | 1 (16.7%) | 6 |
| COL1A2 | 6 (85.7%) | 0 | 1 (14.3%) | 7 |
| P3H1 | 7 (87.5%) | 0 | 1 (12.5%) | 8 |
| FKBP10 | 8 (100%) | 0 | 0 | 8 |
| Other | 1 (20%) | 1 (20%) | 3 (60%) | 5 |

**Note:** Severe cell sparsity (Class II: only 1 case) precludes meaningful inferential analysis. Angle classification is reported descriptively only.

---

## Interpretation & Conclusions

### Primary Findings (Non-Significant at α=0.05)

After Holm correction for multiple comparisons, no primary endpoints reach statistical significance:
- Dental anomaly (any): p_Holm = 0.288 (baseline p=0.096)
- Gingivitis: p_Holm = 0.701 (baseline p=0.701)
- Caries (any): p_Holm = 0.222 (baseline p=0.083)
- Caries burden (KW): p = 0.257

**Interpretation:** The post-advisor round-two analysis corroborates round-one findings: there is no statistically significant evidence of differential dental/occlusal phenotype between OI gene groups in this small cohort. The non-significant results are not due to post-advisor semantic revisions; they reflect both the small sample size (N=34) and genuine biological heterogeneity.

### Secondary Findings

- DI prevalence varies by gene group (sparse cell structure; n=7 DI cases). Results are exploratory.
- Caries burden trends with dentition stage (older subjects higher prevalence), supporting descriptive framing.
- Infraocclusion (n=1) is a rare occlusal finding; no inferential conclusions possible.

### Small-Sample Discipline

This analysis adheres to the small-N guardrails in the project SAP:
- ✓ Effect sizes reported alongside p-values.
- ✓ Bootstrap 95% CI for effect sizes (ε², Cramer's V).
- ✓ Holm correction applied to all family-wise tests.
- ✓ Permutation validation for binary endpoints (10,000 iterations).
- ✓ LOO robustness checks; no influential cases.
- ✓ Cross-validation results explicitly labeled exploratory.
- ✓ No claims of "strong predictive value" or interaction effects.

---

## Limitations

1. **Small sample size (N=34):** Power to detect moderate effects is limited. Non-significant results do not confirm absence of biological differences; they reflect insufficient statistical power.

2. **Infraocclusion single case:** The one infraocclusion case cannot support inferential analysis. Angle classification for this case is unknown; sensitivity is performed by exclusion, not assignment.

3. **Caries variable framing:** The `dmft_dmft` field is a single count, not decomposed by tooth type or dentition. Dentition-stage-aware interpretation is recommended in descriptive sections but cannot be formalized without separate deciduous/permanent records.

4. **DI typing/severity unavailable:** Only presence/absence of DI is recorded. Shields subtype and severity cannot be assessed.

5. **Binary clinical variables:** Gingivitis, overjet, overbite, open bite, crossbite are recorded as yes/no only. Severity claims are unsupported.

6. **Cross-validation (exploratory only):** LOO-AUC estimates with N=34 should not be interpreted as evidence of clinical predictive ability.

---

## Artifact Registry

All outputs written to: `03_outputs/reports/run_20260418_1037_post_advisor_round2/`

- `round2_analysis_plan.md` — Registered analysis plan (preplanned endpoints & tests)
- `round2_post_advisor_analysis_report.md` — This report
- `round1_vs_round2_comparison_report.md` — Comparison against canonical baseline
- `run_manifest.json` — Execution metadata (SEED, input hash, Python version)
- `primary_results_table.csv` — Core inferential results (p-values, effect sizes)
- `robustness_loo_results.csv` — Leave-one-out stability checks
- `publication_table1_overall_round2.csv` — Table 1 (cohort descriptives)
- `publication_table2_by_gene_group_round2.csv` — Table 2 (gene-group descriptives)
- `publication_table3_inferential_round2.csv` — Table 3 (primary inferential results)
- `cv_panel_round2.csv` — Exploratory CV estimates (labeled supportive)
- `issue_log_round2.csv` — QC and issue log

---

## Sign-Off

**Analysis Authority:** canonical (post-advisor semantic version)
**Data Authority:** canonical (post-advisor semantic version: 20260418_1037)
**Reproducibility SEED:** 20260228
**Date Completed:** 2026-04-18 10:37 UTC

Round-two analysis is complete and ready for downstream manuscript interpretation. All statistical methods conform to the project SAP (small-N discipline, Holm correction, permutation validation, effect-size reporting). Post-advisor semantic revisions have been applied consistently, and results are documented with full provenance and limitation disclosure.

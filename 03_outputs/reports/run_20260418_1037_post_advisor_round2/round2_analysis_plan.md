# Round-Two Post-Advisor Analysis Plan

**Date:** 2026-04-18  
**Run ID:** 20260418_1037_post_advisor_round2  
**Data:** `01_data/derived/osteogenesis_imperfecta_analysis_ready_post_advisor_round2_v1_2026-04-18.csv` (N=34, semantic_version: post_advisor_round2_v1_2026-04-18)  
**SEED:** 20260228  
**Authority:** canonical

---

## Registered Endpoint and Analysis Registry

### Primary Binary Endpoints

| Endpoint | Variable | N Eligible | N Cases | Feasibility | Primary Test | Effect Size | Correction |
|----------|----------|------------|---------|-------------|--------------|------------|-----------|
| Any dental anomaly | `doku_anomalisi_any` | 34 | 10 | Feasible | Exact/Permutation χ² | Cramer's V + prevalence diff (95% Wilson CI) | Holm |
| Gingivitis | `gingivitis` | 34 | 7 | Feasible | Exact/Permutation χ² | Cramer's V + prevalence diff (95% Wilson CI) | Holm |
| Any caries | `caries_any` | 34 | 32 | Feasible | Exact/Permutation χ² | Cramer's V + prevalence diff (95% Wilson CI) | Holm |
| Infraocclusion | `infraokluzyon_var_clean` | 34 | 1 | Supportive only (n=1) | Descriptive + permutation sensitivity | N/A (single case) | N/A |

### Primary Continuous/Count Endpoints

| Endpoint | Variable | N | Test | Effect Size | Validation |
|----------|----------|---|------|------------|------------|
| Caries burden | `caries_count_total` | 34 | Kruskal–Wallis (mandatory) | Epsilon-squared (ε²) | Mann–Whitney U pairwise; LOO stability; permutation alternative |

### Secondary Endpoints (Feasibility-Dependent)

| Endpoint | Variable | N Eligible | Condition | Test | Label |
|----------|----------|------------|-----------|------|-------|
| Angle classification | `angle_sinifi_clean` | 33 | Exclude infraocclusion case (n=1) | Descriptive stratified by gene group | Secondary-only; small N after exclusion |
| DI presence | `di_any` | 34 | If feasible after QC | Presence/absence binary test | Secondary; Shields typing/severity unavailable |
| Dominant anomaly type | `doku_anomalisi_dominant_type` | 34 | Descriptive mapping | Prevalence summary | Descriptive; not inferential phenotyping |

### Supplementary Analyses (Planned but Non-Primary)

1. **Infraocclusion sensitivity scenarios** — If Angle-family inference is performed, optionally test:
   - Scenario A: Assign infraocclusion case to Angle I
   - Scenario B: Assign to Angle II
   - Scenario C: Assign to Angle III
   - Report sensitivity (e.g., "Results would not change if case assigned to Angle II")

2. **Dentition-stage stratified descriptives** — Age-aware caries and anomaly summaries by:
   - Mixed/deciduous (age <6)
   - Mixed (age 6–<14)
   - Permanent (age ≥14)

3. **Leave-One-Out (LOO) robustness** — For each binary endpoint, report:
   - LOO p-min, p-max, delta-p-max
   - Validation of stability across drop-one scenarios

---

## Small-N Guardrails (N=34 Constraints)

- **Effect sizes mandatory.** Always report alongside p-values (Cramer's V for binary, ε² for continuous).
- **Bootstrap 95% CI for effect sizes.** ≥2000 replicates; SEED = 20260228.
- **Multiple comparison correction:** Holm correction applied to all family-wise p-values.
- **Permutation validation:** For binary endpoints, report permutation p alongside classic p (≥10,000 permutations; SEED = 20260228).
- **Suppress predictive overclaiming.** Cross-validation outputs are supportive/exploratory, not confirmatory.
- **Infraocclusion constraint:** Single case (n=1) forces descriptive-only treatment or sensitivity scenarios only.

---

## Data Integrity Gates (Pre-Inference)

Before any inferential analysis:

1. ✓ Confirm post-advisor dataset loads without errors.
2. ✓ Validate `angle_sinifi_clean` contains only 1/2/3 or missing.
3. ✓ Validate `infraokluzyon_var_clean = 1` only where `occl_tip = 4`.
4. ✓ Validate `caries_count_total = dmft_dmft`.
5. ✓ Validate `doku_anomalisi_any = (doku_anomalisi != 0)`.
6. ✓ Validate all binary variables are 0/1.
7. ✓ Check for missing data; document any unexpected patterns.
8. ✓ Report sample size by endpoint and gene group.

---

## Analytic Sequence

### Stage 1: Descriptive Analysis
- Cohort demographics by age, gene group, dentition stage.
- Endpoint prevalence (binary) and distribution (continuous).
- Missing data patterns; if any, investigate root cause.

### Stage 2: Feasibility Gate
- For each planned endpoint, confirm feasibility under observed data structure.
- If sparse cells detected (expected <5), use exact/Fisher–Freeman–Halton or permutation χ² instead of standard χ².
- Document any endpoint downgrades or removals with rationale.

### Stage 3: Primary Inferential Analysis
- Binary endpoints: Exact or permutation χ² (family-wise); Holm correction; effect sizes with CI.
- Continuous endpoint (`caries_count_total`): Kruskal–Wallis (global); Mann–Whitney U (pairwise); Holm correction.

### Stage 4: Robustness & Validation
- LOO stability checks for each primary endpoint.
- Permutation validation (≥10,000 replicates).
- Bootstrap effect-size CI (≥2000 replicates).
- Infraocclusion sensitivity if relevant.

### Stage 5: Comparison Against Round-One Baseline
- Compare round-two results against canonical baseline outputs (pre-advisor semantic state).
- Classify differences: semantic, statistical, implementation, or unexplained.
- Adjudicate whether round-two findings are reproduced, partially reproduced, or unsupported.

---

## Non-Primary / Exploratory Analyses (Decision Gate During Execution)

Additional analyses (labeled appropriately) may be added if:
- A discrepancy with round-one results remains unexplained.
- A primary result is fragile or dependent on one case/coding decision.
- A count/binary representation needs cross-validation.
- An effect is borderline but clinically interesting.

All extra analyses must be:
- Labeled as **validation**, **supportive**, or **exploratory**.
- Documented with trigger, rationale, output files, and effect on conclusions.
- Never silently promoted into primary findings.

---

## Statistical Test Defaults (Post-Advisor SAP)

| Scenario | Test | Alternative if Sparse Cells |
|----------|------|------------------------------|
| Binary vs gene group | Exact or Permutation χ² | Fisher–Freeman–Halton or permutation |
| Binary vs continuous covariate | Penalized logistic or Bayesian logistic | N/A |
| Continuous vs gene group | Kruskal–Wallis | Mann–Whitney U pairwise |
| Count data (caries burden) | Kruskal–Wallis or negative binomial | Permutation KW |

---

## Output Files & Artifacts Registry

All outputs written to `03_outputs/reports/run_20260418_1037_post_advisor_round2/`:

- `round2_analysis_plan.md` — This file.
- `round2_post_advisor_analysis_report.md` — Comprehensive results and interpretation.
- `round1_vs_round2_comparison_report.md` — Comparison against baseline.
- `run_manifest.json` — Execution metadata (script hash, input hash, SEED, Python version, packages).
- `qc_summary.csv` — Data integrity checks.
- `endpoint_registry.csv` — All analyzed endpoints with feasibility decisions.
- `primary_results_table.csv` — Core inferential results (p-values, effect sizes, CI).
- `robustness_loo_results.csv` — Leave-one-out stability checks.
- `permutation_validation_results.csv` — Permutation p-values vs classic p.
- `additional_analyses_index.csv` — Index of any extra analyses (if performed).
- `discrepancy_log.csv` — Any differences from round-one baseline.

---

## Sign-Off & Execution Authority

**Analysis Authority:** canonical (post-advisor semantic version)  
**Data Authority:** canonical (post-advisor semantic version)  
**Output Authority:** 03_outputs/reports/run_20260418_1037_post_advisor_round2/  
**Executable Authority:** Notebook and script in 02_analysis/{notebooks,scripts}/validation/  

Plan registered: 2026-04-18 10:37 UTC  
Ready for execution.

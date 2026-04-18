# Claude Rules for OI Replication & Manuscript Assembly

This file encodes canonical execution rules, variable semantics, statistical guardrails, and escalation policy for the OI oral-dental workspace (N=34, deterministic clinical replication).

---

## Authority and Data Governance

### Execution authority
- **Canonical active lane**: execution authority = `01_data/`, `02_analysis/scripts/active/`, `02_analysis/notebooks/active/`, `03_outputs/active/outputs_FINAL_1_2/`
- **Manuscript/handoff authority**: `Manuscript_Data/` — used only for narrative assembly, variable lineage explanation, and AI-transfer context
- **Archival/legacy files**: `99_archive/`, `03_outputs/legacy/` — may be used only in comparison/audit tasks explicitly marked with `source_authority: archival`
- **Rule**: Never mix canonical and archival paths in normal execution. Archival assets are read-only references; all regenerated outputs go to run-specific folders under `03_outputs/reports/`

### Source_authority enum (mandatory on every task)
- `canonical` — canonical active lane (normal execution)
- `manuscript` — Manuscript_Data/ (handoff/narrative only)
- `archival` — legacy/archive folders (comparison/audit only)
- `reference` — codebooks, gene maps, static references (read-only)

---

## Runtime Transformations (Non-Negotiable)

### `occl_tip` → Angle classification + infraocclusion flag
- **Rule**: Only `occl_tip ∈ {1, 2, 3}` map to Angle Class I/II/III.
- **When `occl_tip == 4`**: This is infraocclusion, NOT an Angle class.
  - Exclude from Angle classification (set primary `angle_sinifi_clean` to NaN).
  - Preserve legacy flag `infraokluzyon_var = 1`; use analysis-facing clean alias `infraokluzyon_var_clean = 1`.
  - Report prevalence of infraocclusion separately.
- **Source**: `Manuscript_Data/06_ai_handoff_context/copilot-instructions.md`

### `dmft_dmft` → count-like interpretation
- **Rule**: `dmft_dmft` is NOT a decomposed DMFT index; it is a count of caries/fillings.
- **Runtime interpretation**: `caries_count_total = dmft_dmft` (legacy alias `caries_count` acceptable for backward compatibility)
- **Binary conversion**: `caries_any = 1 if dmft_dmft > 0 else 0`
- **Never**: Use as an ordinal Likert-scale variable or apply multinomial/ordinal regression without explicit caries-count justification.
- **Source**: `Manuscript_Data/04_final_outputs/OUTPUT_SCHEMA_AND_VARIABLE_LINEAGE.md`

### Gene grouping (runtime derived)
- **Rule**: Gene grouping is NOT a pre-joined column in raw data; it is derived at runtime.
- **Primary grouping rule**: n ≥ 6 → separate group; n < 6 → "Other"
  - Groups: COL1A1, COL1A2, FKBP10, P3H1, Other
- **Grouping logic source**: `Manuscript_Data/01_protocol_and_docs/camber_sap_v2_publication_ready.md` §2.1
- **Validation artifact**: `supplementary_gene_group_map_FINAL.csv`

---

## Statistical Guardrails (SAP-Enforced)

### Guiding reference
- All statistical methods are derived from `Manuscript_Data/01_protocol_and_docs/camber_sap_v2_publication_ready.md` (publication-ready v2).
- No deviations from SAP without explicit Main Agent approval.

### Forbidden patterns
- **No naive Pearson correlation** for binary outcomes (e.g., tissue anomaly presence). Use exact test or permutation test.
- **No naive chi-square** for sparse contingency tables. Use exact/Fisher–Freeman–Halton or permutation χ².
- **No ordinary OLS regression** for binary outcomes. Use penalized logistic (Firth or L2-regularized) or Bayesian logistic.

### Mandatory patterns
- **Binary endpoint** (e.g., `doku_anomalisi_any`, `gingivitis`):
  - Global test: exact or permutation χ² (Fisher–Freeman–Halton if possible).
  - Pairwise: 2×2 Fisher exact or penalized logistic.
  - Effect size: Cramer's V + prevalence differences with 95% Wilson CI.
  - Correction: Holm (for multiple comparisons within family).

- **Continuous endpoint** (e.g., `dmft_dmft`):
  - Global test: **Kruskal–Wallis (mandatory, non-negotiable)**.
  - Effect size: epsilon-squared (ε²).
  - Pairwise: Mann–Whitney U + Holm/FDR if needed.
  - Validation: support with caries_any binary OR count model (negative binomial/Poisson).

- **Multiple comparison correction**:
  - Apply **Holm correction** to all family-wise p-values.
  - Report both classic and permutation-corrected p.

- **Effect sizes**:
  - Always report alongside p-values.
  - Bootstrap 95% CI for each effect size (≥2000 replicates, `SEED = 20260228`).

### Small-N suppressions (N=34 constraints)
- **Cross-validation outputs (AUC, etc.) are exploratory/supportive, not confirmatory**.
  - Report with clear caveat: "CV estimates are supportive and should not be over-interpreted given small sample size."
  - Store in separate CV panel (`cv_panel_FINAL.csv`), not in primary inferential table.
- **Suppress any claim of "strong predictive value"** unless held-out test set ≥10 observations AND delta-AUC ≥0.15.
- **Suppress reporting of interaction terms** unless sample size in each cell ≥5 and interaction p-value ≤ 0.01 (after correction).

### Robustness mandatory
- **Leave-One-Out (LOO) stability**: Run for every primary endpoint. Report LOO p-min, p-max, delta-p-max.
- **Permutation validation**: For binary endpoints, report permutation p alongside classic p (≥10,000 permutations, `SEED = 20260228`).
- **Infraocclusion sensitivity**: Rerun binary endpoint tests with infraocclusion case excluded; report delta-p.

---

## Escalation and Retry Policy

### Maximum remediation ceiling
- **Per task**: 2 attempts to fix + 2 Orchestrator remediations = 4 total interventions.
- **Numeric discrepancies**: If the same numeric mismatch persists after 2 fix attempts (e.g., a p-value or table value does not match baseline), the task is marked `blocked` and escalated to Main Agent **immediately**. Do NOT retry a third time.
- **No blind retry**: Never rerun the pipeline hoping the discrepancy resolves without investigating the root cause first.

### Escalation criteria and actions
- **After 2 remediation rounds with no progress**: Escalate to Main Agent with:
  1. Exact discrepancy (metric, expected value, observed value).
  2. Attempted remediations (with evidence).
  3. Suspected root causes (input mismatch, code drift, environment, method change).
  4. Options (extend deadline, reduce scope, escalate to domain expert).
  5. Recommendation.
- **Red-severity blockers** (e.g., missing required input file, infrastructure failure): Escalate within 30 minutes.
- **Yellow-severity blockers** (e.g., numeric drift ≤5%, investigable): Escalate within 4 hours.

---

## Governance Discipline

### No deletion
- No historical analysis artifacts are deleted, ever.
- Archival wave folders in `99_archive/by_date/` are read-only.

### No overwrite of canonical baselines
- `03_outputs/active/outputs_FINAL_1_2/` is never overwritten in place.
- New runs write to `03_outputs/reports/run_YYYYMMDD_HHMM/`.

### Path exactness
- Always use workspace-root-relative paths (e.g., `01_data/raw/...`, not `../01_data/...`).
- Validate path existence before task assignment.

### Artifact reporting
- After every major replication/comparison cycle:
  - Update `WORKSPACE_INDEX.md` if canonical references changed.
  - Append/update `WORKSPACE_MAP.md` and `workspace_map.csv` if new tracked artifacts introduced.
  - Store dated report files under `03_outputs/reports/`.
  - Update `OPEN_ISSUES_REGISTER.csv` and `NEXT_ACTIONS_14_DAYS.md` if new blockers emerge.

---

## Variable Semantics Summary (Quick Reference)

| Variable | Type | SAP Rule | Runtime Handling |
|---|---|---|---|
| `gen_mutasyonu` | categorical | Derive runtime groups: n≥6 separate, else "Other" | Group COL1A1, COL1A2, FKBP10, P3H1, Other |
| `occl_tip` | ordinal 1–4 | 1–3 = Angle; 4 = infraocclusion | If 4, set `angle_sinifi_clean=NaN`; keep separate infra flag |
| `angle_sinifi_clean` | categorical (1/2/3 or missing) | Primary post-advisor Angle variable | Use only non-missing eligible rows in Angle-family analyses |
| `infraokluzyon_var_clean` | binary (0/1) | Primary clean infra flag | Derived as `occl_tip==4`; keep separate from Angle classes |
| `infraokluzyon_var` | binary (0/1) | Legacy/raw compatibility flag | Preserve for provenance/backward compatibility |
| `dmft_dmft` | count | Interpret as count, not DMFT index | `caries_count_total = dmft_dmft`, `caries_any = (dmft_dmft > 0)` |
| `doku_anomalisi_any` | binary (0/1) | Primary post-advisor binary anomaly endpoint | Exact/permutation χ² family analyses |
| `doku_anomalisi_var` | binary (0/1) | Legacy compatibility endpoint | Retained for backward compatibility / cross-checks |
| `gingivitis` | binary (0/1) | Primary endpoint (binary) | Exact/permutation χ², Holm correction |
| `caries_any` | binary (0/1) | Primary endpoint (binary) | Exact/permutation χ², or Kruskal–Wallis if using `caries_count_total` |
| `yas` | continuous | Primary covariate | Report in years; use in models |
| `dentisyon_donemi_kod` | ordinal 1–3 | Derived from age; do NOT use with age in same model | Stratification only (descriptive) |

---

## Determinism and Reproducibility

### Fixed random seed
- **SEED = 20260228** (mandatory for all stochastic operations).
- Operations: cross-validation folds, permutation tests, bootstrap resampling, Monte Carlo simulations.
- Rule: Pipeline output must be byte-identical on every run (to floating-point tolerance).

### Manifest and metadata tracking
- Before analysis execution: capture `script_hash`, `input_file_hash`, `seed`, `python_version`, `package_versions` in `run_manifest.json`.
- After execution: compare manifest with baseline to detect silent drift.

---

## Expected Agent Behaviors and Hard Bans

### Agent responsibilities
- **Orchestrator**: Scopes tasks, resolves authority, delegates, enforces lifecycle, escalates after ceiling is hit.
- **Path Guard**: Rejects ambiguous/archival paths; validates `source_authority` enum.
- **Input QA**: Validates schema, missingness, OI semantics (occl_tip, dmft_dmft, gene grouping).
- **Output Diff**: Compares regenerated vs baseline; classifies discrepancies by severity and delta type.
- **Stat Guard**: Blocks invalid tests, enforces SAP rules, suppresses overclaiming.
- **Claim Auditor**: Maps claims to evidence; rates as robust/tentative/exploratory/unsupported; detects CV overclaiming.
- **Reproducibility Sentinel**: Validates seed consistency and manifest integrity before runs.
- **Section Routing Guard**: Routes manuscript sections safely; grounds Methods/Results in output evidence.

### Hard bans on all agents
- **No hallucination of clinical rules**. Only use workspace documentation (`copilot-instructions.md`, codebooks, SAP).
- **No silent data drops or type coercions**. Fail-fast on unexpected values.
- **No deletion of historical artifacts**.
- **No override of governance rules** (authority, escalation ceiling, reporting discipline).

---

## Completion Criteria for Major Tasks

A replication cycle is **complete** when:
1. Canonical notebook runs end-to-end without path breaks.
2. Core expected output tables (Table 1–3, robustness, CV panel, master table) are regenerated.
3. Input QA auditor confirms schema and variable semantics match baseline codebook.
4. Output diff auditor compares regenerated vs baseline; severity matrix is complete.
5. Statistical method guard confirms all tests obey SAP rules; overclaiming is suppressed.
6. Claim auditor produces claim matrix with confidence classes and caveats.
7. Run report (RUN_REPORT_TEMPLATE.md) is filled with evidence and artifacts saved in dated run folder.
8. Comparison report (COMPARE_RESULTS_TEMPLATE.md) classifies discrepancies, documents root causes, and issues acceptance decision (Accept/Conditional/Reject).
9. Any unresolved critical issues are escalated to Main Agent with full context.

---

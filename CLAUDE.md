# CLAUDE.md

Operational rules for Claude in the `osteogenesis_imperfecta` workspace.

## Scope

- This project is a small-N (n=34) OI oral-dental analysis and manuscript assembly workspace.
- Use only workspace evidence for clinical/statistical interpretation; do not add external clinical assumptions.

## Authority and Path Rules

- Manuscript-facing authority: `04_manuscript/`.
- Baseline/provenance lanes (not manuscript authority): `03_outputs/active/`, `Manuscript_Data/`.
- Canonical analysis entry points:
  - Notebook: `02_analysis/notebooks/active/oi_oro_dental_master_FINAL_1_2.ipynb`
  - Script: `02_analysis/scripts/active/oi_oro_dental_master_FINAL_1_2.py`
- Do not delete historical artifacts; preserve traceability.

## Data Semantics (Non-Negotiable)

- `occl_tip`:
  - Only `1/2/3` are Angle classes.
  - `occl_tip == 4` means infraocclusion, not Angle class.
  - Set `infraokluzyon_var = 1` (analysis alias: `infraokluzyon_var_clean`) and exclude from Angle analyses (`NaN`).
- `dmft_dmft`:
  - Treat as count-like caries/filling burden, not decomposed formal DMFT index.
  - Binary derivation must be `caries_any = (dmft_dmft > 0)`.

## Statistical Guardrails (Small-N)

- If expected cell count < 5, do not use standard Pearson chi-square.
- Use exact/permutation alternatives for sparse categorical analyses.
- Use non-parametric defaults for continuous outcomes:
  - 2 groups: Mann-Whitney U
  - >=3 groups: Kruskal-Wallis
- Report effect sizes with tests:
  - Cramer's V for categorical test families
  - Epsilon-squared for Kruskal-Wallis
- Apply Holm correction for multi-comparison families by default.
- For logistic models in low n, prefer penalized L2/Ridge or Firth logistic.

## Reproducibility and Safety

- Fix all stochastic procedures with `SEED = 20260228`.
- Fail fast on invalid values/types (for example, binary field has value `2`, negative age).
- On fail-fast events, log issues to:
  - `01_data/derived/issue_log_post_advisor_round2_v1_2026-04-18.csv`
  - Keep legacy mirror `issue_log_v3.csv` when required.

## Modeling Constraint

- Never include `yas` and `dentisyon_donemi_kod` in the same multivariate model.
- If one chronological covariate is needed, use `yas`.

## Working Style

- Plan first, execute second: Discovery -> Hypothesis -> Code -> Error handling -> Verification.
- Document exclusions, merged categories, and anomaly handling in user-facing Markdown under a clear decision rationale.
- Keep edits surgical: preserve existing structure unless a change is necessary and evidence-backed.

## Primary References

- `AGENTS.md`
- `.github/copilot-instructions.md`
- `README.md`
- `01_data/README.md`
- `02_analysis/README.md`
- `03_outputs/README.md`
- `04_manuscript/README.md`


# 🤖 Multi-Agent & System Rules (Osteogenesis Imperfecta Analysis)

This workspace is a pediatric disease reporting ecosystem with a small sample size (n=34). Copilot, Claude, and all autonomous assistants must strictly follow the analytical and architectural protocols below.

## 1. Planning and Execution Architecture
- **Multi-Step Planning:** Do not rush user requests directly into code. First design a step-by-step analysis strategy (e.g., Discovery -> Hypothesis building -> Coding -> Error handling -> Verification). If needed, use a `switch_agent` style exploration mode.
- **Full Transparency:** Any cases (`hasta_kodu`) excluded for analytical reasons, merged categories, or ignored anomalies must not stay only in code. They must be clearly reported in user-facing Markdown under a "Decision Rationale" section and also written to `01_data/derived/issue_log_post_advisor_round2_v1_2026-04-18.csv`. For legacy compatibility, keep an equivalent copy in `issue_log_v3.csv` when required.
- **Authority-Domain Discipline:** Manuscript-facing authority is always under `04_manuscript/`; `03_outputs/active/` and `Manuscript_Data/` are baseline/provenance lanes and cannot be used as manuscript authority.
- **Canonical Analysis Entry Point:** Primary entry for current reproduction is `02_analysis/notebooks/active/oi_oro_dental_master_FINAL_1_2.ipynb`; use `02_analysis/scripts/active/oi_oro_dental_master_FINAL_1_2.py` as the script counterpart.
- **Clinical Hallucination Ban:** Clinical thresholds, phenotype rules, and diagnostic interpretations must be derived only from workspace sources (`01_data/reference/`, codebook/SAP/metadata docs); do not introduce external clinical rules.

## 2. Strict Analytical Standards (N=34 Constraints)
- **Small-Cell Prohibition (Categorical Data):** If expected cell count is < 5 in contingency tables or hypothesis tests, **abandon standard Pearson chi-square immediately**. Use **permutation testing (preferably >10k iterations) or Fisher-Freeman-Halton / exact methods** instead.
- **Continuous Data Standards:** Most distributions must be treated as non-parametric/non-normal. For two-group comparisons use **Mann-Whitney U**; for three or more groups use **Kruskal-Wallis** only.
- **Occlusion Red Line (`occl_tip`):** Only `1/2/3` are Angle classes. If `occl_tip == 4`, flag `infraokluzyon_var = 1` (analysis-facing alias: `infraokluzyon_var_clean`) and exclude from Angle analyses as `NaN`.
- **DMFT Interpretation Rule (`dmft_dmft`):** This field is not a decomposed official DMFT index; it is a count variable. If binary conversion is needed, derive `caries_any` only via `dmft_dmft > 0`.

## 3. Model Reliability and Penalty/Correction Rules
- **Overfitting Control Principle:** Because of low n, prefer **penalized Ridge/L2 or Firth logistic** models over classical MLE logistic regression to prevent coefficient explosion.
- **FDR / Multiple-Comparison Corrections:** When listing p-values, apply **Holm-Bonferroni (Holm adjustment)** by default across all families and include corrected values in tables.
- **Effect Size Requirement:** Results cannot be reported with p-values only. Include **Cramer's V (Cramer's phi)** for chi-square/permutation families and **$\varepsilon^2$ (epsilon-squared)** for Kruskal-Wallis analyses.
- **Deterministic Reproducibility:** In all stochastic procedures (permutation/bootstrap/CV), fix `SEED = 20260228`; identical input must produce identical statistical outputs.

## 4. Multicollinearity (Dependent Data) Alert
- In no multivariate regression/statistical model should `yas` and `dentisyon_donemi_kod` be included **at the same time**. One is effectively derived from the other and destabilizes the model. If you run model-based analyses, the primary chronological covariate must be `yas`.
- **Fail-Fast Requirement:** If unexpected data types/values are detected (e.g., value `2` in a binary field, negative age), the analysis must not continue silently; stop with `assert`, raise the error, and log it to `01_data/derived/issue_log_post_advisor_round2_v1_2026-04-18.csv` (and `issue_log_v3.csv` if needed).

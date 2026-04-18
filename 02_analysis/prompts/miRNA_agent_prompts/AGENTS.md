# Notebook instructions

Before doing anything, read `miRNA-qPCR-reanalysis.md` completely and treat it as the governing workflow specification.

Workspace-critical rules:
- Main deliverable: `miRNA_qpcr_reanalysis.ipynb`
- Primary data file: `miRNA-qPCR-analysis-results.csv`
- All observable computations must happen inside notebook cells
- No hidden preprocessing or off-notebook scripts
- Notebook must run from a fresh kernel without manual intervention
- Save major outputs to `outputs/`
- Keep fixed groups exactly:
  - S = Healthy
  - G = Gingivitis
  - P = Periodontitis
- Keep fixed tasks exactly:
  - Task 1 = S vs G
  - Task 2 = G vs P
  - Task 3 = S vs P
- Use leakage-safe logic for classification and feature selection
- Label exploratory analyses clearly
- If anything is ambiguous or impossible, document it explicitly in the notebook and use the most defensible interpretation

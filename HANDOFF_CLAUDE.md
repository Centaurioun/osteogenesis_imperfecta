# Claude Handoff Guide (Replication + Comparison)

This document is for opening this workspace in Claude and reproducing analysis results reliably.

## 1) Primary objective

- Re-run the canonical active analysis pipeline.
- Compare canonical results with legacy versions.
- Document any differences with evidence (paths, metrics, outputs).

## 2) Canonical files to use first

- Notebook: `02_analysis/notebooks/active/oi_oro_dental_master_FINAL_1_2.ipynb`
- Script pair/support: `02_analysis/scripts/active/`
- Inputs:
  - `01_data/raw/osteogenesis_imperfecta_camber_input_minimal_v1.csv`
  - `01_data/reference/codebook_v3_fixed.md`
  - `01_data/reference/gene_map_v1.csv`
- Expected active outputs: `03_outputs/active/outputs_FINAL_1_2/`

## 3) Comparison targets (legacy)

- Legacy notebooks: `02_analysis/notebooks/legacy/`
- Legacy scripts: `02_analysis/scripts/legacy/`
- Legacy outputs: `03_outputs/legacy/`

## 4) Replication workflow in Claude

1. Read `WORKSPACE_INDEX.md` and `README.md`.
2. Inspect active notebook + active scripts.
3. Run canonical analysis and regenerate outputs.
4. Compare with `03_outputs/active/outputs_FINAL_1_2/`.
5. Run targeted comparisons vs legacy outputs.
6. Record deltas in a comparison report (with file paths and reasons).

## 5) What to ignore (unless needed)

- Environment/editor internals: `.venv/`, `.vscode/`, `.tmp.driveupload/`, `.codex/`
- Archived historical bundles under `99_archive/by_date/` unless you need provenance checks.

## 6) Six-cycle refined recommendations (final)

These suggestions were iteratively refined across six passes before finalizing:

### Cycle 1 — Baseline
- Use one canonical notebook as source of truth.
- Avoid executing legacy variants unless comparing.

### Cycle 2 — Path discipline
- Do not run from root assumptions; use explicit relative paths from workspace root.
- Treat `03_outputs/active` as expected target output set.

### Cycle 3 — Provenance
- For every comparison difference, log: metric/file/path + possible cause.
- Keep move/inventory logs untouched.

### Cycle 4 — Reproducibility hardening
- Fix environment drift before comparison.
- Prefer deterministic execution settings in analysis code.

### Cycle 5 — Structure hygiene
- Keep new artifacts inside domain folders, never loose at root.
- Place ad hoc exploratory outputs in clearly labeled subfolders (e.g., `03_outputs/reports/`).

### Cycle 6 — Operational maturity (final)
- Adopt a strict run-report template:
  - run date/time
  - inputs used
  - notebook/script commit/version
  - outputs generated
  - delta summary vs baseline
- Review/update `workspace_map.csv` and `WORKSPACE_INDEX.md` after each major run.

## 7) If you need to extend analysis

- Add new notebooks under `02_analysis/notebooks/active/` only when they become part of canonical flow.
- Put one-off experiments under `02_analysis/validation/` or clearly scoped subfolders.
- Never delete old versions; move superseded materials to `03_outputs/legacy/` or `99_archive/` with logs.

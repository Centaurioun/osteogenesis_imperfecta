# 02_STRUCTURE_AND_NAVIGATION

## Top-level domains

- `../00_governance/` — project docs/context
- `../01_data/` — raw/reference/derived data assets
- `../02_analysis/` — notebooks/scripts/prompts/validation
- `../03_outputs/` — active + legacy outputs
- `../04_manuscript/` — manuscript-facing integration
- `../05_operations/` — operational logs/manifests/automation
- `../99_archive/` — archival storage + provenance indexes
- `../Manuscript_Data/` — structured manuscript package

## What to use vs ignore

Use first:
- `../02_analysis/notebooks/active/`
- `../02_analysis/scripts/active/`
- `../03_outputs/active/outputs_FINAL_1_2/`
- `../01_data/raw/` and `../01_data/reference/`

Ignore unless needed:
- `../.venv/`, `../.vscode/`, `../.tmp.driveupload/`, `../.codex/`
- old archive payloads under `../99_archive/by_date/` (except provenance audits)

## Fast map files

- `../WORKSPACE_MAP.md`
- `../workspace_map.csv`
- `../99_archive/indexes/archive_lookup.csv`

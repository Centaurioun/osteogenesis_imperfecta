# Workspace Map

## Top-level map

```text
osteogenesis_imperfecta/
├─ 00_governance/     # project docs, governance, high-level context
├─ 01_data/           # raw/reference/derived data assets
├─ 02_analysis/       # notebooks, scripts, prompts, validation
├─ 03_outputs/        # active outputs and legacy outputs
├─ 04_manuscript/     # manuscript-facing integration area
├─ 05_operations/     # logs/manifests/automation
├─ 99_archive/        # historical archive (no-delete)
├─ Manuscript_Data/   # structured manuscript package
├─ WORKSPACE_INDEX.md
├─ WORKSPACE_ORGANIZATION_PLAN.md
├─ workspace_map.csv
└─ HANDOFF_CLAUDE.md
```

## Canonical replication path

1. `01_data/raw/` + `01_data/reference/`
2. `02_analysis/notebooks/active/oi_oro_dental_master_FINAL_1_2.ipynb`
3. `02_analysis/scripts/active/` (support scripts)
4. `03_outputs/active/outputs_FINAL_1_2/`

## Historical comparison path

- Legacy notebooks/scripts: `02_analysis/notebooks/legacy/`, `02_analysis/scripts/legacy/`
- Legacy outputs: `03_outputs/legacy/`
- Archived waves and move logs: `99_archive/`

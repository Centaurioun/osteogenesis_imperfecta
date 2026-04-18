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

## Post-advisor semantic control path (additive)

- Controlling report: `OI_POST_ADVISOR_DATA_SEMANTICS_AND_ROUND2_REANALYSIS_STATUS_REPORT.md`
- Decision memo: `data_decisions_post_advisor_round2.md`
- Codebook addendum: `01_data/reference/codebook_post_advisor_round2_addendum_v1.md`
- Analysis-ready semantic dataset: `01_data/derived/osteogenesis_imperfecta_analysis_ready_post_advisor_round2_v1_2026-04-18.csv`
- Builder script: `02_analysis/scripts/active/create_post_advisor_round2_dataset.py`

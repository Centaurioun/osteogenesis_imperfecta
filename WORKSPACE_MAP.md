# Workspace Map

## Top-level map

```text
osteogenesis_imperfecta/
├─ 00_governance/     # project docs, governance, high-level context
├─ 01_data/           # raw/reference/derived data assets
├─ 02_analysis/       # notebooks, scripts, prompts, validation
├─ 03_outputs/        # baseline, legacy, and provenance outputs
├─ 04_manuscript/     # manuscript-facing round-two authority package
├─ 05_operations/     # logs/manifests/automation and bundle mirrors
├─ 99_archive/        # historical archive (no-delete)
├─ Manuscript_Data/   # structured manuscript package
├─ archive_misaligned/ # residual zone; human review required
├─ agents/            # residual zone; human review required
├─ WORKSPACE_INDEX.md
├─ WORKSPACE_ORGANIZATION_PLAN.md
├─ workspace_map.csv
└─ HANDOFF_CLAUDE.md
```

## Manuscript-facing path

1. `04_manuscript/`
2. `01_data/raw/` + `01_data/reference/`
3. `02_analysis/notebooks/validation/` and `02_analysis/scripts/validation/`
4. `03_outputs/active/outputs_FINAL_1_2/`

## Historical comparison path

- Legacy notebooks/scripts: `02_analysis/notebooks/legacy/`, `02_analysis/scripts/legacy/`
- Legacy outputs: `03_outputs/legacy/`
- Archived waves and move logs: `99_archive/`

## Provisional round-two path

- Non-reconciled run folder: `03_outputs/reports/run_20260418_1037_post_advisor_round2/`
- Reconciled provenance source: `03_outputs/reports/run_20260418_1037_post_advisor_round2_colab/`
- Operational bundle mirror: `05_operations/colab_bundles/oi_round2_post_advisor_colab_bundle_20260418/`

## Post-advisor semantic control path (additive)

- Controlling report copy: `04_manuscript/context/semantic_control/OI_POST_ADVISOR_DATA_SEMANTICS_AND_ROUND2_REANALYSIS_STATUS_REPORT.md`
- Decision memo copy: `04_manuscript/context/semantic_control/data_decisions_post_advisor_round2.md`
- Codebook addendum: `01_data/reference/codebook_post_advisor_round2_addendum_v1.md`
- Analysis-ready semantic dataset: `01_data/derived/osteogenesis_imperfecta_analysis_ready_post_advisor_round2_v1_2026-04-18.csv`
- Builder script: `02_analysis/scripts/active/create_post_advisor_round2_dataset.py`
- Provenance note copy: `04_manuscript/context/provenance_note.md`

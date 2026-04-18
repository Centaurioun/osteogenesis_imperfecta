# Osteogenesis Imperfecta Oral-Dental Analysis Workspace

This workspace contains reproducible analysis assets for an osteogenesis imperfecta (OI) oral-dental study, including source data mappings, analysis notebooks/scripts, publication outputs, and archived historical runs.

## What this project is about

- Reproducing and validating OI oral-dental analyses across multiple historical versions.
- Preserving a round-one baseline lane while surfacing a manuscript-facing round-two authority package.
- Supporting manuscript-ready outputs and handoff to collaborators/tools (including Claude).

## Start here (quick navigation)

1. `04_manuscript/README.md` — manuscript-facing round-two package entry point.
2. `WORKSPACE_INDEX.md` — current operating references and key files.
3. `CLAUDE_HANDOFF/README.md` — complete Claude-ready handoff package.
4. `HANDOFF_CLAUDE.md` — concise handoff guide for replication/comparison workflows.
5. `WORKSPACE_ORGANIZATION_PLAN.md` — structure policy and maintenance rules.
6. `WORKSPACE_MAP.md` — high-level folder-purpose map.

## Current authority lanes

- Manuscript-facing authority: `04_manuscript/`
- Round-one baseline notebook: `02_analysis/notebooks/active/oi_oro_dental_master_FINAL_1_2.ipynb`
- Round-one baseline script: `02_analysis/scripts/active/oi_oro_dental_master_FINAL_1_2.py`
- Round-one baseline outputs: `03_outputs/active/outputs_FINAL_1_2/`
- Round-one baseline figures: `03_outputs/active/figures_FINAL_1_2/`

## Main folders

- `00_governance/` — project documentation and governance context.
- `01_data/` — raw/reference/derived data assets.
- `02_analysis/` — notebooks, scripts, prompts, and validation workspaces.
- `03_outputs/` — baseline, legacy, and provenance outputs.
- `04_manuscript/` — manuscript-facing round-two authority package.
- `05_operations/` — logs/manifests/automation utilities and bundle mirrors.
- `99_archive/` — no-delete historical archive with move logs.
- `Manuscript_Data/` — preserved historical FINAL_1_2 manuscript package and baseline reference set.
- `CLAUDE_HANDOFF/` — operational handoff packet (status, playbooks, templates, open issues).

## Ignore for day-to-day analysis

These are not core replication targets unless debugging environment/tooling:

- `.venv/`, `.vscode/`, `.tmp.driveupload/`, `.codex/`
- Internal agent/plugin internals under `.agents/` unless editing agent skills

## Rules

- No deletion of historical files.
- Use `workspace_map.csv` and archive logs for traceability.
- Add new analysis versions instead of overwriting old ones.
- Keep root clean; place new work in the correct domain folder.

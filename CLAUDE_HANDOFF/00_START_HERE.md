# 00_START_HERE

## Objective
Replicate the OI oral-dental analysis with the canonical pipeline, then compare outputs to legacy generations and document any deltas.

## Canonical execution targets

- Notebook: `../02_analysis/notebooks/active/oi_oro_dental_master_FINAL_1_2.ipynb`
- Script support: `../02_analysis/scripts/active/`
- Active outputs baseline: `../03_outputs/active/outputs_FINAL_1_2/`

## Primary references

- `../WORKSPACE_INDEX.md`
- `../WORKSPACE_MAP.md`
- `../WORKSPACE_ORGANIZATION_PLAN.md`
- `agent-architecture.md` (inside `CLAUDE_HANDOFF/`)
- `AGENT_PLAN_REVIEW_PROMPT.md` (mandatory if creating agents)

## Preflight checks (run before execution)

1. Confirm canonical notebook exists:
	- `../02_analysis/notebooks/active/oi_oro_dental_master_FINAL_1_2.ipynb`
2. Confirm baseline outputs folder exists:
	- `../03_outputs/active/outputs_FINAL_1_2/`
3. Confirm input references exist:
	- `../01_data/raw/osteogenesis_imperfecta_camber_input_minimal_v1.csv`
	- `../01_data/reference/codebook_v3_fixed.md`
	- `../01_data/reference/gene_map_v1.csv`

If any required path is missing, stop and record the exact missing path in the issue register.

## Pre-creation architecture review (mandatory for agent launch)

Before creating any sub-agents:
1. Run `AGENT_PLAN_REVIEW_PROMPT.md` in Claude.
2. Produce a review packet with risks, improvements, and go/no-go recommendation.
3. Obtain explicit approval on that packet.
4. Only then proceed with agent creation.

## Quick constraints

- Do not delete historical files.
- Do not overwrite old versions.
- Record run metadata and comparison outcomes with evidence.

## Required output artifacts per run

- One run report (from `RUN_REPORT_TEMPLATE.md`)
- One comparison report (from `COMPARE_RESULTS_TEMPLATE.md`)
- Issue register updates for unresolved findings

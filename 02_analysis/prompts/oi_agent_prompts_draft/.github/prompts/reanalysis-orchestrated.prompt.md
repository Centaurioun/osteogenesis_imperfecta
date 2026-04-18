---
name: reanalysis-orchestrated
description: "Use when running an end-to-end OI analysis workflow with staged prompts and specialist agent review passes."
tools:
  - agent
  - read
  - search
  - edit
---

Goal:
Coordinate the full OI workflow from preprocessing to reporting with conservative interpretation and explicit uncertainty handling.

Input schema:
- project_context: string
- data_assets: list[path]
- analysis_scope: list[preprocessing,variant,de,pathway,database,target,report]
- constraints:
  - reproducibility_seed: int
  - thresholds: dict

Output schema:
- stage_status_table: csv/markdown
- risk_register: markdown
- deliverables_map: csv
- next_actions: markdown

Execution order:
1) `data-preprocessing.prompt.md`
2) `variant-analysis.prompt.md`
3) `differential-expression.prompt.md`
4) `pathway-network-analysis.prompt.md`
5) `literature-database-integration.prompt.md`
6) `therapeutic-target-prioritization.prompt.md`
7) `report-generation.prompt.md`

Error handling:
- If mandatory input missing, mark stage `blocked`, log assumption, propose minimum safe fallback.
- If tool output conflicts with source evidence, downgrade claim confidence and add discrepancy note.

# 06_WORKING_AGREEMENTS

## Working rules

1. No deletions of historical analysis artifacts.
2. No overwriting historical versions.
3. Keep root clean (no new loose analysis files).
4. Use explicit paths from workspace root.
5. Keep provenance indexes up to date after major moves.
6. Do not create agents before architecture review packet is approved.

## Naming hygiene

- Prefer snake_case and explicit version tags.
- Add run date markers for temporary comparison reports.

## Update discipline

After each major replication/comparison cycle:
- update `../WORKSPACE_INDEX.md` if canonical references changed
- append/update `../workspace_map.csv` if new tracked artifacts are introduced
- store dated report files under `../03_outputs/reports/`
- update `OPEN_ISSUES_REGISTER.csv` and `NEXT_ACTIONS_14_DAYS.md`

Before each agent-creation cycle:
- run `AGENT_PLAN_REVIEW_PROMPT.md` against `agent-architecture.md`
- store review packet and explicit go/no-go decision

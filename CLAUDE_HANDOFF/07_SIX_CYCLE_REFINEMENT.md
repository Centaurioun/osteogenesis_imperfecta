# 07_SIX_CYCLE_REFINEMENT

These are the six iterative refinement cycles applied to recommendations before finalization.

## Cycle 1 — Baseline clarity
- One canonical notebook for default runs.
- Legacy assets comparison-only by default.

## Cycle 2 — Path discipline
- Enforce explicit workspace-root-relative paths.
- Define exact baseline output directory.

## Cycle 3 — Provenance hardening
- Every delta must include source/target evidence.
- Keep inventory/move logs untouched.

## Cycle 4 — Reproducibility hardening
- Capture environment notes with each run.
- Separate run metadata from interpretation.

## Cycle 5 — Structure hygiene
- Keep new artifacts in domain folders.
- Place comparison reports in `03_outputs/reports/`.

## Cycle 6 — Operational maturity
- Standard templates for run/comparison.
- Post-run index maintenance workflow.

---

## Second 6-cycle pass (2026-04-17)

### Cycle 1 — Starter onboarding
- Added `CLAUDE_PROMPT_STARTER.md` for copy-paste bootstrap.

### Cycle 2 — Sequencing clarity
- Updated handoff read order and startup flow for deterministic onboarding.

### Cycle 3 — Replication safeguards
- Added preflight checks and fail-fast stop conditions in startup/playbook docs.

### Cycle 4 — Comparison rigor
- Added severity tiers and acceptance decision matrix.

### Cycle 5 — Risk/issue operationalization
- Added `OPEN_ISSUES_REGISTER.csv` and `NEXT_ACTIONS_14_DAYS.md`.

### Cycle 6 — Final consistency polish
- Synchronized cross-file references and update discipline rules.

---

## Third 6-cycle pass (2026-04-17, agent architecture integration)

### Cycle 1 — Architecture quality review
- Performed a new 6-cycle refinement of `agent-architecture.md`.

### Cycle 2 — Pre-creation gate
- Added mandatory Claude review gate before any agent creation.

### Cycle 3 — Protocol hardening
- Added lifecycle `Plan-Review` stage and stricter signoff conditions.

### Cycle 4 — Developer readiness
- Added implementation rollout phases and stronger acceptance rules.

### Cycle 5 — Handoff integration
- Copied `agent-architecture.md` into `CLAUDE_HANDOFF/` and integrated it into read order.

### Cycle 6 — Starter workflow enforcement
- Updated starter/start-here docs to require review packet approval prior to agent launch.

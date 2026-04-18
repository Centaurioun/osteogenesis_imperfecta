# AGENT_PLAN_REVIEW_PACKET_EXAMPLE

## summary

The architecture is **conditionally ready**. Core design is strong (clear hierarchy, orchestration lifecycle, QA gates), but launch should wait until three high-impact controls are enforced: (1) explicit data-class policy per task payload, (2) deterministic retry/remediation limits wired into orchestrator config, and (3) one-run pilot with measured KPI thresholds. After these are satisfied, proceed with staged activation (Orchestrator+QA first, then specialists, then manuscript lane).

## risk_register

| risk_id | severity | area | description | evidence (section) | mitigation | owner | due |
|---|---|---|---|---|---|---|---|
| R-001 | critical | security | Task payload schema lacks explicit `data_classification` field, risking accidental restricted-data routing. | `agent-architecture.md` §8 + §6.1 | Add mandatory `data_classification` and `allowed_roles` fields to every task message. Reject tasks missing them. | Orchestrator Owner | +2 days |
| R-002 | major | reliability | Retry/remediation logic is described but not bound to environment-specific defaults. | §6.5 | Create environment profile: `dev/staging/prod` with explicit N/M and timeout values. | Platform Lead | +3 days |
| R-003 | major | governance | No explicit signoff artifact path for plan-review output. | §2.1, §10 | Require signed review artifact under `CLAUDE_HANDOFF/review_packets/`. | Main Agent Delegate | +1 day |
| R-004 | major | quality | QA pass criteria are defined but no “waiver policy” template exists for urgent ship decisions. | §2, §10 | Add waiver template requiring Main Agent rationale + expiry date. | QA Lead | +4 days |
| R-005 | minor | operations | KPI dashboard fields exist but no threshold bands for Green/Yellow/Red are set. | §7.3 | Define threshold bands and alert triggers for each KPI. | Orchestrator Owner | +5 days |

## recommended_changes

| change_id | priority | change | expected impact | implementation note |
|---|---|---|---|---|
| C-001 | P0 | Add `data_classification`, `allowed_roles`, `retention_class` to task schema. | Prevents policy drift and accidental data exposure. | Update message validator and reject non-compliant tasks. |
| C-002 | P0 | Add `review_packet_path` and `approval_status` fields before agent creation. | Enforces pre-creation gate. | Required in `Plan-Review` -> `Assigned` transition. |
| C-003 | P1 | Define environment-specific retry/timeout profiles. | Improves reliability and predictable SLA behavior. | Use YAML profile loaded by Orchestrator at startup. |
| C-004 | P1 | Add QA waiver template with TTL and owner. | Controlled exceptions without losing auditability. | Store waivers in `05_operations/manifests/`. |
| C-005 | P2 | Add KPI thresholds + automatic status color calculation. | Faster executive visibility. | Compute `status_color` in weekly dashboard job. |

## updated_message_schema

```json
{
  "task_id": "TASK-2026-00123",
  "owner": "Orchestrator",
  "assignee": "DataAnalyst",
  "description": "Clean dataset X to schema Y and run EDA checks",
  "inputs": ["path/to/raw.csv", "path/to/schema.md"],
  "expected_outputs": ["clean.csv", "eda_report.md", "quality_checks.json"],
  "deadline": "2026-04-21T18:00:00Z",
  "priority": "high",
  "retry_policy": {"max_retries": 2, "retry_delay_min": 30},
  "acceptance_criteria": [
    "No nulls in required columns",
    "All transformations documented",
    "QA checklist passes"
  ],
  "data_classification": "internal",
  "allowed_roles": ["DataAnalyst", "QAVerifier", "Orchestrator"],
  "retention_class": "project_12m",
  "review_packet_path": "CLAUDE_HANDOFF/review_packets/review_2026-04-17.md",
  "approval_status": "approved"
}
```

## go_no_go

- **decision**: `CONDITIONAL_GO`
- **rationale**: Core architecture is implementation-ready, but launch safety depends on schema hardening and approval artifact enforcement.

## launch_conditions

1. C-001 and C-002 completed and validated.
2. One pilot sprint (3–5 tasks) executed with:
   - QA first-pass rate >= 80%
   - no unresolved critical blocker
   - mean time to completion within agreed SLA band
3. Main Agent signs launch note referencing review packet path.

## final implementation recommendation

Proceed with phased rollout exactly as in `agent-architecture.md` §12 (Phase 0 -> Phase 4), and keep this packet as the benchmark format for future reviews.

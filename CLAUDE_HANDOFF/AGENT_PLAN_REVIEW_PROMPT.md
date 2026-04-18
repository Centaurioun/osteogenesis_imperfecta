# AGENT_PLAN_REVIEW_PROMPT

Use this prompt in Claude **before creating any agents**.

---

You are reviewing an agent-system architecture before implementation.

Workspace root:
`<WORKSPACE_ROOT>/`

Read first:
1. `CLAUDE_HANDOFF/agent-architecture.md`
2. `CLAUDE_HANDOFF/00_START_HERE.md`
3. `CLAUDE_HANDOFF/06_WORKING_AGREEMENTS.md`

Task:
- Critique and improve the agent architecture in `CLAUDE_HANDOFF/agent-architecture.md`.
- Do **not** create agents yet.
- Produce a review packet with implementation-ready improvements.

Required outputs:
1. Top 5 architecture risks + mitigation for each.
2. Role overlap/ambiguity analysis (Main/Orchestrator/Sub-agents).
3. SLA/retry/timeout tuning recommendations.
4. Security/privacy/compute constraint gaps.
5. Protocol gaps in lifecycle, escalation, and QA gating.
6. Simplification opportunities to reduce cost/latency.
7. Final Go/No-Go recommendation with explicit conditions.

Output format:
- `summary`
- `risk_register` table
- `recommended_changes` table
- `updated_message_schema` (if needed)
- `go_no_go` + `launch_conditions`

Hard rules:
- No agent creation until review is approved.
- Every recommendation must reference exact section(s) of `agent-architecture.md`.
- If uncertain, mark as assumption and request confirmation.

---

Completion criterion:
A reviewer can approve/reject implementation using your output without additional clarification.

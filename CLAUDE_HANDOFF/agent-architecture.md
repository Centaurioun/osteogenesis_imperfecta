# agent-architecture

## 1) One-paragraph summary

This document defines a concrete multi-agent operating model with a **Main Agent (Owner)**, a single **Orchestrator Agent**, and specialist **Sub-Agents** for analytics and documentation, plus a second orchestrated set for manuscript drafting. The architecture is designed for implementation: explicit roles, skills, SLAs, message schemas, lifecycle states, retries/escalation, QA gates, KPI reporting, and security/compute constraints are included. Communication is hub-and-spoke (only via Orchestrator), with deterministic templates for assignments, status updates, and signoff, so teams can run repeatable sprints with low ambiguity and controlled risk.

---

## 2) Scope and design principles

1. **Single coordination hub**: all sub-agent communication routes through Orchestrator.
2. **Separation of concerns**: each specialist has clear scope and acceptance criteria.
3. **Fail-fast and traceability**: structured task updates, retries, escalations, and logs.
4. **Quality-gated completion**: no task is “Done” without QA/Verifier check (unless explicitly waived by Main Agent).
5. **Cost- and risk-aware execution**: timeouts, compute caps, and data-class restrictions per agent.

### 2.1 Mandatory pre-creation review gate (Claude improvement pass)

Before creating any agents, run a **Plan Review Gate** where Claude critiques and improves this architecture.

Required outputs from the gate:
1. Top 5 design risks and mitigations.
2. Role overlap/conflict analysis.
3. Recommended SLA/retry threshold tuning.
4. Proposed simplifications to reduce latency/cost.
5. Final go/no-go decision with rationale.

**Rule**: No agent instantiation until Main Agent approves the review output.

---

## 3) Agent hierarchy (high-level)

- **Main Agent (Owner)**
  - Strategic oversight, scope changes, priority decisions, major approvals.
- **Orchestrator Agent (Coordinator)**
  - Decomposition, assignment, progress tracking, aggregation, QA routing, escalation.
- **Sub-Agents (Specialists)**
  - Execute domain tasks and report only to Orchestrator.

No direct sub-agent-to-sub-agent communication unless explicitly proxied by Orchestrator.

---

## 4) Agent catalog (System A: analysis/delivery)

### 4.1 Main Agent (Owner)
- **Purpose**: Set direction, approve deliverables, resolve escalations.
- **Inputs**: Executive summaries, risk reports, blocker escalations, options analysis.
- **Outputs**: Priority decisions, approval/rejection, policy updates.
- **Key skills**: Leadership, strategy, risk trade-off, stakeholder communication.
- **SLA/timeout**: Respond to escalations in 4–24h depending on severity.
- **Success criteria**: Decisions are timely, documented, and aligned with project goals.

### 4.2 Orchestrator Agent
- **Purpose**: Manage decomposition, assignment, retries, QA routing, aggregation.
- **Inputs**: Project brief, constraints, status updates, specialist artifacts.
- **Outputs**: Task assignments, sprint board state, summary reports to Main Agent.
- **Key skills**: Project management, prioritization, dependency management, validation.
- **Example tasks**:
  - Build weekly sprint plan.
  - Assign data cleaning to Data Analyst.
  - Route outputs to QA and aggregate final package.
- **SLA/timeout**:
  - Ack incoming sub-agent update: <= 10 minutes.
  - Re-plan after blocker: <= 30 minutes.
  - Escalate after configured retry/remediation limits.
- **Success criteria**: >95% tasks have valid state transitions and complete metadata.

### 4.3 Data Analyst
- **Purpose**: Ingest, clean, analyze data; produce metrics/charts/statistical outputs.
- **Inputs**: Raw data, schema, analysis spec, constraints.
- **Outputs**: Cleaned artifacts, analysis report, visualizations, reproducible scripts.
- **Key skills**: Data cleaning, stats, visualization, reproducibility.
- **Example tasks**: cohort retention, A/B tests, feature distributions.
- **SLA/timeout**: First status <= 2h; task completion per complexity (e.g., 24–72h).
- **Success criteria**: Transformations documented; acceptance checks pass.

### 4.4 Researcher
- **Purpose**: Collect and synthesize literature with confidence estimates.
- **Inputs**: Research questions, scope boundaries, preferred sources.
- **Outputs**: Summaries, references, confidence/risk notes.
- **Key skills**: Search strategy, critical appraisal, synthesis.
- **Example tasks**: annotated bibliography, claim verification.
- **SLA/timeout**: Initial evidence map <= 8h; synthesis <= 24–48h.
- **Success criteria**: Claims are source-backed; confidence explicitly graded.

### 4.5 Documenter / Technical Writer
- **Purpose**: Convert decisions and outputs into polished documents.
- **Inputs**: Aggregated analysis, decisions, notes, QA findings.
- **Outputs**: Design docs, README, release notes, user guides.
- **Key skills**: Technical writing, structure, style consistency, versioning.
- **Example tasks**: handoff package, changelog, usage docs.
- **SLA/timeout**: Draft <= 24h after approved inputs.
- **Success criteria**: Clarity, consistency, references/links valid.

### 4.6 QA / Verifier
- **Purpose**: Validate deliverables against acceptance criteria and checklists.
- **Inputs**: Deliverables from specialists, acceptance specs, test/checklist config.
- **Outputs**: Pass/fail verdict, defects list, remediation suggestions.
- **Key skills**: Test design, validation frameworks, domain checks.
- **Example tasks**: verify report completeness, path checks, reproducibility checklist.
- **SLA/timeout**: QA pass within 4–12h based on artifact size.
- **Success criteria**: Deterministic pass/fail with actionable defect output.

---

## 5) Additional agent catalog (System B: manuscript drafting)

> This is a second orchestrated set focused on manuscript sections, coordinated by the same Orchestrator pattern.

### 5.1 Manuscript Orchestrator
- **Purpose**: Coordinate section drafting, enforce coherence, prevent contradiction.
- **Inputs**: Approved analysis findings, target journal format, section requirements.
- **Outputs**: Section assignments, integrated draft, consistency report.
- **Key skills**: Narrative planning, structure control, cross-section consistency.
- **SLA**: Section assignment <= 2h; integrated draft checkpoint daily.
- **Success criteria**: Section drafts align with evidence and shared terminology.

### 5.2 Introduction Drafter
- **Purpose**: Problem framing, background, gap statement, aims/hypotheses.
- **Inputs**: Research synthesis, key references, study objective.
- **Outputs**: Intro draft with citations and explicit aim statement.
- **Success criteria**: Clear rationale and objective consistency with Methods/Results.

### 5.3 Methods Drafter
- **Purpose**: Data, cohort, variables, preprocessing, statistical methods.
- **Inputs**: Analysis specs, codebook, pipeline details, QA notes.
- **Outputs**: Reproducible methods narrative and analysis transparency notes.
- **Success criteria**: Method text matches actual analysis implementation.

### 5.4 Results Drafter
- **Purpose**: Objective reporting of tables/figures/tests without over-interpretation.
- **Inputs**: Final outputs, effect sizes, test results, QA-approved numbers.
- **Outputs**: Results text + figure/table references.
- **Success criteria**: No numeric inconsistencies with source outputs.

### 5.5 Discussion Drafter
- **Purpose**: Interpretation, implications, limitations, future work.
- **Inputs**: Results + literature synthesis + risk notes.
- **Outputs**: Balanced discussion draft.
- **Success criteria**: Claims proportional to evidence; limitations explicit.

### 5.6 Manuscript QA Editor
- **Purpose**: Coherence and policy checks across sections.
- **Inputs**: All section drafts, style guide, acceptance checklist.
- **Outputs**: Consolidation defects list and revision recommendations.
- **Success criteria**: Terminology, claims, and references are consistent end-to-end.

---

## 6) Orchestration protocol (message format + lifecycle)

### 6.1 Required task message schema

```json
{
  "task_id": "TASK-2026-00123",
  "owner": "Orchestrator",
  "assignee": "DataAnalyst",
  "description": "Clean dataset X to schema Y and run EDA checks",
  "inputs": ["path/to/raw.csv", "path/to/schema.md"],
  "expected_outputs": ["clean.csv", "eda_report.md", "quality_checks.json"],
  "deadline": "2026-04-21T18:00:00Z",
  "retry_policy": {"max_retries": 2, "retry_delay_min": 30},
  "priority": "high",
  "acceptance_criteria": [
    "No nulls in required columns",
    "All transformations documented",
    "QA checklist passes"
  ]
}
```

### 6.2 Sub-agent status update schema

```json
{
  "task_id": "TASK-2026-00123",
  "state": "in_progress",
  "progress_percent": 40,
  "artifacts": ["path/to/draft_output.csv"],
  "blockers": ["missing schema mapping for variable Z"],
  "eta": "2026-04-20T12:00:00Z",
  "needs_orchestrator_action": true
}
```

### 6.3 Task lifecycle

`Backlog -> Plan-Review -> Assigned -> In Progress -> Review (QA) -> Done -> Archived`

Only Orchestrator changes lifecycle state.

Definition of `Plan-Review`:
- Architecture/task design is reviewed (by Claude or designated reviewer) before assignment begins.
- Exit criteria: approved scope, acceptance criteria, and retry/escalation thresholds.

### 6.4 Scheduling model

- Prioritization: `critical > high > medium > low`
- Pull every 15 min for updates (or event-driven webhook)
- Daily digest to Main Agent + immediate blocker alert policy

### 6.5 Failure handling and escalation

- Retry: sub-agent retries up to **N** times.
- Remediation: Orchestrator clarifies spec/reassigns up to **M** remediations.
- Escalation: after M failures, send Main Agent:
  - error summary
  - attempted remediations
  - options with recommendation

Suggested defaults (can be tuned by domain):
- `N = 2` retries per sub-agent task.
- `M = 2` orchestrator remediations before escalation.
- soft timeout warning at 70% of deadline, hard timeout at 100%.

### 6.6 Pre-creation review request template (Orchestrator -> Claude)

```json
{
  "request_type": "architecture_review",
  "scope": "main+orchestrator+subagents",
  "inputs": ["agent-architecture.md", "project constraints", "delivery goals"],
  "required_feedback": [
    "risk_register",
    "role_overlap_analysis",
    "sla_retry_tuning",
    "cost_latency_tradeoffs",
    "implementation_readiness_score"
  ],
  "output_format": "markdown+json",
  "deadline": "YYYY-MM-DDTHH:MM:SSZ"
}
```

---

## 7) Progress tracking, KPIs, and reporting cadence

### 7.1 Core KPIs

1. Tasks completed per sprint
2. Mean time to completion (MTTC)
3. QA pass rate (first-pass and final)
4. Requirements coverage (%)
5. Blocker count + blocker aging
6. Rework rate (%)
7. Research confidence average (for literature tasks)
8. Comparison discrepancy closure rate

### 7.2 Cadence

- Sub-agent -> Orchestrator: status every 2–4h (or on state change)
- Orchestrator -> Main Agent:
  - Daily brief (short)
  - Weekly dashboard (full)
  - Immediate alerts for Red severity blockers

### 7.3 Example dashboard fields

- `sprint_id`
- `agent_name`
- `open_tasks`
- `in_progress_tasks`
- `qa_failed_tasks`
- `completed_tasks`
- `mttc_hours`
- `blocker_count`
- `status_color` (Green/Yellow/Red)
- `top_risks`
- `next_24h_plan`

---

## 8) Security, privacy, and compute constraints

### 8.1 Data handling policy by role

- **Data Analyst**: may process raw/derived datasets; must redact/avoid exporting sensitive fields.
- **Researcher**: no direct access to restricted raw data unless explicitly granted.
- **Documenter**: uses approved outputs only, not unrestricted raw extracts.
- **QA**: receives minimum data needed for validation.

### 8.2 PII and retention

- Classify data per task (`public`, `internal`, `restricted`).
- Restrict `restricted` data to approved agents/tasks only.
- Redact sensitive fields in shared artifacts.
- Retain logs/artifacts per project policy; record retention class in metadata.

### 8.3 Rate and compute budgets (example defaults)

- Orchestrator: lightweight reasoning only, <= 2 min per cycle.
- Data Analyst: high compute window, cap per task (e.g., 4 CPU-hours).
- Researcher: capped API/query budgets per sprint.
- QA: bounded validation runtime (e.g., <= 60 min per artifact batch).
- Hard budget alerts at 80% usage; block at 100% until Main Agent decision.

---

## 9) Templates and message examples

### 9.1 Orchestrator -> Data Analyst

"Task: Clean dataset X to schema Y. Inputs: [paths]. Expected outputs: cleaned CSV, EDA report, quality checks JSON. Deadline: 48h. Acceptance: no missing values in key columns, all transformations documented. Return status in JSON with `task_id`, `progress_percent`, `artifacts`, `blockers`, `eta`."

### 9.2 Sub-agent -> Orchestrator

```json
{
  "task_id": "TASK-123",
  "state": "in_progress",
  "progress_percent": 40,
  "artifacts": ["k:/.../draft.csv"],
  "blockers": ["missing lookup table"],
  "eta": "24h"
}
```

### 9.3 Orchestrator -> Main Agent escalation

```json
{
  "task_id": "TASK-123",
  "severity": "red",
  "issue": "2 retries + 2 remediations failed",
  "impact": "blocks sprint deliverable A",
  "options": [
    "extend deadline by 24h and unblock dependency",
    "reassign to backup agent",
    "reduce scope and ship partial"
  ],
  "recommended_option": "reassign to backup agent"
}
```

---

## 10) Acceptance criteria and worked scenarios

### 10.1 Acceptance criteria (this architecture doc)

Must include:
- Agent catalog with roles/skills/inputs/outputs/SLAs/success criteria.
- Orchestration protocol with schemas and lifecycle.
- Failure handling, retries, and escalation logic.
- KPI/reporting model and dashboard fields.
- Security/privacy/compute constraints.
- Two end-to-end scenarios.
- Agent registry sample at the end.
- Mandatory pre-creation review gate with explicit signoff criteria.

Architecture is implementation-ready only if:
1. Plan-review output exists and is approved by Main Agent.
2. No unresolved `critical` risk remains open.
3. Each agent has SLA, timeout, and success criteria.
4. Orchestration lifecycle/state transitions are unambiguous.

### 10.2 Scenario A (analysis flow)

1. Orchestrator assigns Data Analyst task for data cleaning and EDA.
2. Data Analyst reports 40% with blocker (missing mapping).
3. Orchestrator requests mapping from Researcher or documentation source and unblocks.
4. Data Analyst submits outputs; QA validates and finds one failing check.
5. Task returns to Data Analyst for fix; second QA pass succeeds.
6. Orchestrator aggregates and reports Green status to Main Agent.

**Final deliverable**: cleaned dataset + EDA report + QA pass record + sprint summary.

### 10.3 Scenario B (manuscript drafting flow)

1. Manuscript Orchestrator assigns Introduction/Methods/Results/Discussion drafts in parallel.
2. Results Drafter submits numeric claims; Manuscript QA flags two mismatches vs outputs.
3. Results Drafter corrects references and values; QA rechecks pass.
4. Manuscript Orchestrator merges sections and runs coherence check (terminology + claims).
5. Final integrated manuscript package sent to Main Agent for signoff.

**Final deliverable**: coherent draft manuscript with section-level evidence links and QA checklist.

### 10.4 Scenario C (pre-creation review before agent launch)

1. Orchestrator submits architecture review request to Claude.
2. Claude returns risk register + improvement suggestions.
3. Orchestrator updates plan and highlights deltas.
4. QA/Verifier checks that required controls are now present.
5. Main Agent signs off go/no-go.
6. Only then are agents instantiated and assigned tasks.

**Final deliverable**: approved architecture review packet + launch authorization.

---

## 11) Open questions and configurable options

1. **Orchestrator autonomy level**
   - automated decisions vs human-in-the-loop for high-risk actions.
2. **Main-Agent direct override policy**
   - should Main Agent ever message specialists directly in emergencies?
3. **Task granularity**
   - micro-tasks improve observability but increase overhead/latency.
4. **Retry and remediation thresholds**
   - tune N/M by workload criticality.
5. **QA strictness mode**
   - strict for release branches, relaxed for exploratory phases.

6. **Pre-creation reviewer policy**
  - single reviewer vs dual-reviewer consensus for high-risk projects.

---

## 12) Implementation rollout phases (developer-ready)

### Phase 0 — Review & approve
- Run the mandatory pre-creation review gate.
- Resolve critical risks.

### Phase 1 — Bootstrap
- Create Orchestrator and QA/Verifier first.
- Implement lifecycle tracking and message schema validation.

### Phase 2 — Specialist activation
- Add Data Analyst, Researcher, Documenter.
- Run pilot sprint with 3–5 bounded tasks.

### Phase 3 — Manuscript lane activation
- Add Manuscript Orchestrator + section drafters + Manuscript QA.
- Validate cross-section coherence protocol.

### Phase 4 — Scale and optimize
- Tune SLA/retry thresholds by KPI trends.
- Add automation for dashboards/escalation alerts.

---

## 13) What I think of your manuscript sub-agent plan

It is a strong plan and should improve throughput and quality **if** you enforce two controls: (1) a strict evidence contract (Results cannot claim anything not present in approved outputs), and (2) a coherence QA gate before signoff (terminology, numbers, and limitations aligned across sections). With those controls and the orchestrator hub model, your manuscript pipeline will scale better than single-agent drafting and produce more auditable outputs.

---

## 13) Agent registry sample (YAML)

```yaml
agents:
  - name: MainAgentOwner
    role: strategic_owner
    default_sla: "4-24h escalation response"
    contact_pattern: "Orchestrator -> MainAgent only"

  - name: Orchestrator
    role: coordinator
    default_sla: "ack <=10m; blocker replan <=30m"
    contact_pattern: "hub-and-spoke"

  - name: DataAnalyst
    role: analytics_specialist
    default_sla: "first status <=2h; completion 24-72h"
    contact_pattern: "DataAnalyst -> Orchestrator"

  - name: Researcher
    role: evidence_specialist
    default_sla: "evidence map <=8h; synthesis <=48h"
    contact_pattern: "Researcher -> Orchestrator"

  - name: Documenter
    role: technical_writer
    default_sla: "draft <=24h post-approved inputs"
    contact_pattern: "Documenter -> Orchestrator"

  - name: QAVerifier
    role: quality_gate
    default_sla: "QA cycle 4-12h"
    contact_pattern: "QAVerifier -> Orchestrator"

  - name: ManuscriptOrchestrator
    role: manuscript_coordinator
    default_sla: "assignment <=2h; daily integration checkpoint"
    contact_pattern: "Manuscript specialists via Orchestrator"

  - name: IntroductionDrafter
    role: manuscript_section_specialist
    default_sla: "section draft <=24-48h"
    contact_pattern: "Intro -> ManuscriptOrchestrator"

  - name: MethodsDrafter
    role: manuscript_section_specialist
    default_sla: "section draft <=24-48h"
    contact_pattern: "Methods -> ManuscriptOrchestrator"

  - name: ResultsDrafter
    role: manuscript_section_specialist
    default_sla: "section draft <=24-48h"
    contact_pattern: "Results -> ManuscriptOrchestrator"

  - name: DiscussionDrafter
    role: manuscript_section_specialist
    default_sla: "section draft <=24-48h"
    contact_pattern: "Discussion -> ManuscriptOrchestrator"

  - name: ManuscriptQAEditor
    role: manuscript_quality_gate
    default_sla: "consistency review <=12h"
    contact_pattern: "ManuscriptQA -> ManuscriptOrchestrator"
```

## 14) Agent registry sample (JSON)

```json
{
  "agents": [
    {"name": "MainAgentOwner", "default_sla": "4-24h escalation response", "contact_pattern": "Orchestrator -> MainAgent only"},
    {"name": "Orchestrator", "default_sla": "ack <=10m; blocker replan <=30m", "contact_pattern": "hub-and-spoke"},
    {"name": "DataAnalyst", "default_sla": "first status <=2h; completion 24-72h", "contact_pattern": "DataAnalyst -> Orchestrator"},
    {"name": "Researcher", "default_sla": "evidence map <=8h; synthesis <=48h", "contact_pattern": "Researcher -> Orchestrator"},
    {"name": "Documenter", "default_sla": "draft <=24h post-approved inputs", "contact_pattern": "Documenter -> Orchestrator"},
    {"name": "QAVerifier", "default_sla": "QA cycle 4-12h", "contact_pattern": "QAVerifier -> Orchestrator"},
    {"name": "ManuscriptOrchestrator", "default_sla": "assignment <=2h; daily integration checkpoint", "contact_pattern": "Manuscript specialists via Orchestrator"},
    {"name": "IntroductionDrafter", "default_sla": "section draft <=24-48h", "contact_pattern": "Intro -> ManuscriptOrchestrator"},
    {"name": "MethodsDrafter", "default_sla": "section draft <=24-48h", "contact_pattern": "Methods -> ManuscriptOrchestrator"},
    {"name": "ResultsDrafter", "default_sla": "section draft <=24-48h", "contact_pattern": "Results -> ManuscriptOrchestrator"},
    {"name": "DiscussionDrafter", "default_sla": "section draft <=24-48h", "contact_pattern": "Discussion -> ManuscriptOrchestrator"},
    {"name": "ManuscriptQAEditor", "default_sla": "consistency review <=12h", "contact_pattern": "ManuscriptQA -> ManuscriptOrchestrator"}
  ]
}
```

## 15) Six-cycle review log (2026-04-17)

1. Added pre-creation review gate (Claude suggestions required before launch).
2. Added lifecycle `Plan-Review` state and explicit exit criteria.
3. Added retry/remediation defaults and timeout thresholds.
4. Added pre-creation review request template and stronger acceptance rules.
5. Added implementation rollout phases for developers.
6. Added JSON registry and final consistency polish for direct use.

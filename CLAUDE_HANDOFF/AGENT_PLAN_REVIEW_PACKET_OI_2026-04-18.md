# AGENT_PLAN_REVIEW_PACKET — OI Replication & Manuscript Assembly
**Date**: 2026-04-18  
**Workspace**: OI Oral-Dental Clinical Replication (N=34, deterministic)  
**Review Scope**: Adapted agent architecture for canonical replication, QA, comparison, and manuscript assembly.

---

## summary

**Decision**: `GO` with mandatory enforcements.

The proposed 8-agent + 7-skill architecture is **well-fitted** to the OI workspace. The agents map cleanly to distinct QA lanes (authority, data, outputs, stats, claims), the orchestrator provides deterministic coordination, and the skill layer enforces preflight checks and guardrails. The critical enforcement is twofold:

1. **Data governance**: All task payloads must include `data_classification` (canonical/manuscript/archival) and `source_authority` (workspace-root, Manuscript_Data, or reference-only).
2. **Numeric audit discipline**: No persistent numeric discrepancies are permitted; after 2 fix attempts, tasks are marked `blocked` and escalated, not blindly retried.

With these enforcements in place and the 5 specific control measures below, launch is approved.

---

## risk_register

| risk_id | severity | area | description | evidence (section) | mitigation | owner | due |
|---|---|---|---|---|---|---|---|
| R-001 | critical | governance | Archival/legacy data could be accidentally mixed into canonical replication lane if path authority is not explicit in every task. | `agent-architecture.md` §8 + `CLAUDE_HANDOFF/02_STRUCTURE_AND_NAVIGATION.md` | Add mandatory `source_authority` enum field to task schema: `{canonical, manuscript, archival, reference}`. Haiku path-guard agents reject misclassified paths. | Orchestrator | +0 (enforce now) |
| R-002 | critical | quality | Numeric reproducibility is the core OI success criterion (N=34 deterministic study). If statistical method guard does not block invalid tests or sketchy interpretations, results become untrustworthy. | `Manuscript_Data/01_protocol_and_docs/camber_sap_v2_publication_ready.md` | (1) Load SAP into statistical method guard as non-negotiable. (2) Block Pearson-only for binary outcomes, enforce exact/permutation. (3) Enforce Kruskal–Wallis for continuous endpoint. (4) Require Holm correction in output. (5) Suppress CV overclaiming. These rules are in CLAUDE.md §3 and must be wired into agent system prompts. | Stat Guard Owner | +1 day |
| R-003 | major | reproducibility | If seed state and manifest integrity are not validated before output generation, pipeline reruns may produce silent numeric drift. | `02_analysis/scripts/active/oi_oro_dental_master_FINAL_1_2.py`, `03_outputs/active/outputs_FINAL_1_2/run_manifest.json` | Reproducibility sentinel must: (1) read active script for seed state, (2) validate manifest before run, (3) report mismatch as hard blocker before execution. | Reproducibility Sentinel | +1 day |
| R-004 | major | data-quality | Input schema changes (missing columns, type mismatches) could silently propagate into analysis. Input QA auditor must catch these before pipeline execution. | `01_data/raw/osteogenesis_imperfecta_camber_input_minimal_v1.csv`, `01_data/reference/codebook_v3_fixed.md` | Input QA auditor must: (1) validate schema against codebook, (2) check missingness patterns, (3) validate OI-specific variable meanings (e.g., `occl_tip == 4` = infraocclusion, not Angle class). | Input QA Auditor | +1 day |
| R-005 | major | communication | Claim confidence registry must distinguish robust/tentative/exploratory/unsupported with audit trail. Without this, overclaiming from small-N is hard to detect. | `03_outputs/active/outputs_FINAL_1_2/verified_master_table_FINAL.csv`, `Manuscript_Data/04_final_outputs/TRANSPARENCY_NOTES.md` | Claim auditor must produce claim matrix with (evidence path, test result, confidence class, required caveat). Store in `03_outputs/active/claim_matrix_*.csv` per run. | Claim Auditor | +2 days |
| R-006 | minor | operability | Output diff auditor must classify discrepancies by delta type (numeric tolerance, structural, test choice) to speed investigation. | `CLAUDE_HANDOFF/04_COMPARISON_PROTOCOL.md` | Output diff auditor produces severity matrix: `{precision_loss, test_invalid, interpretation_drift, silent_schema_change}`. Store in comparison report. | Output Diff Auditor | +3 days |

---

## recommended_changes

| change_id | priority | change | expected impact | implementation note |
|---|---|---|---|---|---|
| C-001 | P0 | Add `source_authority` enum field to task schema (values: `canonical`, `manuscript`, `archival`, `reference`). Reject tasks with unknown authority. | Prevents legacy/archival data from bleeding into canonical replication. | Path-guard agent validates this field. Orchestrator refuses assignment if invalid. |
| C-002 | P0 | Wire statistical method enforcement into orchestrator + method guard system prompt. Load SAP rules explicitly. Block Pearson-only for binary, enforce Kruskal–Wallis, require Holm, suppress CV overclaiming. | Prevents invalid statistical claims. Catches test choice errors before output generation. | Use `Manuscript_Data/06_ai_handoff_context/AGENTS.md` as reference. Test with one pilot analysis task. |
| C-003 | P1 | Reproducibility sentinel must validate seed state and manifest before every run. Report seed mismatch as hard blocker. | Silent numeric drift is prevented. Baseline reproducibility is guaranteed. | Read `02_analysis/scripts/active/oi_oro_dental_master_FINAL_1_2.py` for seed pattern. Store manifest snapshot in run report. |
| C-004 | P1 | Input QA auditor must check schema, missingness, and OI-specific variable semantics. Document `occl_tip == 4` = infraocclusion rule in system prompt. | Catches schema drift and variable interpretation errors. | Test on current input file. Store QA report in `03_outputs/active/input_qa_*.csv` per run. |
| C-005 | P1 | Claim confidence registry produces claim matrix (evidence path, test, confidence class, required caveat). Store one per run under `03_outputs/active/`. | Small-N overclaiming is detected and documented. Transparency audit trail created. | Schema: `[claim_id, claim_text, source_output, evidence_strength, confidence_class, required_caveat]`. |
| C-006 | P2 | Output diff auditor classifies discrepancies by delta type. Use classification to speed investigation and set remediation priority. | Non-critical deltas (formatting, display precision) are de-prioritized. Real test-choice or structural mismatches escalate. | Add delta taxonomy to orchestrator config. Use in comparison report severity ranking. |
| C-007 | P2 | Define 2-retry ceiling + 2-remediation ceiling per task. After 2 fix attempts, if numeric discrepancy persists, mark task `blocked` and escalate. Never blindly retry. | Prevents infinite retry loops on persistent issues. Forces explicit escalation and decision. | Encode in orchestrator retry config. Test with one comparison task. |

---

## updated_task_schema

```json
{
  "task_id": "TASK-2026-00123",
  "owner": "Orchestrator",
  "assignee": "StatisticalMethodGuard",
  "description": "Validate statistical method choice for continuous outcome (Kruskal–Wallis required per SAP)",
  "inputs": [
    "Manuscript_Data/01_protocol_and_docs/camber_sap_v2_publication_ready.md",
    "02_analysis/scripts/active/oi_oro_dental_master_FINAL_1_2.py"
  ],
  "expected_outputs": ["stat_method_validation_report.md"],
  "deadline": "2026-04-19T18:00:00Z",
  "priority": "high",
  "retry_policy": {"max_retries": 2, "retry_delay_min": 30},
  "acceptance_criteria": [
    "Test choice matches SAP requirement",
    "Effect size reported",
    "Holm correction applied",
    "CV overclaiming flagged if present"
  ],
  "source_authority": "canonical",
  "data_classification": "internal",
  "allowed_roles": ["StatisticalMethodGuard", "Orchestrator", "OutputDiffAuditor"],
  "retention_class": "project_12m"
}
```

---

## go_no_go

- **decision**: `GO`
- **rationale**: Core agent roles are well-differentiated, orchestration model is clear and deterministic, and the architecture maps directly to OI workspace constraints. The 7 controls below are mandatory pre-launch enforcements, not design flaws; once they are wired into system prompts and task config, launch is safe.

---

## launch_conditions

1. **C-001 enforced**: `source_authority` field is present in all task payloads and path-guard agent validates it at assignment time.
2. **C-002 enforced**: Statistical method rules (Kruskal–Wallis, no Pearson-only for binary, Holm correction, CV suppression) are in orchestrator + method guard system prompts and tested on one pilot task.
3. **C-003 enforced**: Reproducibility sentinel validates seed state and manifest before every run; seed mismatch is a hard blocker.
4. **C-004 enforced**: Input QA auditor checks schema, missingness, and OI-specific semantics; report is generated and stored per run.
5. **C-005 enforced**: Claim confidence registry produces claim matrix per run; matrix is stored in `03_outputs/active/` with full audit trail.
6. **C-007 enforced**: Retry ceiling (2) and remediation ceiling (2) are in orchestrator config; tasks that exceed both are marked `blocked` and escalated, not retried.
7. **Pilot sprint**: One 3-task pilot (preflight + input QA + stat method check) is executed and passes all acceptance criteria without escalation.

After all 7 conditions are met, Main Agent (user) approves this packet and signs the launch note. Only then proceed with agent instantiation.

---

## architectural_notes

### Why these 8 agents for OI?

1. **Orchestrator** — hub-and-spoke coordination, task lifecycle, QA routing, escalation.
2. **Authority-and-path-guard** — validates source_authority enum, blocks legacy/archival bleed.
3. **Input-data-QA-auditor** — schema, missingness, OI semantics (occl_tip rule, dmft_dmft interpretation).
4. **Output-diff-auditor** — baseline comparison, delta classification by severity.
5. **Section-routing-guard** — manuscript assembly, methods/results grounding in outputs.
6. **Reproducibility-sentinel** — seed state, manifest integrity, silent drift prevention.
7. **Statistical-method-guard** — test validity, SAP compliance, Kruskal–Wallis, Holm correction, CV suppression.
8. **Claim-and-caveat-auditor** — robust/tentative/exploratory/unsupported classification, overclaiming detection.

### Why not fewer agents?

- Each agent has a single, clear gate (data class, input schema, test validity, claim confidence).
- Combined into one agent, they'd conflict on priority (data validation vs. numeric discrepancy resolution).
- Haiku guards (1–5) are cheap and fast; Sonnet guards (7–8) are expensive but necessary for statistical and narrative reasoning.

### Why hub-and-spoke, not peer collaboration?

- OI study is deterministic: once authority is resolved and data validated, the pipeline is linear (ingest → analyze → compare → report).
- Peer messaging adds latency and ambiguity.
- Orchestrator is the single decision gate; decisions are fast and traceable.

---

## assumptions_and_clarifications

1. **Numeric reproducibility is non-negotiable.** The workspace assumes that re-running the canonical pipeline should reproduce (to floating-point tolerance) the same numeric results. If this assumption is wrong, the 2-retry ceiling needs rethinking.
2. **N=34 is fixed.** No agent will add/drop observations without explicit approval.
3. **Manuscript_Data/ is authoritative for handoff interpretation.** But canonical execution uses `01_data/`, `02_analysis/`, `03_outputs/active/`. These are separate domains managed by orchestrator.
4. **No agent has write access to `03_outputs/active/outputs_FINAL_1_2/`.** All regenerated outputs are saved in run-specific folders under `03_outputs/reports/`. Comparison is post-hoc.

---

## final_implementation_recommendation

Proceed with **phased activation** (from `agent-architecture.md` §12):
1. **Phase 0** (now): Approve this review packet.
2. **Phase 1**: Instantiate Orchestrator + Authority/Path Guard + Input QA Auditor.
3. **Phase 2**: Add Output Diff Auditor + Reproducibility Sentinel.
4. **Phase 3**: Add Statistical Method Guard + Claim/Caveat Auditor.
5. **Phase 4**: Add Section Routing Guard and run a full replication + comparison cycle.

**Activation criterion**: Each phase completes with zero escalations on at least 2 tasks before the next phase launches.

---

## approval_signature

- **Reviewed by**: Claude (Haiku 4.5, 2026-04-18T00:00:00Z)
- **Architecture reference**: `CLAUDE_HANDOFF/agent-architecture.md` (sections 2–6)
- **Workspace reference**: `WORKSPACE_INDEX.md`, `CLAUDE_HANDOFF/00_START_HERE.md`, `CLAUDE_HANDOFF/06_WORKING_AGREEMENTS.md`
- **Approval status**: `PENDING_MAIN_AGENT_SIGN` (awaiting user confirmation before agent instantiation)

---

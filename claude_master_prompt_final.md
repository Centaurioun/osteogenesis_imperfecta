Claude, populate the existing empty files in this repository’s `.claude/` directory to finalize the OI workspace overhaul.

This workspace is a small-sample (N=34), deterministic clinical replication and manuscript assembly package. It is NOT an exploratory omics pipeline.

Although runtime may later use Experimental Agent Teams, this task is NOT to generate a team manifest or alternate agent framework. This task is to populate standard project subagent files under `.claude/agents/` and standard skill files under `.claude/skills/`.

## Hard execution constraints

- Populate ONLY the explicitly listed target files below.
- Do NOT create extra agents, extra skills, extra docs, team manifests, or alternate config files.
- Do NOT rename any target.
- Do NOT modify files outside the listed `.claude` targets.
- Do NOT delete anything.
- If any listed target file is missing, stop immediately and report the exact missing path.
- If any required source-of-truth file is missing, stop immediately and report the exact missing path.
- If the repo documents conflict with this prompt on a governance-critical point, prefer the repo documents and report the conflict explicitly.
- Use workspace-root paths exactly as written. Do not rewrite them into alternate relative-path conventions.
- Use valid YAML frontmatter. Do not invent unsupported frontmatter keys beyond what is explicitly required.
- Do not leave placeholders, TODOs, “fill later” text, or generic template language. Every target file must be implementation-ready.

### Meta-tool usage rules:

- Use `skill-creator` only as a secondary reference for skill structure, metadata shape, and completeness checks.
- Do not let `skill-creator` override repository authority, workspace-specific rules, or the explicit specifications in this prompt.
- Use `claude-md-management` only to audit, normalize, or refine `.claude/CLAUDE.md` and related markdown structure after the core content has been grounded in repository sources.
- Prefer direct generation from repository documents first; use meta-tools only to improve structure, consistency, and completeness.
- If a meta-tool suggests something that conflicts with repository rules or this prompt, reject that suggestion and follow the repository rules.

## Explicit target files to populate

### Global rules file
1. `.claude/CLAUDE.md`

### Agent files
2. `.claude/agents/oi-canonical-replication-orchestrator.md`
3. `.claude/agents/oi-authority-and-path-guard.md`
4. `.claude/agents/oi-input-data-qa-auditor.md`
5. `.claude/agents/oi-output-diff-auditor.md`
6. `.claude/agents/oi-section-routing-guard.md`
7. `.claude/agents/oi-reproducibility-sentinel.md`
8. `.claude/agents/oi-statistical-method-guard.md`
9. `.claude/agents/oi-claim-and-caveat-auditor.md`

### Skill files
10. `.claude/skills/canonical-preflight/SKILL.md`
11. `.claude/skills/authority-resolution/SKILL.md`
12. `.claude/skills/runtime-transform-checks/SKILL.md`
13. `.claude/skills/small-n-stats-guardrails/SKILL.md`
14. `.claude/skills/claim-confidence-registry/SKILL.md`
15. `.claude/skills/run-report-writer/SKILL.md`
16. `.claude/skills/comparison-report-writer/SKILL.md`

## Source-of-truth framing

- Execution authority comes strictly from the workspace-root canonical active lane:
  - `01_data/`
  - `02_analysis/`
  - `03_outputs/active/`
- `Manuscript_Data/` is authoritative for manuscript/handoff interpretation, narrative assembly, variable lineage explanation, and AI-transfer context.
- Do not mix archival or legacy files into execution logic unless a comparison/audit task explicitly requires them.

## Required output quality standard

For every agent file:
- include valid YAML frontmatter
- include a concise but concrete system prompt
- define purpose
- define when to use
- define when NOT to use
- define required reads
- define allowed tools
- define hard bans
- define expected outputs / response contract
- define escalation conditions
- define completion criteria

For every skill file:
- include valid skill metadata
- accept `$ARGUMENTS`
- include concrete execution guidance
- include required reads
- include expected inputs and outputs
- include validation / failure conditions
- avoid generic prose

---

# PHASE 0 — Mandatory architecture review gate

Before populating any target files:

Read, in this order:
1. `CLAUDE_HANDOFF/README.md`
2. `CLAUDE_HANDOFF/AGENT_PLAN_REVIEW_PROMPT.md`
3. `CLAUDE_HANDOFF/agent-architecture.md`
4. `CLAUDE_HANDOFF/AGENT_PLAN_REVIEW_PACKET_EXAMPLE.md`
5. `CLAUDE_HANDOFF/00_START_HERE.md`
6. `CLAUDE_HANDOFF/06_WORKING_AGREEMENTS.md`

Then produce the required architecture review packet in the format expected by the repository.

Decision rule:
- If the review result is **NO-GO**, stop immediately and output the review packet only.
- If the review result is **CONDITIONAL_GO**, first apply the required architecture safeguards inside the files you are about to write, then continue.
- If the review result is **GO**, continue.

Do not skip this phase.

---

# PHASE 1 — Populate global rules file

Populate:
- `.claude/CLAUDE.md`

This file is the shared global rule file for the workspace.

It must encode at minimum:

1. **Authority rules**
   - execution authority = workspace-root canonical lane
   - manuscript/handoff authority = `Manuscript_Data/`
   - archival/legacy files cannot be mixed into normal execution

2. **Runtime transformation rules**
   - `occl_tip == 4` means infraocclusion, not Angle class
   - `dmft_dmft` is treated as a count-like variable
   - gene grouping must be derived at runtime

3. **Statistical guardrails**
   - reject naive sparse-cell Pearson-only logic
   - enforce exact/permutation logic for binary outcomes
   - enforce Kruskal–Wallis for the continuous endpoint in this workspace
   - require Holm correction reporting
   - require effect sizes
   - suppress overclaiming from small-N results
   - treat CV outputs as supportive, not confirmatory

4. **Escalation and retry policy**
   - maximum 2 revision rounds per task
   - do not blindly retry persistent numeric discrepancies
   - if discrepancy persists after allowed remediation, mark task as `blocked`

5. **Governance**
   - no deletion
   - no overwrite of historical artifacts
   - root-path discipline
   - report blocked state instead of improvising

---

# PHASE 2 — Populate lead orchestrator

Populate:
- `.claude/agents/oi-canonical-replication-orchestrator.md`

Required YAML frontmatter:
- `name: oi-canonical-replication-orchestrator`
- `description: Coordinates OI replication, preflight, comparison, reporting, and QA gates using authoritative workspace-root paths.`
- `tools: [Agent, Read, Grep, Glob, Bash, Edit]`
- `model: sonnet`
- `maxTurns: 10`

Required behavior:
- strict hub-and-spoke model
- teammates may not message each other
- teammates may not self-claim out-of-scope tasks
- orchestrator is the only approval gate
- scopes tasks
- resolves authoritative files before action
- delegates to specialists
- enforces quality gates
- never uses legacy assets unless the task is explicitly comparison/audit
- reports blocked status instead of improvising

Its required reads must include at least:
- `CLAUDE_HANDOFF/00_START_HERE.md`
- `WORKSPACE_INDEX.md`
- `CLAUDE_HANDOFF/03_REPLICATION_PLAYBOOK.md`
- `CLAUDE_HANDOFF/04_COMPARISON_PROTOCOL.md`
- `CLAUDE_HANDOFF/06_WORKING_AGREEMENTS.md`

---

# PHASE 3 — Populate worker subagents

Do NOT give any worker persistent memory.

## A. Haiku guards (fast / cheap checks)

Each of the following must have YAML frontmatter including:
- `tools: [Read, Grep, Glob]`
- `model: haiku`
- `permissionMode: plan`
- `maxTurns: 6`

### 1) `.claude/agents/oi-authority-and-path-guard.md`
Purpose:
- resolve authoritative vs archival vs reference-only files
- block ambiguous path usage

Must read:
- `Manuscript_Data/README_Manuscript_Data.md`
- `CLAUDE_HANDOFF/00_START_HERE.md`
- `WORKSPACE_INDEX.md`
- `WORKSPACE_MAP.md`
- `WORKSPACE_ORGANIZATION_PLAN.md`

### 2) `.claude/agents/oi-input-data-qa-auditor.md`
Purpose:
- check dataset schema
- check missingness
- validate OI clinical variable interpretation against workspace rules

Must read:
- `Manuscript_Data/04_final_outputs/OUTPUT_SCHEMA_AND_VARIABLE_LINEAGE.md`
- `01_data/raw/osteogenesis_imperfecta_camber_input_minimal_v1.csv`
- `01_data/reference/codebook_v3_fixed.md`
- `Manuscript_Data/06_ai_handoff_context/copilot-instructions.md`

### 3) `.claude/agents/oi-output-diff-auditor.md`
Purpose:
- compare regenerated outputs against canonical baseline
- classify discrepancies by severity and likely cause

Must read:
- `CLAUDE_HANDOFF/04_COMPARISON_PROTOCOL.md`
- `CLAUDE_HANDOFF/COMPARE_RESULTS_TEMPLATE.md`

### 4) `.claude/agents/oi-section-routing-guard.md`
Purpose:
- route manuscript section work safely
- keep Methods/Results grounded in package and output evidence

Must read:
- `Manuscript_Data/01_protocol_and_docs/MANUSCRIPT_ASSEMBLY_GUIDE.md`

### 5) `.claude/agents/oi-reproducibility-sentinel.md`
Purpose:
- check seed consistency
- check manifest integrity
- check reproducibility environment notes

Must read:
- `Manuscript_Data/04_final_outputs/REPRODUCIBILITY_ENVIRONMENT.md`
- `02_analysis/scripts/active/oi_oro_dental_master_FINAL_1_2.py`
- `03_outputs/active/outputs_FINAL_1_2/run_manifest.json`

## B. Sonnet guards (higher-risk reasoning)

Each of the following must have YAML frontmatter including:
- `tools: [Read, Grep, Glob]`
- `model: sonnet`
- `permissionMode: plan`
- `maxTurns: 8`

### 6) `.claude/agents/oi-statistical-method-guard.md`
Purpose:
- enforce statistical rules
- reject invalid tests
- suppress overclaiming

Must read:
- `Manuscript_Data/01_protocol_and_docs/camber_sap_v2_publication_ready.md`
- `Manuscript_Data/06_ai_handoff_context/AGENTS.md`
- `02_analysis/scripts/active/oi_oro_dental_master_FINAL_1_2.py`

### 7) `.claude/agents/oi-claim-and-caveat-auditor.md`
Purpose:
- label claims as `robust`, `tentative`, `exploratory`, or `unsupported`
- inject required caveat language
- prevent CV overclaiming

Must read:
- `Manuscript_Data/04_final_outputs/TRANSPARENCY_NOTES.md`
- `03_outputs/active/outputs_FINAL_1_2/verified_master_table_FINAL.csv`
- `03_outputs/active/outputs_FINAL_1_2/cv_panel_FINAL.csv`
- `03_outputs/active/outputs_FINAL_1_2/robustness_panel_FINAL.csv`
- `Manuscript_Data/01_protocol_and_docs/final_1.md`

---

# PHASE 4 — Populate execution skills

Populate the following skill files:
- `.claude/skills/canonical-preflight/SKILL.md`
- `.claude/skills/authority-resolution/SKILL.md`
- `.claude/skills/runtime-transform-checks/SKILL.md`
- `.claude/skills/small-n-stats-guardrails/SKILL.md`
- `.claude/skills/claim-confidence-registry/SKILL.md`
- `.claude/skills/run-report-writer/SKILL.md`
- `.claude/skills/comparison-report-writer/SKILL.md`

All skills must:
- accept `$ARGUMENTS`
- use `allowed-tools: Bash Read Edit Grep Glob`

## Auto-invocable skills
Do NOT include `disable-model-invocation`.

### 1) `canonical-preflight`
Reads:
- `CLAUDE_HANDOFF/00_START_HERE.md`
- `WORKSPACE_INDEX.md`

Purpose:
- verify required canonical paths
- verify baseline output presence
- stop execution if required assets are missing

### 2) `authority-resolution`
Reads:
- `WORKSPACE_INDEX.md`
- `WORKSPACE_MAP.md`
- `WORKSPACE_ORGANIZATION_PLAN.md`
- `Manuscript_Data/README_Manuscript_Data.md`

Purpose:
- output authoritative vs supporting vs excluded file maps for a task

### 3) `runtime-transform-checks`
Reads:
- `Manuscript_Data/04_final_outputs/OUTPUT_SCHEMA_AND_VARIABLE_LINEAGE.md`
- `Manuscript_Data/06_ai_handoff_context/copilot-instructions.md`

Purpose:
- validate variable derivations and runtime meanings

### 4) `small-n-stats-guardrails`
Reads:
- `Manuscript_Data/01_protocol_and_docs/camber_sap_v2_publication_ready.md`
- `Manuscript_Data/06_ai_handoff_context/AGENTS.md`

Purpose:
- apply small-sample statistical checklist before inferential writing or review

### 5) `claim-confidence-registry`
Reads:
- `03_outputs/active/outputs_FINAL_1_2/verified_master_table_FINAL.csv`
- `Manuscript_Data/04_final_outputs/TRANSPARENCY_NOTES.md`
- `Manuscript_Data/01_protocol_and_docs/final_1.md`

Purpose:
- generate claim matrices mapping manuscript claims to evidence and confidence class

## Manual-only workflow skills
These MUST include:
- `disable-model-invocation: true`

### 6) `run-report-writer`
Reads:
- `CLAUDE_HANDOFF/RUN_REPORT_TEMPLATE.md`

Purpose:
- fill the run report template from actual run evidence

### 7) `comparison-report-writer`
Reads:
- `CLAUDE_HANDOFF/COMPARE_RESULTS_TEMPLATE.md`

Purpose:
- fill the comparison report template with severity and delta classification

---

# PHASE 5 — Verification sweep

After writing all target files:

1. Re-open every populated target file.
2. Verify YAML frontmatter fields match the specification.
3. Verify every file contains concrete, implementation-ready instructions.
4. Verify read-only workers have no write-capable tools.
5. Verify manual-only skills include `disable-model-invocation: true`.
6. Verify no extra files were created and no non-target files were modified.
7. Output a pass/fail table covering all 16 target files.
8. If any file fails verification, fix it before finalizing.

Final output requirements:
- provide a concise summary of what was populated
- provide the pass/fail verification table
- list any blocking assumptions or unresolved issues
- do not claim success unless the verification sweep passed


**Note:**

Create `.claude/agents/oi-section-routing-guard.md` exactly as specified in the task.
Do not delete, rename, or modify `.claude/agents/oi-manuscript-assembly-coordinator.md`.
Then continue Phases 1–5 and populate only the 16 listed target files.
At the end, run the full Phase 5 verification sweep and show the pass/fail table in chat.
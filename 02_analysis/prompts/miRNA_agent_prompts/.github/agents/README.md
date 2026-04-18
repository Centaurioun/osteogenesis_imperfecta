# Workspace subagents for miRNA reanalysis

This workspace defines a coordinator-worker subagent system for the notebook workflow.

Design goals:
- Keep the coordinator context focused while delegating specialized review tasks.
- Enforce notebook-only observability and conservative interpretation.
- Improve repeatability of QA, statistical review, leakage audit, and narrative synthesis.

## Available agents

- `miRNA Reanalysis Coordinator` (user-facing): orchestrates specialized subagents.
- `Spec Mapper` (subagent): turns `miRNA-qPCR-reanalysis.md` into a checklist.
- `Data QA Auditor` (subagent): audits schema, missingness, and transformations.
- `Biostatistics Reviewer` (subagent): checks test choice, assumptions, and multiplicity.
- `Modeling Leakage Auditor` (subagent): enforces leakage-safe pairwise classification.
- `Interpretation Reviewer` (subagent): stress-tests claims and caveats.

## Recommended usage

1. Start chat with `miRNA Reanalysis Coordinator`.
2. Ask for a specific objective, such as:
   - Build the next notebook section
   - Review classification logic for leakage
   - Review final interpretation and caveats
3. Let the coordinator delegate to worker subagents and synthesize final actions.

Useful prompt patterns:
- "Build Section 10 and Section 11 with explicit assumptions and discrepancy logging."
- "Audit current pairwise classification for leakage and propose fold-safe redesign."
- "Grade final claims as robust/tentative/exploratory/unsupported with caveat language."

## Operational notes

- Worker agents are configured as `user-invocable: false` to bias toward coordinated use.
- Worker agents are configured with `disable-model-invocation: true`; the coordinator can still call them via explicit `agents` allow-list.
- Coordinator explicitly allow-lists worker agents via frontmatter `agents`.
- If a required input is missing, require explicit Assumption Ledger and Discrepancy Log entries.
- Keep fixed groups/tasks unchanged across all outputs.

## Quick smoke-test workflow

1. Invoke `miRNA Reanalysis Coordinator` with a read-only task (no file edits).
2. Invoke one worker (e.g., `Spec Mapper`) with a constrained mini-output contract.
3. Verify returned output includes status, evidence, and next actions/risk flags.
4. Run diagnostics to ensure no frontmatter/configuration errors.

## Prompt shortcut

Use prompt file:
- `.github/prompts/mirna-reanalysis-orchestrated.prompt.md`

This prompt is designed to trigger coordinated delegation and preserve workspace constraints.

## Maintenance checklist

- Keep agent names synchronized with coordinator `agents` allow-list.
- Keep descriptions explicit and searchable ("Use when...").
- Keep tool access least-privilege for worker agents.
- Re-run diagnostics after changes to frontmatter.

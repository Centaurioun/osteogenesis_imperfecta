# Objective
Produce a **read-only forensic diagnosis** of why the expected final consolidated notebook was not actually populated with analyses.

Primary failure to explain:
- `Manuscript_Data/03_analysis_scripts/oi_oro_dental_consolidated_v1.ipynb` exists, but appears to contain no substantive analyses.

Your diagnosis must focus on instruction quality (conflicts, ambiguity, missing acceptance criteria, sequencing problems), using verifiable evidence from this repository.

# Background

Original workflow status:

- [x] Create `rapor_promptu.md` with a goal + checklist to collect latest analysis artifacts into `/analysis_documentation_package`.
- [x] Create `/analysis_documentation_package` in project root.
- [x] Analyze project directory + `rapor_promptu.md` and execute that process.
- [ ] Summarize updated `/analysis_documentation_package`, then provide a complete guide to merge all analyses/scripts/notebooks into a single comprehensive `.ipynb`.
- [ ] Run the merged notebook and obtain full results.
- [ ] Archive old remnants.
- [ ] Zip archive and clean root.

Observed concern:
- The produced consolidated notebook was created but effectively empty from an analysis standpoint.

# Scope and non-goals
You are diagnosing **why this failed**. You are **not** continuing the pipeline.

Do **not**:
- execute pending checklist items,
- create/modify/merge/archive/delete files,
- claim that you ran the notebook or produced new outputs.

Allowed actions:
- inspect files and directory structure,
- compare instructions/prompts/checklists,
- report evidence-based failure causes and instruction-level fixes.

# Mandatory evidence targets
At minimum, inspect and cite evidence from:
1. `rapor_promptu.md`
2. `fixing-promot.md`
3. `Manuscript_Data/03_analysis_scripts/oi_oro_dental_consolidated_v1.ipynb`
4. `/analysis_documentation_package` contents (structure-level evidence)

If any target is missing or inaccessible, explicitly state that and explain impact on confidence.

# Minimum verification protocol (required)
Before concluding, perform and report evidence checks for all items below:
1. Notebook structure check: total cell count, code-cell count, markdown-cell count.
2. Notebook substance check: whether code cells contain real analysis logic vs placeholders/comments only.
3. Notebook execution metadata check: whether outputs/execution traces exist (if present on disk).
4. Source-traceability check: whether the instructions define which source notebooks/scripts must be merged.
5. Package completeness check: whether `/analysis_documentation_package` includes a traceable inventory that can drive consolidation.

If any check cannot be performed from available files, state exactly which check failed and why.

# Definition of “empty notebook” for this diagnosis
Treat the notebook as effectively empty if one or more conditions hold:
- zero meaningful analysis code cells,
- code cells contain only scaffolding/placeholders/no-op statements,
- required analysis blocks are absent even if some boilerplate exists.

# What to diagnose (required)
Evaluate whether the instructions had one or more of these failure modes:
1. **Conflicting objectives** (e.g., package/collect vs actually merge/execute analyses).
2. **Ambiguous deliverable definition** (what counts as “complete consolidated notebook” was undefined).
3. **Missing acceptance tests** (no explicit checks for number of code cells, required sections, outputs, executed status, or included analyses).
4. **Weak sequencing constraints** (ordering allows premature “completion” before merge quality validation).
5. **Insufficient file-selection logic** (no deterministic source-of-truth rules for picking latest versions among many similarly named files).
6. **Tool/process blind spots** (instructions do not force notebook-content verification after generation).
7. **Undefined terminology** (e.g., “latest”, “comprehensive”, “complete”, “analysis included”) that allows weak interpretation.
8. **Path/target ambiguity** (multiple plausible output folders or notebook targets without explicit precedence).

Only include failure modes supported by evidence.

# Terminology normalization requirement
When discussing ambiguity, explicitly flag terms that were not operationally defined and state how they should be defined in the next-attempt prompt.
Examples of terms to test: `latest`, `complete`, `comprehensive`, `final`, `include analyses`, `run and obtain results`.

# Quality bar for findings
Each finding must be:
- specific,
- evidence-backed,
- causally linked to the empty notebook outcome,
- paired with a concrete fix that is directly usable in the next prompt iteration.

For each finding, use causal strength language tied to evidence quality:
- `High confidence` = directly observed contradiction/gap in cited files.
- `Medium confidence` = strong but indirect evidence.
- `Low confidence` = plausible but weakly evidenced (use sparingly and label explicitly).

If evidence supports fewer than 3 findings, report only supported findings and list exactly what could not be verified.

Prioritize findings by likely impact on the failure outcome (highest-impact first).

# Output format (strict)
Return **exactly four sections** in this exact order. No extra sections, no preamble, no epilogue.

1. `Summary`
   - 2-4 sentences with most likely overall failure mechanism(s).

2. `Findings`
   - Numbered list.
   - For each item, include exactly these fields in this order:
     - `Issue:` (append confidence label here, e.g., `Issue: ... [High confidence]`)
     - `Evidence:`
     - `Why this could cause an empty notebook:`
     - `Recommended fix:`

3. `Conflicts and ambiguities`
   - Numbered list of instruction conflicts, omissions, undefined terms, or unclear sequencing.

4. `Next-attempt prompt fixes`
   - Numbered list of concrete instruction upgrades for a future run.
   - Include at least:
     - explicit acceptance criteria for consolidated notebook completeness,
     - deterministic file-selection/version rules,
     - deterministic tie-break rules when multiple files look "latest" (e.g., explicit precedence by semantic version, then timestamp),
     - mandatory post-generation verification checks,
     - stop conditions if consolidation quality gates fail.

# Evidence and citation rules
- Every finding must cite at least one concrete path and (when relevant) a prompt section or quoted phrase.
- For notebook-related findings, cite at least one concrete notebook fact (cell-level or metadata-level observation).
- Prefer citation format `path :: quoted snippet` (or section label) for reproducibility.
- `fixing-promot.md` can support methodological context, but it cannot be the sole evidence source for root-cause findings.
- If evidence is insufficient for a claim, do not infer; mark it as not verifiable and explain what evidence is missing.
- Do not rely on unstated assumptions.
- Do not claim actions you did not perform.

# Suggested acceptance checks to propose (for future prompt)
When writing recommended fixes, prioritize verifiable checks such as:
- minimum required notebook sections,
- minimum required analysis blocks migrated,
- non-empty code cell count threshold,
- evidence that analysis cells are not placeholders,
- explicit mapping table: source file -> destination notebook section,
- completion gate: fail if any required analysis block is missing.

Recommended fixes must be operational (testable), not generic. Prefer wording like: "Require X artifact, verify with Y check, fail with Z stop condition."

# Final self-check before answering
Ensure all conditions are satisfied:
- Exactly 4 required sections.
- At least 3 findings if supported by evidence.
- Every finding includes all 4 required fields and citations.
- No prohibited action claims.
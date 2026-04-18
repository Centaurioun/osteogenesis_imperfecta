---
name: mirna-reanalysis-orchestrated
description: "Use when running a coordinated miRNA notebook workflow with specialized subagents for specification mapping, QA, statistics, leakage-safe modeling, and interpretation."
tools:
  - agent
  - read
  - search
  - edit
---

Use the `miRNA Reanalysis Coordinator` agent behavior.

Goal:
Build or review `miRNA_qpcr_reanalysis.ipynb` in a notebook-native, auditable, leakage-safe manner using workspace rules.

Input expectations:
- Governing spec: `miRNA-qPCR-reanalysis.md`
- Primary data: `miRNA-qPCR-analysis-results.csv`

Execution guidance:
1. Delegate directive extraction to `Spec Mapper`.
2. Delegate schema and transformation risks to `Data QA Auditor`.
3. Delegate test-choice and multiplicity review to `Biostatistics Reviewer`.
4. Delegate classification safeguards to `Modeling Leakage Auditor`.
5. Delegate narrative and caveat quality control to `Interpretation Reviewer`.
6. Synthesize findings into notebook edits plus explicit logs:
   - Assumption Ledger
   - Discrepancy Log
   - Transformation Registry
   - Results Registry
7. If the user explicitly requests read-only review, do not edit files; return findings, risks, and recommended changes only.

Required final deliverables:
- Completed/partial/blocked mapping of directives to notebook sections
- Top-priority risk list (data, statistics, leakage, interpretation)
- Concrete notebook edit actions with rationale
- Claim confidence labels with required caveat text
- Explicit blockers with safest fallback path when full completion is not possible

Quality gates:
- No hidden or off-notebook computation assumptions
- Fixed groups/tasks preserved exactly
- Exploratory work labeled explicitly
- Any unresolved ambiguity documented with evidence and impact

Always preserve fixed groups and fixed tasks exactly as defined by workspace instructions.

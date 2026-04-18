# CLAUDE_PROMPT_STARTER (improved)

Workspace root: <WORKSPACE_ROOT>/

Purpose: Replicate the canonical OI oral-dental analysis, compare results to the baseline, and produce reproducible artifacts. If agent creation is being considered, perform an architecture review and obtain explicit signoff before creating agents.

Required sequence (run in order):
1. Open and read: CLAUDE_HANDOFF/00_START_HERE.md
2. Open and read: WORKSPACE_INDEX.md
3. If any agent(s) are planned: run CLAUDE_HANDOFF/AGENT_PLAN_REVIEW_PROMPT.md against CLAUDE_HANDOFF/agent-architecture.md and produce a review packet. Stop until explicit approval is recorded.
4. Read: CLAUDE_HANDOFF/03_REPLICATION_PLAYBOOK.md
5. Execute canonical replication notebook: 02_analysis/notebooks/active/oi_oro_dental_master_FINAL_1_2.ipynb
6. Save all run artifacts and reports under: 03_outputs/reports/ (use clear filenames with timestamps and git commit id)
7. Run comparison following: CLAUDE_HANDOFF/04_COMPARISON_PROTOCOL.md using baseline: 03_outputs/active/outputs_FINAL_1_2/
8. Produce final documents from templates:
   - CLAUDE_HANDOFF/RUN_REPORT_TEMPLATE.md -> 03_outputs/reports/run-report_<ts>.md
   - CLAUDE_HANDOFF/COMPARE_RESULTS_TEMPLATE.md -> 03_outputs/reports/compare-results_<ts>.md
9. Record unresolved problems as rows in: CLAUDE_HANDOFF/OPEN_ISSUES_REGISTER.csv (include file path, expected, observed, severity, recommended action)

Hard constraints (must obey):
- Never delete or overwrite historical files; always write new files.
- Use explicit paths from workspace root.
- Treat 03_outputs/active/outputs_FINAL_1_2/ as the canonical baseline.
- If a required path or input is missing, stop immediately and report the exact missing path (full absolute path). Do not continue.
- No agent creation before architecture review signoff.

Expected outputs:
- Run report: environment (OS, python, package versions), git commit id, notebook executed, inputs used, outputs produced, runtime logs, checksums for artifacts.
- Comparison report: path-level evidence for each discrepancy (baseline path, new path, diff summary, root cause hypothesis).
- Updated OPEN_ISSUES_REGISTER.csv rows for unresolved discrepancies.

If uncertain which file to prefer, use this precedence:
1. WORKSPACE_INDEX.md
2. CLAUDE_HANDOFF/00_START_HERE.md
3. CLAUDE_HANDOFF/03_REPLICATION_PLAYBOOK.md

Notes and operational tips:
- Windows path artifacts: if a path doesn't exist, check for alternate separators (\ vs /) and report both the missing path and any found equivalent.
- This workspace may lack Claude-specific config files. Run a "missing-files" check and list exact missing paths.

Agent/skill/plugin guidance (brief):
- Recommended agents: DataIngestor (validate inputs, checksums), NotebookRunner (execute notebooks reproducibly, capture env), Comparator (diff outputs, produce evidence), Reporter (populate templates), IssueTracker (append CSV rows).
- Useful skills: filesystem ops, notebook execution (nbconvert/nbclient), data diffing (file, table, image), metadata collection, git metadata retrieval, artifact packaging.
- Plugin vs agents: plugins provide external integrations (CI, storage, secure credentials) and stable endpoints for automation; agents are LLM-driven workers/orchestrators. Use a plugin only if you need persistent external integrations (artifact storage, CI triggers, or custom APIs). For pure orchestration within this repo, agents + skills are sufficient.

Agent-creation rule: always run the architecture review (step 3) and attach a review packet to the run report. Do not create or deploy agents until signoff is recorded.

Sample file-check checklist to run before replication:
- Confirm existence: 02_analysis/notebooks/active/oi_oro_dental_master_FINAL_1_2.ipynb
- Confirm baseline: 03_outputs/active/outputs_FINAL_1_2/
- Confirm templates: CLAUDE_HANDOFF/RUN_REPORT_TEMPLATE.md, CLAUDE_HANDOFF/COMPARE_RESULTS_TEMPLATE.md
- Confirm handoff docs: CLAUDE_HANDOFF/00_START_HERE.md, CLAUDE_HANDOFF/03_REPLICATION_PLAYBOOK.md, CLAUDE_HANDOFF/04_COMPARISON_PROTOCOL.md

When reporting missing items, print exact absolute paths and stop.

End.


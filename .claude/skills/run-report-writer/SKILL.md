---
name: run-report-writer
description: Manual-only skill. Fill the run report template from actual run evidence (logs, manifests, artifacts). Document execution and outcomes.
allowed-tools: Bash Read Edit Grep Glob
disable-model-invocation: true
---

## Purpose

Populate `RUN_REPORT_TEMPLATE.md` with actual evidence from a completed analysis run (logs, timing, artifacts, issues encountered). Create reproducible, auditable execution record.

---

## When to Use (Manual Only)

Invoke after a replication run completes:
- Collect run logs, manifest, generated artifacts.
- Fill template with actual data (not placeholders).
- Store in dated run folder: `03_outputs/reports/run_YYYYMMDD_HHMM/run_report.md`

---

## Required Template

`CLAUDE_HANDOFF/RUN_REPORT_TEMPLATE.md`

---

## Expected Inputs

- Run folder path (e.g., `03_outputs/reports/run_20260418_1200/`)
- Run manifest JSON
- Execution logs
- Generated output tables
- Timing and environment info

---

## Template Sections to Complete

1. **Execution metadata**: script, input file, seed, timestamp, duration.
2. **Input validation**: schema check, missingness summary, OI semantics validation.
3. **Generated outputs**: tables, figures, counts (e.g., "3 tables, 4 figures, 1 manifest").
4. **QA results**: preflight pass, reproducibility sentinel pass, statistical method pass.
5. **Issues encountered**: any warnings, failed assertions, manual fixes.
6. **Artifacts inventory**: list all files in run folder with sizes.

---

## Expected Output

Completed `run_report.md` in run folder with:
- [ ] Execution metadata (script, seed, timestamp)
- [ ] Input validation summary
- [ ] Output table counts
- [ ] QA gate results
- [ ] Issue log
- [ ] Artifact inventory

---

## No Model Invocation

This skill is manual only. Do NOT auto-invoke. User fills template by hand from run evidence.

---

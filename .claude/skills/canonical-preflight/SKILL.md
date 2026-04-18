---
name: canonical-preflight
description: Use before any replication execution. Verifies required canonical paths exist, baseline output presence confirmed, execution safety gates passed. Fail-fast if assets missing.
allowed-tools: Bash Read Edit Grep Glob
---

## Purpose

Quick safety gate: confirm that all required input files, baseline outputs, and reference documents are present and accessible. Stop execution before any analysis if required assets are missing.

---

## When to Use (Auto-Invoked)

Use this skill automatically before launching any replication task. Accept `$ARGUMENTS` for custom path lists.

---

## Required Reads (Load Once)

1. `CLAUDE_HANDOFF/00_START_HERE.md`
2. `WORKSPACE_INDEX.md`

---

## Expected Input ($ARGUMENTS)

```json
{
  "task": "preflight",
  "check_inputs": true,
  "check_baseline": true,
  "check_references": true,
  "custom_paths": []
}
```

---

## Execution Steps

1. **Input asset validation**:
   - Confirm `01_data/raw/osteogenesis_imperfecta_camber_input_minimal_v1.csv` exists and is readable.
   - Confirm `01_data/reference/codebook_v3_fixed.md` exists.
   - Confirm `01_data/reference/gene_map_v1.csv` exists.

2. **Baseline output validation**:
   - Confirm `03_outputs/active/outputs_FINAL_1_2/` folder exists.
   - Confirm `publication_table1_overall_FINAL.csv` exists.
   - Confirm `publication_table3_inferential_FINAL.csv` exists.
   - Confirm `robustness_panel_FINAL.csv` exists.
   - Confirm `cv_panel_FINAL.csv` exists.
   - Confirm `verified_master_table_FINAL.csv` exists.

3. **Reference validation**:
   - Confirm `Manuscript_Data/04_final_outputs/OUTPUT_SCHEMA_AND_VARIABLE_LINEAGE.md` exists.
   - Confirm `Manuscript_Data/01_protocol_and_docs/camber_sap_v2_publication_ready.md` exists.

4. **Run folder creation**:
   - Create `03_outputs/reports/run_YYYYMMDD_HHMM/` for new outputs (if not exists).

---

## Expected Output

JSON report:

```json
{
  "preflight_status": "PASS" | "FAIL",
  "timestamp": "2026-04-18T12:00:00Z",
  "checks": {
    "input_files": {"status": "PASS", "missing": []},
    "baseline_outputs": {"status": "PASS", "missing": []},
    "references": {"status": "PASS", "missing": []}
  },
  "run_folder": "03_outputs/reports/run_20260418_1200/",
  "blocked_issues": []
}
```

---

## Failure Conditions

- ✗ Input file missing → FAIL, escalate immediately.
- ✗ Baseline folder missing → FAIL, escalate immediately.
- ✗ Any required output table missing → FAIL, escalate immediately.

---

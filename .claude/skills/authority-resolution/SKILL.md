---
name: authority-resolution
description: Use when path/authority is ambiguous. Maps files to authoritative domains (canonical, manuscript, archival, reference). Prevents legacy data bleed.
allowed-tools: Bash Read Edit Grep Glob
---

## Purpose

Resolve whether a given file path belongs to canonical execution lane, manuscript handoff, archival comparison, or reference-only domain. Output authoritative vs. supporting vs. excluded file maps for a task.

---

## When to Use

Invoke when:
- A task specifies paths and authority is unclear.
- You need to validate that a task is not mixing canonical + archival data.
- You need to generate a file authority map for a new replication cycle.

Accept `$ARGUMENTS` for custom path lists.

---

## Required Reads (Load Once)

1. `WORKSPACE_INDEX.md`
2. `WORKSPACE_MAP.md`
3. `WORKSPACE_ORGANIZATION_PLAN.md`
4. `Manuscript_Data/README_Manuscript_Data.md`
5. `.claude/CLAUDE.md` (authority section)

---

## Expected Input ($ARGUMENTS)

```json
{
  "paths": ["01_data/raw/...", "Manuscript_Data/...", "99_archive/..."],
  "output_format": "json" | "csv",
  "task_authority": "canonical" | "manuscript" | "archival" | "comparison"
}
```

---

## Execution Steps

1. For each path in input:
   - Classify as `canonical` (01_data, 02_analysis/*/active, 03_outputs/active), `manuscript` (Manuscript_Data/), `archival` (99_archive, legacy/), or `reference` (codebooks, static tables).

2. Output map:
   - Authoritative files (use in canonical execution)
   - Supporting files (reference only)
   - Excluded files (do not use unless task_authority is archival/comparison)

3. Validate coherence:
   - Flag if canonical task mixes archival/legacy paths.

---

## Expected Output

JSON map:

```json
{
  "task_authority": "canonical",
  "authoritative": [
    {"path": "01_data/raw/osteogenesis_imperfecta_camber_input_minimal_v1.csv", "reason": "Canonical input lane"}
  ],
  "supporting": [
    {"path": "01_data/reference/codebook_v3_fixed.md", "reason": "Reference-only"}
  ],
  "excluded": [
    {"path": "99_archive/by_date/2026-04-15_legacy/outputs_legacy_v1/", "reason": "Archival; excluded from canonical execution"}
  ],
  "governance_violations": []
}
```

---

## Failure Conditions

- Canonical task includes archival path → FAIL.
- Manuscript task includes analysis output → conditional FAIL (handoff only, no analysis).
- Path does not exist → FAIL (validate existence first).

---

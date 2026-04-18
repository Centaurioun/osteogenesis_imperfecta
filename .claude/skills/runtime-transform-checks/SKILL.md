---
name: runtime-transform-checks
description: Use before analysis to validate variable derivations and runtime meanings match workspace rules. Prevents variable interpretation errors.
allowed-tools: Bash Read Edit Grep Glob
---

## Purpose

Validate that runtime variable transformations (gene grouping, occl_tip → Angle + infraocclusion, dmft_dmft as count) are correctly applied. Check analysis code for compliance with workspace semantic rules.

---

## When to Use

Invoke when:
- Before analysis execution to validate variable handling.
- When investigating numeric discrepancies (may be root cause).
- When checking whether a derived variable is correctly computed.

Accept `$ARGUMENTS` for custom variable lists.

---

## Required Reads (Load Once)

1. `Manuscript_Data/04_final_outputs/OUTPUT_SCHEMA_AND_VARIABLE_LINEAGE.md`
2. `Manuscript_Data/06_ai_handoff_context/copilot-instructions.md`
3. `.claude/CLAUDE.md` (runtime transformations section)

---

## Expected Input ($ARGUMENTS)

```json
{
  "variables_to_check": ["occl_tip", "dmft_dmft", "gen_mutasyonu"],
  "script_path": "02_analysis/scripts/active/oi_oro_dental_master_FINAL_1_2.py",
  "output_format": "json"
}
```

---

## Execution Steps

1. **occl_tip validation**:
   - Rule: 1–3 = Angle class; 4 = infraocclusion.
   - Check: Does analysis code distinguish 4 from 1–3? Is 4 excluded from Angle calculation?
   - Output: Validated or flagged mismatch.

2. **dmft_dmft validation**:
   - Rule: Treat as count (not decomposed DMFT index).
   - Check: Does analysis use `dmft_dmft` as continuous count for Kruskal–Wallis?
   - Check: Is binary conversion `caries_any = (dmft_dmft > 0)` applied correctly?

3. **Gene grouping validation**:
   - Rule: Runtime grouping, n ≥ 6 separate, else "Other".
   - Check: Does code implement this thresholding at analysis time?
   - Check: Are groups COL1A1, COL1A2, FKBP10, P3H1, Other?

---

## Expected Output

Validation report:

```json
{
  "variable": "occl_tip",
  "rule": "1–3 = Angle; 4 = infraocclusion",
  "script_inspection": {
    "infraocclusion_handling": "if occl_tip == 4: infraokluzyon_var_clean = 1; exclude from Angle",
    "compliant": true
  },
  "approval": "PASS" | "FAIL"
}
```

---

## Failure Conditions

- occl_tip treated as ordinal Angle scale → FAIL.
- dmft_dmft used with ordinal/categorical test → FAIL.
- Gene grouping not applied → FAIL.

---

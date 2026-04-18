---
name: claim-confidence-registry
description: Use when generating or reviewing manuscript claims. Maps claims to evidence, assigns confidence classes (robust/tentative/exploratory/unsupported), injects required caveats.
allowed-tools: Bash Read Edit Grep Glob
---

## Purpose

Generate claim matrices mapping every manuscript claim to supporting evidence and assign confidence class. Prevent overclaiming and ensure small-N transparency.

---

## When to Use (Auto-Invoked)

Use when:
- Results section is drafted (claim validation).
- Methods claims need evidence mapping.
- Discussion makes causal/predictive claims (exploratory flagging).

Accept `$ARGUMENTS` for custom claim lists.

---

## Required Reads (Load Once)

1. `03_outputs/active/outputs_FINAL_1_2/verified_master_table_FINAL.csv`
2. `Manuscript_Data/04_final_outputs/TRANSPARENCY_NOTES.md`
3. `Manuscript_Data/01_protocol_and_docs/final_1.md`
4. `.claude/CLAUDE.md` (small-N suppressions)

---

## Expected Input ($ARGUMENTS)

```json
{
  "claims": [
    "COL1A1 has tissue anomaly in 60% of cases",
    "Kruskal–Wallis p = 0.032 for caries count",
    "Gene group explains 18% of caries variation (AUC = 0.72)"
  ],
  "output_format": "csv|json"
}
```

---

## Execution Steps

1. For each claim:
   - Search output tables for supporting evidence (exact table/cell).
   - Assign confidence class (robust/tentative/exploratory/unsupported).
   - Specify required caveat language.

2. Generate claim matrix with columns:
   - claim_id, claim_text, source_output, evidence_cell, test_result, confidence_class, required_caveat

3. Flag overclaiming patterns:
   - CV results presented as confirmatory → downgrade to exploratory.
   - Subgroup (n<5) without "hypothesis-generating" caveat → flag.
   - Null finding without "non-significance caveat" → flag.

---

## Expected Output

CSV/JSON claim matrix:

```csv
claim_id,claim_text,source_output,confidence_class,required_caveat
C001,"COL1A1 tissue anomaly 60%","publication_table2_by_gene_group_FINAL.csv","robust","Include 95% CI."
C003,"Gene group explains 18% caries (AUC=0.72)","cv_panel_FINAL.csv","exploratory","CAVEAT: Exploratory; N=34 small sample."
```

---

## Confidence Classes

- **Robust**: Primary hypothesis, SAP-compliant, adequate sample.
- **Tentative**: Secondary analysis, small group (5–10), non-significance caveat needed.
- **Exploratory**: CV, sensitivity, subgroup (n<5), or hypothesis-generating.
- **Unsupported**: No evidence or contradicts outputs.

---

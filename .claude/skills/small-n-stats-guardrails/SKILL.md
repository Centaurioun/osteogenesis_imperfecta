---
name: small-n-stats-guardrails
description: Use before statistical inference or manuscript results writing. Apply small-N checklist, suppress overclaiming, enforce SAP compliance. Guardrail for N=34 datasets.
allowed-tools: Bash Read Edit Grep Glob
---

## Purpose

Apply small-sample (N=34) statistical guardrails before publishing or reporting results. Suppress overclaiming, enforce SAP rules, and ensure effect sizes + caveats are present.

---

## When to Use (Auto-Invoked)

Use before:
- Results section is drafted (ensure no overclaiming).
- Manuscript goes to final review (ensure small-N caveats present).
- Statistical claims are made in any context.

Accept `$ARGUMENTS` for custom check lists.

---

## Required Reads (Load Once)

1. `Manuscript_Data/01_protocol_and_docs/camber_sap_v2_publication_ready.md`
2. `Manuscript_Data/06_ai_handoff_context/AGENTS.md`
3. `.claude/CLAUDE.md` (statistical guardrails and small-N suppressions)

---

## Expected Input ($ARGUMENTS)

```json
{
  "test_type": "binary|continuous",
  "endpoint": "doku_anomalisi_var|dmft_dmft|gingivitis",
  "sample_size": 34,
  "group_n": [10, 8, 7, 9],
  "p_value": 0.032,
  "effect_size": 0.18,
  "check_cv_overclaiming": true
}
```

---

## Checklist

- [ ] Test choice matches endpoint type (exact/permutation for binary, Kruskal–Wallis for continuous).
- [ ] Effect size is reported alongside p-value.
- [ ] Holm correction applied (all p-values post-correction shown).
- [ ] Bootstrap confidence intervals for effect sizes (≥2000 replicates).
- [ ] Leave-One-Out sensitivity check run (LOO p-range reported).
- [ ] No CV overclaiming: AUC/predictive claims suppressed unless delta-AUC ≥0.15 and held-out N ≥10.
- [ ] Small-N caveat present: "This study includes N=34 OI patients from a single center."
- [ ] Null findings caveat: "Non-significance does not exclude a true difference; larger sample needed."
- [ ] Subgroup disclaimer: If n < 10 in subgroup, marked as "hypothesis-generating" and exploratory.

---

## Expected Output

Checklist report:

```json
{
  "endpoint": "dmft_dmft",
  "checks_passed": 8,
  "checks_total": 10,
  "failed_checks": [
    {"check": "Effect size reported", "status": "FAIL", "remediation": "Add epsilon² to output table"},
    {"check": "Holm correction applied", "status": "FAIL", "remediation": "Re-run with Holm correction"}
  ],
  "approval": "CONDITIONAL" | "PASS"
}
```

---

## Suppression Rules

- Suppress "strong predictive value" claims from CV unless delta-AUC ≥0.15.
- Suppress interaction term reporting unless n per cell ≥5 and p ≤0.01.
- Suppress "significant" descriptors for n <5 per group (use "higher prevalence" with numbers/CI instead).

---

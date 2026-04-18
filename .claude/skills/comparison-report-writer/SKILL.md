---
name: comparison-report-writer
description: Manual-only skill. Fill the comparison report template with severity and delta classification. Document baseline vs. regenerated discrepancies.
allowed-tools: Bash Read Edit Grep Glob
disable-model-invocation: true
---

## Purpose

Populate `COMPARE_RESULTS_TEMPLATE.md` with comparison evidence (baseline vs. regenerated outputs, discrepancies classified by severity and root cause). Create auditable comparison record for acceptance decision.

---

## When to Use (Manual Only)

Invoke after output comparison is complete:
- Collect baseline vs. regenerated output tables.
- Classify each discrepancy by severity (critical/major/minor) and cause (path/input/code/environment/methodology/unknown).
- Fill template with actual delta values and remediation notes.
- Store in dated run folder: `03_outputs/reports/run_YYYYMMDD_HHMM/comparison_report.md`

---

## Required Template

`CLAUDE_HANDOFF/COMPARE_RESULTS_TEMPLATE.md`

---

## Expected Inputs

- Baseline output folder: `03_outputs/active/outputs_FINAL_1_2/`
- Regenerated output folder: `03_outputs/reports/run_YYYYMMDD_HHMM/`
- Comparison analysis (from output diff auditor)

---

## Template Sections to Complete

1. **Executive summary**: Overall acceptance decision (Accept/Conditional/Reject) with rationale.
2. **Discrepancy matrix**: For each delta, document:
   - Baseline file/cell
   - Regenerated file/cell
   - Numeric/text delta
   - Severity (critical/major/minor)
   - Likely cause (path/input/code/environment/methodology/unknown)
   - Root cause determination (if known)
   - Remediation (if applicable)

3. **Severity summary**: Count critical/major/minor discrepancies.
4. **Root cause analysis**: Summarize suspected causes and remediation steps taken.
5. **Acceptance decision**: Explicit Accept/Conditional Accept/Reject with conditions (if conditional).

---

## Expected Output

Completed `comparison_report.md` in run folder with:
- [ ] Executive summary with acceptance decision
- [ ] Discrepancy matrix (>95% of deltas documented)
- [ ] Severity summary
- [ ] Root cause analysis
- [ ] Acceptance decision (explicit and conditions if conditional)

---

## Severity Classification Reference

- **Critical**: Table structure different, core p-value differs >0.05, sample size mismatch, blockers trust.
- **Major**: Test choice changed, meaningful analytical divergence, method drift.
- **Minor**: Formatting, rounding (p matches to 3 decimals but differs at 4th), display precision.

---

## No Model Invocation

This skill is manual only. Do NOT auto-invoke. User fills template by hand from comparison evidence.

---

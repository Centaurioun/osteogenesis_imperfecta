# 04_COMPARISON_PROTOCOL

## Comparison order

1. Canonical baseline vs freshly regenerated outputs.
2. Freshly regenerated outputs vs selected legacy outputs.

## Preferred baseline folders

- Canonical: `../03_outputs/active/outputs_FINAL_1_2/`
- Legacy: `../03_outputs/legacy/` and selective `../99_archive/` references

## Evidence requirements

For every discrepancy, capture:
- metric/table/file name
- source path and target path
- numeric/text delta
- likely cause classification:
  - path/input mismatch
  - code/version drift
  - environment/package drift
  - expected methodological change
  - unknown (needs investigation)

Also classify severity:
- `critical`: blocks trust in replication or indicates likely pipeline/input break
- `major`: meaningful analytical divergence needing explanation
- `minor`: formatting/ordering/non-substantive drift

Minimum evidence format per discrepancy:
- baseline file path
- candidate file path
- concrete value/row/cell delta
- suspected cause
- next action owner

## Output artifact

Complete and store `COMPARE_RESULTS_TEMPLATE.md` as a dated report under `../03_outputs/reports/`.

## Acceptance decision matrix

- **Accept** if only minor diffs remain and causes are documented.
- **Conditional accept** if major diffs remain but root cause is known and bounded.
- **Reject** if critical diffs are unresolved or baseline equivalence cannot be established.

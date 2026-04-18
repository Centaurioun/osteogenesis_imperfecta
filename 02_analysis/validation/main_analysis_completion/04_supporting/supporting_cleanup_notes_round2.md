# Supporting Cleanup Notes (Round2)

## 7.1 Alternative grouping output
- Checked against authoritative `supplementary_gene_group_map_FINAL.csv`.
- Primary/k=3/k=4 are duplicate scenarios in current data composition.
- Revised file now explicitly marks duplicate scenarios as trace-only.

## 7.2 Robustness classification wording
- Implemented in Stage 5 with refined labels (`stable`, `stable null`, `partly stable`, `fragility-sensitive`).

## 7.3 CV reporting inconsistency
- Implemented in Stage 6 with `ci_point_consistency` and `interpretive_status` flags.
- Inconsistent rows are retained for transparency but suppressed for predictive interpretation.

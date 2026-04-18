# notebook_blueprint

## immutable_layer
- Cell 1 | markdown | purpose: Scope + authoritative boundaries | depends_on: none
- Cell 2 | code | purpose: Load authoritative FINAL tables only | input_files: publication_table1/2/3, robustness_panel_FINAL, cv_panel_FINAL
- Cell 3 | markdown | purpose: Explain variable lineage constraints (`occl_tip==4`, `dmft_dmft`)

## mutable_layer
- Cell 4 | code | purpose: Build supporting summary views (no primary metric overwrite) | depends_on: Cell 2
- Cell 5 | code | purpose: Add robustness/context annotations | depends_on: Cell 2
- Cell 6 | code | purpose: Add CV warning context as secondary internal verification | depends_on: Cell 2
- Cell 7 | markdown | purpose: Narrative synthesis with evidence tags

## cell_schema_required
- Each cell record must include: cell_no, cell_type, purpose, input_files, output_artifacts, depends_on

## rollback_strategy
- If a mutable cell fails, rerun from latest successful immutable cell boundary.
- Immutable cells are read-only evidence loaders; do not rewrite authoritative metrics.

# 01_data

Purpose: data assets organized by lifecycle stage.

## Structure

- `raw/` — source data files used by analysis.
- `reference/` — codebook and mapping files used to interpret fields.
- `derived/` — generated intermediate datasets (if needed).

## Current key files

- `raw/osteogenesis_imperfecta_camber_input_minimal_v1.csv`
- `reference/codebook_v3_fixed.md`
- `reference/gene_map_v1.csv`

## Rules

- Do not overwrite raw/reference files in place.
- Add derived artifacts in `derived/` with versioned names.

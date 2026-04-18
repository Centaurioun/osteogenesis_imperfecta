# 05_OPEN_ISSUES_AND_RISKS

## Open items

1. **Raw data convenience gap**
   - `01_data/raw/` currently contains `osteogenesis_imperfecta_camber_input_minimal_v1.csv`.
   - `osteogenesis_imperfecta_original_data.csv` exists in:
     - `../Manuscript_Data/02_source_data/raw_data/`
     - `../99_archive/by_date/2026-04-17_reorg_wave1/archive/`
   - Decision needed: copy/link canonical original dataset into `01_data/raw/` for easier replication.

2. **Validation/report standardization pending**
   - Comparison outputs should be normalized via templates in this folder and saved under `../03_outputs/reports/`.

## Risks

- Running legacy notebooks by mistake can produce inconsistent comparisons.
- Environment drift can create false deltas.
- Missing run metadata reduces reproducibility confidence.

## Mitigations

- Always start from `00_START_HERE.md`.
- Use canonical notebook first.
- Fill run and comparison templates for every replication cycle.

## Tracking files

- Issue tracker: `OPEN_ISSUES_REGISTER.csv`
- Short-term plan: `NEXT_ACTIONS_14_DAYS.md`

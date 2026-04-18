# Post-Advisor Round 2 Provenance Note

Date: 2026-04-18

## Purpose

This note records the additive semantic revision step performed before any round-two rerun. Historical artifacts were preserved; no pre-advisor output set was deleted.

## Pre-advisor semantic state (preserved)

- Existing raw+legacy analysis-ready file:
  - `01_data/raw/osteogenesis_imperfecta_camber_input_minimal_v1.csv`
- Existing active/legacy outputs remain unchanged under:
  - `03_outputs/active/outputs_FINAL_1_2/`
  - `03_outputs/legacy/`

## Post-advisor semantic state (new additive artifacts)

- New decision memo:
  - `data_decisions_post_advisor_round2.md`
- New codebook addendum:
  - `01_data/reference/codebook_post_advisor_round2_addendum_v1.md`
- New analysis-ready dataset:
  - `01_data/derived/osteogenesis_imperfecta_analysis_ready_post_advisor_round2_v1_2026-04-18.csv`
- New issue log for this revision step:
  - `01_data/derived/issue_log_v3.csv`

## Key semantic controls applied

1. `angle_sinifi_clean` is the primary Angle field with values only in `1/2/3` or missing.
2. `occl_tip == 4` is carried as infraocclusion (`infraokluzyon_var_clean = 1`) and excluded from primary Angle classification.
3. `dmft_dmft` is carried as count-like `caries_count_total`.
4. `doku_anomalisi` is represented as binary any (`doku_anomalisi_any`) and dominant-type (`doku_anomalisi_dominant_type`) interpretations.
5. `di_any` is presence/absence only; no subtype/severity inference is encoded.

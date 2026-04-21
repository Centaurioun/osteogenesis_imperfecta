# Codebook Addendum — Post-Advisor Round 2 (v1)

Date: 2026-04-18
Applies to: `01_data/derived/osteogenesis_imperfecta_analysis_ready_post_advisor_round2_v1_2026-04-18.csv`

This is an additive semantic layer. It does **not** replace `codebook_v3_fixed.md`; it refines analysis-facing interpretation for post-advisor round-two preparation.

## Raw vs derived separation

- **Raw provenance fields kept unchanged:** `occl_tip`, `dmft_dmft`, `doku_anomalisi`, `gingivitis`, existing legacy-derived fields.
- **Legacy derived fields preserved:** `angle_sinifi`, `caries_any`, `doku_anomalisi_var`, `dentisyon_donemi_kod`, `infraokluzyon_var`.
- **Post-advisor derived fields added:** `angle_sinifi_clean`, `caries_count_total`, `doku_anomalisi_any`, `doku_anomalisi_dominant_type`, `dentition_donemi_clean`, `infraokluzyon_var_clean`, `di_any`.

## Post-advisor variable definitions

## `angle_sinifi_clean`
- Type: coded categorical (primary Angle analysis variable)
- Allowed values: `1, 2, 3, missing`
- Rule: derived from `occl_tip`; only `1/2/3` retained.
- Rule: if `occl_tip == 4`, then `angle_sinifi_clean = missing`.

## `infraokluzyon_var_clean`
- Type: binary (0/1)
- Rule: `1` if and only if `occl_tip == 4`, else `0`.
- Interpretation: infraocclusion is separate from Angle class.

## `caries_count_total`
- Type: numeric count-like
- Rule: `caries_count_total = dmft_dmft`.
- Interpretation: single recorded total caries burden field.
- Wording control: do not present as an unqualified standard split WHO DMFT/dmft index.

## `doku_anomalisi_any`
- Type: binary (0/1)
- Rule: `1` if `doku_anomalisi != 0`, else `0`.
- Primary anomaly endpoint for round-two inferential analyses.

## `doku_anomalisi_dominant_type`
- Type: text label
- Rule: dominant recorded anomaly type mapped from `doku_anomalisi` code.
- Interpretation limit: dominant single code only; not a full phenotype inventory.

## `di_any`
- Type: binary (0/1)
- Rule: `1` if `doku_anomalisi == 2`, else `0`.
- Limitation: DI subtype/severity (e.g., Shields-based severity typing) is unavailable.

## `dentition_donemi_clean`
- Type: coded categorical (1/2/3)
- Rule: age-derived clean dentition-stage field for descriptive stratification.

## Explicit interpretation limits (reinforced)

1. `doku_anomalisi` and derived type fields are dominant-code records, not multi-label phenotype captures.
2. DI subtype/severity analysis is unsupported.
3. Gingivitis/overjet/overbite/open bite/crossbite remain binary presence/absence variables only.
4. Unknown underlying Angle class for infraocclusion is not imputed.

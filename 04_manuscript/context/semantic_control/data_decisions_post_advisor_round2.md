# Data Decisions — Post-Advisor Round 2

Date: 2026-04-18
Source authority: `canonical` (controlled by post-advisor clarification hierarchy)

## Authority hierarchy (İnci clarification files)

When clarification files disagree, use:

1. `inci-sorular-danisman-sonrasi-revize-cevap.md`
2. `inci-sorular-ilk-cevap.md`
3. Older assumptions in previous codebook/output/prompt layers

This hierarchy governs this round-two semantic revision.

## Binding semantic decisions

1. **Occlusion split is mandatory**
   - Raw `occl_tip` remains unchanged for provenance.
   - Primary Angle variable is `angle_sinifi_clean`.
   - `angle_sinifi_clean` can contain only `1/2/3`.
   - If `occl_tip == 4`, then `angle_sinifi_clean = missing`.
   - `infraokluzyon_var` remains separate and binary.

2. **No imputation of unknown underlying Angle class**
   - The infraocclusion case is not force-assigned to Angle I/II/III.
   - Unknown remains unknown in primary analysis.

3. **Caries variable framing**
   - `dmft_dmft` is treated as a single count-like total caries burden field.
   - Analysis-facing alias: `caries_count_total = dmft_dmft`.
   - Binary derivation remains `caries_any = (dmft_dmft > 0)`.
   - Avoid unqualified wording that presents this as a standard WHO-style split DMFT/dmft index.

4. **`doku_anomalisi` interpretation**
   - `doku_anomalisi` is a dominant-code field (single recorded dominant type), not a full multi-label phenotype inventory.
   - Primary endpoint: `doku_anomalisi_any` (binary any-anomaly).
   - Secondary descriptive endpoint: `doku_anomalisi_dominant_type`.

5. **DI limitation**
   - DI subtype/severity (e.g., Shields subtype severity analysis) is unavailable from this dataset.
   - Only transparent presence/absence-level handling is allowed.

6. **Binary-only clinical variable discipline**
   - Gingivitis, overjet, overbite, open bite, and crossbite are interpreted as binary presence/absence only.
   - No severity-threshold indexed-interpretation claims are allowed unless independently evidenced.

7. **Provenance-preserving versioning is mandatory**
   - Pre-advisor outputs and earlier semantic state artifacts are preserved.
   - Post-advisor artifacts are additive and clearly version-labeled.
   - No silent destructive overwrite.

## Round-two readiness conditions (semantic layer)

Round-two analysis preparation can proceed only if all are true:

1. Post-advisor decision memo exists (this file).
2. Codebook addendum exists with explicit raw-vs-clean semantics.
3. New versioned post-advisor analysis-ready dataset exists.
4. Active instruction/prompt layer does not encode outdated occlusion logic.
5. Pre-advisor artifacts remain preserved and discoverable.

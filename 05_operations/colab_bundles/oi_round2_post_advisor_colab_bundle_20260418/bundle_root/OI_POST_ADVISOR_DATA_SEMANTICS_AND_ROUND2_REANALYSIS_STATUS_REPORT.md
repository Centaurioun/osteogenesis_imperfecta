# OI post-advisor data semantics and round-two reanalysis status report

## Executive summary

This report consolidates the current post-advisor understanding of the OI dataset and translates it into an operational revision plan before round-two analysis. The key conclusion is that the project remains scientifically workable, but the semantic control layer is no longer identical to the one used in the earlier analysis cycle.

The most consequential change concerns occlusion. The earlier working state allowed `occl_tip = 4` to behave as an extra category within the same occlusion family. The later advisor-discussed clarification requires a stricter separation: Angle classification must remain limited to `1/2/3`, while infraocclusion must be handled separately. Because the current analysis-ready CSV still contains one case with `occl_tip = 4` and blank `angle_sinifi`, the dataset is not unusable, but it is only partially aligned with the latest semantic decision.

This means the next step is not immediate rerun. The correct next step is a controlled semantic revision phase: preserve the pre-advisor state, revise the data-decision layer, update the analysis-ready dataset and supporting definitions, and only then begin the second-round analysis. The goal is not to erase prior work, but to create a defensible post-advisor version that can be reanalyzed cleanly and compared against the earlier version.

---

## Suggested repository filename and intended role

Suggested filename:
- `OI_POST_ADVISOR_DATA_SEMANTICS_AND_ROUND2_REANALYSIS_STATUS_REPORT.md`

Suggested role in the repo:
- authoritative briefing document for post-advisor semantic revision work
- controlling background document for Copilot when preparing surgical file revisions before round-two rerun
- persistent provenance record explaining why round-two differs from round-one

This report is now suitable to live in the repo as-is. It should be referenced explicitly in revision prompts so Copilot treats it as a controlling project document rather than as casual background context.

---

## Purpose of this report

This document is intended to serve as the controlling briefing for the next Copilot phase. It should enable a surgical revision process across the files that require updates, while preserving provenance and preventing unnecessary changes to files that are already acceptable.

Accordingly, this report does five things:

1. establishes which human clarifications are authoritative,
2. distinguishes analysis-changing issues from interpretation-only issues,
3. identifies exactly what is currently aligned and misaligned,
4. defines the round-two semantic rules that should govern revision,
5. translates those rules into a file-by-file surgical revision plan.

---

## Materials reviewed

### Human clarification files
- `inci-sorular.md`
- `inci-sorular-ilk-cevap.md`
- `inci-sorular-danisman-sonrasi-revize-cevap.md`

### Current data and metadata files
- `osteogenesis_imperfecta_camber_input_minimal_v1.csv`
- `codebook_v3_fixed.md`
- `gene_map_v1.csv`

### Existing project context already known from the workspace
- current analysis-ready OI package
- existing derived fields and round-one logic
- small-sample, effect-size-aware analysis framework already adopted in the project

---

## Decision hierarchy

When the three İnci documents disagree, the following authority order should be used:

1. `inci-sorular-danisman-sonrasi-revize-cevap.md`
2. `inci-sorular-ilk-cevap.md`
3. earlier assumptions embedded in codebook, draft notes, or prior analysis logic

This hierarchy must be made explicit in the semantic revision memo for round two. The post-advisor clarification should now be treated as the highest-priority human decision source unless a new clarification later supersedes it.

---

## Current dataset snapshot

### Core structure
- Sample size: 34
- Age range: 2–18

### Current dentition-stage counts from derived field
- code 1: 8
- code 2: 14
- code 3: 12

### Current occlusion-related counts
- `occl_tip`
  - 1: 27
  - 2: 1
  - 3: 5
  - 4: 1
- `angle_sinifi`
  - 1: 27
  - 2: 1
  - 3: 5
  - blank: 1
- `infraokluzyon_var`
  - 1 case

### Current doku anomalisi counts
- 0: 24
- 1: 1
- 2: 7
- 7: 2

### Immediate implication
The current CSV is internally coherent as a pre-advisor analysis-ready file, but it is not yet a fully explicit post-advisor analysis-ready file. The raw values are still usable, but the semantic interpretation layer now needs to be revised and formalized.

---

## High-level conclusion: what changed and what did not

### Changes that affect the analysis itself
1. occlusion handling
2. the formal presentation and framing of the caries variable
3. the rule set governing analysis-ready derived variables

### Changes that mainly affect interpretation and manuscript wording
1. doku anomalisi should not be overread as a full phenotype spectrum
2. DI subtype/severity claims are not supportable
3. gingivitis and related clinical variables must remain binary only

### What did not fundamentally change
1. the dataset is still analyzable
2. the gene-mapping layer is not the main source of instability here
3. the stricter small-sample analysis philosophy remains appropriate
4. the project does not need to be restarted from zero

---

## Variable-by-variable adjudication

## 1. `occl_tip` / `angle_sinifi` / `infraokluzyon_var`

### Stable facts
- There is exactly one current case coded as `occl_tip = 4`.
- The current derived `angle_sinifi` leaves that case blank.
- The current derived `infraokluzyon_var` marks that case separately.

### Post-advisor decision
The advisor-discussed clarification requires the following conceptual split:
- Angle classification must remain limited to `1/2/3`.
- Infraocclusion must be handled as a separate finding.

### Unresolved point
The underlying Angle class for the infraocclusion case is still unknown and should not be assumed.

### Scientific recommendation
Do **not** impute or invent the missing underlying Angle class.

Instead, adopt the following rule set for round two:
- Keep raw `occl_tip` unchanged for provenance.
- Create `angle_sinifi_clean` as the primary Angle analysis variable.
- `angle_sinifi_clean` must contain only `1/2/3`.
- If raw `occl_tip = 4`, then `angle_sinifi_clean = missing`.
- Keep `infraokluzyon_var = 1` for that case.
- Use `angle_sinifi_clean` only among eligible cases with non-missing Angle class.
- Report infraocclusion separately as a binary feature and descriptive finding.

### Why this is the best available scientific handling
- It follows the strongest human clarification currently available.
- It prevents fabricated classification.
- It preserves the patient in the dataset.
- It avoids forcing a non-Angle state into the Angle family.

### Supplementary sensitivity option
Because there is only one infraocclusion case, a supplementary scenario analysis may be added:
- scenario A: assign to Angle I
- scenario B: assign to Angle II
- scenario C: assign to Angle III

These scenarios may be used only as supplementary sensitivity checks to test whether Angle-related inference would change materially. They must not replace the primary analysis.

### Required consequence
All previous analyses that treated `1/2/3/4` as a single Angle-family primary variable should now be treated as pre-advisor outputs and must be rerun under the new rules.

---

## 2. `dmft_dmft`

### Stable facts
- The field is a single recorded numeric value.
- It reflects total caries burden in the mouth rather than a clean WHO-style pair of separate indices.
- The existing codebook already describes it as total caries count without component decomposition.

### Post-advisor refinement
The advisor-discussed clarification adds an age/dentition interpretation:
- under 14: mixed/deciduous context
- 14 and above: permanent dentition context

### Scientific recommendation
- Keep the core analytical treatment as a count-like caries burden variable.
- Stop describing it as a standard WHO-style DMFT/dmft index unless the sentence is carefully qualified.
- Add dentition-stage-aware descriptive summaries.
- Consider supplementary sensitivity analysis by dentition stage or age-band.

### Safe wording for manuscript and reports
Preferred language:
- “single recorded total caries burden count”
- “count-like caries outcome derived from the recorded `dmft_dmft` field”

Avoid:
- “standard WHO DMFT/dmft index”
- language implying separate, formally measured deciduous and permanent subindices were available for each subject

### Required consequence
The primary statistical handling of this variable does not necessarily need to be discarded, but the definition, presentation, subgrouping, and manuscript wording require revision.

---

## 3. `doku_anomalisi`

### Stable facts
- `0` means no anomaly.
- The field is a single dominant-code record, not a multi-label phenotype inventory.
- DI type and severity were not recorded.

### Code map currently available
- 0 = none
- 1 = AI
- 2 = DI
- 3 = dentin dysplasia
- 4 = odontodysplasia
- 5 = Turner hypoplasia
- 6 = hypercementosis
- 7 = hypoplasia

### Scientific recommendation
Primary use:
- binary `doku_anomalisi_var`

Secondary use:
- dominant recorded anomaly type

Unsafe use:
- treating this field as a complete phenotype spectrum
- making fine-grained multi-phenotype claims
- making DI subtype or severity claims

### Required consequence
Any existing or planned text that treats this field as a full anomaly map should be downgraded. The current code map is usable, but only with explicit acknowledgment that it records the dominant coded anomaly, not the total anomaly burden.

---

## 4. DI-specific interpretation

### Stable facts
- DI can be inferred by code mapping if coded as such.
- Shields subtype and severity are unavailable.

### Scientific recommendation
- Allow DI presence/absence analysis if coding is fully supported and transparent.
- Forbid subtype or severity analyses.
- Add a clear limitation note in Methods and Limitations.

### Required consequence
Any manuscript or result text that suggests Shields-based DI typing or severity analysis must be revised or removed.

---

## 5. Gingivitis and other 0/1 clinical variables

### Stable facts
The following are recorded as presence/absence only:
- gingivitis
- overjet
- overbite
- open bite
- crossbite

### Scientific recommendation
- Binary prevalence analyses are acceptable.
- Severity analyses are not supported.
- Interpretation must explicitly describe these as yes/no clinical records.

### Required consequence
Do not use severity language, threshold language, or standard indexed-measure language unless separate evidence exists outside the current dataset.

---

## 6. Gene variables and gene grouping

### Stable facts
- `gene_map_v1.csv` provides the current text-to-code mapping support.
- The new semantic clarifications from İnci do not directly destabilize the gene variable layer.

### Scientific recommendation
Retain the current gene mapping logic unless another human clarification changes it later. The current semantic revision effort should focus on occlusion, caries framing, anomaly interpretation, and clinical variable wording rather than on rethinking the gene map.

---

## What is currently aligned vs misaligned

## Aligned
- `dmft_dmft` as a total count-like caries burden measure
- `doku_anomalisi` as a single dominant-code field
- DI subtype/severity absent
- binary yes/no interpretation for gingivitis and related clinical variables
- dentition stage derivation by age
- current raw gene-mapping support

## Misaligned
- `codebook_v3_fixed.md` still presents raw `occl_tip = 4` as infraocclusion without fully separating raw coding from the new primary Angle analysis logic
- the current analysis-ready dataset does not yet formalize `angle_sinifi_clean` as the new primary Angle analysis variable
- round-one outputs reflect the earlier semantic state and therefore cannot simply be treated as the final post-advisor outputs

---

## Controlled round-two semantic rules

These rules should become the explicit control layer for the next revision cycle.

### Rule 1 — raw vs analysis-ready must be separated
Raw fields should remain traceable, but analysis-ready fields must reflect the post-advisor rules.

### Rule 2 — Angle and infraocclusion must be split
- raw `occl_tip` remains unchanged
- `angle_sinifi_clean` becomes the primary Angle analysis field
- `infraokluzyon_var` remains separate and binary

### Rule 3 — unknown Angle class must stay unknown
Do not impute or guess the underlying Angle class for the infraocclusion case.

### Rule 4 — `dmft_dmft` is a count-like caries burden field
Do not present it as a standard WHO-style DMFT/dmft index without strong qualification.

### Rule 5 — `doku_anomalisi` is dominant-code only
Do not interpret it as full multi-label phenotype capture.

### Rule 6 — DI subtype and severity are unavailable
All DI interpretation must remain presence/absence level only.

### Rule 7 — gingivitis and related variables are binary only
No severity or threshold claims should be made from the current data.

### Rule 8 — preserve provenance
Do not silently overwrite pre-advisor outputs. Preserve them as a distinct semantic version.

---

## What must be revised before round-two analysis

## A. Create a post-advisor data decision memo
Create a dedicated markdown file that explicitly states the controlling round-two semantic rules.

Suggested filename:
- `data_decisions_post_advisor_round2.md`

Required contents:
1. `occl_tip = 4` is not part of the primary Angle-family analysis
2. `angle_sinifi_clean` must contain only 1/2/3
3. `infraokluzyon_var` is separate and binary
4. `dmft_dmft` is a count-like total caries burden field
5. `doku_anomalisi` is a single dominant code
6. DI type/severity are unavailable
7. gingivitis and related variables are binary only
8. pre-advisor outputs must be preserved as a prior semantic state

## B. Revise the codebook using additive discipline
Do not destroy the current codebook. Instead:
- create a revised version, or
- add a clearly labeled post-advisor addendum

Key required update:
- distinguish raw `occl_tip` from `angle_sinifi_clean`
- define `infraokluzyon_var` as separate from Angle class
- refine `dmft_dmft` wording
- reinforce dominant-code interpretation for `doku_anomalisi`

## C. Build a new analysis-ready dataset version
Do not overwrite the current CSV silently.

Create a new analysis-ready version with explicit round-two columns, such as:
- `angle_sinifi_clean`
- `infraokluzyon_var`
- `caries_count_total`
- `dentition_donemi_clean`
- `doku_anomalisi_dominant_type`
- `doku_anomalisi_any`
- optional `di_any`

## D. Freeze old outputs
Preserve the current outputs as pre-advisor semantic outputs.

## E. Update rules and instructions
Any rule files, prompts, or analysis instructions that still treat `occl_tip = 4` as part of the main Angle family must be revised before reanalysis begins.

## F. Only then launch round-two analysis
The rerun should be explicitly labeled as the first post-advisor semantic analysis cycle.

---

## Surgical revision map for Copilot

This section is designed specifically to guide the next Copilot revision prompt.

## Files that almost certainly need revision
1. analysis-ready CSV derivative or dataset-preparation script
2. codebook or codebook addendum
3. any semantic control memo or analysis decision file
4. any rule files or prompt files that still encode `occl_tip = 4` inside the primary Angle family
5. any manuscript draft text that describes `dmft_dmft` as standard DMFT/dmft
6. any results/discussion text that overreads `doku_anomalisi`, DI, or gingivitis-related fields

## Files that likely need review but not necessarily deep revision
1. gene-mapping artifacts
2. general small-sample statistics guidance
3. robustness and reporting templates

## Files that should be preserved, not mutated blindly
1. raw data source file
2. pre-advisor outputs
3. historical run manifests
4. archived or provenance folders

## Revision discipline for Copilot
- make surgical revisions only
- preserve provenance
- create new versioned artifacts rather than silent in-place semantic overwrite
- document every semantic revision in a memo or change log

---

## Recommended round-two analysis structure

## Primary analyses
1. cohort descriptives
2. gene-group descriptives
3. binary outcomes:
   - `doku_anomalisi_any`
   - `gingivitis`
   - `caries_any`
   - `infraokluzyon_var` if feasible
4. count/continuous-like outcome:
   - `caries_count_total`

## Secondary analyses
1. `angle_sinifi_clean` among eligible cases only
2. dominant anomaly type analysis
3. DI presence/absence if coding is fully supported
4. dentition-stage-stratified caries summaries

## Supplementary analyses
1. infraocclusion sensitivity scenarios for hypothetical Angle assignment
2. leave-one-out and robustness checks
3. supplementary tables clarifying semantic revisions
4. supplementary note comparing pre-advisor vs post-advisor semantic outputs where relevant

---

## What should not be done in round two

- Do not impute the missing underlying Angle class as if known.
- Do not keep using `1/2/3/4` as the main Angle-family analysis variable.
- Do not call `dmft_dmft` a standard WHO-style DMFT/dmft index without qualification.
- Do not treat `doku_anomalisi` as a full multi-label phenotype field.
- Do not write DI subtype or severity claims.
- Do not write severity claims for gingivitis, overjet, overbite, open bite, or crossbite.
- Do not silently overwrite pre-advisor outputs.
- Do not begin round-two analysis before the semantic control layer is updated.

---

## Risk assessment

### High-impact issue
- occlusion semantic revision

### Moderate-impact issues
- caries-variable framing and dentition-stage presentation
- dominant-code interpretation for `doku_anomalisi`
- manuscript wording drift

### Lower-impact but still important issues
- DI limitation wording
- binary-variable wording discipline
- ensuring that rule files and prompts no longer encode outdated occlusion logic

---

## Acceptance criteria before round-two rerun

Round-two analysis should not begin until all of the following are true:

1. a post-advisor data decision memo exists
2. the codebook has been revised or supplemented
3. a new analysis-ready dataset version exists
4. pre-advisor outputs are clearly preserved
5. outdated occlusion logic has been removed from active rule/prompt/instruction files
6. the round-two primary analysis variables are explicitly defined
7. a change log or revision memo records what was changed and why

---

## Final judgment

The project is still scientifically salvageable and methodologically workable.

This is not a case where the earlier analysis becomes worthless. It is a case where:
- one variable family (`occl_tip`) requires a real analytical revision,
- one major dental-burden outcome (`dmft_dmft`) requires stricter framing and subgroup-aware reporting,
- and several phenotype variables require narrower interpretation.

The correct immediate action is not analysis execution. The correct immediate action is semantic revision and analysis-readiness reconstruction.

The proper sequence is:
1. revise the semantic control documents,
2. create a new analysis-ready dataset version,
3. preserve pre-advisor outputs,
4. update rule files and prompts,
5. then rerun the full analysis under post-advisor rules.

---

## Bottom-line answer to the key scientific question

Can the unknown underlying Angle class for the one infraocclusion case be scientifically merged into the results without asking İnci again?

Yes, but only in the following disciplined form:
- primary Angle analysis: exclude that case by setting `angle_sinifi_clean` to missing
- keep the patient in the dataset through `infraokluzyon_var = 1`
- report infraocclusion separately
- optionally run supplementary sensitivity scenarios to test whether hypothetical Angle assignment would materially change inference

That approach is scientifically safer than inventing a class label and safer than deleting the patient from the analysis entirely.

---

## Operational next-step checklist

1. Create `data_decisions_post_advisor_round2.md`
2. Create revised codebook or codebook addendum
3. Create new analysis-ready CSV version
4. Preserve old outputs as pre-advisor outputs
5. Update any active rule files, prompts, or instructions that still encode outdated occlusion logic
6. Launch second-round analysis only after the above revisions are completed
7. Compare pre-advisor and post-advisor outputs explicitly where meaningful

---

## Final use instruction

This report should now be treated as the main briefing document for the next Copilot prompt. The next prompt should instruct Copilot to revise only what must be revised, preserve what should be preserved, and prepare the project for a clean round-two rerun under explicit post-advisor semantic rules.


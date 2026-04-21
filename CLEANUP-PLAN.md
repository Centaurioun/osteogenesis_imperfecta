## 1. Executive Summary

This blueprint defines a **planning-only**, provenance-preserving cleanup and reorganization of the repository. It does **not** execute any changes. Its purpose is to make the repository safer and easier to use for manuscript preparation while preserving the evidentiary chain from round one to the finalized round-two reconciled package.

The target state makes `04_manuscript/` the **single manuscript-facing home** for the **round-two reconciled package**, while preserving `FINAL_1_2` as the **round-one canonical baseline** for comparison, audit, and provenance.

This plan is governed by six controlling principles:

- The **round-two reconciled package** becomes the only manuscript-facing authority.
- `FINAL_1_2` remains preserved and visible as **baseline/provenance**, not manuscript authority.
- Post-advisor semantic-control files that explain why round two differs from round one remain explicitly linked to the manuscript-facing package.
- Operational mirrors, Colab bundles, validation workspaces, and AI handoff materials are separated from manuscript-facing assets.
- Cleanup must be **reversible**, **fully backed up**, and **validated after execution**.
- The plan must distinguish clearly between items that should be **copied**, **kept in place and referenced**, **reclassified**, **archived later**, or **left untouched**.

This blueprint is therefore not just an organization plan. It is an **authority-control plan**, a **provenance-preservation plan**, and a **future execution map**.

---

## 2. Planning Assumptions and Authority Rules

### 2.1 Binding assumptions

The following assumptions are binding for the later cleanup execution:

- The manuscript-facing authority after cleanup is the **final reconciled round-two package**, centered under `04_manuscript/`.
- The manuscript-facing authority set is derived primarily from:
  - final reconciled round-two reports currently under `03_outputs/reports/run_20260418_1037_post_advisor_round2_colab/`
  - final manuscript-facing round-two tables and figures
  - post-advisor semantic-control files required to interpret round two
- The following remain essential, but as **baseline/supporting/provenance authority**, not final manuscript authority:
  - `03_outputs/active/outputs_FINAL_1_2/`
  - `03_outputs/active/figures_FINAL_1_2/`
  - `03_outputs/active/figures_FINAL_1_2_TR/`
  - `Manuscript_Data/`
- Root-level round-two files and bundle mirrors are transitional and must not remain manuscript-facing after cleanup.
- Colab bundles under `05_operations/colab_bundles/` are operational packaging artifacts, not authority.
- Historical preservation is **no-delete by default**. Future execution may move, relabel, or archive, but not destructively remove repository-tracked content.

### 2.2 Authority rules to enforce later

The following authority model must be enforced after cleanup:

- `04_manuscript/` becomes the **only manuscript-facing authority zone**.
- `01_data/` remains the authoritative **data source zone**.
- `02_analysis/` remains the authoritative **analysis code and validation zone**.
- `03_outputs/` remains the authoritative **machine-output and release-history zone**.
- `05_operations/` remains the **operational/tooling zone**.
- `99_archive/` remains the **archive and historical retrieval zone**.
- `Manuscript_Data/` becomes an explicitly labeled **preserved historical manuscript package**, not active manuscript authority.

### 2.3 Minimum manuscript-facing authority set

The cleanup execution must define and preserve a **minimum manuscript-facing authority set**. That minimum set should include only:

- final reconciled round-two manuscript-facing reports
- final manuscript-facing round-two tables
- final manuscript-facing round-two figures
- a manuscript README / authority index
- links or references to the semantic-control files needed to interpret the package
- links to the round-one baseline and provenance materials

This minimum set must **not** include raw data copies, operational bundle mirrors, general prompts, or AI handoff materials.

### 2.4 Supporting but non-manuscript-facing set

The following should remain supporting, not manuscript-facing:

- round-two validation notebook and scripts
- round-two run manifests and robustness tables
- round-two derived dataset and source codebooks
- round-one baseline output lanes
- archival release lineages
- operational bundles and portability artifacts

### 2.5 Artifact handling policy

Before any future execution, every major artifact group must be assigned exactly one of the following handling rules:

- **Copy into manuscript authority**
  - use for final manuscript-facing reports/tables/figures where a curated manuscript-facing package is needed.
- **Keep in place and reference/index**
  - use for data, code, manifests, baseline packages, and other artifacts whose authoritative source should remain where it already belongs.
- **Relabel/reclassify in place**
  - use where movement is unnecessary but role clarity must change.
- **Archive later**
  - use for superseded or historical materials that should remain retrievable but no longer sit near active manuscript work.
- **Leave untouched pending review**
  - use for ambiguous or low-confidence areas.

No artifact should be moved or copied during execution without first being assigned one of these policy classes.

### 2.6 Handling rules that must apply during execution

To reduce ambiguity later, the following execution rules are binding:

- Any file copied into `04_manuscript/` must have a clearly traceable source location recorded in a migration log or manuscript authority index.
- Any artifact handled as **REFERENCE\_ONLY** must be reachable through an explicit index or README entry from `04_manuscript/` if manuscript users are expected to consult it.
- Any artifact handled as **RECLASSIFY\_IN\_PLACE** must receive a role label in documentation, so its status is obvious without opening git history.
- Any artifact handled as **ARCHIVE\_LATER** must not be moved in the first execution wave unless its replacement or retained reference path is already stable and validated.
- Any artifact marked **HUMAN\_REVIEW\_REQUIRED** is out of scope for automatic execution until a decision is recorded.

### 2.7 First-wave cleanup boundaries

The first cleanup wave should be intentionally conservative. It should:

- establish `04_manuscript/` as the manuscript-facing authority zone,
- copy only the necessary manuscript-facing round-two materials,
- add indexes, README files, provenance notes, and role labels,
- reclassify ambiguous authority claims in-place,
- and defer deep archival normalization until the new structure is stable.

The first cleanup wave should **not**:

- deeply restructure `01_data/`,
- deeply restructure `02_analysis/`,
- move baseline packages aggressively,
- archive `Manuscript_Data/`,
- archive unresolved or ambiguous zones,
- or attempt a broad tooling cleanup across AI/operations directories.

### 2.8 Checkpoint 1

- Manuscript authority is explicitly separated from provenance authority.

- The minimum manuscript-facing authority set is explicitly defined.

- Operational/tooling material is separated from manuscript-facing outputs.

- An artifact handling policy now exists.

- First-wave scope is explicitly constrained.

- No execution actions were taken; this remains a planning document only.

- Manuscript authority is explicitly separated from provenance authority.

- The minimum manuscript-facing authority set is explicitly defined.

- Operational/tooling material is separated from manuscript-facing outputs.

- An artifact handling policy now exists.

- No execution actions were taken; this remains a planning document only.

---

## 3. Backup Strategy

Before any future cleanup execution, require all four backup layers below.

### 3.1 Required backup layers

1. **Full filesystem snapshot**

   - Create a full repo zip snapshot of the working tree, including top-level docs, manuscript assets, operations bundles, and archive indexes.
   - Exclude only clearly regenerable environment internals if storage is an issue, but prefer a full working-tree capture.

2. **Git-native backup**

   - Create an annotated pre-cleanup git tag such as `pre_cleanup_manuscript_reorg_2026-04-18`.
   - Create a `git bundle` file containing all refs so the repository can be reconstructed even outside the local clone.

3. **Optional freeze branch**

   - Create a branch such as `freeze/pre_cleanup_manuscript_reorg`.
   - Use it as the rollback anchor if the cleanup later spans multiple commits.

4. **Inventory snapshot**

   - Export a path inventory and file count manifest before any changes.
   - Include checksums at least for manuscript-facing and provenance-critical files.

### 3.2 Why one backup method is not sufficient

- A zip snapshot preserves the visible working tree, including untracked files and operational bundles that may not be committed.
- Git preserves history, tags, and tracked-file reconstruction, but may miss untracked or ignored working-tree artifacts that matter here.
- A rollback branch makes iterative reversal easier than restoring from a bundle alone.
- An inventory/checksum snapshot verifies that the backups are usable and complete.

### 3.3 Rollback strategy

- If any post-cleanup validation fails, stop further moves immediately.
- Restore repo state from the freeze branch or reset to the tagged commit in a separate recovery branch.
- Restore any untracked or bundle artifacts from the zip snapshot.
- Use the move log and checksum manifest to reverse path changes in reverse order.
- Re-run path validation and manuscript authority validation before resuming.

### 3.4 Backup verification

- Confirm the zip opens and contains `04_manuscript/`, `Manuscript_Data/`, `03_outputs/`, `01_data/`, `05_operations/colab_bundles/`, and `99_archive/`.
- Confirm the git tag resolves and `git bundle verify` passes.
- Confirm the freeze branch exists and points to the intended pre-cleanup commit.
- Confirm inventory counts and spot-check hashes for the key authority files.

### 3.5 Checkpoint 2

- At least two backup layers are proposed; this plan uses four.
- Rollback is explicitly defined.
- Backup verification is part of the mandatory pre-execution workflow.

---

## 4. Current-State Functional Inventory

### 4.1 Root documentation and control files

Includes:

- `README.md`
- `WORKSPACE_INDEX.md`
- `WORKSPACE_MAP.md`
- `WORKSPACE_ORGANIZATION_PLAN.md`
- `AGENTS.md`
- `HANDOFF_CLAUDE.md`
- `OI_POST_ADVISOR_DATA_SEMANTICS_AND_ROUND2_REANALYSIS_STATUS_REPORT.md`
- `data_decisions_post_advisor_round2.md`

Function:

- workspace navigation
- governance and handoff
- round-two semantic control

Current classification:

- mixed governance + manuscript-supporting + operational

Future treatment:

- keep governance/navigation at root
- copy or surface manuscript-critical semantic-control files into `04_manuscript/`
- retain original root locations as provenance or governance sources unless later explicitly reclassified

### 4.2 `00_governance/`

Function:

- project-scope and protocol-style documentation
- study framing and historical briefing

Classification:

- supporting reference

Future treatment:

- keep in place
- cross-link from manuscript docs only where needed

### 4.3 `01_data/`

Function:

- raw source data
- reference codebooks
- derived round-two semantic outputs

Classification:

- raw/reference = authoritative supporting data
- derived round-two dataset and provenance note = manuscript-supporting authority

Future treatment:

- keep in place as source data zone
- reference from `04_manuscript/`
- do not duplicate raw or primary derived datasets into the manuscript-facing zone unless there is a compelling reason and no authority confusion results

### 4.4 `02_analysis/`

Function:

- active FINAL\_1\_2 notebook/script lane
- legacy lineages
- prompts
- validation workspaces

Classification:

- active FINAL\_1\_2 lane = baseline/provenance authority
- validation round-two scripts/notebooks = manuscript-supporting authority
- prompts = operational/provenance

Future treatment:

- keep as analysis zone
- index manuscript-supporting round-two scripts/notebooks from `04_manuscript/`
- do not move authoritative scripts/notebooks into manuscript-facing authority unless execution later explicitly requires a curated copy

### 4.5 `03_outputs/active/`

Function:

- FINAL\_1\_2 outputs and figures

Classification:

- provenance/history plus comparison authority

Future treatment:

- keep in place
- relabel in docs as round-one baseline
- do not let it remain manuscript-facing after cleanup

### 4.6 `03_outputs/legacy/`

Function:

- v3 through FINAL\_1\_1 generations and summary remnants

Classification:

- superseded but preserved
- selective archive candidate

Future treatment:

- remain outside manuscript-facing areas
- eligible for later archive normalization

### 4.7 `03_outputs/reports/`

Function:

- round-two run folders, including the reconciled Colab folder

Classification:

- `run_20260418_1037_post_advisor_round2_colab` = manuscript-facing authority source
- non-reconciled sibling run folder = superseded/provisional support

Future treatment:

- manuscript-facing reports/tables/figures surfaced into `04_manuscript/`
- source run folders retained as provenance or run history
- no direct manuscript-facing authority claims should remain in `03_outputs/reports/` after cleanup

### 4.8 `04_manuscript/`

Function:

- intended manuscript-facing home

Current state:

- reserved integration domain with only a README

Classification:

- future authoritative destination

Future treatment:

- becomes the central manuscript package

### 4.9 `05_operations/`

Function:

- Colab bundles
- empty operations subfolders
- future automation/manifests/logs structure

Classification:

- operational/tooling

Future treatment:

- keep operational bundles here
- never let them remain manuscript-facing

### 4.10 `99_archive/`

Function:

- prior reorg wave
- snapshots
- indexes
- non-manuscript historical docs

Classification:

- provenance/history + archive

Future treatment:

- keep as archival zone
- expand with future cleanup-wave records if needed

### 4.11 `Manuscript_Data/`

Function:

- curated FINAL.1.2 manuscript package with registry files, outputs, figures, provenance, and AI handoff materials

Classification:

- baseline/provenance authority
- not future manuscript-facing authority

Future treatment:

- preserved as a historical package
- cross-linked from new manuscript provenance notes
- not removed and not casually archived during the first cleanup wave

### 4.12 AI coordination and automation zones

Includes:

- `CLAUDE_HANDOFF/`
- `.claude/`
- `.agents/`
- `.github/`
- `skill/`

Function:

- AI coordination and repo automation context

Classification:

- operational/tooling and limited provenance

Future treatment:

- keep outside manuscript-facing areas

### 4.13 Residual / ambiguous zones

Includes:

- `archive_misaligned/`
- `agents/`
- `scripts/` (including `scripts/download_claude_docs.py`)

Classification:

- unclear / needs review or operational residue

Future treatment:

- flag for human review before any move/archive decision

### 4.14 Checkpoint 3

- Major zones have been identified.
- The final round-two authority source has been recognized.
- Provisional, operational, provenance, and archival zones are explicitly distinguished.
- Ambiguous zones are explicitly flagged instead of being silently classified.

---

## 5. Classification Framework

### 5.1 Classification categories

- **Authoritative for manuscript**
  - what the manuscript team should read first after cleanup
- **Supporting reference**
  - needed to interpret, trace, or reproduce the authoritative package
- **Operational tooling**
  - bundles, handoff systems, prompts, AI context, automation, portability assets
- **Provenance/history**
  - baselines, historical packages, move logs, registries, comparison anchors
- **Superseded but preserved**
  - replaced materials that still matter for traceability
- **Archive candidate**
  - material that should remain retrievable but no longer stay near active work
- **Unclear / needs review**
  - material whose future role is not obvious from current structure

### 5.2 Action classes to apply later

For execution safety, each major artifact group must later receive both:

- a **classification category**, and
- an **action class**.

Action classes:

- **COPY\_TO\_MANUSCRIPT**
- **REFERENCE\_ONLY**
- **RECLASSIFY\_IN\_PLACE**
- **ARCHIVE\_LATER**
- **HUMAN\_REVIEW\_REQUIRED**

### 5.3 Application to major artifact groups

| Artifact group                                                                                                   | Classification                               | Action class                                                                     | Notes                                                               |
| ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Reconciled round-two reports/tables/figures in `03_outputs/reports/run_20260418_1037_post_advisor_round2_colab/` | Authoritative for manuscript                 | COPY\_TO\_MANUSCRIPT                                                             | Manuscript-facing curated copies should live under `04_manuscript/` |
| Root semantic-control files and round-two derived dataset/codebook addendum                                      | Supporting reference                         | REFERENCE\_ONLY or selective COPY\_TO\_MANUSCRIPT for key narrative control docs | Avoid duplicating source-of-truth data/codebooks casually           |
| `02_analysis/scripts/validation/` and `02_analysis/notebooks/validation/`                                        | Supporting reference                         | REFERENCE\_ONLY                                                                  | Keep authoritative code in `02_analysis/`                           |
| `03_outputs/reports/run_20260418_1037_post_advisor_round2/`                                                      | Superseded but preserved                     | RECLASSIFY\_IN\_PLACE or ARCHIVE\_LATER                                          | Must be clearly marked non-authoritative                            |
| `03_outputs/active/outputs_FINAL_1_2/` and figures                                                               | Provenance/history                           | REFERENCE\_ONLY                                                                  | Round-one baseline only                                             |
| `Manuscript_Data/`                                                                                               | Provenance/history                           | REFERENCE\_ONLY for first wave; ARCHIVE\_LATER only by later decision            | Must not remain ambiguous manuscript authority                      |
| `03_outputs/legacy/`                                                                                             | Superseded but preserved / archive candidate | ARCHIVE\_LATER                                                                   | Keep accessible until migration confidence is high                  |
| `05_operations/colab_bundles/`                                                                                   | Operational tooling                          | RECLASSIFY\_IN\_PLACE                                                            | Explicitly label as operational mirrors only                        |
| `CLAUDE_HANDOFF/`, `.claude/`, prompts, AI instructions                                                          | Operational tooling plus limited provenance  | RECLASSIFY\_IN\_PLACE                                                            | Keep out of manuscript-facing structure                             |
| `99_archive/`                                                                                                    | Provenance/history and archive               | RECLASSIFY\_IN\_PLACE                                                            | Keep as archive home                                                |
| `archive_misaligned/`, `agents/`                                                                                 | Unclear / needs review                       | HUMAN\_REVIEW\_REQUIRED                                                          | Do not move/archive automatically                                   |

### 5.4 Checkpoint 4

- Every major artifact group now has both a classification and an action class.
- No major zone is left unclassified.
- Ambiguities are surfaced rather than hidden.

---

## 6. Authoritative Manuscript Package Definition

After cleanup, the manuscript-facing authority must be defined as a **single curated package under **``.

### 6.1 Minimum manuscript-facing authority set

This set should contain only what a manuscript writer or reviewer needs first:

- final reconciled round-two narrative reports
- final manuscript-facing round-two result tables
- final manuscript-facing round-two figures
- a manuscript authority README / index that states this is the only manuscript-facing authority set
- a semantic-control index that points to the post-advisor files needed to interpret round two
- a provenance note that points to the round-one baseline and historical package locations

### 6.2 Baseline materials that must remain linked

These remain necessary for comparison and provenance and must be referenced from the manuscript package, but not absorbed into it as manuscript-facing authority:

- `03_outputs/active/outputs_FINAL_1_2/`
- `03_outputs/active/figures_FINAL_1_2/`
- `03_outputs/active/figures_FINAL_1_2_TR/`
- `Manuscript_Data/`
- selected `03_outputs/legacy/` release lineages where comparison history matters
- relevant `99_archive/` indexes and prior move logs

### 6.3 Supporting materials that must stay connected

These should remain linked but not manuscript-facing:

- round-two validation notebook and script
- versioned round-two derived dataset
- round-two run manifests and robustness tables
- codebook addendum and provenance note
- minimal methods-supporting references from governance and baseline manuscript materials

### 6.4 What must never be confused with manuscript authority

- Colab bundles and their mirrored contents in `05_operations/colab_bundles/`
- root-level transient placement of semantic-control files
- non-reconciled round-two run folder
- FINAL\_1\_2 baseline outputs
- legacy v3/vFINAL generations
- AI handoff and prompt materials

### 6.5 Checkpoint 5

- Manuscript-facing authority is explicit.
- The minimum manuscript-facing set is explicit.
- Provenance authority is explicit.
- The two are not conflated.

---

## 7. Proposed Target Repo Architecture

The target structure should be simpler and more use-oriented than the current draft. The goal is clarity, not bureaucratic nesting.

### 7.1 Proposed manuscript-facing structure

```text
04_manuscript/
├─ README.md
├─ MAP.md
├─ authority/
│  ├─ manuscript_authority_index.md
│  ├─ reports/
│  ├─ tables/
│  └─ figures/
├─ context/
│  ├─ semantic_control/
│  ├─ methods_support/
│  └─ provenance_note.md
├─ trace/
│  ├─ analysis_code_index.md
│  ├─ run_manifests/
│  └─ robustness_and_supporting_tables/
└─ baseline/
   ├─ round1_baseline_index.md
   └─ comparison_reports/
```

### 7.2 Why this version is better than the earlier over-nested draft

- It reduces unnecessary numeric subzones.
- It is easier for a new collaborator to understand quickly.
- It still separates manuscript authority, context, trace, and baseline.
- It minimizes documentation sprawl while preserving enough structure for clarity.

### 7.3 Complementary non-manuscript structure

- `01_data/` stays the data source zone.
- `02_analysis/` stays the code and validation zone.
- `03_outputs/active/` stays the round-one baseline output zone.
- `03_outputs/reports/` stays the run-output/provenance zone.
- `05_operations/` stays operational only.
- `99_archive/` stays the archive zone.
- `Manuscript_Data/` stays preserved as historical manuscript package unless a later approved archival step moves it.

### 7.4 Design constraints

- No unnecessary deep nesting beyond the functional separation above.
- `04_manuscript/` holds the authoritative manuscript package and its immediate interpretation aids, not full duplicated raw data and not operational bundles.
- Where duplication would create authority confusion, prefer link/index/reference behavior in docs over copied content.
- Manuscript-facing copies must be curated, not wholesale folder dumps.
- The same artifact should not silently appear as manuscript authority in more than one location.

### 7.5 Minimum required population of `04_manuscript/`

At minimum, the future manuscript structure should contain:

- one clear manuscript-facing README,
- one authority index,
- the final round-two reconciled report set,
- the final manuscript-facing tables,
- the final manuscript-facing figures if they exist and are approved,
- one provenance note,
- one baseline index,
- and one trace/index document linking to analysis code and source data.

Anything beyond that must justify its inclusion.

### 7.6 Checkpoint 6

- The target architecture is coherent.

- Manuscript-facing materials are easy to find.

- Provenance is preserved.

- Operational artifacts are separated from manuscript-facing materials.

- The manuscript structure is not a dumping ground.

- Minimum required population is explicitly defined.

- The target architecture is coherent.

- Manuscript-facing materials are easy to find.

- Provenance is preserved.

- Operational artifacts are separated from manuscript-facing materials.

- The manuscript structure is not a dumping ground.

---

## 8. Migration Map

### 8.1 Major manuscript-facing round-two materials

| Source                                                                                                                   | Proposed future location                     | Action class         | Notes / risks                                                        |
| ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- | -------------------- | -------------------------------------------------------------------- |
| `03_outputs/reports/run_20260418_1037_post_advisor_round2_colab/round2_post_advisor_analysis_report_final_reconciled.md` | `04_manuscript/authority/reports/`           | COPY\_TO\_MANUSCRIPT | Primary manuscript-facing report; retain source folder as provenance |
| `03_outputs/reports/run_20260418_1037_post_advisor_round2_colab/round1_vs_round2_comparison_report_final_reconciled.md`  | `04_manuscript/baseline/comparison_reports/` | COPY\_TO\_MANUSCRIPT | Comparison support for manuscript interpretation                     |
| `03_outputs/reports/run_20260418_1037_post_advisor_round2_colab/round2_analysis_plan_final_reconciled.md`                | `04_manuscript/context/methods_support/`     | COPY\_TO\_MANUSCRIPT | Methods-supporting context, not primary results authority            |
| `03_outputs/reports/run_20260418_1037_post_advisor_round2_colab/primary_results_table.csv`                               | `04_manuscript/authority/tables/`            | COPY\_TO\_MANUSCRIPT | Manuscript-facing numeric authority                                  |
| manuscript-facing round-two figure set (once confirmed)                                                                  | `04_manuscript/authority/figures/`           | COPY\_TO\_MANUSCRIPT | Only final figure set, not operational image clutter                 |

### 8.2 Supporting trace and reproducibility materials

| Source                                                                                      | Proposed future location                                      | Action class                                                   | Notes / risks                                                  |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `03_outputs/reports/run_20260418_1037_post_advisor_round2_colab/robustness_loo_results.csv` | `04_manuscript/trace/robustness_and_supporting_tables/`       | COPY\_TO\_MANUSCRIPT or REFERENCE\_ONLY pending manuscript use | Decide whether manuscript-facing supplement or trace-only      |
| `03_outputs/reports/run_20260418_1037_post_advisor_round2_colab/run_manifest.json`          | `04_manuscript/trace/run_manifests/`                          | COPY\_TO\_MANUSCRIPT or REFERENCE\_ONLY                        | Reproducibility trace, not reader-facing core authority        |
| `02_analysis/scripts/validation/oi_oro_dental_post_advisor_round2_reanalysis_v1.py`         | remain in `02_analysis/`; indexed from `04_manuscript/trace/` | REFERENCE\_ONLY                                                | Keep authoritative code in analysis zone                       |
| `02_analysis/notebooks/validation/oi_oro_dental_post_advisor_round2_reanalysis_v1.ipynb`    | remain in `02_analysis/`; indexed from `04_manuscript/trace/` | REFERENCE\_ONLY                                                | Do not duplicate unless later needed for manuscript supplement |

### 8.3 Semantic-control and provenance materials

| Source                                                                                         | Proposed future location                                          | Action class                            | Notes / risks                                                |
| ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------- | ------------------------------------------------------------ |
| `OI_POST_ADVISOR_DATA_SEMANTICS_AND_ROUND2_REANALYSIS_STATUS_REPORT.md`                        | `04_manuscript/context/semantic_control/`                         | COPY\_TO\_MANUSCRIPT                    | Also keep root version for provenance/governance             |
| `data_decisions_post_advisor_round2.md`                                                        | `04_manuscript/context/semantic_control/`                         | COPY\_TO\_MANUSCRIPT                    | Binding semantic memo                                        |
| `01_data/reference/codebook_post_advisor_round2_addendum_v1.md`                                | reference from `04_manuscript/context/semantic_control/`          | REFERENCE\_ONLY                         | Avoid duplicating codebook source-of-truth casually          |
| `01_data/derived/POST_ADVISOR_ROUND2_PROVENANCE_NOTE.md`                                       | `04_manuscript/context/provenance_note.md` or linked from there   | COPY\_TO\_MANUSCRIPT or REFERENCE\_ONLY | Depends on whether a manuscript-facing copy improves clarity |
| `01_data/derived/osteogenesis_imperfecta_analysis_ready_post_advisor_round2_v1_2026-04-18.csv` | remain in `01_data/derived/`; indexed from `04_manuscript/trace/` | REFERENCE\_ONLY                         | Data source belongs in `01_data/`                            |

### 8.4 Round-one baseline materials

| Source                                    | Proposed future location                                | Action class    | Notes / risks                                                |
| ----------------------------------------- | ------------------------------------------------------- | --------------- | ------------------------------------------------------------ |
| `03_outputs/active/outputs_FINAL_1_2/`    | remain in place; indexed from `04_manuscript/baseline/` | REFERENCE\_ONLY | Must stay clearly baseline only                              |
| `03_outputs/active/figures_FINAL_1_2/`    | remain in place; indexed from `04_manuscript/baseline/` | REFERENCE\_ONLY | Do not duplicate unless later needed for comparison appendix |
| `03_outputs/active/figures_FINAL_1_2_TR/` | remain in place; indexed from `04_manuscript/baseline/` | REFERENCE\_ONLY | Baseline-only                                                |
| `Manuscript_Data/`                        | remain in place; indexed from `04_manuscript/baseline/` | REFERENCE\_ONLY | Historical package preserved in place for first cleanup wave |

### 8.5 Operational mirrors and superseded round-two materials

| Source                                                                              | Proposed future location                                | Action class                              | Notes / risks                                         |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------- | ----------------------------------------- | ----------------------------------------------------- |
| `05_operations/colab_bundles/oi_round2_post_advisor_colab_bundle_20260418/` and zip | remain in `05_operations/colab_bundles/`                | RECLASSIFY\_IN\_PLACE                     | Label explicitly as operational portability artifacts |
| `03_outputs/reports/run_20260418_1037_post_advisor_round2/`                         | remain in place for first wave; later archive candidate | RECLASSIFY\_IN\_PLACE then ARCHIVE\_LATER | Must be explicitly labeled provisional/superseded     |
| `03_outputs/legacy/`                                                                | later archive normalization                             | ARCHIVE\_LATER                            | Preserve retrievability                               |

### 8.6 Highest-risk ambiguity items needing hard decisions before execution

- Whether `primary_results_table.csv` and `robustness_loo_results.csv` should both be copied into `04_manuscript/` or only indexed there.
- Whether a manuscript-facing copy of the semantic status report is preferable to a manuscript-facing index pointing to the original file.
- Whether `Manuscript_Data/` should remain fully in place for the first wave or be partially surfaced via curated provenance notes only.

### 8.7 Migration-map execution gate

Before the future cleanup execution starts, the migration map must be frozen into an approved source-to-destination sheet that identifies for every major artifact group:

- source path
- target path
- action class
- whether a copy or reference strategy is used
- whether post-move labeling is required
- whether checksum verification is required
- whether human approval is required before movement

No execution should begin until that sheet is reviewed and accepted.

### 8.8 Checkpoint 7

- All major future moves and normalizations are mapped.
- Every major artifact group now has an action class.
- No manuscript-facing group is left without a planned home.
- Dependency risks are explicitly acknowledged.

---

## 9. Archive Strategy

### 9.1 What should eventually be archived

- deep legacy output generations in `03_outputs/legacy/` that are no longer routinely consulted
- historical reorg materials already under `99_archive/by_date/`
- superseded prompt/handoff residues not needed near active manuscript work
- potentially `Manuscript_Data/`, but **not in the first cleanup wave** unless a later explicit approval is given

### 9.2 What should remain easily reachable

- the round-two manuscript package in `04_manuscript/`
- the round-one baseline in `03_outputs/active/` and `Manuscript_Data/`
- `01_data/` source materials
- `02_analysis/validation/` round-two code lineage
- archive indexes and move logs

### 9.3 Labeling strategy

- use `superseded`, `baseline`, `provenance`, and `archive_candidate` labels in README/index files
- never label baseline comparison assets as archive-only
- bundles must be labeled `operational mirror` or `portable bundle`, not `canonical`

### 9.4 Retrievability rules

- every future archive move must create or update:
  - archive lookup CSV
  - source-to-destination map
  - archive note with rationale and retrieval path
- archived payloads may be compressed later, but indexes and README notes remain uncompressed

### 9.5 Required archive documentation

- archive rationale note per wave
- move log
- retrieval instructions
- list of any external dependencies or scripts affected by the move

### 9.6 Checkpoint 8

- Archive candidates are identified.
- Archive rationale is documented.
- Retrievability is preserved.
- First-wave cleanup avoids premature archiving of high-provenance materials.

---

## 10. Documentation / README / Map Plan

### 10.1 Top-level docs

- Keep root `README.md` as workspace overview, but revise later to point first to `04_manuscript/README.md` for manuscript use.
- Keep `WORKSPACE_INDEX.md` as the operational index across all zones.
- Revise `WORKSPACE_MAP.md` so `04_manuscript/` is shown as the manuscript-facing authority zone.

### 10.2 `04_manuscript/` docs

Add:

- `README.md` as the manuscript start point
- `MAP.md` showing the round-two package layout
- `authority/manuscript_authority_index.md` listing authoritative reports, tables, figures, semantic-control links, and baseline comparison links
- `context/provenance_note.md` explaining what remains elsewhere and why

### 10.3 `03_outputs/` docs

Update later so:

- `active/` is clearly marked as round-one baseline
- `reports/` is clearly marked as run/provenance zone
- no claim remains that `outputs_FINAL_1_2` is the manuscript-facing canonical package

### 10.4 `05_operations/` docs

- add a bundle note stating all Colab bundles are operational mirrors only
- add a manifest/index for bundle contents if one does not already exist

### 10.5 `Manuscript_Data/` docs

- preserve existing docs
- add future note marking it as preserved FINAL\_1\_2 historical manuscript package and baseline package

### 10.6 `99_archive/` docs

- keep archive README and MAP
- add cleanup-wave note when future execution happens

### 10.7 Additional documentation layers

- add a glossary or legend only if naming remains ambiguous after cleanup
- add a migration map doc under `04_manuscript/context/` or `04_manuscript/trace/`
- add manuscript-usage notes to help a reader know which files to cite, compare, or ignore

### 10.8 Checkpoint 9

- Documentation needs are specified at each major level.
- Naming conventions are coherent with the documentation plan.
- The documentation plan serves manuscript use, not just tidiness.

---

## 11. Naming Convention Plan

### 11.1 Manuscript-facing reports

- Pattern: `round2_<purpose>_final_reconciled.<ext>`
- Preserve existing filenames where provenance matters; normalize only where ambiguity is high.
- Use `final_reconciled` only for round-two manuscript authority.

### 11.2 Final analysis outputs

- Pattern: `round2_<artifact>_final.<ext>` for manuscript-facing exports where renaming is needed.
- Baseline round-one outputs retain historical FINAL\_1\_2 naming and are documented as baseline, not renamed casually.

### 11.3 Scripts and notebooks

- Keep execution lineage names in `02_analysis/` unless later standardization is approved.
- Prefer future pattern: `oi_<scope>_round2_<role>_v1`.
- Validation variants like `_fast` remain clearly non-authoritative.

### 11.4 Superseded files

- Label in docs and indexes as `superseded` rather than renaming in bulk.
- If future renames happen, suffix with `_superseded_<date>` only when needed to prevent confusion.

### 11.5 Archive folders

- Use `YYYY-MM-DD_cleanup_wave_name` under `99_archive/by_date/`.
- Use lineage-based folders under `99_archive/by_release/` only for stable historical families.

### 11.6 Maps, indexes, and READMEs

- Root-level shared docs remain `README.md`, `WORKSPACE_INDEX.md`, `WORKSPACE_MAP.md`.
- Manuscript-specific docs use `README.md`, `MAP.md`, `manuscript_authority_index.md`, and `provenance_note.md`.
- Avoid multiple files all called “final” without round context.

---

## 12. Risk Assessment

### 12.1 Major risks and mitigations

- **Broken script/notebook paths**

  - Matters because notebooks, manifests, and reports reference current locations.
  - Mitigation: do not move code out of `02_analysis/`; update references after moves; validate paths.
  - Check: grep for old paths after cleanup.

- **Broken README/map links**

  - Matters because this repo is documentation-heavy and navigation is a core function.
  - Mitigation: update all maps after movement; maintain a source-destination map.
  - Check: link/path audit across root docs and manuscript docs.

- **Duplicate authority**

  - Matters because both `Manuscript_Data/` and new `04_manuscript/` could look canonical.
  - Mitigation: explicit authority statement in both locations.
  - Check: only one location may claim manuscript-facing authority.

- **Loss of provenance clarity**

  - Matters because round-one vs round-two distinction is central.
  - Mitigation: baseline index plus semantic-control note plus migration note.
  - Check: a reviewer should be able to trace round two back to round one without guessing.

- **Operational mirrors mistaken for authority**

  - Matters because bundle contents mirror repo materials.
  - Mitigation: label bundle roots and `05_operations/README` clearly.
  - Check: no manuscript doc points users to bundle paths as source of truth.

- **Superseded round-two materials left ambiguous**

  - Matters because both reconciled and non-reconciled round-two folders exist.
  - Mitigation: explicitly mark non-reconciled run folder as superseded/provisional.
  - Check: manuscript authority index references only reconciled versions.

- **Stale references after reorganization**

  - Matters because many files cite historical canonical paths.
  - Mitigation: post-move grep audit and manual spot review.
  - Check: no README or index still claims `03_outputs/active/outputs_FINAL_1_2/` is manuscript authority.

- **Dirty worktree collision**

  - Matters because current modified files exist in round-two validation and report areas.
  - Mitigation: freeze backup before execution and avoid assuming a clean working tree.
  - Check: confirm intended changes against current git status before any move.

- **Over-archiving**

  - Matters because old does not equal disposable.
  - Mitigation: archive by function and relevance, not age.
  - Check: baseline and semantic-control materials must remain reachable.

### 12.2 New collaborator clarity test

After execution, a new collaborator who has never seen the repo before should be able to answer in under two minutes:

- where the manuscript-facing authority lives
- where the round-one baseline lives
- where semantic-control files live
- what is provenance only
- and what is operational only

If they cannot answer those questions quickly, the cleanup should be considered incomplete.

### 12.3 Checkpoint 10

- Risks are substantive, not superficial.
- Mitigations are proposed for each major risk.
- The future cleanup remains reversible.
- A user-clarity test is now part of the validation logic.

---

## 13. Future Cleanup Execution Sequence

1. Create the backup layers: zip snapshot, git tag, git bundle, optional freeze branch, and inventory/checksum export.
2. Verify all backups before touching structure.
3. Freeze the execution map: approve the source-to-destination migration sheet.
4. Create the target folder structure under `04_manuscript/`.
5. Copy manuscript-facing round-two authority materials into `04_manuscript/authority/`.
6. Surface or link semantic-control materials under `04_manuscript/context/`, keeping source data/codebooks authoritative in place where appropriate.
7. Add trace and baseline-comparison references under `04_manuscript/trace/` and `04_manuscript/baseline/`.
8. Reclassify documentation in `03_outputs/`, `Manuscript_Data/`, and `05_operations/` so their roles are explicit.
9. Label superseded/provisional round-two and legacy materials in docs and indexes.
10. Relocate only approved archive candidates into `99_archive/` after manuscript authority and provenance references are stable.
11. Generate or update README, MAP, authority index, provenance note, and migration note files.
12. Run path/link validation and authority-claim validation.
13. Perform final completeness review against the post-cleanup checklist.

### 13.1 Execution gates during the future cleanup

The future execution should include explicit stop-and-validate gates:

- **Gate A — backup verification complete**
  - no structural changes begin until all backup layers are verified.
- **Gate B — migration sheet approved**
  - no file movement begins until the source-to-destination sheet is frozen.
- **Gate C — manuscript authority copied and indexed**
  - no archival or relabeling of older zones begins until `04_manuscript/` is populated and readable.
- **Gate D — documentation pass complete**
  - no final validation begins until README, MAP, authority index, and provenance notes are written.
- **Gate E — path and authority validation complete**
  - no archive moves or final sign-off occur until links, authority claims, and source references pass validation.

### 13.2 Checkpoint 11

- The future execution order is safe.
- Irreversible risk is deferred until after backup verification.
- Documentation and validation occur after movement and labeling, not before.
- The movement logic distinguishes copy vs reference vs archive.

---

## 14. Post-Cleanup Validation Checklist

### 14.1 Structural validation

- Confirm no tracked or required untracked artifact was lost relative to the pre-cleanup inventory.
- Confirm `04_manuscript/README.md` clearly names the round-two reconciled package as the only manuscript-facing authority.
- Confirm `FINAL_1_2` materials are still present and clearly labeled as baseline/provenance.
- Confirm semantic-control files are reachable from the manuscript package.
- Confirm round-two dataset, notebook/script lineage, and run manifests are linked correctly.
- Confirm `03_outputs/active/` no longer claims manuscript-facing canonical status in docs.
- Confirm `05_operations/colab_bundles/` is documented as operational only.
- Confirm `Manuscript_Data/` is documented as preserved historical manuscript package, not active manuscript authority.
- Confirm all required README/MAP/index/provenance files exist in `04_manuscript/`.
- Confirm naming conventions are consistent within the new manuscript area.
- Confirm all internal links and referenced relative paths resolve.
- Confirm archive lookup and move logs exist for any archived payloads.
- Confirm no bundle mirror or provisional run folder is still implied to be manuscript-facing.

### 14.2 Authority validation

- Confirm only one zone explicitly claims manuscript-facing authority.
- Confirm baseline materials are clearly labeled baseline-only.
- Confirm copied manuscript-facing files record or link back to their provenance source.
- Confirm reference-only materials are accessible through an index and do not require guesswork.
- Confirm superseded materials are labeled as such in-place or via local README/index notes.

### 14.3 Usability validation

- Confirm a reviewer unfamiliar with the repo can answer, without guessing:
  - where the manuscript-facing round-two package lives
  - where the round-one baseline lives
  - where semantic-control files live
  - where operational bundles live
  - where historical archive material lives
- Confirm the new collaborator clarity test passes.
- Confirm a manuscript writer can find the final report, final tables, and baseline comparison path in under two minutes.

### 14.4 Rollback readiness validation

- Confirm the post-cleanup state can still be reversed using the pre-cleanup backup layers.
- Confirm the migration log is complete enough to reverse moved/copied items.
- Confirm no irreversible archival action occurred before the manuscript authority zone stabilized.

### Final Checkpoint

- This blueprint is planning-only.

- The target architecture is clear.

- The migration map exists.

- Backup and rollback are specified.

- Archive, documentation, and naming plans exist.

- Post-cleanup validation is fully defined.

- Execution gates are defined for the later cleanup wave.

- This blueprint is planning-only.

- The target architecture is clear.

- The migration map exists.

- Backup and rollback are specified.

- Archive, documentation, and naming plans exist.

- Post-cleanup validation is fully defined.

---

## 15. Open Questions / Ambiguities / Human Review Points

- Decide whether `primary_results_table.csv` and `robustness_loo_results.csv` should both be copied into `04_manuscript/` or whether one should remain trace-only and merely be indexed.
- Decide whether a manuscript-facing copy of the semantic status report is preferable to a manuscript-facing index pointing to the original file.
- Decide whether the non-reconciled folder `03_outputs/reports/run_20260418_1037_post_advisor_round2/` should stay in place as superseded provenance or later move into a more explicit superseded/provisional subzone.
- Decide whether `Manuscript_Data/` should remain in place indefinitely as a preserved historical package or later move into a provenance/legacy manuscript area after the new `04_manuscript/` package is accepted.
- Review `archive_misaligned/` and `agents/`; they appear empty and may be residue, but they should not be archived or removed without confirmation.
- Review whether root-level handoff files like `HANDOFF_CLAUDE.md` should remain at root for operator convenience or be partially cross-linked into governance/manuscript docs after cleanup.
- Review whether bundle zips under `05_operations/colab_bundles/` should get per-bundle manifest notes before any broader operations cleanup.
- Confirm whether current modified files in the dirty worktree are intended to be part of the future cleanup baseline; this matters before any execution-phase backup is taken.

### 15.1 Final reviewer questions before execution

Before the plan is executed, a reviewer should explicitly answer:

- Is the minimum manuscript-facing set sufficiently small and clear?
- Are any proposed manuscript-facing copies actually better handled as references?
- Is the first-wave scope conservative enough?
- Are any archive actions being attempted too early?
- Is there any location that would still look manuscript-authoritative after cleanup by mistake?

If any answer is uncertain, revise the plan again before execution.


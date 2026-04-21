# Second-Wave Cleanup Blueprint — Revised Execution-Safe Version

## 1. Executive Summary

The repository is **not** a candidate for a broad structural second wave.
First wave already solved the highest-risk problem by making `04_manuscript/` the single manuscript-facing authority zone and by downgrading round-one materials to baseline/provenance status.

The correct next step is a **small, documentation-first, relabeling-focused second wave**.

This second wave should:
- clarify unresolved roles,
- strengthen local documentation in a few remaining ambiguous areas,
- explicitly label the non-reconciled round-two run folder as provisional/superseded,
- clarify the figure policy,
- strengthen bundle-local role labeling,
- and harmonize stale authority wording in planning/governance docs where it could still mislead later maintenance.

This second wave should **not**:
- move major folders,
- relocate `Manuscript_Data/`,
- normalize archive payloads,
- restructure `01_data/`, `02_analysis/`, or `05_operations/`,
- or broaden `04_manuscript/` beyond its current curated authority/context/trace/baseline shape.

The intent of second wave is **clarification, not compaction**.

---

## 2. What First Wave Already Solved

First wave is already considered successful because it established:

- `04_manuscript/` as the single manuscript-facing authority zone
- a manuscript-facing authority index
- a manuscript-facing README / MAP / trace / baseline structure
- copied reconciled round-two report materials into the manuscript package
- surfaced semantic-control materials into the manuscript package
- preserved round-one baseline/provenance materials without destructive movement
- updated root and zone-level navigation docs to reflect the new authority model

Second wave must not destabilize those gains.

---

## 3. Second-Wave Mission

The mission of second wave is to make the repository **clearer**, not more complicated.

The specific goal is to ensure that a new collaborator can immediately understand:

- where manuscript-facing round-two authority lives
- what remains baseline/provenance only
- what is provisional/superseded
- what is operational/tooling only
- and what has been intentionally deferred to a later archive-focused wave

This wave is therefore a **bounded documentation and relabeling wave**.

---

## 4. Hard Boundaries

### 4.1 Do not do these things in second wave

- Do not move `Manuscript_Data/`
- Do not move `03_outputs/legacy/`
- Do not move `03_outputs/reports/run_20260418_1037_post_advisor_round2/`
- Do not archive anything
- Do not rename major repo zones
- Do not restructure `01_data/`
- Do not restructure `02_analysis/`
- Do not restructure `05_operations/`
- Do not broaden `04_manuscript/` into a dump zone
- Do not copy baseline figures into manuscript authority
- Do not invent a round-two figure set if one has not been explicitly validated
- Do not touch ambiguous residual directories except through documentation or explicit review notes

### 4.2 Scope type

Second wave is limited to:
- documentation edits
- local README / role-note additions
- wording harmonization
- local superseded/provisional labeling
- minor index/map updates if needed

No structural second-wave execution should begin unless a later approved wave explicitly authorizes it.

---

## 5. Exact Second-Wave Scope

Second wave should focus only on the following unresolved areas.

### 5.1 Figure policy area
Target zone:
- `04_manuscript/authority/figures/`

Goal:
- clarify that no validated manuscript-facing round-two figure set has been surfaced yet
- explain that baseline figures remain comparison-only
- prevent false assumptions that the folder implies an available round-two figure package

### 5.2 Non-reconciled round-two run folder
Target zone:
- `03_outputs/reports/run_20260418_1037_post_advisor_round2/`

Goal:
- make its provisional / non-reconciled / superseded status explicit in-place
- avoid any lingering implication that it is equivalent to the reconciled Colab-based round-two authority source

### 5.3 Bundle-local role clarity
Target zone:
- `05_operations/colab_bundles/oi_round2_post_advisor_colab_bundle_20260418/`

Goal:
- add a bundle-local note that clearly states:
  - it is an operational portability mirror
  - it is not manuscript authority
  - its contents may mirror provenance-supporting materials but should not be treated as the manuscript-facing source of truth

### 5.4 Stale authority wording in governance/planning docs
Target docs to review:
- `WORKSPACE_ORGANIZATION_PLAN.md`
- `WORKSPACE_MAP.md`
- `WORKSPACE_INDEX.md`

Goal:
- remove any remaining deeper wording that still implies old “canonical lane” assumptions in a way that conflicts with the round-two manuscript-facing authority model
- only revise if wording is genuinely misleading
- do not rewrite these docs broadly

### 5.5 Residual-zone documentation only
Candidate zones:
- `archive_misaligned/`
- `agents/`

Goal:
- do not move them
- do not delete them
- do not archive them
- only document them in a map/index/governance note if they remain confusing

---

## 6. Artifact-by-Artifact Action Table

|  Artifact / Zone                                                                    |  Role                                             |  Action                   |  Second-wave treatment                                                                             |
| ----------------------------------------------------------------------------------- | ------------------------------------------------- | ------------------------- | -------------------------------------------------------------------------------------------------- |
|  `04_manuscript/authority/figures/`                                                 |  Manuscript-facing placeholder                    |  `RELABEL_IN_PLACE`       |  Expand the README into a figure policy note; do not copy figure assets                            |
|  `03_outputs/reports/run_20260418_1037_post_advisor_round2/`                        |  Provisional/superseded round-two run provenance  |  `RELABEL_IN_PLACE`       |  Add local README or status note stating it is non-reconciled and not manuscript-facing authority  |
|  `03_outputs/reports/run_20260418_1037_post_advisor_round2_colab/`                  |  Reconciled provenance source                     |  `KEEP_IN_PLACE`          |  No structural changes; keep as provenance source for manuscript-facing copied assets              |
|  `Manuscript_Data/`                                                                 |  Preserved round-one baseline manuscript package  |  `KEEP_IN_PLACE`          |  No move; no archive; no structural change                                                         |
|  `03_outputs/legacy/`                                                               |  Historical lineage / archive candidate           |  `DEFER`                  |  No normalization in second wave                                                                   |
|  `99_archive/`                                                                      |  Archive infrastructure                           |  `KEEP_IN_PLACE`          |  No archive-wave execution now                                                                     |
|  `05_operations/colab_bundles/oi_round2_post_advisor_colab_bundle_20260418/`        |  Operational portability mirror                   |  `RELABEL_IN_PLACE`       |  Add bundle-local role note only                                                                   |
|  `archive_misaligned/`                                                              |  Residual / ambiguous                             |  `HUMAN_REVIEW_REQUIRED`  |  Documentation only if needed                                                                      |
|  `agents/`                                                                          |  Residual / ambiguous                             |  `HUMAN_REVIEW_REQUIRED`  |  Documentation only if needed                                                                      |
|  `04_manuscript/trace/run_manifests/run_manifest.json`                              |  Trace support                                    |  `KEEP_IN_PLACE`          |  No slimming needed in second wave                                                                 |
|  `04_manuscript/trace/robustness_and_supporting_tables/robustness_loo_results.csv`  |  Trace support                                    |  `KEEP_IN_PLACE`          |  No slimming needed in second wave                                                                 |
|  `04_manuscript/context/semantic_control/*`                                         |  Manuscript-supporting interpretation layer       |  `KEEP_IN_PLACE`          |  Already appropriate as copied support materials                                                   |
|  `04_manuscript/authority/tables/primary_results_table.csv`                         |  Manuscript-facing results table                  |  `KEEP_IN_PLACE`          |  Already appropriate as copied manuscript-facing authority                                         |

---

## 7. Exact File Targets to Prefer

If second wave is later executed, prefer a **small whitelist** of touched files.

### 7.1 Files that are reasonable second-wave targets

- `04_manuscript/authority/figures/README.md`
- `03_outputs/reports/run_20260418_1037_post_advisor_round2/README.md`
  or a local file with equivalent status-note purpose
- `05_operations/colab_bundles/oi_round2_post_advisor_colab_bundle_20260418/README.md`
  or a bundle-local role note with equivalent meaning
- `WORKSPACE_ORGANIZATION_PLAN.md`
- `WORKSPACE_MAP.md` only if needed
- `WORKSPACE_INDEX.md` only if needed
- possibly one small note in a root or governance doc if residual zones remain unclear

### 7.2 Files that should normally remain untouched in second wave

- anything under `01_data/` except if a documentation cross-link is truly necessary
- anything under `02_analysis/`
- the reconciled Colab run payload itself
- baseline output payloads
- archive payloads
- manuscript authority payload files that already read correctly

---

## 8. Figure Strategy Recommendation

### 8.1 Decision

**Do not surface round-two figures in second wave unless a validated round-two figure set is explicitly identified first.**

### 8.2 Reason

At present:
- the manuscript package explicitly says no dedicated round-two figure assets have been surfaced
- baseline figures remain comparison-only
- copying baseline figures into manuscript authority would blur baseline vs manuscript-facing authority

### 8.3 Second-wave action

The figures folder should contain a stronger policy note that says:

- no validated manuscript-facing round-two figure set is currently surfaced here
- the presence of the folder does not imply approved figure assets exist
- baseline figures remain in round-one locations for comparison only
- future figure surfacing requires either:
  - confirmed round-two figure assets, or
  - explicit human approval

---

## 9. Non-Reconciled Run Folder Strategy

### 9.1 Decision

Do **not** move the non-reconciled folder in second wave.

### 9.2 Reason

It remains useful provenance, and moving it now would create more churn than value.

### 9.3 Second-wave action

Relabel it in place with a local note stating:

- it is a provisional / non-reconciled / superseded round-two run
- it is not the manuscript-facing authority source
- the reconciled manuscript-facing authority is surfaced under `04_manuscript/`
- the reconciled provenance-source run remains the `_colab` folder

---

## 10. `Manuscript_Data/` Strategy

### 10.1 Decision

Keep `Manuscript_Data/` where it is.

### 10.2 Reason

It is already correctly documented as preserved baseline/provenance and still works as a self-contained historical package.

### 10.3 Second-wave action

No structural action.

Optional:
- strengthen one cross-reference from `04_manuscript/baseline/round1_baseline_index.md` if needed
- do not relocate the folder

---

## 11. Archive Strategy

### 11.1 Decision

Defer archive normalization entirely.

### 11.2 Reason

Second wave should not become an archive-compaction wave.
That requires its own retrieval policy and own execution plan.

### 11.3 Second-wave action

At most:
- add one planning note somewhere appropriate that `03_outputs/legacy/` remains a future archive-normalization candidate

Do not move archive payloads.

---

## 12. Bundle Strategy

### 12.1 Decision

Add bundle-local labeling only.

### 12.2 Action

At the bundle root or local bundle level, add a short note stating:

- this bundle is an operational portability mirror
- it is not manuscript-facing authority
- it may contain mirrored or provenance-supporting artifacts
- manuscript users should start from `04_manuscript/`, not the bundle

No structural change is recommended.

---

## 13. Residual-Zone Strategy

### 13.1 `archive_misaligned/`
- Role: unresolved residual zone
- Action: `HUMAN_REVIEW_REQUIRED`

### 13.2 `agents/`
- Role: unresolved residual zone
- Action: `HUMAN_REVIEW_REQUIRED`

### 13.3 Rule

Second wave should not try to “clean them up” automatically.
If anything is done, it should be limited to documenting their status in a map or planning note.

---

## 14. Risks of Over-Aggressive Second-Wave Execution

- Copying baseline figures into manuscript authority would reintroduce authority ambiguity.
- Moving the non-reconciled run folder too early would weaken provenance traceability.
- Moving `Manuscript_Data/` would create churn without clear benefit.
- Starting archive normalization now would mix multiple goals into one wave.
- Expanding `04_manuscript/` too much would turn it into a convenience dump instead of a curated authority package.
- Touching ambiguous residual zones without a decision risks deleting context or misclassifying tooling residue.

---

## 15. Proposed Second-Wave Execution Order

If a later execution is approved, the safest order is:

1. Approve second-wave scope as documentation/relabeling only.
2. Update the figure policy note under `04_manuscript/authority/figures/`.
3. Add an explicit provisional/superseded note for `03_outputs/reports/run_20260418_1037_post_advisor_round2/`.
4. Add a bundle-local role note for `05_operations/colab_bundles/oi_round2_post_advisor_colab_bundle_20260418/`.
5. Harmonize stale authority wording in planning/governance docs if still misleading.
6. Optionally add a residual-zone note in a workspace map/index if needed.
7. Re-run documentation validation only.

---

## 16. Validation Checklist for Second Wave

Second wave should pass only if all of the following are true:

- `04_manuscript/authority/figures/README.md` clearly states figure policy and absence of surfaced round-two figure assets
- `03_outputs/reports/run_20260418_1037_post_advisor_round2/` clearly identifies itself as provisional/superseded provenance
- bundle docs clearly state operational-only status at both folder and bundle level
- `Manuscript_Data/` remains undisturbed and still reads as preserved baseline package
- no files were moved from `03_outputs/legacy/` or `99_archive/`
- no new manuscript-facing authority claims appear outside `04_manuscript/`
- `04_manuscript/` still contains only curated authority/context/trace/baseline materials
- no new ambiguity was introduced into root navigation docs

---

## 17. Open Decisions Requiring Human Approval

- Should second wave add only a stronger figure policy note, or is there a validated round-two figure set that should be surfaced later?
- Should the non-reconciled run folder remain in place permanently with labeling, or move only in a later dedicated provenance/archive wave?
- Should `Manuscript_Data/` remain permanently at root as preserved provenance, or is a later legacy-zone move still desirable?
- Should `03_outputs/legacy/` remain untouched until a dedicated archive wave?
- What should `archive_misaligned/` and `agents/` ultimately represent, if anything?

---

## 18. Final Recommendation

The repo is best served by **a small second-wave execution**, but only in the narrow sense of:
- documentation tightening,
- local relabeling,
- and role clarification.

It is **not** best served by structural cleanup, archive movement, or another reorganization wave yet.

Second wave should remain:
- conservative,
- provenance-preserving,
- whitelist-based,
- and documentation-first.
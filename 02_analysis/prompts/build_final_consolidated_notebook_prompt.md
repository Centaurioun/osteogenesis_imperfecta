# OI Final Consolidated Notebook Build Prompt

## Mission
Build the real final consolidated Jupyter notebook for this repository. Do not stop at documentation, readiness, packaging, or a guide. The task is complete only when a populated, executed, and validated notebook exists on disk and its contents cover the required analysis layers.

## Historical failure to avoid
- `analysis_documentation_package/run_20260317_1347` was created at `2026-03-17 13:47:21`.
- `analysis_documentation_package/run_20260317_1411` was created at `2026-03-17 14:11:48`.
- `Manuscript_Data/03_analysis_scripts/oi_oro_dental_consolidated_v1.ipynb` was created later at `2026-03-17 14:32:25` and modified at `2026-03-17 14:55:10`.
- Therefore package creation and notebook creation are separate phases in repo history.
- The existing `oi_oro_dental_consolidated_v1.ipynb` is a failed historical artifact and must not be treated as a valid final notebook or as a template to preserve.
- An output is invalid if it is a notebook about creating a notebook, a scaffold, a placeholder, a guide, or a builder script with `nbformat` / path-writing logic instead of substantive analysis content.

## Execution mode
- Execute this task end-to-end without asking whether you should proceed from discovery to building the notebook.
- You are already authorized to inspect files, select sources, create the new final notebook, execute it, and validate it.
- Do not stop after summarizing `analysis_documentation_package/`, and do not ask for approval to continue once package-style discovery is complete.
- Ask the user only if you hit a true blocker that cannot be resolved from repository evidence.
- Do not create a hollow notebook just to satisfy the file-creation step.

## Primary output target
- Create the next available versioned notebook at:
  - `Manuscript_Data/03_analysis_scripts/oi_oro_dental_consolidated_v{N}.ipynb`
- Do not overwrite the historical `v1` notebook unless explicitly instructed.
- If `v2` does not exist, create `oi_oro_dental_consolidated_v2.ipynb`.

## Required supporting artifacts
Create these beside the notebook:
- `Manuscript_Data/03_analysis_scripts/oi_oro_dental_consolidated_v{N}_source_map.csv`
- `Manuscript_Data/03_analysis_scripts/oi_oro_dental_consolidated_v{N}_validation.md`
- `Manuscript_Data/03_analysis_scripts/oi_oro_dental_consolidated_v{N}_execution_summary.md`

The execution summary must include:
- notebook path
- selected version number
- execution start time
- execution end time
- whether execution succeeded
- total cells
- code-cell count
- markdown-cell count
- substantive code-cell count
- major sources used
- major outputs shown or generated
- residual caveats or blockers

## Core objective
Produce one comprehensive notebook that consolidates the authoritative OI dental analysis workflow, the manuscript-facing outputs, and the supporting / robustness / internal verification layers into a single reproducible artifact. The notebook may load authoritative output tables where appropriate, may call existing scripts where appropriate, and may embed essential logic where necessary, but the final notebook itself must contain substantive runnable analysis cells and visible results.

## Terminology normalization
For this prompt, use these definitions:
- `final notebook` = the new versioned notebook created in this run, not the historical `v1`, saved after successful execution.
- `comprehensive` = covers every mandatory section and every required result family in this prompt.
- `include analyses` = each required result family is backed by at least one substantive code cell, visible notebook output, and at least one row in the source map.
- `complete` = satisfies every item under `Definition of complete` and passes the validation gates.

## Role of analysis_documentation_package
- Treat `analysis_documentation_package/` as a discovery and traceability aid, not as the end goal.
- It may help identify the latest organized source set, but it cannot substitute for the actual consolidated notebook.
- A readiness file, blueprint, manifest, or summary inside `analysis_documentation_package/` never counts as completion of this task.
- If multiple `run_*` folders exist, select the package run deterministically by newest timestamped run folder name first, then by newer filesystem modification time if needed, and log that decision in the source map.

## Repository-specific non-negotiable rules
- Respect the workspace clinical/statistical rules from `AGENTS.md`.
- Never place `yas` and `dentisyon_donemi_kod` in the same multivariable model.
- If categorical expected counts are below 5, use exact / permutation methods instead of standard Pearson chi-square.
- Use Mann-Whitney U for 2-group continuous comparisons and Kruskal-Wallis for 3+ groups unless a stronger repository-grounded reason is documented.
- Apply Holm correction when reporting families of p-values.
- Report effect sizes where applicable.
- Treat CV / AUC / delta-AUC as secondary internal verification, not standalone clinical prediction claims.
- Keep `occl_tip == 4` as infraocclusion and do not fold it back into Angle I/II/III.
- Treat `dmft_dmft` as the project-specific count-like variable, not a standard split DMFT/dmft field.
- Do not invent DI subtype or severity if absent.

## Source hierarchy
Use sources in this order:

### Tier 1: Authoritative
- `Manuscript_Data/README_Manuscript_Data.md`
- `Manuscript_Data/ANALYSIS_RESULT_MAP.csv`
- `Manuscript_Data/FILE_REGISTRY.csv`
- `Manuscript_Data/06_ai_handoff_context/FINAL_HANDOFF_QUICKSTART.md`
- `Manuscript_Data/01_protocol_and_docs/final_1.md`
- `Manuscript_Data/01_protocol_and_docs/camber_sap_v2_publication_ready.md`
- `Manuscript_Data/02_source_data/metadata/codebook_v3_fixed.md`
- `Manuscript_Data/03_analysis_scripts/oi_oro_dental_master_FINAL_1_2.py`
- `Manuscript_Data/03_analysis_scripts/oi_oro_dental_master_FINAL_1_2.ipynb`
- `Manuscript_Data/04_final_outputs/OUTPUT_SCHEMA_AND_VARIABLE_LINEAGE.md`
- `Manuscript_Data/04_final_outputs/TRANSPARENCY_NOTES.md`
- `Manuscript_Data/04_final_outputs/REPRODUCIBILITY_ENVIRONMENT.md`
- `Manuscript_Data/04_final_outputs/tables_csv_and_logs/verified_master_table_FINAL.csv`
- `Manuscript_Data/04_final_outputs/tables_csv_and_logs/publication_table1_overall_FINAL.csv`
- `Manuscript_Data/04_final_outputs/tables_csv_and_logs/publication_table2_by_gene_group_FINAL.csv`
- `Manuscript_Data/04_final_outputs/tables_csv_and_logs/publication_table3_inferential_FINAL.csv`
- `Manuscript_Data/04_final_outputs/tables_csv_and_logs/robustness_panel_FINAL.csv`
- `Manuscript_Data/04_final_outputs/tables_csv_and_logs/cv_panel_FINAL.csv`
- manuscript-facing methods / results / discussion files if present

### Tier 2: Supporting
- `missing_statistical_analyses/analysis_gap_audit.md`
- `missing_statistical_analyses/supporting_alternative_grouping.csv`
- `missing_statistical_analyses/robustness_classification_table.csv`
- `missing_statistical_analyses/cv_reporting_support_table.csv`
- `missing_statistical_analyses/analysis_support_synthesis.md`
- `missing_statistical_analyses/copilot_analysis_completion_report.md`
- `main_analysis_completion/04_supporting/supporting_alternative_grouping_revised.csv`
- `main_analysis_completion/05_robustness/robustness_classification_table_revised.csv`
- `main_analysis_completion/06_model_verification/cv_reporting_support_table_revised.csv`
- `main_analysis_completion/07_reporting/analysis_support_synthesis_revised.md`
- `main_analysis_completion/07_reporting/main_analysis_completion_report.md`
- the latest selected `analysis_documentation_package/run_*/07_notebook_readiness/notebook_source_priority.csv`
- the latest selected `analysis_documentation_package/run_*/07_notebook_readiness/notebook_blueprint.md`
- the latest selected `analysis_documentation_package/run_*/06_final_summary/analysis_to_code_to_output_map.csv`

### Tier 3: Reference-only
- `reanalysis_statistician_vs_project/`

### Explicit exclusion
- `Manuscript_Data/03_analysis_scripts/oi_oro_dental_consolidated_v1.ipynb` is excluded as a valid source for final content except as a failure example to avoid.

## Candidate notebook inventory requirement
Before selecting sources, explicitly inventory the existing notebook candidates, including at minimum:
- `oi_oro_dental_master_FINAL.ipynb`
- `oi_oro_dental_master_FINAL_1.ipynb`
- `oi_oro_dental_master_FINAL_1_1.ipynb`
- `oi_oro_dental_master_FINAL_1_2.ipynb`
- `oi_oro_dental_master_v3.ipynb`
- `oi_oro_dental_master_v3_1.ipynb`
- `oi_oro_dental_master_v3_2.ipynb`
- `oi_oro_dental_master_v3_2_1.ipynb`
- `oi_oro_dental_master_v3_2_2.ipynb`
- `oi_oro_dental_master_v3_2_3.ipynb`
- `Manuscript_Data/03_analysis_scripts/oi_oro_dental_master_FINAL_1_2.ipynb`
- `Manuscript_Data/03_analysis_scripts/oi_oro_dental_consolidated_v1.ipynb`

For each candidate, decide one of:
- `selected_as_primary_source`
- `used_for_reference_only`
- `excluded`

## Deterministic file-selection rules
When multiple similarly named candidates exist, select sources using this precedence order:
1. `FINAL_1_2`
2. `FINAL_1_1`
3. `FINAL_1`
4. `FINAL`
5. `v3_2_3`
6. `v3_2_2`
7. `v3_2_1`
8. `v3_2`
9. `v3_1`
10. `v3`

Then apply deterministic tie-break rules in this exact order:
1. Prefer files under `Manuscript_Data/` over root-level historical copies.
2. Prefer notebooks/scripts directly inside `Manuscript_Data/03_analysis_scripts/` over other folders.
3. Prefer newer `LastWriteTime`.
4. Prefer lexicographically smaller full path if still tied.

Record every selected source and every rejected alternative in `oi_oro_dental_consolidated_v{N}_source_map.csv` with these columns:
- `analysis_block`
- `selected_source`
- `source_tier`
- `selection_reason`
- `rejected_alternatives`
- `merge_mode`
- `destination_section`
- `destination_cells`
- `expected_outputs`

Allowed `merge_mode` values are:
- `load_authoritative_output`
- `import_or_reuse_script_logic`
- `reference_structure_only`
- `supporting_context_only`

## Required process
Follow this sequence without skipping steps:

1. Discover and read the authoritative and supporting files.
2. Inventory all candidate notebooks, scripts, output tables, and reporting artifacts relevant to the consolidated notebook.
3. Create the source map before building the notebook.
4. Define the notebook section plan and cell plan before writing cells.
5. Build the notebook content.
6. Execute the notebook end-to-end.
7. Validate the executed notebook against the required quality gates.
8. Produce the validation and execution summary artifacts.
9. Only then report completion.

## Required pre-build cell plan
Before writing notebook cells, create an internal cell plan and mirror it in the execution summary. The plan must include one row per intended notebook cell with:
- `cell_no`
- `cell_type`
- `section_name`
- `purpose`
- `source_files`
- `expected_outputs`
- `depends_on`

The plan must be specific enough that another reviewer could compare the saved notebook against the plan and detect omissions.

## Mandatory notebook sections
The final notebook must include, at minimum, these sections in this order:
1. Title, scope, and provenance
2. Environment and reproducibility notes
3. Source selection summary
4. Data / output loading and path validation
5. Authoritative overall descriptive results
6. Authoritative gene-group results
7. Authoritative inferential results
8. Robustness and supporting analyses
9. CV / model verification with explicit cautionary framing
10. Figures / tables display or regeneration path
11. Integrated narrative synthesis and limitations
12. Validation summary and completion checklist

At least one substantive code cell must appear under each of sections 4 through 10.

## Evidence labeling rules inside the notebook
- Every major result block must be labeled as one of:
  - `Authoritative`
  - `Supporting`
  - `Reference-only`
  - `Assumption`
- Do not present supporting or reference-only content as if it were authoritative primary evidence.
- If an interpretation depends on inference rather than direct file evidence, label it explicitly as `Assumption`.

## Required section-to-output coverage
At minimum, the notebook must display or generate these concrete artifacts in visible notebook cells:
- `publication_table1_overall_FINAL.csv`
- `publication_table2_by_gene_group_FINAL.csv`
- `publication_table3_inferential_FINAL.csv`
- `robustness_panel_FINAL.csv`
- `cv_panel_FINAL.csv`
- at least one figure display or an explicit regeneration/display path for the final figures

## Mandatory notebook substance requirements
- The notebook must contain real analysis content, not only boilerplate.
- Minimum notebook structure:
  - at least 18 total cells
  - at least 8 substantive code cells
  - at least 8 markdown cells
- A code cell counts as substantive only if it performs real work such as loading authoritative outputs, running analysis logic, validating parity, generating tables/figures, or synthesizing results.
- Cells that only define file names, create notebook objects, write notebook files, contain TODOs, or store code inside string literals do not count as substantive.
- The notebook must visibly cover all five required result families:
  - overall descriptive table
  - gene-group table
  - inferential table
  - robustness results
  - CV / internal verification results
- The notebook must clearly label authoritative vs supporting vs reference-only material.

## Allowed implementation patterns
- You may load already-generated authoritative CSV outputs when they are the correct single source of truth.
- You may import or adapt existing script logic from authoritative scripts when needed for reproducibility or missing displays.
- You may use existing notebooks as structural references, but do not blindly concatenate notebooks.
- You may simplify duplicated historical code paths if the authoritative source is clear.

## Forbidden implementation patterns
- Do not create a notebook whose purpose is to generate another notebook.
- Do not leave placeholder cells, commented stubs, or "to be filled" sections.
- Do not treat the readiness package as the final deliverable.
- Do not claim success after only creating a file.
- Do not omit source selection logging.
- Do not silently downgrade missing analyses into narrative-only mentions.

## Mandatory execution requirements
- Run the actual final notebook file after building it.
- Preserve execution counts and outputs in the saved notebook.
- If execution fails, fix the notebook and re-run it until it either passes or a true blocker remains.
- Validate that all required sections have outputs where outputs are expected.
- Validate that all paths referenced in the notebook resolve correctly in this repository.

## Mandatory validation checks
Write the results of every check into `oi_oro_dental_consolidated_v{N}_validation.md`.

### Structure checks
- Confirm total cell count, code-cell count, markdown-cell count.
- Confirm minimum substantive code-cell threshold is met.
- Confirm required sections exist in the correct order.

### Substance checks
- Confirm no scaffold-only cells are being counted.
- Confirm no notebook-generation logic remains as part of the final narrative flow.
- Confirm every required result family is represented by real code/output, not prose only.
- Confirm the final notebook does not contain failure signatures such as:
  - `nbf.v4.new_notebook()`
  - `target_notebook_path`
  - `with target_notebook_path.open`
  - `example_code =`
  - code stored mainly as string literals for a future notebook

### Execution checks
- Confirm the final notebook has non-null execution counts for the required code cells.
- Confirm outputs exist for path validation, main result displays, and validation summary cells.
- Confirm the notebook saved to disk is the executed notebook, not a pre-run draft.

### Traceability checks
- Confirm every required analysis block maps to at least one selected source.
- Confirm every selected source appears in the source map.
- Confirm every rejected plausible source is documented with a reason.

### Parity checks
- Confirm key authoritative metrics match the authoritative CSV outputs.
- At minimum validate `N`, key inferential p-values, and the main table row counts against the authoritative files.
- If a mismatch appears, diagnose it and resolve it before claiming completion.

## Stop conditions
Do not claim completion if any of these are true:
- the final notebook is unexecuted
- any required section is missing
- any required result family is absent
- the notebook is still scaffold / placeholder heavy
- scaffold failure signatures are still present in the saved notebook
- source selection is undocumented
- parity checks fail without resolution
- the saved notebook differs materially from the notebook that was executed

If a hard blocker remains, stop with a precise blocker report in `oi_oro_dental_consolidated_v{N}_validation.md` and do not pretend the notebook is complete.

## Definition of complete
This task is complete only if all of the following are true:
- the final notebook exists at the new versioned target path
- the notebook is the actual analysis notebook, not a builder or scaffold
- the notebook was executed successfully and saved with outputs
- the notebook covers all mandatory sections and all required result families
- source selection is documented and reproducible
- validation artifacts exist and show pass status or clearly bounded residual caveats

## Final response requirements
When you finish, report:
- exact notebook path created
- exact supporting artifact paths created
- selected `analysis_documentation_package` run, if one was used
- selected authoritative sources
- whether execution succeeded
- whether validation succeeded
- any residual caveats

## Self-check before finishing
Before you stop, verify all of the following:
- A new versioned consolidated notebook exists and is not the historical `v1`.
- The notebook is populated with substantive analysis content.
- The notebook was executed and saved with outputs.
- The notebook covers the authoritative and supporting layers required by this prompt.
- The source map and validation artifacts exist.
- No part of the workflow was silently replaced by a guide, scaffold, or readiness-only artifact.

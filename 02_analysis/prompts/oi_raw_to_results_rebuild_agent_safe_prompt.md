# OI Raw-to-Results Rebuild Prompt - Agent-Safe Final

## 0) Mission
Build a new canonical OI oro-dental analysis workspace in the project root and create one single main notebook that recomputes the full analysis from canonical raw/meta inputs.

This task is not:
- a traceability-only consolidation task
- a historical-results comparison task inside the main notebook
- a cleanup/archive/delete task
- a repo-wide refactor task

Primary target:
- `oi_oro_dental_analysis/oi_oro_dental_consolidated_v3.ipynb`

Required principle:
- The notebook must compute from canonical raw/meta inputs.
- The notebook must not use historical `FINAL` result CSVs as its analytical backbone.
- Historical validation, if ever needed, must be done in a separate downstream file and separate workflow, not inside the main notebook.

## 1) Hard Scope Boundary
This run must:
- create a new canonical analysis folder in the root directory
- create canonical copies of the required input files inside that folder
- build the main notebook inside that folder
- execute the notebook end-to-end
- generate tables, figures, documents, logs, and a run manifest
- produce explicit PASS/FAIL QC outputs

This run must not:
- embed old-vs-new result comparison inside the main notebook
- rename, move, delete, or archive the original root-level source files
- overwrite historical `FINAL` outputs elsewhere in the repository
- use historical notebooks as the execution engine
- ask the user for approval between iterative review cycles

If a requested action conflicts with these boundaries, prefer the safer interpretation and continue only within this scope.

## 2) Canonical Workspace to Create
Create this workspace in the project root:

```text
osteogenesis_imperfecta/
├── README.md
├── AGENTS.md
├── oi_oro_dental_analysis/
│   ├── README.md
│   ├── oi_oro_dental_consolidated_v3.ipynb
│   ├── input_data/
│   │   ├── meta_data/
│   │   │   ├── codebook.md
│   │   │   ├── gene_map.csv
│   │   │   ├── oi_descriptive_mapping.csv
│   │   │   └── oi_project_description_and_ethics_approval.md
│   │   └── raw_data/
│   │       └── oi_dataset.csv
│   └── output_data/
│       ├── figures/
│       ├── tables/
│       ├── documents/
│       └── logs/
├── agents/
├── archive/        # if already present; do not modify
├── skill/          # if already present; do not create if absent
├── .venv/
└── .github/
```

Rules:
- `oi_oro_dental_analysis/` is the canonical workspace for the rebuild.
- `input_data/` is immutable input territory.
- `output_data/` is generated-artifact territory.
- No logs under `input_data/`.
- No duplicate authoritative `codebook.md` under `output_data/`.
- Do not overwrite the existing `oi_oro_dental_consolidated_v2.ipynb`.

## 3) Canonical Input Mapping
Create canonical copies with these mappings:

- `codebook_v3_fixed.md` -> `oi_oro_dental_analysis/input_data/meta_data/codebook.md`
- `gene_map_v1.csv` -> `oi_oro_dental_analysis/input_data/meta_data/gene_map.csv`
- `osteogenesis_imperfecta_camber_input_minimal_v1.csv` -> `oi_oro_dental_analysis/input_data/meta_data/oi_descriptive_mapping.csv`
- `osteogenesis_imperfecta_original_data.csv` -> `oi_oro_dental_analysis/input_data/raw_data/oi_dataset.csv`
- `Osteogenesis-Imperfecta-Oro-Denta-Bulgular-Etik-Kurul-Basvuru-Rev3.md` -> `oi_oro_dental_analysis/input_data/meta_data/oi_project_description_and_ethics_approval.md`

Hard rules:
- Do not rename the original files.
- Do not move the original files.
- Do not delete the original files.
- Create canonical copies only.
- Verify the integrity of each copy immediately after copy.
- Record all mappings in a manifest.

## 4) Input Integrity and Provenance Manifest
Before analysis starts:

1. Confirm all required source files exist in the root.
2. Create canonical copies in the analysis workspace.
3. Verify integrity using file size plus a checksum or similarly strong verification.
4. Write `oi_oro_dental_analysis/output_data/documents/input_manifest_v3.json`.
5. Stop immediately if any required input is missing, unreadable, malformed, or mismatched after copy.

`input_manifest_v3.json` must include at least:
- `original_path`
- `canonical_path`
- `file_size`
- `checksum`
- `copied_at`
- `status`

## 5) Primary Inputs vs Reference-Only Sources
### 5.1 Primary analytical inputs
The notebook must use only these canonical files as primary analysis inputs:

- `oi_oro_dental_analysis/input_data/raw_data/oi_dataset.csv`
- `oi_oro_dental_analysis/input_data/meta_data/codebook.md`
- `oi_oro_dental_analysis/input_data/meta_data/gene_map.csv`
- `oi_oro_dental_analysis/input_data/meta_data/oi_descriptive_mapping.csv`
- `oi_oro_dental_analysis/input_data/meta_data/oi_project_description_and_ethics_approval.md`

### 5.2 Reference-only sources
Historical notebooks and historical result files may be consulted only for context or structural inspiration outside the main computational pipeline.

Examples:
- `oi_oro_dental_consolidated_v2.ipynb`
- `oi_oro_dental_master_FINAL_1_2.ipynb`
- historical `oi_oro_dental_master_*.ipynb`
- `publication_table1_overall_FINAL.csv`
- `publication_table2_by_gene_group_FINAL.csv`
- `publication_table3_inferential_FINAL.csv`
- `robustness_panel_FINAL.csv`
- `cv_panel_FINAL.csv`
- `verified_master_table_FINAL.csv`

Hard rule:
- The notebook must not load historical result tables as the thing being analyzed.
- The notebook must compute from the canonical raw/meta inputs.

## 6) Main Output Artifacts
Create at minimum:

- `oi_oro_dental_analysis/README.md`
- `oi_oro_dental_analysis/oi_oro_dental_consolidated_v3.ipynb`
- `oi_oro_dental_analysis/output_data/logs/issue_log_v3.csv`
- `oi_oro_dental_analysis/output_data/logs/run_manifest_v3.json`
- `oi_oro_dental_analysis/output_data/logs/export_registry_v3.csv`
- `oi_oro_dental_analysis/output_data/logs/qc_gate_report_v3.md`
- `oi_oro_dental_analysis/output_data/documents/input_manifest_v3.json`
- `oi_oro_dental_analysis/output_data/documents/analysis_decisions_v3.md`
- publication-ready tables in `oi_oro_dental_analysis/output_data/tables/`
- figures in `oi_oro_dental_analysis/output_data/figures/`

## 7) Required Notebook Behavior
The notebook is the single visible main analysis file.

Core analytical logic must be present in notebook cells.
Small helper functions are allowed, but the notebook must remain readable and self-contained.

The notebook must:
- run from its own directory
- discover paths safely
- initialize deterministic settings
- load only canonical inputs for analysis
- log QC issues and analytical decisions
- generate outputs and save them
- finish with an explicit PASS/FAIL QC summary

The notebook must not:
- include a section that compares new results to old results
- present itself as a validation wrapper
- contain placeholder, no-op, fake PASS, or scaffold-only sections

## 8) Required Notebook Section Order
Build the notebook in this order:

1. Cover and study objective
2. Scope, exclusions, and done-definition
3. Environment setup and determinism
4. Safe path discovery and canonical file inventory
5. Raw data loading
6. Codebook/schema/type validation
7. Data QC and fail-fast checks
8. Issue log initialization
9. Feature engineering
10. Derived variables and exclusion logic
11. Overall descriptive analysis
12. Gene-group descriptive analysis
13. Global inferential analysis
14. Post-hoc or pairwise analysis where justified
15. Multiple-comparison correction
16. Effect size reporting
17. Robustness or sensitivity analysis
18. Penalized modeling if justified
19. CV/internal verification only if clearly secondary
20. Figure generation
21. Publication-ready export
22. Limitations, exclusions, and rationale log
23. Final QC gate summary
24. Completion status

Historical comparison must not be added as a notebook section.

## 9) Markdown Standard for Every Analysis Block
Before each analysis block, include markdown that answers:

- Why is this analysis being done?
- Which variables are used?
- Which test or model is used?
- Why is this method appropriate here?
- What are the assumptions and limits?
- Which outputs will be generated?

## 10) Determinism and Runtime Safety
Use:
- `SEED = 20260228`

Rules:
- All randomness must be seeded.
- All iteration counts must be recorded in `run_manifest_v3.json`.
- The notebook must not assume `Path.cwd()` is the repo root.
- The notebook must auto-discover the project root or canonical workspace safely.
- All key package versions and timestamps must be written to `run_manifest_v3.json`.

## 11) Clinical Red Lines
- `occl_tip`:
  - only `1, 2, 3` are valid Angle classes
  - `4` means infraocclusion
  - if `occl_tip == 4`, record infraocclusion and keep Angle classification as `NaN`
- `dmft_dmft`:
  - do not present it as a formal DMFT index without qualification
  - if a binary caries variable is needed, derive it only as `caries_any = (dmft_dmft > 0)`

Every recode, derivation, exclusion, ambiguity, and override must be logged.

## 12) Statistical Red Lines
For categorical analyses:
- if expected cell count is `< 5`, do not use plain Pearson chi-square
- use exact or permutation-based logic instead
- default permutation floor: `>= 10000` iterations with fixed seed

For continuous analyses:
- default to non-parametric methods
- two groups: `Mann-Whitney U`
- three or more groups: `Kruskal-Wallis`

For multiplicity and effect sizes:
- use `Holm` correction by default
- report `Cramer's V` for categorical analyses
- report `epsilon-squared` for Kruskal-Wallis
- report an appropriate rank-based effect size for Mann-Whitney where applicable
- do not report naked p-values without effect sizes

For models:
- only add multivariable models if there is a clear analytical justification
- prefer penalized logic such as Ridge/L2 or Firth-style approaches
- never place `yas` and `dentisyon_donemi_kod` in the same multivariable model
- any model section must be labeled as supportive, not automatically primary evidence

## 13) Data QC and Fail-Fast Rules
Stop immediately on:
- missing canonical input
- unreadable canonical input
- schema mismatch that makes analysis invalid
- catastrophic type failure
- path-resolution failure

Do not silently:
- drop rows
- drop columns
- coerce types
- impute values
- merge categories
- ignore unexpected missingness

If a non-catastrophic issue can be handled safely, it must still be logged to `issue_log_v3.csv`.

## 14) Issue Logging Requirements
`issue_log_v3.csv` must include at least:

- `issue_id`
- `severity`
- `stage`
- `record_identifier`
- `variable`
- `issue_type`
- `description`
- `decision`
- `rationale`
- `action_taken`

Must log:
- excluded records
- recoding decisions
- merged categories
- schema mismatches
- invalid values
- unmatched genes
- unexpected missingness
- suspicious values
- model eligibility restrictions
- QC gate failures
- export failures

## 15) Export Rules
All generated artifacts must remain inside:
- `oi_oro_dental_analysis/output_data/tables/`
- `oi_oro_dental_analysis/output_data/figures/`
- `oi_oro_dental_analysis/output_data/documents/`
- `oi_oro_dental_analysis/output_data/logs/`

Do not overwrite historical outputs elsewhere in the repo.

`export_registry_v3.csv` must include at least:
- `artifact_path`
- `artifact_type`
- `section`
- `source_data`
- `generated_at`
- `status`

## 16) Required README Files
Create:
- `oi_oro_dental_analysis/README.md`

This README must explain:
- what the canonical workspace is
- which files are the canonical inputs
- which outputs are produced
- what the notebook does
- what this run does not do
- where logs and QC artifacts are written

## 17) Final QC Gates
Produce explicit `PASS/FAIL + evidence + rationale` for each gate:

1. Canonical workspace created correctly
2. Canonical input copies complete and verified
3. Safe path discovery works from the notebook directory
4. Raw data loads successfully
5. Schema/type validation passes
6. Clinical rules are enforced
7. Feature engineering is logged and reproducible
8. Small-sample test selection is appropriate
9. Multiple-comparison correction is present
10. Effect size reporting is present
11. Outputs are exported and registered
12. Issue log is populated appropriately
13. Notebook executes end-to-end without errors
14. No placeholder or fake PASS behavior remains

If any critical gate fails, the task is not complete.

## 18) Six-Cycle Autonomous Improvement System
Apply 6 full autonomous cycles without asking the user for intermediate approval.

Each cycle must:
1. Read the entire prompt, notebook, and support artifacts end-to-end
2. Identify ambiguity, path fragility, weak QC, missing sections, missing logs, wrong tests, poor explanations, placeholder behavior, or output gaps
3. Apply all needed fixes autonomously
4. Re-run affected sections or the full notebook as needed
5. Update logs, manifest, QC report, export registry, and README if needed
6. Continue to the next cycle

Cycle 1:
- scope integrity, canonical workspace correctness, source-boundary enforcement

Cycle 2:
- canonical copy logic, path safety, manifest, schema/type validation

Cycle 3:
- QC, issue logging, feature engineering, exclusion transparency

Cycle 4:
- descriptive and inferential correctness, test appropriateness, Holm, effect sizes

Cycle 5:
- robustness, supportive modeling if justified, CV caution framing, export completeness

Cycle 6:
- full rerun, final QC gates, placeholder removal, final near-perfect pass

## 19) Prohibitions
Do not:
- turn this into a historical-comparison notebook
- embed old-vs-new validation inside the notebook
- use old `FINAL` CSVs as the analytical backbone
- use historical notebooks as the execution engine
- rename, move, delete, or archive the original root-level source files
- silently swallow errors
- silently drop rows or columns
- silently coerce types
- skip effect sizes
- skip Holm correction
- declare completion before all critical QC gates pass

## 20) Final Report Format
Return the final report in this order:

1. `Summary`
2. `Canonical inputs created`
3. `Actions taken`
4. `Notebook sections completed`
5. `QC gates (PASS/FAIL)`
6. `Artifacts generated`
7. `Risks / unresolved items`
8. `Next steps`

## 21) Final Reminder
The main notebook exists for one job:
- produce new analysis results from canonical raw/meta inputs.

It does not exist to:
- inventory old notebooks,
- display historical final outputs as the main analysis,
- compare old and new outputs inside itself,
- or act as a traceability-only wrapper.

If the notebook's analytical backbone is not computed from:
- `oi_dataset.csv`
- `codebook.md`
- `gene_map.csv`
- `oi_descriptive_mapping.csv`

then the task has failed.

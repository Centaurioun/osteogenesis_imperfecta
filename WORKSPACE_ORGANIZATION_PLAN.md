# Workspace Organization Plan (No-Delete, Minimal-Disruption)

This plan reorganizes the workspace **without deleting files**, preserves historical outputs, and makes active work easy to find, run, and update.

## 0) Operating boundaries and success criteria

### 0.1 Boundaries
- No destructive operations (no delete, no overwrite-in-place of historical artifacts).
- Reorganization should preserve reproducibility and provenance.
- Tooling must remain simple: Git + local folders + common cloud drives.

### 0.2 Protected paths (never move in reorg waves)
- `.git/`, `.venv/`, `.vscode/`, `.codex/`, `.tmp.driveupload/`
- Tooling/config roots: `.github/`, `.agents/`
- Manuscript-facing and baseline lanes remain protected until cutover sign-off is complete.

### 0.3 Status definitions (used across this plan)
- `active`: currently maintained and used for ongoing deliverables.
- `hold`: not currently edited, but retained for near-term reference.
- `legacy`: superseded by a newer tracked version; still may be useful for traceability.
- `archive_candidate`: approved for move to archive layout after inventory + logging.

### 0.4 Reorg success criteria
1. A single documented manuscript-facing authority lane is visible.
2. Root-level clutter is reduced by moving non-active material into organized domains.
3. Every moved item is discoverable via index/log files.
4. No analysis path breaks for preserved notebook/script runs.

## 1) Active work first: current active locations and recommended focus

1. **Primary manuscript-facing package:**
   - `04_manuscript/`
   - Contains the reconciled round-two authority set, semantic-control copies, trace links, and baseline pointers.
2. **Primary preserved baseline package:**
   - `Manuscript_Data/`
   - Contains the round-one FINAL_1_2 baseline structure and registry files (`FILE_REGISTRY.csv`, `ANALYSIS_RESULT_MAP.csv`).
3. **Primary preserved outputs (final track baseline):**
   - `outputs_FINAL_1_2/` (FINAL publication-grade outputs and manifests).
4. **Primary supporting scripts/notebooks (latest practical lineage):**
   - `oi_oro_dental_master_FINAL_1_2.ipynb`, `oi_oro_dental_master_FINAL_1_2.py`
   - Build/figure scripts: `build_FINAL.py`, `make_figures_final_1_2.py`, `make_figures_FINAL_1_2_TR.py`
5. **Secondary supporting QA/comparison work:**
   - `main_analysis_completion/`
   - `reanalysis_statistician_vs_project/`
6. **Recent prompt/governance updates:**
   - `fixing-promot.md`, `.agents/`, `.github/`, `AGENTS.md`

**Recommendation:** treat `04_manuscript/` as the manuscript-facing authority package and `Manuscript_Data/` + `outputs_FINAL_1_2/` + `FINAL_1_2` notebook/script pair as preserved baseline/comparison authority; everything else should be indexed as legacy, support, or archive-candidate.

### 1.1 Execution phases (minimal-disruption)
1. **Phase A — index-first:** create indexes and labels before moving anything.
2. **Phase B — low-risk moves:** move prompts/notes/legacy docs into organized domains.
3. **Phase C — analysis/output consolidation:** organize notebook/script/output lineages.
4. **Phase D — archive wave:** move approved archive candidates and log everything.

### 1.2 Current-to-target mapping examples
- Root `oi_oro_dental_master_FINAL_1_2.ipynb` -> `02_analysis/notebooks/active/`
- Root `oi_oro_dental_master_v3_2_3.ipynb` -> `02_analysis/notebooks/legacy/` (or `99_archive/by_release/v3_series/`)
- Root `build_FINAL.py` -> `02_analysis/scripts/active/`
- Root `build_v3_2_3.py` -> `02_analysis/scripts/legacy/`
- Root `outputs_FINAL_1_2/` -> `03_outputs/active/outputs_FINAL_1_2/`
- Root `outputs_v3_2_3/` -> `03_outputs/legacy/outputs_v3_2_3/` (or `99_archive/by_release/v3_series/`)

---

## 2) Recommended folder/subfolder structure (tailored tree)

```text
osteogenesis_imperfecta/
├─ 00_governance/
│  ├─ AGENTS.md
│  ├─ .github/
│  ├─ .agents/
│  └─ docs/
│     ├─ project_scope/
│     └─ meeting_notes/
├─ 01_data/
│  ├─ raw/
│  │  ├─ osteogenesis_imperfecta_original_data.csv
│  │  └─ osteogenesis_imperfecta_camber_input_minimal_v1.csv
│  ├─ reference/
│  │  ├─ codebook_v3_fixed.md
│  │  └─ gene_map_v1.csv
│  └─ derived/
├─ 02_analysis/
│  ├─ notebooks/
│  │  ├─ active/
│  │  └─ legacy/
│  ├─ scripts/
│  │  ├─ active/
│  │  └─ legacy/
│  ├─ prompts/
│  └─ validation/
├─ 03_outputs/
│  ├─ active/
│  │  ├─ outputs_FINAL_1_2/
│  │  └─ figures_FINAL_1_2/
│  ├─ reports/
│  └─ legacy/
├─ 04_manuscript/
├─ 05_operations/
│  ├─ logs/
│  ├─ manifests/
│  └─ automation/
└─ 99_archive/
   ├─ by_release/
   ├─ by_date/
   ├─ snapshots/
   └─ indexes/
```

Notes:
- Keep `Manuscript_Data/` physically intact at first (low disruption), but surface it under `04_manuscript/` in docs/index.
- Keep `.venv/` and `.vscode/` where they are; exclude from archival moves.

---

## 3) Naming convention + versioning rules (files/folders)

### 3.1 File naming pattern
Use:
- `{project}_{artifact}_{scope}_{status}_{version}.{ext}`
- lowercase, snake_case; no spaces; ASCII preferred.

Controlled vocabulary:
- `project`: `oi`
- `status`: `wip`, `candidate`, `reviewed`, `final`, `legacy`, `archived`
- `scope` examples: `overall`, `gene_group`, `inferential`, `robustness`, `sensitivity`, `manifest`

Examples:
- `oi_table1_overall_final_v1_2.csv`
- `oi_table3_inferential_final_v1_2.xlsx`
- `oi_master_analysis_final_v1_2.ipynb`
- `oi_figures_publication_final_v1_2.py`
- `oi_discrepancy_report_round2_v1.md`
- `oi_run_manifest_final_v1_2.json`

### 3.2 Folder naming pattern
Use:
- `NN_domain_purpose` (numeric prefix for stable ordering)

Examples:
- `01_data_raw`
- `02_analysis_notebooks_active`
- `03_outputs_active`

### 3.3 Versioning rules
1. **Working drafts:** suffix `_wip_YYYYMMDD` (e.g., `oi_master_analysis_wip_20260417.ipynb`)
2. **Milestones:** `_vX_Y` (e.g., `_v1_2`)
3. **Publication-locked:** add `_final_vX_Y`
4. **Never overwrite prior milestone files**; create next version.
5. `run_manifest.json` must include:
   - input dataset IDs
   - git commit hash (if in git)
   - script/notebook name
   - generated outputs list

Version precedence (for identifying latest preferred file):
1. higher semantic version (`vX_Y`)
2. if tied, prefer `final` over `reviewed` over `candidate` over `wip`
3. if tied, latest `LastWriteTime`

Notebook/script pairing rule:
- For preserved runs, maintain matching base names for notebook and script when both exist.
- Example: `oi_master_analysis_final_v1_2.ipynb` and `oi_master_analysis_final_v1_2.py`.

Sample 8 names (ready-to-use):
1. `oi_master_analysis_final_v1_2.ipynb`
2. `oi_master_analysis_legacy_v3_2_3.ipynb`
3. `oi_build_pipeline_final_v1_2.py`
4. `oi_table1_overall_final_v1_2.csv`
5. `oi_table2_gene_group_final_v1_2.csv`
6. `oi_table3_inferential_final_v1_2.csv`
7. `oi_robustness_panel_final_v1_2.csv`
8. `oi_workspace_reorg_plan_v1.md`

---

## 4) Archiving policy/procedure + archive layout

### 4.1 Policy
- **No deletion.** Archive only by moving/copying and indexing.
- Archive candidates:
  - superseded notebook/script chains (e.g., multiple `v3_*` and intermediate `FINAL_1_1` if not active)
  - old output families (`outputs_v3*`, previous figure sets)
  - one-off patch scripts after supersession.
- Keep one canonical active lineage visible in `02_analysis/*/active` and `03_outputs/active`.

### 4.2 Archive layout
```text
99_archive/
├─ by_release/
│  ├─ v3_series/
│  ├─ final_1_0_to_1_1/
│  └─ pre_final/
├─ by_date/
│  └─ 2026-04-17_reorg_wave1/
├─ snapshots/
│  ├─ root_inventory_YYYYMMDD.csv
│  └─ move_log_YYYYMMDD.csv
└─ indexes/
   ├─ archive_index.md
   └─ archive_lookup.csv
```

### 4.3 Procedure
1. Create pre-move inventory snapshot.
2. Tag each item: `active`, `hold`, `archive_candidate`.
3. Run a **dry-run move plan** and review the move list before execution.
4. Execute moves in small batches (recommended: 20-50 items per batch).
5. Move only `archive_candidate` items to `99_archive/by_release/...`.
6. Resolve name conflicts by preserving source name and appending archive date suffix (e.g., `_archived_20260417`).
7. Write move records (`from`, `to`, `date`, `owner`, `reason`).
8. Validate post-move integrity (file count parity at batch level).
9. Optional compression:
   - zip sub-archives older than 90 days that are not frequently accessed.
   - keep index files uncompressed for discoverability.

### 4.4 Rollback procedure
1. If any smoke test fails, pause further moves.
2. Use the move log to reverse moves in reverse chronological order.
3. Re-run smoke checks on preserved notebook/script/output paths.
4. Mark rollback event in `99_archive/snapshots/move_log_YYYYMMDD.csv` with reason.

### 4.5 Archive quality checks
- Each archive wave must produce:
   - `dry_run_candidates_YYYYMMDD.csv`
   - `move_log_YYYYMMDD.csv`
   - updated `archive_lookup.csv`
- Batch acceptance criteria:
   - source batch item count == destination batch item count
   - no files from protected paths included
   - preserved active notebook/script/output paths still valid

---

## 5) Labeling/mapping scheme (discoverability)

Use lightweight metadata via index files (Git/cloud/local friendly):

1. **Root index:** `WORKSPACE_INDEX.md`
   - preserved active notebook
   - preserved active outputs
   - latest validated run date
2. **Folder-level README template:**
   - purpose
   - owner
   - update frequency
   - key files
   - upstream/downstream dependencies
3. **Machine-readable inventory:** `workspace_map.csv`
   - columns:
     - `path`
     - `category` (data/script/notebook/output/doc/archive)
     - `status` (active/legacy/archive)
     - `owner`
     - `version`
     - `last_reviewed`
     - `source_of_truth` (yes/no)
4. **Archive lookup:** `99_archive/indexes/archive_lookup.csv`
   - `original_path`, `archive_path`, `moved_on`, `reason`, `release_tag`

---

## 6) Step-by-step migration checklist (safe, no deletions)

1. **Freeze naming + approved sources**
   - Declare approved active notebook/script/output set in `WORKSPACE_INDEX.md`.
2. **Snapshot current state**
   - Generate root inventory CSV and top-level checksum list (optional).
3. **Create new target folders**
   - Create `00_governance` ... `99_archive` structure.
4. **Classify items**
   - Label all top-level items as active/hold/archive_candidate.
5. **Move low-risk docs first**
   - Prompts, notes, and references into `00_governance/docs` / `02_analysis/prompts`.
6. **Move legacy analysis artifacts**
   - `v3*` notebooks/scripts to `02_analysis/*/legacy` or `99_archive/by_release/v3_series`.
7. **Consolidate outputs**
   - Keep `outputs_FINAL_1_2` in `03_outputs/active`; move older output families to `03_outputs/legacy` or archive.
8. **Register all moves**
   - Update `workspace_map.csv` + `archive_lookup.csv`.
9. **Run smoke check**
   - Open canonical notebook; verify data/script paths resolve.
10. **Tag reorg milestone**
   - Add `reorg_wave1_YYYYMMDD` note in root index and git commit/tag if using git.

### Useful PowerShell snippets

Create target folders:
```powershell
$root = "Users/centaurioun/Repos/osteogenesis_imperfecta"
@("00_governance","01_data","02_analysis","03_outputs","04_manuscript","05_operations","99_archive") |
  ForEach-Object { New-Item -ItemType Directory -Force -Path (Join-Path $root $_) | Out-Null }
```

Inventory snapshot:
```powershell
$root = "Users/centaurioun/Repos/osteogenesis_imperfecta"
Get-ChildItem -Path $root -Recurse -Force |
  Select-Object FullName, Length, LastWriteTime, Extension |
  Export-Csv -NoTypeInformation -Encoding UTF8 (Join-Path $root "99_archive\snapshots\root_inventory_$(Get-Date -Format yyyyMMdd).csv")
```

Move with log:
```powershell
$from = "Users/centaurioun/Repos/osteogenesis_imperfecta\outputs_v3_2_3"
$to   = "Users/centaurioun/Repos/osteogenesis_imperfecta\99_archive\by_release\v3_series\outputs_v3_2_3"
New-Item -ItemType Directory -Force -Path (Split-Path $to -Parent) | Out-Null
Move-Item -Path $from -Destination $to -Force
"$((Get-Date).ToString('s')),`"$from`",`"$to`",archive_candidate,v3_series" |
  Add-Content "Users/centaurioun/Repos/osteogenesis_imperfecta\99_archive\snapshots\move_log_$(Get-Date -Format yyyyMMdd).csv"
```

Dry-run candidate list (no move):
```powershell
$root = "Users/centaurioun/Repos/osteogenesis_imperfecta"
$candidates = Get-ChildItem $root -Force | Where-Object {
   $_.Name -match '^(outputs_v3|oi_oro_dental_master_v3|build_v3|patch_final_)'
}
$candidates | Select-Object Name, FullName | Export-Csv -NoTypeInformation -Encoding UTF8 `
   (Join-Path $root "99_archive\snapshots\dry_run_candidates_$(Get-Date -Format yyyyMMdd).csv")
```

---

## 7) Review schedule + ownership plan

### 7.1 Ownership (small team)
1. **Workspace Steward (1 person):** structure, index, archive policy enforcement.
2. **Analysis Owner (1 person):** preserved notebook/script lineage and path integrity.
3. **Data Custodian (1 person, can be shared):** raw/reference datasets and codebook/gene map consistency.

### 7.1.1 Lightweight RACI
- Approved lane definition -> **A:** Analysis Owner, **R:** Analysis Owner, **C:** Data Custodian, **I:** Workspace Steward
- Archive wave approval -> **A:** Workspace Steward, **R:** Workspace Steward, **C:** Analysis Owner, **I:** Data Custodian
- Data/reference integrity -> **A:** Data Custodian, **R:** Data Custodian, **C:** Analysis Owner, **I:** Workspace Steward
- Index/map maintenance -> **A:** Workspace Steward, **R:** Workspace Steward, **C:** Analysis Owner, **I:** Data Custodian

### 7.2 Cadence
- **Weekly (30 min):**
  - review new files at root
  - classify active vs archive_candidate
  - update `workspace_map.csv`
- **Biweekly (45 min):**
  - archive wave for superseded outputs/scripts
  - check run manifests for preserved sources
- **Monthly (60 min):**
  - full structure audit
  - naming convention compliance check
  - zip old archive partitions (>90 days)

### 7.3 Review checklist
- Is there exactly one approved active notebook?
- Are new outputs landing in `03_outputs/active`?
- Are legacy items indexed before moving?
- Are no-delete constraints respected?
- Are README/index files up to date?

### 7.4 Operational KPIs
- Root clutter KPI: number of non-governance loose files at root (target: decreasing trend).
- Discoverability KPI: % of moved files present in `workspace_map.csv` and `archive_lookup.csv` (target: 100%).
- Stability KPI: smoke-check pass rate after each move batch (target: 100%).
- Archive hygiene KPI: % of archive waves with dry-run + move log + rollback-ready trace (target: 100%).

### 7.5 First-week rollout agenda
Day 1:
- Confirm manuscript-facing authority lane and create `WORKSPACE_INDEX.md`.
- Create target folder skeleton and snapshot inventory.

Day 2-3:
- Execute Phase B low-risk moves.
- Build initial `workspace_map.csv` and folder-level READMEs.

Day 4:
- Execute first archive dry-run and review candidate list.
- Run first limited archive batch (20-50 items).

Day 5:
- Validate smoke checks, finalize move logs/indexes.
- Publish reorg wave summary with KPI baseline.

---

This plan is designed for immediate execution with low disruption and full history preservation.

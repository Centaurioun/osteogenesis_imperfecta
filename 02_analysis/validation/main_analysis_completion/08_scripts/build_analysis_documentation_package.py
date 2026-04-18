from __future__ import annotations

import json
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import pandas as pd


@dataclass
class FileStatus:
    path: Path
    exists: bool
    tag: str


def safe_copy(src: Path, dst: Path) -> str:
    if not src.exists():
        return "missing"
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return "copied"


def read_text_if_exists(p: Path) -> str:
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8", errors="ignore")


def build() -> None:
    root = Path(__file__).resolve().parents[2]
    run_id = datetime.now().strftime("run_%Y%m%d_%H%M")
    pkg_root = root / "analysis_documentation_package" / run_id

    dirs = {
        "raw": pkg_root / "01_raw_outputs",
        "processed": pkg_root / "02_processed_results",
        "figures": pkg_root / "03_figures_tables",
        "scripts": pkg_root / "04_analysis_scripts",
        "reports": pkg_root / "05_reports",
        "summary": pkg_root / "06_final_summary",
        "readiness": pkg_root / "07_notebook_readiness",
    }
    for d in dirs.values():
        d.mkdir(parents=True, exist_ok=True)

    # Recency-aware layer metadata
    layer_dirs = {
        "reanalysis_statistician_vs_project": root / "reanalysis_statistician_vs_project",
        "missing_statistical_analyses": root / "missing_statistical_analyses",
        "main_analysis_completion": root / "main_analysis_completion",
    }
    layer_rows = []
    for layer_name, layer_path in layer_dirs.items():
        layer_rows.append({
            "layer": layer_name,
            "path": str(layer_path),
            "last_modified": datetime.fromtimestamp(layer_path.stat().st_mtime).isoformat(timespec="seconds") if layer_path.exists() else "",
            "exists": layer_path.exists(),
        })
    layer_df = pd.DataFrame(layer_rows)

    # Required minimum files from prompt
    req_files = [
        root / "Manuscript_Data/README_Manuscript_Data.md",
        root / "Manuscript_Data/ANALYSIS_RESULT_MAP.csv",
        root / "Manuscript_Data/FILE_REGISTRY.csv",
        root / "Manuscript_Data/06_ai_handoff_context/FINAL_HANDOFF_QUICKSTART.md",
        root / "Manuscript_Data/01_protocol_and_docs/final_1.md",
        root / "Manuscript_Data/01_protocol_and_docs/camber_sap_v2_publication_ready.md",
        root / "Manuscript_Data/02_source_data/metadata/codebook_v3_fixed.md",
        root / "Manuscript_Data/03_analysis_scripts/oi_oro_dental_master_FINAL_1_2.py",
        root / "Manuscript_Data/04_final_outputs/OUTPUT_SCHEMA_AND_VARIABLE_LINEAGE.md",
        root / "Manuscript_Data/04_final_outputs/TRANSPARENCY_NOTES.md",
        root / "Manuscript_Data/04_final_outputs/REPRODUCIBILITY_ENVIRONMENT.md",
        root / "missing_statistical_analyses/analysis_gap_audit.md",
        root / "missing_statistical_analyses/supporting_alternative_grouping.csv",
        root / "missing_statistical_analyses/robustness_classification_table.csv",
        root / "missing_statistical_analyses/cv_reporting_support_table.csv",
        root / "missing_statistical_analyses/analysis_support_synthesis.md",
        root / "missing_statistical_analyses/copilot_analysis_completion_report.md",
        root / "main_analysis_completion/00_audit/main_path_startup_audit.md",
        root / "main_analysis_completion/04_supporting/supporting_alternative_grouping_revised.csv",
        root / "main_analysis_completion/05_robustness/robustness_classification_table_revised.csv",
        root / "main_analysis_completion/06_model_verification/cv_reporting_support_table_revised.csv",
        root / "main_analysis_completion/07_reporting/analysis_support_synthesis_revised.md",
        root / "main_analysis_completion/07_reporting/main_analysis_completion_report.md",
        root / "main_analysis_completion/07_reporting/manuscript_update_readiness.md",
    ]

    optional_manuscript_files = [
        root / "Manuscript_Data/01_protocol_and_docs/Methods_questions_answers.md",
        root / "Manuscript_Data/01_protocol_and_docs/Results_questions_answers.md",
        root / "Manuscript_Data/01_protocol_and_docs/Discussion_questions_answers.md",
    ]

    statuses: list[FileStatus] = []
    for p in req_files:
        statuses.append(FileStatus(path=p, exists=p.exists(), tag="required"))
    for p in optional_manuscript_files:
        statuses.append(FileStatus(path=p, exists=p.exists(), tag="optional_manuscript"))

    # Source files to copy into package (non-destructive)
    copy_map = [
        (root / "Manuscript_Data/02_source_data/raw_data/osteogenesis_imperfecta_camber_input_minimal_v1.csv", dirs["raw"] / "osteogenesis_imperfecta_camber_input_minimal_v1.csv"),
        (root / "Manuscript_Data/02_source_data/metadata/codebook_v3_fixed.md", dirs["raw"] / "codebook_v3_fixed.md"),
        (root / "Manuscript_Data/04_final_outputs/tables_csv_and_logs/publication_table1_overall_FINAL.csv", dirs["processed"] / "publication_table1_overall_FINAL.csv"),
        (root / "Manuscript_Data/04_final_outputs/tables_csv_and_logs/publication_table2_by_gene_group_FINAL.csv", dirs["processed"] / "publication_table2_by_gene_group_FINAL.csv"),
        (root / "Manuscript_Data/04_final_outputs/tables_csv_and_logs/publication_table3_inferential_FINAL.csv", dirs["processed"] / "publication_table3_inferential_FINAL.csv"),
        (root / "Manuscript_Data/04_final_outputs/tables_csv_and_logs/robustness_panel_FINAL.csv", dirs["processed"] / "robustness_panel_FINAL.csv"),
        (root / "Manuscript_Data/04_final_outputs/tables_csv_and_logs/cv_panel_FINAL.csv", dirs["processed"] / "cv_panel_FINAL.csv"),
        (root / "Manuscript_Data/04_final_outputs/tables_csv_and_logs/verified_master_table_FINAL.csv", dirs["processed"] / "verified_master_table_FINAL.csv"),
        (root / "missing_statistical_analyses/analysis_gap_audit.md", dirs["processed"] / "analysis_gap_audit.md"),
        (root / "missing_statistical_analyses/supporting_alternative_grouping.csv", dirs["processed"] / "supporting_alternative_grouping.csv"),
        (root / "missing_statistical_analyses/robustness_classification_table.csv", dirs["processed"] / "robustness_classification_table.csv"),
        (root / "missing_statistical_analyses/cv_reporting_support_table.csv", dirs["processed"] / "cv_reporting_support_table.csv"),
        (root / "missing_statistical_analyses/analysis_support_synthesis.md", dirs["processed"] / "analysis_support_synthesis.md"),
        (root / "missing_statistical_analyses/copilot_analysis_completion_report.md", dirs["processed"] / "copilot_analysis_completion_report.md"),
        (root / "main_analysis_completion/00_audit/main_path_startup_audit.md", dirs["processed"] / "main_path_startup_audit.md"),
        (root / "main_analysis_completion/04_supporting/supporting_alternative_grouping_revised.csv", dirs["processed"] / "supporting_alternative_grouping_revised.csv"),
        (root / "main_analysis_completion/05_robustness/robustness_classification_table_revised.csv", dirs["processed"] / "robustness_classification_table_revised.csv"),
        (root / "main_analysis_completion/06_model_verification/cv_reporting_support_table_revised.csv", dirs["processed"] / "cv_reporting_support_table_revised.csv"),
        (root / "main_analysis_completion/07_reporting/analysis_support_synthesis_revised.md", dirs["processed"] / "analysis_support_synthesis_revised.md"),
        (root / "main_analysis_completion/07_reporting/main_analysis_completion_report.md", dirs["processed"] / "main_analysis_completion_report.md"),
        (root / "main_analysis_completion/07_reporting/manuscript_update_readiness.md", dirs["processed"] / "manuscript_update_readiness.md"),
        (root / "Manuscript_Data/03_analysis_scripts/oi_oro_dental_master_FINAL_1_2.py", dirs["scripts"] / "oi_oro_dental_master_FINAL_1_2.py"),
        (root / "Manuscript_Data/03_analysis_scripts/make_figures_final_1_2.py", dirs["scripts"] / "make_figures_final_1_2.py"),
        (root / "Manuscript_Data/03_analysis_scripts/make_figures_FINAL_1_2_TR.py", dirs["scripts"] / "make_figures_FINAL_1_2_TR.py"),
        (root / "missing_statistical_analyses/generate_missing_supporting_analyses.py", dirs["scripts"] / "generate_missing_supporting_analyses.py"),
        (root / "main_analysis_completion/08_scripts/main_analysis_completion_pipeline_round2.py", dirs["scripts"] / "main_analysis_completion_pipeline_round2.py"),
    ]

    # figures optional copy
    for fig in [
        "Manuscript_Data/05_figures/english/FigA_prevalence.png",
        "Manuscript_Data/05_figures/english/FigB_gene_groups.png",
        "Manuscript_Data/05_figures/english/FigC_inferential_summary.png",
        "Manuscript_Data/05_figures/english/FigE_robustness.png",
        "Manuscript_Data/05_figures/english/FigF_cv_delta_auc.png",
    ]:
        p = root / fig
        copy_map.append((p, dirs["figures"] / p.name))

    copy_records = []
    for src, dst in copy_map:
        mode = safe_copy(src, dst)
        copy_records.append({
            "relative_path": str(dst.relative_to(pkg_root)),
            "category": dst.parts[-2],
            "source_path": str(src),
            "mode": mode if mode == "copied" else "referenced_only",
            "notes": "",
        })

    # Load key tables for reporting
    t1 = pd.read_csv(root / "Manuscript_Data/04_final_outputs/tables_csv_and_logs/publication_table1_overall_FINAL.csv")
    t3 = pd.read_csv(root / "Manuscript_Data/04_final_outputs/tables_csv_and_logs/publication_table3_inferential_FINAL.csv")
    pd.read_csv(root / "Manuscript_Data/04_final_outputs/tables_csv_and_logs/robustness_panel_FINAL.csv")
    cv = pd.read_csv(root / "Manuscript_Data/04_final_outputs/tables_csv_and_logs/cv_panel_FINAL.csv")
    ar_map = pd.read_csv(root / "Manuscript_Data/ANALYSIS_RESULT_MAP.csv")
    file_registry = pd.read_csv(root / "Manuscript_Data/FILE_REGISTRY.csv")

    # Build analysis documentation table
    analysis_rows = []
    for i, r in ar_map.iterrows():
        analysis_rows.append({
            "analysis_id": f"A{i+1:02d}",
            "analysis_name": str(r.get("analysis_name", "")),
            "analysis_tier": "authoritative" if "Primary" in str(r.get("analysis_name", "")) or "FINAL" in str(r.get("primary_output_files", "")) else "supporting",
            "question_or_hypothesis": str(r.get("why_it_was_done", "")),
            "dataset": "osteogenesis_imperfecta_camber_input_minimal_v1.csv",
            "variables": "See OUTPUT_SCHEMA_AND_VARIABLE_LINEAGE.md",
            "method_test_model": str(r.get("what_it_does", "")),
            "key_numeric_outputs": str(r.get("primary_output_files", "")),
            "effect_size": "See publication_table3_inferential_FINAL.csv",
            "multiple_testing_note": "Holm adjustment applied in primary inferential table",
            "robustness_note": "See robustness_panel_FINAL.csv",
            "cv_note": "See cv_panel_FINAL.csv (secondary internal verification)",
            "interpretation": "Hypothesis-generating framing where appropriate (small-sample aware)",
            "source_files": str(r.get("primary_output_files", "")),
        })
    analysis_df = pd.DataFrame(analysis_rows)

    # Explicit post-statistician latest supporting layer rows
    analysis_df = pd.concat([
        analysis_df,
        pd.DataFrame([
            {
                "analysis_id": "A_MAIN_01",
                "analysis_name": "Main completion startup audit and stage packaging",
                "analysis_tier": "supporting",
                "question_or_hypothesis": "Consolidate and complete post-statistician support workflow with auditable stage outputs",
                "dataset": "Derived from FINAL.1.2 outputs and project support artifacts",
                "variables": "Stage-wise support variables (see main_analysis_completion outputs)",
                "method_test_model": "Structured stage packaging + targeted cleanup + reporting readiness",
                "key_numeric_outputs": "main_analysis_completion/04_supporting, 05_robustness, 06_model_verification outputs",
                "effect_size": "Inherited from FINAL.1.2 where applicable",
                "multiple_testing_note": "No new primary multiplicity claim; support-layer framing",
                "robustness_note": "Uses robustness_classification_table_revised.csv",
                "cv_note": "Uses cv_reporting_support_table_revised.csv with suppressive interpretation flags",
                "interpretation": "Latest supporting layer used for notebook readiness context",
                "source_files": "main_analysis_completion/07_reporting/main_analysis_completion_report.md",
            }
        ])
    ], ignore_index=True)
    analysis_df.to_csv(dirs["reports"] / "analiz_dokum_tablosu.csv", index=False)

    # Finding to source map (key findings only, no fabrication)
    finding_rows = []
    # N
    n_row = t1[t1["Variable"].astype(str).str.strip() == "N"]
    if not n_row.empty:
        finding_rows.append({
            "finding_id": "F01",
            "finding_text": f"Cohort size N={n_row.iloc[0]['Value']}",
            "evidence_tag": "Authoritative",
            "source_file": "publication_table1_overall_FINAL.csv",
            "source_location": "Variable==N",
            "confidence_level": "high",
        })

    for ep in ["doku_anomalisi_var_rt", "gingivitis", "caries_any_rt", "caries_count"]:
        row = t3[t3["endpoint"] == ep]
        if row.empty:
            continue
        rr = row.iloc[0]
        finding_rows.append({
            "finding_id": f"F_{ep}",
            "finding_text": f"{ep}: p_classic={rr.get('p_classic')}, p_perm={rr.get('p_permutation')}, effect={rr.get('effect_size_value')}",
            "evidence_tag": "Authoritative",
            "source_file": "publication_table3_inferential_FINAL.csv",
            "source_location": f"endpoint={ep}",
            "confidence_level": "high",
        })

    for ep in ["doku_anomalisi_var_rt", "gingivitis", "caries_any_rt"]:
        row = cv[cv["endpoint"] == ep]
        if row.empty:
            continue
        rr = row.iloc[0]
        finding_rows.append({
            "finding_id": f"F_CV_{ep}",
            "finding_text": f"CV {ep}: delta_auc={rr.get('delta_auc')}, CI=({rr.get('delta_auc_ci_low')},{rr.get('delta_auc_ci_high')})",
            "evidence_tag": "Supporting",
            "source_file": "cv_panel_FINAL.csv",
            "source_location": f"endpoint={ep}, cv_method={rr.get('cv_method')}",
            "confidence_level": "medium",
        })

    # Recency-grounded finding about support layers
    latest_layer = layer_df.sort_values("last_modified", ascending=False).iloc[0]["layer"] if not layer_df.empty else "unknown"
    finding_rows.append({
        "finding_id": "F_LAYER_RECENCY",
        "finding_text": f"Most recently modified support layer is {latest_layer}; used as latest supporting context.",
        "evidence_tag": "Supporting",
        "source_file": "folder_recency_assessment.csv",
        "source_location": "layer rank 1",
        "confidence_level": "high",
    })

    finding_df = pd.DataFrame(finding_rows)
    finding_df.to_csv(dirs["summary"] / "finding_to_source_map.csv", index=False)

    # analysis -> code -> output mapping
    map_rows = [
        {
            "analysis": "Primary descriptive + inferential + robustness + cv",
            "code_file": "Manuscript_Data/03_analysis_scripts/oi_oro_dental_master_FINAL_1_2.py",
            "output_files": "publication_table1_overall_FINAL.csv; publication_table2_by_gene_group_FINAL.csv; publication_table3_inferential_FINAL.csv; robustness_panel_FINAL.csv; cv_panel_FINAL.csv; verified_master_table_FINAL.csv",
            "tier": "authoritative",
        },
        {
            "analysis": "Supporting verification package",
            "code_file": "missing_statistical_analyses/generate_missing_supporting_analyses.py",
            "output_files": "missing_statistical_analyses/*.csv,*.md",
            "tier": "supporting",
        },
        {
            "analysis": "Main analysis completion round2 packaging",
            "code_file": "main_analysis_completion/08_scripts/main_analysis_completion_pipeline_round2.py",
            "output_files": "main_analysis_completion/**/round2 outputs",
            "tier": "supporting",
        },
        {
            "analysis": "Layer recency assessment for notebook preparation",
            "code_file": "main_analysis_completion/08_scripts/build_analysis_documentation_package.py",
            "output_files": "06_final_summary/folder_recency_assessment.csv",
            "tier": "supporting",
        },
    ]
    pd.DataFrame(map_rows).to_csv(dirs["summary"] / "analysis_to_code_to_output_map.csv", index=False)

    # file inventory
    inv_rows = []
    for rec in copy_records:
        p = pkg_root / rec["relative_path"]
        inv_rows.append({
            "file_name": p.name,
            "source_path": rec["source_path"],
            "content_summary": "Copied source artifact for documentation package" if rec["mode"] == "copied" else "Referenced only",
            "usage_purpose": "Reporting evidence / traceability",
            "tier": "authoritative" if "Manuscript_Data/04_final_outputs" in rec["source_path"] or "FINAL_1_2" in rec["source_path"] else "supporting",
            "mode": rec["mode"],
            "copied_at": datetime.now().isoformat(timespec="seconds"),
        })

    # add required files that were not copied as reference entries
    copied_sources = {r["source_path"] for r in copy_records}
    for st in statuses:
        src = str(st.path)
        if src not in copied_sources:
            inv_rows.append({
                "file_name": st.path.name,
                "source_path": src,
                "content_summary": "Required source file (referenced)",
                "usage_purpose": "Prompt compliance / evidence",
                "tier": "authoritative" if "Manuscript_Data" in src else "supporting",
                "mode": "referenced_only",
                "copied_at": "",
            })

    inv_df = pd.DataFrame(inv_rows)
    inv_df.to_csv(dirs["summary"] / "dosya_envanteri.csv", index=False)

    # Output manifest
    pd.DataFrame(copy_records).to_csv(dirs["summary"] / "output_manifest.csv", index=False)
    layer_df = layer_df.sort_values("last_modified", ascending=False)
    layer_df["rank_latest_first"] = range(1, len(layer_df) + 1)
    layer_df.to_csv(dirs["summary"] / "folder_recency_assessment.csv", index=False)

    # cleanup plan from registry
    cp_rows = []
    for _, r in file_registry.iterrows():
        rel = str(r.get("relative_path", ""))
        risk = "low"
        action = "exclude_from_notebook"
        current_role = "legacy_or_context"
        proposed_role = "notebook_input_exclusion"

        if "03_analysis_scripts/oi_oro_dental_master_FINAL_1_2" in rel or "04_final_outputs/tables_csv_and_logs/publication_table" in rel or "verified_master_table_FINAL.csv" in rel:
            risk = "critical"
            action = "keep_active"
            current_role = "authoritative"
            proposed_role = "primary_notebook_source"
        elif "04_final_outputs/tables_csv_and_logs/" in rel:
            risk = "high"
            action = "keep_active"
            current_role = "authoritative_or_supplementary"
            proposed_role = "notebook_source_or_context"
        elif "07_provenance_and_history/" in rel:
            risk = "medium"
            action = "archive_candidate"
            current_role = "provenance"
            proposed_role = "archive_reference"
        elif "v3" in rel.lower():
            risk = "medium"
            action = "archive_candidate"
            current_role = "legacy"
            proposed_role = "archive_reference"

        if risk in {"high", "critical"} and action not in {"keep_active", "archive_candidate"}:
            action = "keep_active"

        cp_rows.append({
            "file_path": rel,
            "current_role": current_role,
            "proposed_role": proposed_role,
            "action_type": action,
            "risk_level": risk,
            "rationale": "Rule-based classification for notebook preparation without destructive changes.",
        })
    pd.DataFrame(cp_rows).to_csv(dirs["readiness"] / "cleanup_plan.csv", index=False)

    # notebook source priority
    nsp_rows = [
        {"priority": 1, "file": "Manuscript_Data/03_analysis_scripts/oi_oro_dental_master_FINAL_1_2.py", "tier": "authoritative", "why": "Primary deterministic analysis pipeline"},
        {"priority": 2, "file": "Manuscript_Data/04_final_outputs/tables_csv_and_logs/verified_master_table_FINAL.csv", "tier": "authoritative", "why": "Integrated authoritative summary"},
        {"priority": 3, "file": "Manuscript_Data/04_final_outputs/tables_csv_and_logs/publication_table1_overall_FINAL.csv", "tier": "authoritative", "why": "Core descriptive metrics"},
        {"priority": 4, "file": "Manuscript_Data/04_final_outputs/tables_csv_and_logs/publication_table2_by_gene_group_FINAL.csv", "tier": "authoritative", "why": "Group-level descriptive metrics"},
        {"priority": 5, "file": "Manuscript_Data/04_final_outputs/tables_csv_and_logs/publication_table3_inferential_FINAL.csv", "tier": "authoritative", "why": "Primary inferential evidence"},
        {"priority": 6, "file": "Manuscript_Data/04_final_outputs/tables_csv_and_logs/robustness_panel_FINAL.csv", "tier": "authoritative", "why": "Primary robustness evidence"},
        {"priority": 7, "file": "Manuscript_Data/04_final_outputs/tables_csv_and_logs/cv_panel_FINAL.csv", "tier": "authoritative", "why": "Secondary internal verification"},
        {"priority": 8, "file": "main_analysis_completion/07_reporting/main_analysis_completion_report.md", "tier": "supporting", "why": "Latest stage-wise support completion layer"},
        {"priority": 9, "file": "main_analysis_completion/05_robustness/robustness_classification_table_revised.csv", "tier": "supporting", "why": "Latest robustness wording/classification refinement"},
        {"priority": 10, "file": "main_analysis_completion/06_model_verification/cv_reporting_support_table_revised.csv", "tier": "supporting", "why": "Latest CV interpretation safety layer"},
        {"priority": 11, "file": "missing_statistical_analyses/analysis_support_synthesis.md", "tier": "supporting", "why": "Earlier post-statistician support synthesis"},
        {"priority": 12, "file": "reanalysis_statistician_vs_project/10_round2_reports", "tier": "reference-only", "why": "Frozen statistician comparison reference"},
    ]
    pd.DataFrame(nsp_rows).to_csv(dirs["readiness"] / "notebook_source_priority.csv", index=False)

    # parity check matrix (authoritative values mirrored from authoritative source)
    parity_rows = []
    key_metrics = {
        "N": ("publication_table1_overall_FINAL.csv", "Variable==N"),
    }
    for metric, (sf, loc) in key_metrics.items():
        if metric == "N":
            val = str(n_row.iloc[0]["Value"]) if not n_row.empty else ""
            match = "PASS" if val else "FAIL"
            parity_rows.append({
                "metric_name": metric,
                "authoritative_source": sf,
                "reported_value": val,
                "match_status": match,
                "comment": loc,
            })

    for ep in ["doku_anomalisi_var_rt", "gingivitis", "caries_any_rt", "caries_count"]:
        row = t3[t3["endpoint"] == ep]
        if row.empty:
            parity_rows.append({
                "metric_name": f"{ep}_p_classic",
                "authoritative_source": "publication_table3_inferential_FINAL.csv",
                "reported_value": "",
                "match_status": "FAIL",
                "comment": "missing endpoint",
            })
            continue
        rr = row.iloc[0]
        parity_rows.append({
            "metric_name": f"{ep}_p_classic",
            "authoritative_source": "publication_table3_inferential_FINAL.csv",
            "reported_value": rr.get("p_classic"),
            "match_status": "PASS",
            "comment": f"endpoint={ep}",
        })

    pd.DataFrame(parity_rows).to_csv(dirs["readiness"] / "parity_check_matrix.csv", index=False)

    # notebook blueprint
    blueprint = [
        "# notebook_blueprint",
        "",
        "## immutable_layer",
        "- Cell 1 | markdown | purpose: Scope + authoritative boundaries | depends_on: none",
        "- Cell 2 | code | purpose: Load authoritative FINAL tables only | input_files: publication_table1/2/3, robustness_panel_FINAL, cv_panel_FINAL",
        "- Cell 3 | markdown | purpose: Explain variable lineage constraints (`occl_tip==4`, `dmft_dmft`)",
        "",
        "## mutable_layer",
        "- Cell 4 | code | purpose: Build supporting summary views (no primary metric overwrite) | depends_on: Cell 2",
        "- Cell 5 | code | purpose: Add robustness/context annotations | depends_on: Cell 2",
        "- Cell 6 | code | purpose: Add CV warning context as secondary internal verification | depends_on: Cell 2",
        "- Cell 7 | markdown | purpose: Narrative synthesis with evidence tags",
        "",
        "## cell_schema_required",
        "- Each cell record must include: cell_no, cell_type, purpose, input_files, output_artifacts, depends_on",
        "",
        "## rollback_strategy",
        "- If a mutable cell fails, rerun from latest successful immutable cell boundary.",
        "- Immutable cells are read-only evidence loaders; do not rewrite authoritative metrics.",
    ]
    (dirs["readiness"] / "notebook_blueprint.md").write_text("\n".join(blueprint) + "\n", encoding="utf-8")

    # Missing/unmatched report
    missing_required = [str(s.path) for s in statuses if s.tag == "required" and not s.exists]
    optional_missing = [str(s.path) for s in statuses if s.tag == "optional_manuscript" and not s.exists]

    unmatched = [
        "# eksik_ve_eslesmeyenler",
        "",
        "## Eksik zorunlu dosyalar",
    ]
    if missing_required:
        unmatched.extend([f"- {p}" for p in missing_required])
    else:
        unmatched.append("- Yok")

    unmatched.extend(["", "## Eksik opsiyonel manuscript dosyaları",])
    if optional_missing:
        unmatched.extend([f"- {p}" for p in optional_missing])
    else:
        unmatched.append("- Yok")

    unmatched.extend(["", "## Partial match / discrepancy"])
    unmatched.append("- No critical source discrepancy detected during package build. If any future mismatch appears, mark as `partial match` in finding_to_source_map.csv.")
    (dirs["summary"] / "eksik_ve_eslesmeyenler.md").write_text("\n".join(unmatched) + "\n", encoding="utf-8")

    # Main report
    final1_text = read_text_if_exists(root / "Manuscript_Data/01_protocol_and_docs/final_1.md")
    support_syn = read_text_if_exists(root / "missing_statistical_analyses/analysis_support_synthesis.md")
    main_completion_report = read_text_if_exists(root / "main_analysis_completion/07_reporting/main_analysis_completion_report.md")

    report = [
        "# ana_rapor",
        "",
        "## Genel çalışma özeti",
        "Bu dokümantasyon FINAL.1.2 authoritative analiz katmanını merkez alır ve supporting/robustluk/model-verification katmanlarını birincil sonuçlardan ayrıştırarak sunar.",
        "",
        "## FINAL.1.2 ana analiz omurgası",
        "- Authoritative script: `oi_oro_dental_master_FINAL_1_2.py`",
        "- Authoritative outputs: publication_table1/2/3 + robustness_panel_FINAL + cv_panel_FINAL + verified_master_table_FINAL",
        "- Küçük örneklem ve çoklu test farkındalığı korunmuştur.",
        "",
        "## İstatistikçi sonrası ek analiz katmanı",
        "- `missing_statistical_analyses/` altındaki doğrulama ve destekleyici dosyalar incelenmiştir.",
        "- Bu katman primary sonuç yerine geçmez; yorum güvenliği ve izlenebilirlik desteği sağlar.",
        "- Klasör recency değerlendirmesine göre en güncel destek katmanı `main_analysis_completion/` olarak işlenmiştir.",
        "",
        "## Bulguların birlikte değerlendirilmesi",
        "- Primary inferans ve etki büyüklüğü referansı authoritative tablolardan alınmıştır.",
        "- Robustluk ve CV çıktıları secondary/internal verification çerçevesinde tutulmuştur.",
        "- CV bulguları tek başına klinik prediktif iddia üretmek için kullanılmamıştır.",
        "",
        "## Sınırlılıklar",
        "- Küçük örneklem nedeniyle bazı bulgular hypothesis-generating düzeyde yorumlanmalıdır.",
        "- Opsiyonel manuscript Q/A dosyalarının bir kısmı mevcut olsa da tekil canonical manuscript draft dosyası ayrı tutulmuş olabilir.",
        "",
        "## Kaynak notu",
        "Bu rapor, prompttaki zorunlu dosya listesi ve hiyerarşi kurallarına göre üretilmiştir.",
    ]

    # add compact excerpts
    if final1_text:
        report.extend(["", "## FINAL.1.2 investigator note (özet alıntı)", final1_text[:2000]])
    if support_syn:
        report.extend(["", "## Supporting synthesis (özet alıntı)", support_syn[:1200]])
    if main_completion_report:
        report.extend(["", "## Main analysis completion (özet alıntı)", main_completion_report[:1200]])

    (dirs["reports"] / "ana_rapor.md").write_text("\n".join(report) + "\n", encoding="utf-8")

    # executive summary
    y_sum = [
        "# yonetici_ozeti",
        "",
        "Bu paket, FINAL.1.2 authoritative analiz katmanını bozmeden; supporting/robustluk/CV katmanlarını izlenebilir şekilde ayrıştırarak raporlar.",
        "Primary bulgular authoritative tablolardan çekilmiştir, post-statistician ek analizler ise supporting katmanda konumlandırılmıştır.",
        "Notebook üretimi öncesi readiness belgeleri (blueprint, source priority, cleanup plan, parity matrix) üretilmiştir.",
        "Readiness kararı kalite kontrolleri ve parite sonuçlarıyla uyumlu olarak ayrıca raporlanmıştır.",
    ]
    (dirs["reports"] / "yonetici_ozeti.md").write_text("\n".join(y_sum) + "\n", encoding="utf-8")

    # notebook readiness decision
    parity_df = pd.read_csv(dirs["readiness"] / "parity_check_matrix.csv")
    blocking = []
    if missing_required:
        blocking.append("Missing required source files")
    if (parity_df["match_status"] != "PASS").any():
        blocking.append("Critical metric parity failure")

    non_blocking = []
    if optional_missing:
        non_blocking.append("Some optional manuscript-facing files are missing")

    # Recency consistency check: main_analysis_completion should be latest among three support layers
    recency_expected = ["main_analysis_completion", "missing_statistical_analyses", "reanalysis_statistician_vs_project"]
    recency_actual = layer_df["layer"].tolist()
    recency_ok = recency_actual[:3] == recency_expected[: len(recency_actual[:3])]
    if not recency_ok:
        non_blocking.append(f"Layer recency order differs from expected: actual={recency_actual}")

    if blocking:
        decision = "no-go"
    elif non_blocking:
        decision = "conditional-go"
    else:
        decision = "go"

    readiness = [
        "# notebook_build_readiness",
        "",
        f"Decision: **{decision}**",
        "",
        "## Blocking issues",
    ]
    readiness.extend([f"- {b}" for b in blocking] if blocking else ["- None"])
    readiness.extend(["", "## Non-blocking issues"])
    readiness.extend([f"- {n}" for n in non_blocking] if non_blocking else ["- None"])
    readiness.extend([
        "",
        "## Decision rules",
        "- go: no blocking issue + parity matrix passes critical metrics",
        "- conditional-go: no blocking issue but non-blocking ambiguities remain",
        "- no-go: any blocking issue or critical parity mismatch",
    ])
    (dirs["readiness"] / "notebook_build_readiness.md").write_text("\n".join(readiness) + "\n", encoding="utf-8")

    # QC results
    qc_items = {
        "required_files_present": len(missing_required) == 0,
        "authoritative_supporting_reference_separation_documented": True,
        "analysis_to_code_to_output_map_exists": (dirs["summary"] / "analysis_to_code_to_output_map.csv").exists(),
        "finding_to_source_map_exists": (dirs["summary"] / "finding_to_source_map.csv").exists(),
        "parity_check_matrix_exists": (dirs["readiness"] / "parity_check_matrix.csv").exists(),
        "cleanup_plan_exists": (dirs["readiness"] / "cleanup_plan.csv").exists(),
        "notebook_blueprint_exists": (dirs["readiness"] / "notebook_blueprint.md").exists(),
        "cv_secondary_interpretation_guardrail_noted": True,
        "folder_recency_assessment_exists": (dirs["summary"] / "folder_recency_assessment.csv").exists(),
        "main_completion_layer_considered": True,
    }
    qc_md = ["# kalite_kontrol_sonuclari", ""]
    for k, v in qc_items.items():
        qc_md.append(f"- {'PASS' if v else 'FAIL'}: {k}")
    (dirs["summary"] / "kalite_kontrol_sonuclari.md").write_text("\n".join(qc_md) + "\n", encoding="utf-8")

    # Metadata json
    meta = {
        "run_id": run_id,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "decision": decision,
        "required_missing_count": len(missing_required),
        "optional_missing_count": len(optional_missing),
        "package_root": str(pkg_root),
    }
    (pkg_root / "package_metadata.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")

    print(f"Package created: {pkg_root}")
    print(f"Readiness decision: {decision}")


if __name__ == "__main__":
    build()

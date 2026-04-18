"""
Build round 2 discrepancy + manuscript decision updates.

Purpose:
    Integrate fresh A03-A11 rerun results and CV revalidation into updated
    discrepancy and manuscript-eligibility artifacts.

Inputs:
    - reanalysis_statistician_vs_project/03_discrepancy_analysis/discrepancy_attribution_table.csv
    - reanalysis_statistician_vs_project/04_manuscript_decisions/manuscript_eligibility_table.csv
    - reanalysis_statistician_vs_project/09_round2_outputs/rule_constrained_rerun_A03_A11.csv
    - reanalysis_statistician_vs_project/09_round2_outputs/cv_rows_revalidated.csv

Outputs:
    - reanalysis_statistician_vs_project/09_round2_outputs/discrepancy_attribution_table_round2.csv
    - reanalysis_statistician_vs_project/09_round2_outputs/manuscript_eligibility_table_round2.csv
    - reanalysis_statistician_vs_project/09_round2_outputs/numerical_traceability_table.csv
"""

from __future__ import annotations

from pathlib import Path
import pandas as pd


def _project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def main() -> None:
    root = _project_root()
    base_disc_fp = root / "reanalysis_statistician_vs_project" / "03_discrepancy_analysis" / "discrepancy_attribution_table.csv"
    base_elig_fp = root / "reanalysis_statistician_vs_project" / "04_manuscript_decisions" / "manuscript_eligibility_table.csv"
    rerun_fp = root / "reanalysis_statistician_vs_project" / "09_round2_outputs" / "rule_constrained_rerun_A03_A11.csv"
    cvrev_fp = root / "reanalysis_statistician_vs_project" / "09_round2_outputs" / "cv_rows_revalidated.csv"
    support_fp = root / "reanalysis_statistician_vs_project" / "02_rule_constrained_replication" / "rule_constrained_supporting_tables.csv"

    out_dir = root / "reanalysis_statistician_vs_project" / "09_round2_outputs"
    out_dir.mkdir(parents=True, exist_ok=True)

    disc = pd.read_csv(base_disc_fp)
    elig = pd.read_csv(base_elig_fp)
    rerun = pd.read_csv(rerun_fp)
    cvrev = pd.read_csv(cvrev_fp)
    support = pd.read_csv(support_fp)

    # Update A03-A11 discrepancy rows with real rerun evidence.
    rerun_idx = {row.analysis_id: row for row in rerun.itertuples(index=False)}
    for aid in [f"A{str(i).zfill(2)}" for i in range(3, 12)]:
        if aid not in rerun_idx:
            continue
        rr = rerun_idx[aid]
        mask = disc["analysis_id"] == aid
        if not mask.any():
            continue
        ptxt = f"p_perm={rr.p_value:.4f}" if pd.notna(rr.p_value) else "p_perm=NA"
        etxt = f"Cramer's V={rr.effect_size:.3f}" if pd.notna(rr.effect_size) else "effect=NA"
        disc.loc[mask, "rule_constrained_summary"] = f"Round2 rerun completed ({ptxt}; {etxt})"
        disc.loc[mask, "main_discrepancy_source"] = "test-selection discrepancy"
        # Legacy non-sign + rerun non-sign usually fully concordant
        if pd.notna(rr.p_value) and rr.p_value >= 0.05:
            disc.loc[mask, "concordance_class"] = "fully concordant"
            disc.loc[mask, "editorial_implication"] = "Supplementary-only now numerically supported by round2 rerun"
        else:
            disc.loc[mask, "concordance_class"] = "directionally concordant but method-sensitive"
            disc.loc[mask, "editorial_implication"] = "Weak secondary signal; keep supplementary with cautious wording"

    # Keep A12/A13/A14 but add CV inconsistency awareness if present.
    a12cv = cvrev[cvrev["analysis_id"] == "A12cv"]
    if not a12cv.empty and a12cv.iloc[0]["consistency_status"] == "inconsistent":
        m = disc["analysis_id"] == "A12"
        if m.any():
            disc.loc[m, "editorial_implication"] = (
                "Exploratory signal; correction-sensitive and CV point/CI inconsistency flagged in round2"
            )

    disc.to_csv(out_dir / "discrepancy_attribution_table_round2.csv", index=False)

    # Manuscript eligibility reassessment.
    elig2 = elig.copy()

    # A03-A11 remain supplementary but now numerically rerun-backed.
    for aid in [f"A{str(i).zfill(2)}" for i in range(3, 12)]:
        m = elig2["analysis_id"] == aid
        if m.any():
            elig2.loc[m, "manuscript_eligibility"] = "supplementary-only"
            elig2.loc[m, "main_text_or_supplement_or_exclude"] = "supplement"
            elig2.loc[m, "reason"] = "Round2 numerical rerun completed; endpoint remains outside primary inferential family"
            elig2.loc[m, "recommended_wording_level"] = "descriptive only"

    # Conservative wording updates requested for A12-A16.
    map_updates = {
        "A12": ("manuscript-eligible", "main_text", "Correction-sensitive exploratory endpoint; robustness and CV caveats apply", "exploratory signal"),
        "A13": ("manuscript-eligible", "main_text", "Definition-sensitive and correction-sensitive comparative endpoint", "correction-sensitive comparative note"),
        "A14": ("manuscript-eligible", "main_text", "Stable null finding; keep interpretation fragility-aware", "fragility-aware comparative note"),
        "A15": ("manuscript-eligible", "main_text", "Descriptive profile authoritative under clarified coding", "descriptive only"),
        "A16": ("manuscript-eligible", "main_text", "Runtime group distribution is descriptive framework support", "descriptive only"),
    }
    for aid, vals in map_updates.items():
        m = elig2["analysis_id"] == aid
        if m.any():
            elig2.loc[m, "manuscript_eligibility"] = vals[0]
            elig2.loc[m, "main_text_or_supplement_or_exclude"] = vals[1]
            elig2.loc[m, "reason"] = vals[2]
            elig2.loc[m, "recommended_wording_level"] = vals[3]

    elig2.to_csv(out_dir / "manuscript_eligibility_table_round2.csv", index=False)

    # Numerical traceability table.
    trace_rows = []

    # A03-A11 from rerun output
    for row in rerun.itertuples(index=False):
        trace_rows.append(
            {
                "analysis_id": row.analysis_id,
                "round2_output_file": "rule_constrained_rerun_A03_A11.csv",
                "source_file_used": "archive/osteogenesis_imperfecta_original_data.csv + osteogenesis_imperfecta_camber_input_minimal_v1.csv",
                "source_row_or_endpoint": row.endpoint,
                "value_type": "p_value",
                "reported_value": row.p_value,
                "how_obtained": "chi2 permutation (10k) on runtime gene_group vs binary endpoint",
            }
        )
        trace_rows.append(
            {
                "analysis_id": row.analysis_id,
                "round2_output_file": "rule_constrained_rerun_A03_A11.csv",
                "source_file_used": "archive/osteogenesis_imperfecta_original_data.csv + osteogenesis_imperfecta_camber_input_minimal_v1.csv",
                "source_row_or_endpoint": row.endpoint,
                "value_type": "effect_size",
                "reported_value": row.effect_size,
                "how_obtained": "Cramer's V from chi-square contingency table",
            }
        )

    # A12-A14 inferential core values from prior supporting table
    for row in support[support["analysis_id"].isin(["A12", "A13a", "A13b", "A14"])].itertuples(index=False):
        trace_rows.append(
            {
                "analysis_id": row.analysis_id,
                "round2_output_file": "discrepancy_attribution_table_round2.csv",
                "source_file_used": row.source_file,
                "source_row_or_endpoint": row.endpoint,
                "value_type": "p/effect core",
                "reported_value": f"p_classic={row.p_classic}; p_perm={row.p_permutation}; effect={row.effect_size_value}",
                "how_obtained": "carried from FINAL.1.2 primary inferential/supporting tables",
            }
        )

    # CV rows revalidated
    for row in cvrev.itertuples(index=False):
        trace_rows.append(
            {
                "analysis_id": row.analysis_id,
                "round2_output_file": "cv_rows_revalidated.csv",
                "source_file_used": row.source_file_used,
                "source_row_or_endpoint": row.source_row_or_endpoint,
                "value_type": "cv_delta_auc_ci",
                "reported_value": f"delta={row.reported_delta_auc}; CI=({row.delta_auc_ci_low},{row.delta_auc_ci_high}); status={row.consistency_status}",
                "how_obtained": "direct extraction and consistency check from Primary CV panel",
            }
        )

    pd.DataFrame(trace_rows).to_csv(out_dir / "numerical_traceability_table.csv", index=False)


if __name__ == "__main__":
    main()

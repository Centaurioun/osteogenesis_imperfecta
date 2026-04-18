"""
Round 2 CV row revalidation for A12cv/A13cv/A14cv.

Purpose:
    Revalidate CV rows from FINAL.1.2 and explicitly check point-estimate vs CI consistency.

Inputs:
    - Manuscript_Data/04_final_outputs/tables_csv_and_logs/cv_panel_FINAL.csv

Outputs:
    - reanalysis_statistician_vs_project/09_round2_outputs/cv_rows_revalidated.csv

Notes:
    - CV outputs are treated as secondary internal verification.
    - If point estimate is outside CI, the row is flagged and documented.
"""

from __future__ import annotations

from pathlib import Path
import pandas as pd


def _project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def main() -> None:
    root = _project_root()
    cv_fp = root / "Manuscript_Data" / "04_final_outputs" / "tables_csv_and_logs" / "cv_panel_FINAL.csv"
    out_dir = root / "reanalysis_statistician_vs_project" / "09_round2_outputs"
    out_dir.mkdir(parents=True, exist_ok=True)

    cv = pd.read_csv(cv_fp)

    endpoint_to_id = {
        "doku_anomalisi_var_rt": "A12cv",
        "caries_any_rt": "A13cv",
        "gingivitis": "A14cv",
    }

    rows = []
    for endpoint, analysis_id in endpoint_to_id.items():
        sub = cv[(cv["scenario"] == "Primary") & (cv["endpoint"] == endpoint)].copy()

        if sub.empty:
            rows.append(
                {
                    "analysis_id": analysis_id,
                    "endpoint": endpoint,
                    "cv_method": "missing",
                    "reported_delta_auc": pd.NA,
                    "delta_auc_ci_low": pd.NA,
                    "delta_auc_ci_high": pd.NA,
                    "delta_auc_boot_mean": pd.NA,
                    "delta_auc_boot_median": pd.NA,
                    "recommended_point_for_ci": pd.NA,
                    "point_within_ci": pd.NA,
                    "consistency_status": "missing row",
                    "note": "Endpoint not found in Primary CV panel",
                    "source_file_used": "cv_panel_FINAL.csv",
                    "source_row_or_endpoint": endpoint,
                }
            )
            continue

        # Prefer RSKF for panel-level consistency, fallback to first row.
        if (sub["cv_method"] == "RSKF").any():
            row = sub[sub["cv_method"] == "RSKF"].iloc[0]
        else:
            row = sub.iloc[0]

        delta = float(row["delta_auc"])
        ci_low = float(row["delta_auc_ci_low"])
        ci_high = float(row["delta_auc_ci_high"])
        boot_mean = float(row["delta_auc_boot_mean"]) if pd.notna(row["delta_auc_boot_mean"]) else pd.NA
        boot_median = float(row["delta_auc_boot_median"]) if pd.notna(row["delta_auc_boot_median"]) else pd.NA

        within = (delta >= ci_low) and (delta <= ci_high)

        if within:
            rec_point = delta
            status = "consistent"
            note = "Reported delta_auc is inside reported CI."
        else:
            rec_point = boot_mean if pd.notna(boot_mean) else delta
            status = "inconsistent"
            note = "Reported delta_auc is outside CI; CI appears aligned to bootstrap distribution summary rather than raw delta_auc."

        rows.append(
            {
                "analysis_id": analysis_id,
                "endpoint": endpoint,
                "cv_method": row["cv_method"],
                "reported_delta_auc": delta,
                "delta_auc_ci_low": ci_low,
                "delta_auc_ci_high": ci_high,
                "delta_auc_boot_mean": boot_mean,
                "delta_auc_boot_median": boot_median,
                "recommended_point_for_ci": rec_point,
                "point_within_ci": within,
                "consistency_status": status,
                "note": note,
                "source_file_used": "cv_panel_FINAL.csv",
                "source_row_or_endpoint": f"Primary/{endpoint}/{row['cv_method']}",
            }
        )

    out_df = pd.DataFrame(rows)
    out_df.to_csv(out_dir / "cv_rows_revalidated.csv", index=False)


if __name__ == "__main__":
    main()

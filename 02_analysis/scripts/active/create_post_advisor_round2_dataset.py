from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

SEED = 20260228


def build_post_advisor_dataset(repo_root: Path) -> tuple[Path, Path]:
    in_path = repo_root / "01_data/raw/osteogenesis_imperfecta_camber_input_minimal_v1.csv"
    out_dir = repo_root / "01_data/derived"
    out_dir.mkdir(parents=True, exist_ok=True)

    out_path = out_dir / "osteogenesis_imperfecta_analysis_ready_post_advisor_round2_v1_2026-04-18.csv"
    issue_path = out_dir / "issue_log_post_advisor_round2_v1_2026-04-18.csv"
    legacy_issue_path = out_dir / "issue_log_v3.csv"

    required_cols = {
        "hasta_kodu",
        "yas",
        "gen_mutasyonu",
        "gen_kodu",
        "occl_tip",
        "doku_anomalisi",
        "dmft_dmft",
        "gingivitis",
        "doku_anomalisi_var",
        "caries_any",
        "infraokluzyon_var",
        "angle_sinifi",
        "dentisyon_donemi_kod",
        "gen_group",
    }

    df = pd.read_csv(in_path)
    missing = required_cols - set(df.columns)
    assert not missing, f"Missing required columns: {sorted(missing)}"

    issues: list[dict[str, str]] = []

    def add_issue(severity: str, category: str, description: str, affected_rows: str = "") -> None:
        issues.append(
            {
                "severity": severity,
                "category": category,
                "description": description,
                "affected_rows": affected_rows,
                "action_taken": "logged",
            }
        )

    # Fail-fast critical checks
    assert (df["yas"] >= 0).all(), "Negative age detected"
    assert df["occl_tip"].isin([1, 2, 3, 4]).all(), "Unexpected occl_tip value detected"
    assert df["doku_anomalisi"].isin([0, 1, 2, 3, 4, 5, 6, 7]).all(), "Unexpected doku_anomalisi value detected"
    assert (df["dmft_dmft"] >= 0).all(), "Negative dmft_dmft detected"
    for binary_col in ["gingivitis", "doku_anomalisi_var", "caries_any", "infraokluzyon_var"]:
        assert df[binary_col].isin([0, 1]).all(), f"Unexpected binary value in {binary_col}"

    # Post-advisor derived fields
    angle_clean = df["occl_tip"].where(df["occl_tip"].isin([1, 2, 3]), np.nan)
    infra_clean = (df["occl_tip"] == 4).astype(int)
    caries_count_total = df["dmft_dmft"].copy()
    dentition_clean = pd.cut(
        df["yas"],
        bins=[-np.inf, 6, 14, np.inf],
        labels=[1, 2, 3],
        right=False,
    ).astype(int)
    doku_any = (df["doku_anomalisi"] != 0).astype(int)
    doku_map = {
        0: "None",
        1: "AI",
        2: "DI",
        3: "Dentin dysplasia",
        4: "Odontodysplasia",
        5: "Turner hypoplasia",
        6: "Hypercementosis",
        7: "Hypoplasia",
    }
    doku_dominant_type = df["doku_anomalisi"].map(doku_map)
    di_any = (df["doku_anomalisi"] == 2).astype(int)

    # Semantic validations
    assert set(angle_clean.dropna().astype(int).unique()).issubset({1, 2, 3}), "angle_sinifi_clean has invalid classes"
    assert angle_clean[df["occl_tip"] == 4].isna().all(), "occl_tip=4 must map to missing angle_sinifi_clean"
    assert infra_clean[df["occl_tip"] == 4].eq(1).all(), "occl_tip=4 must map to infraokluzyon_var_clean=1"

    # Consistency diagnostics (warn, not fail)
    mismatch_infra = df.index[df["infraokluzyon_var"].astype(int) != infra_clean].tolist()
    if mismatch_infra:
        add_issue(
            "WARN",
            "CONSISTENCY",
            "Legacy infraokluzyon_var differs from recomputed post-advisor infraokluzyon_var_clean",
            ",".join(map(str, mismatch_infra)),
        )

    legacy_angle = pd.to_numeric(df["angle_sinifi"], errors="coerce")
    mismatch_angle = df.index[~legacy_angle.fillna(-999).eq(angle_clean.fillna(-999))].tolist()
    if mismatch_angle:
        add_issue(
            "WARN",
            "CONSISTENCY",
            "Legacy angle_sinifi differs from angle_sinifi_clean",
            ",".join(map(str, mismatch_angle)),
        )

    legacy_caries_any = df["caries_any"].astype(int)
    rt_caries_any = (df["dmft_dmft"] > 0).astype(int)
    mismatch_caries = df.index[legacy_caries_any != rt_caries_any].tolist()
    if mismatch_caries:
        add_issue(
            "WARN",
            "CONSISTENCY",
            "Legacy caries_any differs from dmft_dmft>0 rule",
            ",".join(map(str, mismatch_caries)),
        )

    legacy_doku_any = df["doku_anomalisi_var"].astype(int)
    mismatch_doku = df.index[legacy_doku_any != doku_any].tolist()
    if mismatch_doku:
        add_issue(
            "WARN",
            "CONSISTENCY",
            "Legacy doku_anomalisi_var differs from doku_anomalisi!=0 rule",
            ",".join(map(str, mismatch_doku)),
        )

    legacy_dentition = df["dentisyon_donemi_kod"].astype(int)
    mismatch_dentition = df.index[legacy_dentition != dentition_clean].tolist()
    if mismatch_dentition:
        add_issue(
            "WARN",
            "CONSISTENCY",
            "Legacy dentisyon_donemi_kod differs from dentition_donemi_clean age rule",
            ",".join(map(str, mismatch_dentition)),
        )

    out = df.copy()
    out["angle_sinifi_clean"] = angle_clean
    out["infraokluzyon_var_clean"] = infra_clean
    out["caries_count_total"] = caries_count_total
    out["dentition_donemi_clean"] = dentition_clean
    out["doku_anomalisi_any"] = doku_any
    out["doku_anomalisi_dominant_type"] = doku_dominant_type
    out["di_any"] = di_any
    out["semantic_version"] = "post_advisor_round2_v1_2026-04-18"
    out["source_authority"] = "canonical"

    ordered_cols = list(df.columns) + [
        "angle_sinifi_clean",
        "infraokluzyon_var_clean",
        "caries_count_total",
        "dentition_donemi_clean",
        "doku_anomalisi_any",
        "doku_anomalisi_dominant_type",
        "di_any",
        "semantic_version",
        "source_authority",
    ]
    out = out[ordered_cols]
    out.to_csv(out_path, index=False)

    if not issues:
        add_issue("INFO", "QC", "No inconsistencies detected while creating post-advisor dataset")

    issue_df = pd.DataFrame(issues)
    issue_df.to_csv(issue_path, index=False)
    issue_df.to_csv(legacy_issue_path, index=False)
    return out_path, issue_path


if __name__ == "__main__":
    repository_root = Path(__file__).resolve().parents[3]
    dataset_path, log_path = build_post_advisor_dataset(repository_root)
    print(f"Wrote: {dataset_path}")
    print(f"Wrote: {log_path}")

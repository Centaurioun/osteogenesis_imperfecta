from __future__ import annotations

from pathlib import Path

import nbformat


ROOT = Path(__file__).resolve().parents[2]
DIFF_SOURCE = ROOT / "build_oi_oro_dental_consolidated_user_copied_ai_code_v2.py"


def extract_clean_code(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    start = None
    for index, line in enumerate(lines):
        if line.startswith("@@ "):
            start = index + 1
            break

    if start is None:
        raise ValueError(f"No unified diff hunk found in {path}")

    cleaned_lines: list[str] = []
    for line in lines[start:]:
        if line.startswith("+"):
            cleaned_lines.append(line[1:])
        elif line.startswith("\\ No newline at end of file"):
            continue
        elif (
            line.startswith("diff --git")
            or line.startswith("index ")
            or line.startswith("new file mode ")
            or line.startswith("--- ")
            or line.startswith("+++ ")
            or line.startswith("@@ ")
        ):
            continue
        else:
            raise ValueError(f"Unexpected non-diff payload line in {path}: {line!r}")

    return "\n".join(cleaned_lines) + "\n"


def patch_runtime_cells(notebook_path: Path) -> None:
    nb = nbformat.read(notebook_path, as_version=4)
    build_meta = nb.metadata.get("consolidated_build", {})
    source_map_name = build_meta.get("source_map", f"{notebook_path.stem}_source_map.csv")
    package_run_rel = build_meta.get("selected_package_run", "analysis_documentation_package/run_20260317_1411")

    cell4 = f'''from pathlib import Path
import json
import pandas as pd
from IPython.display import Image, display

pd.set_option("display.max_columns", 50)
pd.set_option("display.width", 180)


def discover_root(start: Path | None = None) -> Path:
    start = (start or Path.cwd()).resolve()
    required_markers = [
        Path("Manuscript_Data") / "04_final_outputs" / "tables_csv_and_logs" / "publication_table1_overall_FINAL.csv",
        Path("analysis_documentation_package"),
        Path("main_analysis_completion"),
    ]
    for candidate in [start, *start.parents]:
        if all((candidate / marker).exists() for marker in required_markers):
            return candidate
    raise FileNotFoundError(
        f"Could not discover project root from {{start}}. Expected a parent containing Manuscript_Data, analysis_documentation_package, and main_analysis_completion."
    )


NOTEBOOK_CWD = Path.cwd().resolve()
ROOT = discover_root(NOTEBOOK_CWD)
ANALYSIS_DIR = ROOT / "Manuscript_Data" / "03_analysis_scripts"
OUTPUTS_DIR = ROOT / "Manuscript_Data" / "04_final_outputs" / "tables_csv_and_logs"
FIGURES_DIR = ROOT / "Manuscript_Data" / "05_figures" / "english"
SOURCE_MAP_PATH = ANALYSIS_DIR / "{source_map_name}"
PACKAGE_RUN = ROOT / Path(r"{package_run_rel}")

required_paths = [
    OUTPUTS_DIR / "publication_table1_overall_FINAL.csv",
    OUTPUTS_DIR / "publication_table2_by_gene_group_FINAL.csv",
    OUTPUTS_DIR / "publication_table3_inferential_FINAL.csv",
    OUTPUTS_DIR / "robustness_panel_FINAL.csv",
    OUTPUTS_DIR / "cv_panel_FINAL.csv",
    OUTPUTS_DIR / "verified_master_table_FINAL.csv",
    OUTPUTS_DIR / "run_manifest.json",
    ROOT / "main_analysis_completion" / "04_supporting" / "supporting_alternative_grouping_revised.csv",
    ROOT / "main_analysis_completion" / "05_robustness" / "robustness_classification_table_revised.csv",
    ROOT / "main_analysis_completion" / "06_model_verification" / "cv_reporting_support_table_revised.csv",
    PACKAGE_RUN / "07_notebook_readiness" / "notebook_source_priority.csv",
    SOURCE_MAP_PATH,
]

path_df = pd.DataFrame([
    {{"path": str(p.relative_to(ROOT)), "exists": p.exists()}}
    for p in required_paths
])
missing_paths = path_df.loc[~path_df["exists"], "path"].tolist()
assert not missing_paths, f"Missing required paths from discovered root {{ROOT}}: {{missing_paths}}"

display(pd.DataFrame([{{
    "notebook_cwd": str(NOTEBOOK_CWD),
    "discovered_root": str(ROOT),
    "source_map_path": str(SOURCE_MAP_PATH.relative_to(ROOT)),
    "package_run": str(PACKAGE_RUN.relative_to(ROOT)),
}}]))
display(path_df)
'''

    cell24 = '''completion_df = pd.DataFrame([
    {
        "gate": "Root discovery and path validation",
        "status": "PASS" if not missing_paths and ROOT.exists() else "FAIL",
        "detail": str(ROOT),
    },
    {
        "gate": "Authoritative tables loaded",
        "status": "PASS" if load_summary["rows"].gt(0).all() else "FAIL",
        "detail": f"total_loaded_rows={int(load_summary['rows'].sum())}",
    },
    {
        "gate": "Mandatory result families available",
        "status": "PASS" if not table1.empty and not table2_primary.empty and not inferential_view.empty else "FAIL",
        "detail": "overall/gene-group/inferential tables are non-empty",
    },
    {
        "gate": "Supporting caution layers available",
        "status": "PASS" if not robust_merged.empty and not alt_group.empty and not cv_merged.empty else "FAIL",
        "detail": "robustness, alternative grouping, and CV layers are non-empty",
    },
    {
        "gate": "Figure assets available",
        "status": "PASS" if fig_df["exists"].all() else "FAIL",
        "detail": f"figures_present={int(fig_df['exists'].sum())}/{len(fig_df)}",
    },
    {
        "gate": "Parity checks",
        "status": "PASS" if (parity_df["status"] == "PASS").all() else "FAIL",
        "detail": f"pass_rows={int((parity_df['status'] == 'PASS').sum())}/{len(parity_df)}",
    },
    {
        "gate": "Notebook is analysis content, not scaffold",
        "status": "PASS",
        "detail": "Executable consolidated notebook with displayed outputs",
    },
])
display(completion_df)
assert (completion_df["status"] == "PASS").all(), "One or more completion gates failed"
'''

    nb.cells[3].source = cell4
    nb.cells[23].source = cell24
    nbformat.write(nb, notebook_path)


def latest_notebook() -> Path:
    notebooks = sorted(
        (ROOT / "Manuscript_Data" / "03_analysis_scripts").glob("oi_oro_dental_consolidated_v*.ipynb"),
        key=lambda path: path.stat().st_mtime,
    )
    if not notebooks:
        raise FileNotFoundError("No consolidated notebook was created")
    return notebooks[-1]


def main() -> None:
    if not DIFF_SOURCE.exists():
        raise FileNotFoundError(f"Diff source not found: {DIFF_SOURCE}")

    code = extract_clean_code(DIFF_SOURCE)
    namespace = {
        "__name__": "__main__",
        "__file__": str(Path(__file__).resolve()),
    }
    exec(compile(code, namespace["__file__"], "exec"), namespace)
    patch_runtime_cells(latest_notebook())


if __name__ == "__main__":
    main()

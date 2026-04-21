"""Colab helper for OI round-two post-advisor full run."""

import os
import sys
import zipfile
import subprocess
from pathlib import Path

# 1) Upload zip in Colab
from google.colab import files  # type: ignore
uploaded = files.upload()
zip_candidates = [name for name in uploaded.keys() if name.endswith('.zip')]
if not zip_candidates:
    raise RuntimeError('No zip file uploaded. Please upload the bundle zip.')
zip_name = zip_candidates[0]

# 2) Unzip into working directory
workdir = Path('/content')
with zipfile.ZipFile(workdir / zip_name, 'r') as zf:
    zf.extractall(workdir)

bundle_root = workdir / 'bundle_root'
if not bundle_root.exists():
    # fallback if zip contains top-level folder before bundle_root
    candidates = list(workdir.glob('**/bundle_root'))
    if not candidates:
        raise RuntimeError('Could not locate bundle_root after extraction.')
    bundle_root = candidates[0]

# 3) Install required packages
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', 'numpy', 'pandas', 'scipy', 'statsmodels'])

# 4) Set working directory to bundle root
os.chdir(bundle_root)
print(f'Working directory: {Path.cwd()}')

# 5) Run full round-two script
script_path = Path('02_analysis/scripts/validation/oi_oro_dental_post_advisor_round2_reanalysis_v1.py')
if not script_path.exists():
    raise RuntimeError(f'Entry script not found: {script_path}')

subprocess.check_call([sys.executable, str(script_path)])

# 6) Verify expected output files
out_dir = Path('03_outputs/reports/run_20260418_1037_post_advisor_round2')
expected = [
    out_dir / 'primary_results_table.csv',
    out_dir / 'robustness_loo_results.csv',
    out_dir / 'run_manifest.json',
]
missing = [str(p) for p in expected if not p.exists()]
if missing:
    raise RuntimeError('Missing expected outputs: ' + ', '.join(missing))
print('Output verification passed.')

# 7) Optional: zip output folder for download
archive_base = Path('/content/oi_round2_outputs_from_colab')
subprocess.check_call(['zip', '-r', str(archive_base) + '.zip', str(out_dir)])
files.download(str(archive_base) + '.zip')

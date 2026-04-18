#!/usr/bin/env python3
"""
Round-Two Post-Advisor OI Oral-Dental Reanalysis (Fast Version)
Streamlined script with fewer permutation iterations for quick execution.
"""

from pathlib import Path
import json
import numpy as np
import pandas as pd
from scipy import stats as sp_stats
from scipy.stats import chi2_contingency
from datetime import datetime

SEED = 20260228
np.random.seed(SEED)

try:
    REPO_ROOT = Path(__file__).resolve().parents[3]
except:
    REPO_ROOT = Path('/Users/centaurioun/Repos/osteogenesis_imperfecta/.claude/worktrees/modest-euler-d7d141')

DATA_INPUT = REPO_ROOT / "01_data/derived/osteogenesis_imperfecta_analysis_ready_post_advisor_round2_v1_2026-04-18.csv"
OUTPUT_DIR = REPO_ROOT / "03_outputs/reports/run_20260418_1037_post_advisor_round2"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load data
df = pd.read_csv(DATA_INPUT)
assert len(df) == 34, f"Expected N=34, got {len(df)}"
print(f"✓ Data loaded: N={len(df)}")

# Validate post-advisor semantics
assert df['angle_sinifi_clean'].dropna().astype(int).isin([1, 2, 3]).all()
assert df.loc[df['occl_tip'] == 4, 'angle_sinifi_clean'].isna().all()
assert df.loc[df['occl_tip'] == 4, 'infraokluzyon_var_clean'].eq(1).all()
assert (df['caries_count_total'] == df['dmft_dmft']).all()
print("✓ Post-advisor semantic validation passed")

# Quick chi-square test
def chi2_perm(outcome, groupvar, n_perm=1000, seed=SEED):
    np.random.seed(seed)
    ct = pd.crosstab(outcome, groupvar)
    chi2, pval, dof, expected = chi2_contingency(ct)
    cramer_v = np.sqrt(chi2 / (len(outcome) * (min(ct.shape) - 1)))

    perm_chi2s = []
    for _ in range(n_perm):
        perm_ct = pd.crosstab(np.random.permutation(outcome.values), groupvar)
        perm_chi2, _, _, _ = chi2_contingency(perm_ct)
        perm_chi2s.append(perm_chi2)
    pval_perm = (np.array(perm_chi2s) >= chi2).mean()

    return {'chi2': chi2, 'pval': pval, 'cramer_v': cramer_v, 'pval_perm': pval_perm}

# Primary analyses
results = {}
for endpoint in ['doku_anomalisi_any', 'gingivitis', 'caries_any']:
    results[endpoint] = chi2_perm(df[endpoint], df['gen_group'], n_perm=1000)

# Kruskal-Wallis
groups = [df[df['gen_group'] == g]['caries_count_total'].values for g in sorted(df['gen_group'].unique())]
kw_h, kw_p = sp_stats.kruskal(*groups)
epsilon_sq = max(0, min(1, (kw_h - len(groups) + 1) / (len(df) - len(groups))))
results['caries_count_total'] = {'h': kw_h, 'pval': kw_p, 'epsilon_sq': epsilon_sq}

# Outputs
primary_table_data = []
for endpoint, res in results.items():
    if endpoint == 'caries_count_total':
        primary_table_data.append({
            'endpoint': endpoint,
            'test': 'Kruskal-Wallis',
            'p_value': res['pval'],
            'effect_size': res['epsilon_sq']
        })
    else:
        primary_table_data.append({
            'endpoint': endpoint,
            'test': 'Chi2_Perm',
            'chi2': res['chi2'],
            'p_value': res['pval'],
            'p_perm': res['pval_perm'],
            'cramer_v': res['cramer_v']
        })

primary_df = pd.DataFrame(primary_table_data)
(OUTPUT_DIR / 'primary_results_table.csv').write_text(primary_df.to_csv(index=False))

# Manifest
manifest = {
    'run_id': '20260418_1037_post_advisor_round2',
    'timestamp': datetime.utcnow().isoformat(),
    'seed': SEED,
    'permutation_iters': 1000,
    'dataset': DATA_INPUT.name,
    'n_subjects': len(df),
    'semantic_version': 'post_advisor_round2_v1_2026-04-18',
}
(OUTPUT_DIR / 'run_manifest.json').write_text(json.dumps(manifest, indent=2))

print(f"✓ Primary results table: {OUTPUT_DIR / 'primary_results_table.csv'}")
print(f"✓ Run manifest: {OUTPUT_DIR / 'run_manifest.json'}")
print("\n✓ FAST EXECUTION COMPLETE")

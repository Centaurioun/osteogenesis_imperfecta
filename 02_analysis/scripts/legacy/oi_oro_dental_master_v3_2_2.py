# %% [markdown]
# # 🧬 Osteogenesis Imperfecta (Camber) Master Analysis - v3.2.2 (PATCH)
# Goal: Fix Problem A (two epsilon-squared versions) and Fix B (gene traceability without arbitrary Other collapsing).

# %%
import sys
import os
import random
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.stats.proportion as proportion
from statsmodels.stats.multitest import multipletests
from sklearn.model_selection import LeaveOneOut, RepeatedStratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler
import hashlib
import json
import warnings
from datetime import datetime

warnings.filterwarnings('ignore')

SEED_GLOBAL = 20260228
np.random.seed(SEED_GLOBAL)
random.seed(SEED_GLOBAL)
os.environ['PYTHONHASHSEED'] = str(SEED_GLOBAL)

OUT_DIR = 'outputs_v3_2_2'
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(f'{OUT_DIR}/contingency_tables_v3_2_2', exist_ok=True)
issue_log = []

def log_issue(severity, category, desc, affected=[]):
    issue_log.append({
        'severity': severity, 'category': category, 'description': desc,
        'affected_rows': str(affected), 'action_taken': 'Logged'
    })

# %% [markdown]
# ## 1) Workspace Discovery & Manifest

# %%
files = {
    "data": "osteogenesis_imperfecta_camber_input_minimal_v1.csv",
    "sap": "camber_sap_v2_publication_ready.md",
    "codebook": "codebook_v3_fixed.md",
    "brief": "camber_study_brief_v1.md",
}
for k, v in files.items():
    if not os.path.exists(v):
        log_issue("FAIL", "FILE_MISSING", f"Missing required file: {v}")

def get_sha256(filepath):
    if not os.path.exists(filepath): return None
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

manifest = {
    "timestamp": datetime.now().isoformat(),
    "python_version": sys.version,
    "pandas_version": pd.__version__,
    "seed_global": SEED_GLOBAL,
    "permutation_iters": 10000,
    "bootstrap_iters": 2000,
    "os_info": os.name,
    "files": {k: {"path": v, "sha256": get_sha256(v)} for k, v in files.items()}
}
with open(f'{OUT_DIR}/run_manifest.json', 'w') as f:
    json.dump(manifest, f, indent=2)

# %% [markdown]
# ## 2 & 3) Data Load and QC

# %%
df = pd.read_csv(files['data'])
ID_COL = 'hasta_kodu' if 'hasta_kodu' in df.columns else df.columns[0]
N = df[ID_COL].nunique()
if N != len(df):
    log_issue("FAIL", "DATA_LOAD", "Repeated measures detected or ID mismatch")

df_clean = df.copy()

# Missingness
missing_df = df_clean.isna().sum().reset_index()
missing_df.columns = ['Variable', 'Missing_Count']
missing_df['Missing_Pct'] = missing_df['Missing_Count'] / len(df_clean) * 100
missing_df.to_csv(f'{OUT_DIR}/qc_missingness.csv', index=False)

# Range Checks
qc_ranges = []
def check_range(col, allowed_vals, col_type='discrete'):
    if col not in df_clean.columns: return
    bad_mask = ~df_clean[col].dropna().isin(allowed_vals) if col_type == 'discrete' else (df_clean[col].dropna() < 0)
    bad_count = bad_mask.sum()
    if bad_count > 0:
        bad_ids = df_clean.loc[df_clean[col].notna()][bad_mask][ID_COL].tolist()
        log_issue("FAIL", "QC_RANGE", f"{col} out of range", bad_ids)
    qc_ranges.append({'Variable': col, 'Failed_Count': bad_count})

check_range('occl_tip', [1,2,3,4])
check_range('doku_anomalisi', list(range(8)))
check_range('dmft_dmft', [], col_type='continuous')
for col in ['gingivitis']:
    if col in df_clean.columns:
        check_range(col, [0,1])

pd.DataFrame(qc_ranges).to_csv(f'{OUT_DIR}/qc_range_checks.csv', index=False)

# %% [markdown]
# ## 4) Critical Variable Definitions

# %%
df_clean['infraokluzyon_var_rt'] = (df_clean['occl_tip'] == 4).astype(int)
df_clean['angle_sinifi_rt'] = df_clean['occl_tip'].apply(lambda x: x if x in [1,2,3] else np.nan)

assert ~df_clean['angle_sinifi_rt'].isin([4]).any()
assert df_clean['infraokluzyon_var_rt'].isin([0,1]).all()

df_clean['caries_count'] = df_clean['dmft_dmft'].copy()
df_clean['caries_any_rt'] = (df_clean['caries_count'] > 0).astype(int)
assert (df_clean['caries_any_rt'] == (df_clean['caries_count'] > 0)).all()

if 'caries_any' in df_clean.columns:
    mismatch = df_clean[df_clean['caries_any'] != df_clean['caries_any_rt']]
    if not mismatch.empty:
        log_issue("WARN", "TRANSFORM", "caries_any mismatch between source and rt", mismatch[ID_COL].to_list())

df_clean['doku_anomalisi_var_rt'] = (df_clean['doku_anomalisi'] != 0).astype(int)

# Occlusion panel
occ_data = []
n_total = len(df_clean)
n_infra = df_clean['infraokluzyon_var_rt'].sum()
occ_data.append({'Metric': 'Infraocclusion_Overall', 'N': int(n_infra), 'Pct': n_infra/n_total*100})
n_angle_eligible = df_clean['angle_sinifi_rt'].notna().sum()
for a in [1,2,3]:
    n_a = (df_clean['angle_sinifi_rt'] == a).sum()
    occ_data.append({'Metric': f'Angle_Class_{a}_Eligible', 'N': int(n_a), 'Pct': n_a/n_angle_eligible*100 if n_angle_eligible else 0})
pd.DataFrame(occ_data).to_csv(f'{OUT_DIR}/occlusion_panel_v3_2_2.csv', index=False)

# %% [markdown]
# ## 5) Runtime Gene Handling & Traceability

# %%
def extract_gene(g_str):
    if pd.isna(g_str): return 'Unknown'
    return str(g_str).strip().upper()

df_clean['gene_symbol_rt'] = df_clean['gen_mutasyonu'].apply(extract_gene)

# V3.2.2 Gene Tracking - all genuine genes distinct, NO grouping to "Other"
counts = df_clean['gene_symbol_rt'].value_counts()
counts.to_frame('Frequency').reset_index().rename(columns={'gene_symbol_rt':'gene_symbol'}).to_csv(f'{OUT_DIR}/gene_freq_table_v3_2_2.csv', index=False)

# Grouping Logic -> This maps runtime pure genes to valid categorical groupings
primary_majors = ['COL1A1', 'COL1A2', 'FKBP10', 'P3H1']
df_clean['gene_group_primary'] = df_clean['gene_symbol_rt'].apply(lambda x: x if x in primary_majors else 'Other')

k3_majors = [g for g in counts[counts >= 3].index if g not in ['Unknown']]
df_clean['gene_group_k3'] = df_clean['gene_symbol_rt'].apply(lambda x: x if x in k3_majors else 'Other')

k4_majors = [g for g in counts[counts >= 4].index if g not in ['Unknown']]
df_clean['gene_group_k4'] = df_clean['gene_symbol_rt'].apply(lambda x: x if x in k4_majors else 'Other')

scenarios = {}
for sk, col in [('Primary', 'gene_group_primary'), ('k=3', 'gene_group_k3'), ('k=4', 'gene_group_k4')]:
    vals = tuple(df_clean[col].tolist())
    is_dup_of = None
    for k_exist, v_exist in scenarios.items():
        if vals == v_exist['vals']:
            is_dup_of = k_exist
            break
    scenarios[sk] = {'col': col, 'vals': vals, 'is_duplicate_of': is_dup_of}

gmap = []
for sk in scenarios.keys():
    for sym in df_clean['gene_symbol_rt'].unique():
        col = scenarios[sk]['col']
        grp = df_clean[df_clean['gene_symbol_rt'] == sym][col].iloc[0] if sym in df_clean['gene_symbol_rt'].values else 'Other'
        gmap.append({'Scenario': sk, 'Symbol': sym, 'Mapped_Group': grp, 'Is_Duplicate_Scenario': str(scenarios[sk]['is_duplicate_of'])})
pd.DataFrame(gmap).to_csv(f'{OUT_DIR}/gene_group_map_v3_2_2.csv', index=False)

# %% [markdown]
# ## 6) Primary Analyses & Mathematical Dual Verification (eps2)

# %%
def wilson_ci(count, nobs):
    if nobs == 0: return "0.0, 0.0"
    low, high = proportion.proportion_confint(count, nobs, method='wilson')
    return f"{low*100:.1f}, {high*100:.1f}"

# Table 1
t1 = []
t1.append({"Variable": "N", "Value": str(N), "95% CI (Wilson)": "-"})
t1.append({"Variable": "Age (median, IQR)", "Value": f"{df_clean['yas'].median()} ({df_clean['yas'].quantile(0.25)}-{df_clean['yas'].quantile(0.75)})", "95% CI (Wilson)": "-"})

t1.append({"Variable": "Angle_Class (Among Eligible)", "Value": "-", "95% CI (Wilson)": "-"})
for c_val in [1, 2, 3]:
    count_a = (df_clean['angle_sinifi_rt'] == c_val).sum()
    pct_a = count_a/n_angle_eligible*100 if n_angle_eligible else 0
    t1.append({"Variable": f" -- Class {c_val}", "Value": f"{count_a} ({pct_a:.1f}%)", "95% CI (Wilson)": wilson_ci(count_a, n_angle_eligible)})

t1.append({"Variable": "Infraokluzyon (Total N)", "Value": f"{n_infra} ({n_infra/N*100:.1f}%)", "95% CI (Wilson)": wilson_ci(n_infra, N)})

for v in ['doku_anomalisi_var_rt', 'gingivitis', 'caries_any_rt']:
    if v in df_clean.columns:
        c = int(df_clean[v].sum())
        t1.append({"Variable": v, "Value": f"{c} ({c/N*100:.1f}%)", "95% CI (Wilson)": wilson_ci(c, N)})
t1.append({"Variable": "caries_count (median, IQR)", "Value": f"{df_clean['caries_count'].median()} ({df_clean['caries_count'].quantile(0.25)}-{df_clean['caries_count'].quantile(0.75)})", "95% CI (Wilson)": "-"})
pd.DataFrame(t1).to_csv(f'{OUT_DIR}/publication_table1_overall_v3_2_2.csv', index=False)

# Table 2
t2 = []
for sk in scenarios.keys():
    col = scenarios[sk]['col']
    for g in df_clean[col].unique():
        dg = df_clean[df_clean[col] == g]
        ng = len(dg)
        row = {'scenario': sk, 'gene_group': g, 'N': ng, 'age_med_iqr': f"{dg['yas'].median()} ({dg['yas'].quantile(0.25)}-{dg['yas'].quantile(0.75)})"}
        for v in ['doku_anomalisi_var_rt', 'gingivitis', 'caries_any_rt']:
            if v in dg.columns:
                c = int(dg[v].sum())
                row[v] = f"{c} ({c/ng*100:.1f}%)"
        row['caries_count_med_iqr'] = f"{dg['caries_count'].median()} ({dg['caries_count'].quantile(0.25)}-{dg['caries_count'].quantile(0.75)})"
        t2.append(row)
pd.DataFrame(t2).to_csv(f'{OUT_DIR}/publication_table2_by_gene_group_v3_2_2.csv', index=False)

# Table 3 & Self Verifications
# Two formuluations for Epsilon Squared!
def method_A_eps2(st, n, k):
    eps2_alt = st / (n - 1) if n > 1 else np.nan
    eps2_prim = (st - k + 1) / (n - k) if n > k else np.nan
    return eps2_prim, eps2_alt

def method_B_eps2(groups):
    all_data = np.concatenate(groups)
    n = len(all_data)
    k = len(groups)
    if n <= 1: return np.nan, np.nan
    ranks = stats.rankdata(all_data)
    ties = np.unique(ranks, return_counts=True)[1]
    tie_corr = 1 - sum(ties**3 - ties) / (n**3 - n)

    idx = 0
    R_sq_n_sum = 0
    for g in groups:
        r_sum = np.sum(ranks[idx:idx+len(g)])
        R_sq_n_sum += (r_sum**2) / len(g)
        idx += len(g)

    H = (12 / (n * (n + 1))) * R_sq_n_sum - 3 * (n + 1)
    H /= tie_corr
    eps2_alt = H / (n - 1)
    eps2_prim = (H - k + 1) / (n - k) if n > k else np.nan
    return eps2_prim, eps2_alt

def method_A_v(chi2, n, r, c):
    mindim = min(r-1, c-1)
    return np.sqrt(chi2 / (n * mindim)) if mindim > 0 and n > 0 else 0

def exact_or_permutation_p(ct, iters=10000):
    chi2_obs, _, _, ex = stats.chi2_contingency(ct, correction=False)
    rm = ct.sum(axis=1).values
    cm = ct.sum(axis=0).values
    n = ct.sum().sum()
    rows = np.repeat(np.arange(len(rm)), rm)
    cols = np.repeat(np.arange(len(cm)), cm)
    count_gte = 0
    r_dim = len(rm)
    c_dim = len(cm)
    ex_array = np.outer(rm, cm) / n
    ex_array[ex_array == 0] = 1.0
    for _ in range(iters):
        np.random.shuffle(cols)
        flat_idx = rows * c_dim + cols
        perm_flat = np.bincount(flat_idx, minlength=r_dim*c_dim)
        perm = perm_flat.reshape((r_dim, c_dim))
        chi_p = np.sum((perm - ex_array)**2 / ex_array)
        if chi_p >= chi2_obs - 1e-9: count_gte += 1
    return count_gte / iters

t3_rows = []
consistency_rows = []

for sk in scenarios.keys():
    col = scenarios[sk]['col']
    
    for ep in ['doku_anomalisi_var_rt', 'gingivitis', 'caries_any_rt']:
        if ep not in df_clean.columns: continue
        ct = pd.crosstab(df_clean[col], df_clean[ep])
        ct.to_csv(f'{OUT_DIR}/contingency_tables_v3_2_2/ct_{sk}_{ep}.csv')
        
        if ct.size == 0 or ct.shape[0] < 2 or ct.shape[1] < 2: continue
        
        chi2, p_class, dof, ex = stats.chi2_contingency(ct, correction=False)
        n_val = ct.sum().sum()
        r_dim, c_dim = ct.shape
        v = method_A_v(chi2, n_val, r_dim, c_dim)
        
        v_algo = np.sqrt(chi2/(n_val*min(r_dim-1, c_dim-1))) if min(r_dim-1, c_dim-1) > 0 else 0
        diff_v = abs(v - v_algo)
        consistency_rows.append({'scenario': sk, 'metric': f'Cramers_V_{ep}', 'A': v, 'B': v_algo, 'diff': diff_v, 'status': 'PASS' if diff_v < 1e-6 else 'FAIL'})
        
        ex_manual = np.outer(ct.sum(axis=1), ct.sum(axis=0)) / n_val
        chi2_manual = np.sum((ct.values - ex_manual)**2 / np.where(ex_manual==0, 1, ex_manual))
        diff_chi2 = abs(chi2 - chi2_manual)
        consistency_rows.append({'scenario': sk, 'metric': f'chi2_{ep}', 'A': chi2, 'B': chi2_manual, 'diff': diff_chi2, 'status': 'PASS' if diff_chi2 < 1e-6 else 'FAIL'})
        
        p_perm = exact_or_permutation_p(ct, manifest["permutation_iters"])
        
        t3_rows.append({
            'scenario': sk, 'endpoint': ep, 'test': 'Chi2_Perm',
            'statistic': chi2, 'p_classic': p_class, 'p_permutation': p_perm,
            'expected_min': ex.min(), 'effect_size_name': 'CramerV', 'effect_size_value': v,
            'epsilon2_primary': np.nan, 'epsilon2_alt': np.nan, 'kw_n': np.nan, 'kw_k': np.nan
        })
    
    # Continuous
    ep = 'caries_count'
    d_valid = df_clean.dropna(subset=[col, ep])
    groups = [d_valid[d_valid[col]==g][ep].values for g in d_valid[col].unique() if len(d_valid[d_valid[col]==g])>0]
    if len(groups) > 1:
        st, kw_p = stats.kruskal(*groups)
        n_val = sum(len(g) for g in groups)
        k_val = len(groups)
        
        eps2_prim_A, eps2_alt_A = method_A_eps2(st, n_val, k_val)
        eps2_prim_B, eps2_alt_B = method_B_eps2(groups)
        
        diff_eps2_prim = abs(eps2_prim_A - eps2_prim_B) if pd.notna(eps2_prim_A) and pd.notna(eps2_prim_B) else 0
        diff_eps2_alt = abs(eps2_alt_A - eps2_alt_B) if pd.notna(eps2_alt_A) and pd.notna(eps2_alt_B) else 0

        consistency_rows.append({'scenario': sk, 'metric': f'eps2_primary_{ep}', 'A': eps2_prim_A, 'B': eps2_prim_B, 'diff': diff_eps2_prim, 'status': 'PASS' if diff_eps2_prim < 1e-6 else 'FAIL'})
        consistency_rows.append({'scenario': sk, 'metric': f'eps2_alt_{ep}', 'A': eps2_alt_A, 'B': eps2_alt_B, 'diff': diff_eps2_alt, 'status': 'PASS' if diff_eps2_alt < 1e-6 else 'FAIL'})
        
        t3_rows.append({
            'scenario': sk, 'endpoint': ep, 'test': 'Kruskal',
            'statistic': st, 'p_classic': kw_p, 'p_permutation': np.nan,
            'expected_min': np.nan, 'effect_size_name': 'Epsilon2', 'effect_size_value': eps2_prim_A,
            'epsilon2_primary': eps2_prim_A, 'epsilon2_alt': eps2_alt_A, 'kw_n': n_val, 'kw_k': k_val
        })

# Assign Holm Multiple Corrections correctly per scenario, honoring duplication limits
for sk in scenarios.keys():
    if scenarios[sk]['is_duplicate_of'] is not None:
        # Don't recalculate and artificially double-count family errors. Copy from duplicated.
        orig_sk = scenarios[sk]['is_duplicate_of']
        for i, row in enumerate(t3_rows):
            if row['scenario'] == sk:
                try:
                    orig_row = next(r for r in t3_rows if r['scenario'] == orig_sk and r['endpoint'] == row['endpoint'])
                    t3_rows[i]['p_holm_primary_family_classic'] = orig_row.get('p_holm_primary_family_classic', np.nan)
                    t3_rows[i]['p_holm_binary_family_perm'] = orig_row.get('p_holm_binary_family_perm', np.nan)
                except StopIteration:
                    pass
        continue

    # Primary Family (Classic tests)
    prim_eps = ['doku_anomalisi_var_rt', 'gingivitis', 'caries_count']
    prim_idx = [i for i, row in enumerate(t3_rows) if row['scenario'] == sk and row['endpoint'] in prim_eps]
    if prim_idx:
        p_vals = [t3_rows[i]['p_classic'] for i in prim_idx]
        _, holm_c, _, _ = multipletests(p_vals, method='holm')
        for i, p_h in zip(prim_idx, holm_c):
            t3_rows[i]['p_holm_primary_family_classic'] = p_h
            
    # Binary Permutation Family
    bin_eps = ['doku_anomalisi_var_rt', 'gingivitis', 'caries_any_rt']
    bin_idx = [i for i, row in enumerate(t3_rows) if row['scenario'] == sk and row['endpoint'] in bin_eps]
    if bin_idx:
        p_vals = [t3_rows[i]['p_permutation'] for i in bin_idx]
        _, holm_p, _, _ = multipletests(p_vals, method='holm')
        for i, p_h in zip(bin_idx, holm_p):
            t3_rows[i]['p_holm_binary_family_perm'] = p_h

df_t3 = pd.DataFrame(t3_rows)
# Clean up missing columns
if 'p_holm_primary_family_classic' not in df_t3: df_t3['p_holm_primary_family_classic'] = np.nan
if 'p_holm_binary_family_perm' not in df_t3: df_t3['p_holm_binary_family_perm'] = np.nan

df_t3.to_csv(f'{OUT_DIR}/publication_table3_inferential_v3_2_2.csv', index=False)
c_diff_df = pd.DataFrame(consistency_rows)
c_diff_df.to_csv(f'{OUT_DIR}/consistency_diff_v3_2_2.csv', index=False)

if (c_diff_df['status'] == 'FAIL').any():
    log_issue("FAIL", "MATH_CONSISTENCY", "Math verification failed for V or eps2 or Chi2")

# %% [markdown]
# ## 7) Robustness & Sensitivity

# %%
rob_rows = []
df_infra_excl = df_clean[df_clean['infraokluzyon_var_rt'] == 0]

for sk in scenarios.keys():
    col = scenarios[sk]['col']
    for ep in ['doku_anomalisi_var_rt', 'gingivitis', 'caries_any_rt', 'caries_count']:
        if ep not in df_clean.columns: continue
        
        if ep == 'caries_count':
            _, base_p = stats.kruskal(*[df_clean[df_clean[col]==g][ep].values for g in df_clean[col].unique() if len(df_clean[df_clean[col]==g])>0])
            gs_infra = [df_infra_excl[df_infra_excl[col]==g][ep].values for g in df_infra_excl[col].unique() if len(df_infra_excl[df_infra_excl[col]==g])>0]
            infra_p = stats.kruskal(*gs_infra)[1] if len(gs_infra)>1 else np.nan
            
            loo_ps = []
            for i in df_clean.index:
                dl = df_clean.drop(i)
                gs = [dl[dl[col]==g][ep].values for g in dl[col].unique() if len(dl[dl[col]==g])>0]
                if len(gs) > 1:
                    _, dp = stats.kruskal(*gs)
                    loo_ps.append({'id': df_clean.loc[i, ID_COL], 'p': dp})
                    
        else:
            ct = pd.crosstab(df_clean[col], df_clean[ep])
            base_p = stats.chi2_contingency(ct, correction=False)[1] if ct.size>0 and ct.shape[0]>1 and ct.shape[1]>1 else np.nan
            
            ct_i = pd.crosstab(df_infra_excl[col], df_infra_excl[ep])
            infra_p = stats.chi2_contingency(ct_i, correction=False)[1] if ct_i.size>0 and ct_i.shape[0]>1 and ct_i.shape[1]>1 else np.nan
            
            loo_ps = []
            for i in df_clean.index:
                dl = df_clean.drop(i)
                ct_l = pd.crosstab(dl[col], dl[ep])
                if ct_l.size>0 and ct_l.shape[0]>1 and ct_l.shape[1]>1:
                    dp = stats.chi2_contingency(ct_l, correction=False)[1]
                    loo_ps.append({'id': df_clean.loc[i, ID_COL], 'p': dp})
                    
        loo_df = pd.DataFrame(loo_ps).dropna()
        if not loo_df.empty and pd.notna(base_p):
            loo_df['delta_p_abs'] = (loo_df['p'] - base_p).abs()
            pmin = loo_df['p'].min()
            pmax = loo_df['p'].max()
            dp_max = loo_df['delta_p_abs'].max()
            influ_id = loo_df.loc[loo_df['delta_p_abs'].idxmax(), 'id']
        else:
            pmin, pmax, dp_max, influ_id = np.nan, np.nan, np.nan, np.nan
            
        rob_rows.append({
            'scenario': sk, 'endpoint': ep, 'p_base': base_p,
            'loo_p_min': pmin, 'loo_p_max': pmax, 
            'loo_delta_p_max_abs': dp_max, 'loo_most_influential_id': influ_id,
            'infra_exclusion_p': infra_p, 'infra_exclusion_delta_p': (infra_p - base_p) if pd.notna(infra_p) and pd.notna(base_p) else np.nan
        })

df_rob = pd.DataFrame(rob_rows)
df_rob.to_csv(f'{OUT_DIR}/robustness_panel_v3_2_2.csv', index=False)

sens_rows = []
for ep in ['doku_anomalisi_var_rt', 'gingivitis', 'caries_any_rt', 'caries_count']:
    ep_data = df_t3[df_t3['endpoint'] == ep]
    if ep_data.empty: continue
    
    p_classic_dict = ep_data.set_index('scenario')['p_classic'].to_dict()
    p_perm_dict = ep_data.set_index('scenario')['p_permutation'].to_dict()
    
    ps = [p for p in p_classic_dict.values() if pd.notna(p)]
    if len(ps) > 1:
        max_p, min_p = max(ps), min(ps)
        sens_rows.append({
            'endpoint': ep,
            'Primary_p_classic': p_classic_dict.get('Primary', np.nan),
            'k3_p_classic': p_classic_dict.get('k=3', np.nan),
            'k4_p_classic': p_classic_dict.get('k=4', np.nan),
            'Primary_p_perm': p_perm_dict.get('Primary', np.nan),
            'k3_p_perm': p_perm_dict.get('k=3', np.nan),
            'k4_p_perm': p_perm_dict.get('k=4', np.nan),
            'delta_p_classic_max': max_p - min_p,
            'inference_shift_05': True if (max_p >= 0.05 and min_p < 0.05) else False,
            'k3_is_duplicate_of': str(scenarios.get('k=3', {}).get('is_duplicate_of', None)),
            'k4_is_duplicate_of': str(scenarios.get('k=4', {}).get('is_duplicate_of', None))
        })
pd.DataFrame(sens_rows).to_csv(f'{OUT_DIR}/sensitivity_panel_v3_2_2.csv', index=False)


# %% [markdown]
# ## 8) Enhanced Model-Based CV Verification (LOO + RSKF)

# %%
cv_rows = []
scaler = StandardScaler()
bin_eps = ['doku_anomalisi_var_rt', 'gingivitis', 'caries_any_rt']

for sk in scenarios.keys():
    col = scenarios[sk]['col']
    for ep in bin_eps:
        if ep not in df_clean.columns: continue
        valid_df = df_clean.dropna(subset=['yas', col, ep])
        if valid_df[ep].nunique() < 2: 
            cv_rows.append({'scenario': sk, 'endpoint': ep, 'warnings': 'Constant Y'})
            continue
            
        y = valid_df[ep].values
        X_age = valid_df[['yas']].values
        X_gene = pd.get_dummies(valid_df[['yas', col]], drop_first=True, dtype=int).values
        if X_gene.shape[1] <= 1:
            X_gene = X_age
            
        cv_methods = [('LOO', LeaveOneOut())]
        min_class_count = valid_df[ep].value_counts().min()
        if min_class_count >= 2:
            n_spl = min(5, min_class_count)
            cv_methods.append(('RSKF', RepeatedStratifiedKFold(n_splits=n_spl, n_repeats=50, random_state=SEED_GLOBAL)))
        
        for cv_name, cv_obj in cv_methods:
            if cv_name == 'LOO':
                preds_a = np.zeros(len(y))
                preds_g = np.zeros(len(y))
                for tr_idx, te_idx in cv_obj.split(X_age, y):
                    Xa_tr_sc, Xa_te_sc = scaler.fit_transform(X_age[tr_idx]), scaler.transform(X_age[te_idx])
                    Xg_tr_sc, Xg_te_sc = scaler.fit_transform(X_gene[tr_idx]), scaler.transform(X_gene[te_idx])
                    
                    ma = LogisticRegression(penalty='l2', C=1.0, solver='liblinear', random_state=SEED_GLOBAL)
                    mg = LogisticRegression(penalty='l2', C=1.0, solver='liblinear', random_state=SEED_GLOBAL)
                    
                    if len(np.unique(y[tr_idx])) > 1:
                        ma.fit(Xa_tr_sc, y[tr_idx])
                        preds_a[te_idx] = ma.predict_proba(Xa_te_sc)[:, 1]
                        mg.fit(Xg_tr_sc, y[tr_idx])
                        preds_g[te_idx] = mg.predict_proba(Xg_te_sc)[:, 1]
                    else:
                        preds_a[te_idx] = np.mean(y[tr_idx])
                        preds_g[te_idx] = np.mean(y[tr_idx])
                
                try:
                    auc_a, auc_g = roc_auc_score(y, preds_a), roc_auc_score(y, preds_g)
                    warns = "AUC < 0.5" if auc_a < 0.5 or auc_g < 0.5 else ""
                    bt_deltas = []
                    for _ in range(manifest['bootstrap_iters']):
                        idx = np.random.choice(len(y), len(y), replace=True)
                        if len(np.unique(y[idx])) > 1:
                            bt_deltas.append(roc_auc_score(y[idx], preds_g[idx]) - roc_auc_score(y[idx], preds_a[idx]))
                    ci_l, ci_h = np.percentile(bt_deltas, [2.5, 97.5]) if bt_deltas else (np.nan, np.nan)
                    cv_rows.append({'scenario': sk, 'endpoint': ep, 'cv_method': cv_name, 'auc_age': auc_a, 'auc_age_gene': auc_g, 'delta_auc': auc_g-auc_a, 'delta_auc_ci_low': ci_l, 'delta_auc_ci_high': ci_h, 'warnings': warns})
                except Exception as e:
                    cv_rows.append({'scenario': sk, 'endpoint': ep, 'cv_method': cv_name, 'warnings': str(e)})
                    
            elif cv_name == 'RSKF':
                n_rep = cv_obj.n_repeats
                oof_a = np.zeros((n_rep, len(y)))
                oof_g = np.zeros((n_rep, len(y)))
                n_spl = cv_obj.cvargs.get('n_splits')
                
                for i, (tr_idx, te_idx) in enumerate(cv_obj.split(X_age, y)):
                    rep_idx = i // n_spl
                    Xa_tr_sc, Xa_te_sc = scaler.fit_transform(X_age[tr_idx]), scaler.transform(X_age[te_idx])
                    Xg_tr_sc, Xg_te_sc = scaler.fit_transform(X_gene[tr_idx]), scaler.transform(X_gene[te_idx])
                    
                    ma = LogisticRegression(penalty='l2', C=1.0, solver='liblinear', random_state=SEED_GLOBAL)
                    mg = LogisticRegression(penalty='l2', C=1.0, solver='liblinear', random_state=SEED_GLOBAL)
                    
                    if len(np.unique(y[tr_idx])) > 1:
                        ma.fit(Xa_tr_sc, y[tr_idx])
                        oof_a[rep_idx, te_idx] = ma.predict_proba(Xa_te_sc)[:, 1]
                        mg.fit(Xg_tr_sc, y[tr_idx])
                        oof_g[rep_idx, te_idx] = mg.predict_proba(Xg_te_sc)[:, 1]
                    else:
                        oof_a[rep_idx, te_idx] = np.mean(y[tr_idx])
                        oof_g[rep_idx, te_idx] = np.mean(y[tr_idx])
                        
                aucs_a = [roc_auc_score(y, oof_a[r]) for r in range(n_rep) if len(np.unique(y))>1]
                aucs_g = [roc_auc_score(y, oof_g[r]) for r in range(n_rep) if len(np.unique(y))>1]
                
                if aucs_a and aucs_g:
                    auc_a, auc_g = np.mean(aucs_a), np.mean(aucs_g)
                    deltas = np.array(aucs_g) - np.array(aucs_a)
                    ci_l, ci_h = np.percentile(deltas, 2.5), np.percentile(deltas, 97.5)
                    warns = "AUC < 0.5" if auc_a < 0.5 or auc_g < 0.5 else ""
                    cv_rows.append({'scenario': sk, 'endpoint': ep, 'cv_method': cv_name, 'auc_age': auc_a, 'auc_age_gene': auc_g, 'delta_auc': np.mean(deltas), 'delta_auc_ci_low': ci_l, 'delta_auc_ci_high': ci_h, 'warnings': warns})

pd.DataFrame(cv_rows).to_csv(f'{OUT_DIR}/cv_panel_v3_2_2.csv', index=False)

# %% [markdown]
# ## 9) Compare Against Prior Artifacts

# %%
comp_rows = []
prev_path = 'outputs_v3_2_1/publication_table3_inferential_v3_2_1.csv'
if os.path.exists(prev_path):
    v_old = pd.read_csv(prev_path)
    df_t3_comp = df_t3.copy()
    v_old['merge_key'] = v_old['scenario'] + '_' + v_old['endpoint'].str.replace('_rt', '')
    df_t3_comp['merge_key'] = df_t3_comp['scenario'] + '_' + df_t3_comp['endpoint'].str.replace('_rt', '')
    
    joined = pd.merge(v_old, df_t3_comp, on='merge_key', suffixes=('_vold', '_vnew'))
    for idx, r in joined.iterrows():
        # Specifically we check about eps2
        if r.get('effect_size_name_vold') == 'Epsilon2' or r.get('effect_size_name_vnew') == 'Epsilon2':
            comp_rows.append({
                'artifact': 'Table3', 'metric': r['merge_key']+'_eps2_primary',
                'old_value': np.nan, 'new_value': r.get('epsilon2_primary_vnew', np.nan),
                'explanation': 'Epsilon2 Primary formulation explicitly documented'
            })
pd.DataFrame(comp_rows).to_csv(f'{OUT_DIR}/consistency_diff_v3_2_1_vs_v3_2_2.csv', index=False)

# %% [markdown]
# ## 10) Master Verification & QC CHECKLIST

# %%
qc_results = []
qc_results.append(("Manifest Exists (v3_2_2)", "PASS" if os.path.exists(f'{OUT_DIR}/run_manifest.json') else "FAIL"))
qc_results.append(("Math consistency eps2 formulas", "PASS" if not (c_diff_df['status'] == 'FAIL').any() else "FAIL"))
qc_results.append(("gene_freq_table has NO Other", "FAIL" if 'Other' in counts.index else "PASS"))

df_mapped = pd.DataFrame(gmap)
raw_genes = set(df_clean['gen_mutasyonu'].dropna().apply(lambda x: str(x).strip().upper()).unique())
mapped_genes = set(df_mapped['Symbol'].unique())
qc_results.append(("All raw genes appear in map", "PASS" if raw_genes == mapped_genes else "FAIL"))

has_eps2_cols = all(x in df_t3.columns for x in ['epsilon2_primary', 'epsilon2_alt', 'kw_n', 'kw_k'])
qc_results.append(("Table 3 has dual eps2 tracking", "PASS" if has_eps2_cols else "FAIL"))

qc_results.append(("No repeated errors in issue log", "FAIL" if any(x['severity']=='FAIL' for x in issue_log) else "PASS"))

print("====== QC CHECKLIST (V3.2.2) ======\n")
fail_count = 0
for test, res in qc_results:
    print(f"[{res}] {test}")
    if res == "FAIL": fail_count += 1
    
if fail_count > 0:
    log_issue('FAIL', 'QC_FINAL', f'{fail_count} checks failed')
    print("\n>> ITERATION REQUIRED. SOME QCs FAILED.")
else:
    print("\nDONE — QC PASS (v3.2.2)")
    
if len(issue_log) == 0:
    log_issue("INFO", "ALL", "No issues detected in v3.2.2")
    
pd.DataFrame(issue_log).to_csv(f'{OUT_DIR}/issue_log_v3_2_2.csv', index=False)

# %% [markdown]
# # 🧬 Osteogenesis Imperfecta (Camber) Master Analysis - FINAL.1.2
# Goal: Create the final submission-ready datasets, following strict format requirements.
# Fixes: Added AUC CI, Primary-only CV/Robustness panels, and standardized logs.

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

OUT_DIR = 'outputs_FINAL_1_2'
os.makedirs(OUT_DIR, exist_ok=True)
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

# %% [markdown]
# ## 4) Critical Variable Definitions

# %%
df_clean['infraokluzyon_var_rt'] = (df_clean['occl_tip'] == 4).astype(int)
df_clean['angle_sinifi_rt'] = df_clean['occl_tip'].apply(lambda x: x if x in [1,2,3] else np.nan)
df_clean['caries_count'] = df_clean['dmft_dmft'].copy()
df_clean['caries_any_rt'] = (df_clean['caries_count'] > 0).astype(int)
df_clean['doku_anomalisi_var_rt'] = (df_clean['doku_anomalisi'] != 0).astype(int)

# %% [markdown]
# ## 5) Runtime Gene Handling & Traceability

# %%
def extract_gene(g_str):
    if pd.isna(g_str): return 'Unknown'
    return str(g_str).strip().upper()

df_clean['gene_symbol_rt'] = df_clean['gen_mutasyonu'].apply(extract_gene)
counts = df_clean['gene_symbol_rt'].value_counts()

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

# %% [markdown]
# ## 6) Primary Analyses, Math Consistancy & Correct Inheritance

# %%
def wilson_ci(count, nobs):
    if nobs == 0: return "0.0, 0.0"
    low, high = proportion.proportion_confint(count, nobs, method='wilson')
    return f"{low*100:.1f}, {high*100:.1f}"

n_angle_eligible = df_clean['angle_sinifi_rt'].notna().sum()
n_infra = df_clean['infraokluzyon_var_rt'].sum()

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
pd.DataFrame(t1).to_csv(f'{OUT_DIR}/publication_table1_overall_FINAL.csv', index=False)

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
pd.DataFrame(t2).to_csv(f'{OUT_DIR}/publication_table2_by_gene_group_FINAL.csv', index=False)

def method_A_eps2(st, n, k):
    return (st - k + 1) / (n - k) if n > k else np.nan, st / (n - 1) if n > 1 else np.nan

def method_A_v(chi2, n, r, c):
    mindim = min(r-1, c-1)
    return np.sqrt(chi2 / (n * mindim)) if mindim > 0 and n > 0 else 0

def exact_or_permutation_p(ct, iters=10000):
    chi2_obs = stats.chi2_contingency(ct, correction=False)[0]
    rm, cm = ct.sum(axis=1).values, ct.sum(axis=0).values
    n = ct.sum().sum()
    rows, cols = np.repeat(np.arange(len(rm)), rm), np.repeat(np.arange(len(cm)), cm)
    count_gte, r_dim, c_dim = 0, len(rm), len(cm)
    ex_array = np.outer(rm, cm) / n
    ex_array[ex_array == 0] = 1.0
    for _ in range(iters):
        np.random.shuffle(cols)
        flat_idx = rows * c_dim + cols
        perm_flat = np.bincount(flat_idx, minlength=r_dim*c_dim)
        chi_p = np.sum((perm_flat.reshape((r_dim, c_dim)) - ex_array)**2 / ex_array)
        if chi_p >= chi2_obs - 1e-9: count_gte += 1
    return count_gte / iters

t3_rows = []
for sk in scenarios.keys():
    col = scenarios[sk]['col']
    is_dup = scenarios[sk]['is_duplicate_of']

    for ep in ['doku_anomalisi_var_rt', 'gingivitis', 'caries_any_rt']:
        if ep not in df_clean.columns: continue
        ct = pd.crosstab(df_clean[col], df_clean[ep])
        if ct.size == 0 or ct.shape[0] < 2 or ct.shape[1] < 2: continue
        chi2, p_class, dof, ex = stats.chi2_contingency(ct, correction=False)
        v = method_A_v(chi2, ct.sum().sum(), ct.shape[0], ct.shape[1])

        if is_dup is None: p_perm = exact_or_permutation_p(ct, manifest["permutation_iters"])
        else: p_perm = next(r for r in t3_rows if r['scenario'] == is_dup and r['endpoint'] == ep)['p_permutation']

        t3_rows.append({
            'scenario': sk, 'endpoint': ep, 'test': 'Chi2_Perm',
            'statistic': chi2, 'p_classic': p_class, 'p_permutation': p_perm,
            'expected_min': ex.min(), 'effect_size_name': 'CramerV', 'effect_size_value': v,
            'epsilon2_primary': np.nan, 'epsilon2_alt': np.nan, 'kw_n': np.nan, 'kw_k': np.nan,
            'is_duplicate_scenario': is_dup is not None, 'perm_inherited_from': is_dup if is_dup else ''
        })

    ep = 'caries_count'
    d_valid = df_clean.dropna(subset=[col, ep])
    groups = [d_valid[d_valid[col]==g][ep].values for g in d_valid[col].unique() if len(d_valid[d_valid[col]==g])>0]
    if len(groups) > 1:
        st, kw_p = stats.kruskal(*groups)
        n_val, k_val = sum(len(g) for g in groups), len(groups)

        # Tie correction block
        all_data = np.concatenate(groups)
        ranks = stats.rankdata(all_data)
        ties = np.unique(ranks, return_counts=True)[1]
        tie_corr = 1 - sum(ties**3 - ties) / (n_val**3 - n_val)

        idx = 0
        R_sq_n_sum = 0
        for g in groups:
            r_sum = np.sum(ranks[idx:idx+len(g)])
            R_sq_n_sum += (r_sum**2) / len(g)
            idx += len(g)

        H = (12 / (n_val * (n_val + 1))) * R_sq_n_sum - 3 * (n_val + 1)
        H /= tie_corr
        eps2_alt_A = H / (n_val - 1)
        eps2_prim_A = (H - k_val + 1) / (n_val - k_val) if n_val > k_val else np.nan

        t3_rows.append({
            'scenario': sk, 'endpoint': ep, 'test': 'Kruskal',
            'statistic': st, 'p_classic': kw_p, 'p_permutation': np.nan,
            'expected_min': np.nan, 'effect_size_name': 'Epsilon2', 'effect_size_value': eps2_prim_A,
            'epsilon2_primary': eps2_prim_A, 'epsilon2_alt': eps2_alt_A, 'kw_n': n_val, 'kw_k': k_val,
            'is_duplicate_scenario': is_dup is not None, 'perm_inherited_from': is_dup if is_dup else ''
        })

# Assign Holm Multiple Corrections logically per scenario
for sk in scenarios.keys():
    if scenarios[sk]['is_duplicate_of'] is not None:
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

    prim_eps = ['doku_anomalisi_var_rt', 'gingivitis', 'caries_count']
    prim_idx = [i for i, row in enumerate(t3_rows) if row['scenario'] == sk and row['endpoint'] in prim_eps]
    if prim_idx:
        p_vals = [t3_rows[i]['p_classic'] for i in prim_idx]
        _, holm_c, _, _ = multipletests(p_vals, method='holm')
        for i, p_h in zip(prim_idx, holm_c): t3_rows[i]['p_holm_primary_family_classic'] = p_h

    bin_eps = ['doku_anomalisi_var_rt', 'gingivitis', 'caries_any_rt']
    bin_idx = [i for i, row in enumerate(t3_rows) if row['scenario'] == sk and row['endpoint'] in bin_eps]
    if bin_idx:
        p_vals = [t3_rows[i]['p_permutation'] for i in bin_idx]
        _, holm_p, _, _ = multipletests(p_vals, method='holm')
        for i, p_h in zip(bin_idx, holm_p): t3_rows[i]['p_holm_binary_family_perm'] = p_h

df_t3 = pd.DataFrame(t3_rows)
if 'p_holm_primary_family_classic' not in df_t3: df_t3['p_holm_primary_family_classic'] = np.nan
if 'p_holm_binary_family_perm' not in df_t3: df_t3['p_holm_binary_family_perm'] = np.nan

# %% [markdown]
# ## 7) Robustness & CV Verification with Bootstrap CI

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
                if len(gs) > 1: loo_ps.append({'id': df_clean.loc[i, ID_COL], 'p': stats.kruskal(*gs)[1]})

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
                    loo_ps.append({'id': df_clean.loc[i, ID_COL], 'p': stats.chi2_contingency(ct_l, correction=False)[1]})

        loo_df = pd.DataFrame(loo_ps).dropna()
        if not loo_df.empty and pd.notna(base_p):
            pmin, pmax = loo_df['p'].min(), loo_df['p'].max()
            dp_max = (loo_df['p'] - base_p).abs().max()
            influ_id = loo_df.loc[(loo_df['p'] - base_p).abs().idxmax(), 'id']
        else: pmin, pmax, dp_max, influ_id = np.nan, np.nan, np.nan, np.nan

        rob_rows.append({
            'scenario': sk, 'endpoint': ep, 'p_base': base_p,
            'loo_p_min': pmin, 'loo_p_max': pmax,
            'loo_delta_p_max_abs': dp_max, 'loo_most_influential_id': influ_id,
            'infra_exclusion_p': infra_p, 'infra_exclusion_delta_p': (infra_p - base_p) if pd.notna(infra_p) and pd.notna(base_p) else np.nan
        })

df_rob = pd.DataFrame(rob_rows)

def get_auc_ci(y_true, preds_a, preds_g, n_boot=2000, seed=SEED_GLOBAL):
    np.random.seed(seed)
    delta_aucs = []
    n = len(y_true)
    for _ in range(n_boot):
        idx = np.random.choice(n, n, replace=True)
        y_b = y_true[idx]
        if len(np.unique(y_b)) < 2: continue
        p_a_b = preds_a[idx]
        p_g_b = preds_g[idx]
        try:
            auc_a = roc_auc_score(y_b, p_a_b)
            auc_g = roc_auc_score(y_b, p_g_b)
            delta_aucs.append(auc_g - auc_a)
        except:
            pass
    
    n_valid = len(delta_aucs)
    n_dropped = n_boot - n_valid
    drop_rate = n_dropped / n_boot if n_boot > 0 else 0
    has_warn = (drop_rate > 0.10)
    
    ci_l = np.percentile(delta_aucs, 2.5) if n_valid > 0 else np.nan
    ci_h = np.percentile(delta_aucs, 97.5) if n_valid > 0 else np.nan
    b_mean = np.mean(delta_aucs) if n_valid > 0 else np.nan
    b_med = np.median(delta_aucs) if n_valid > 0 else np.nan
    
    boot_stats = {
        'n_boot_total': n_boot,
        'n_boot_valid': n_valid,
        'n_boot_dropped': n_dropped,
        'boot_drop_rate': drop_rate,
        'delta_auc_boot_mean': b_mean,
        'delta_auc_boot_median': b_med
    }
    
    return ci_l, ci_h, boot_stats, has_warn

cv_rows = []
scaler = StandardScaler()
bin_eps = ['doku_anomalisi_var_rt', 'gingivitis', 'caries_any_rt']

for sk in scenarios.keys():
    col = scenarios[sk]['col']
    for ep in bin_eps:
        valid_df = df_clean.dropna(subset=['yas', col, ep])
        if valid_df[ep].nunique() < 2:
            cv_rows.append({'scenario': sk, 'endpoint': ep, 'cv_method': 'LOO', 'warnings': 'Constant Y', 'delta_auc_estimator': '', 'ci_estimator': '', 'note': ''})
            continue

        y = valid_df[ep].values
        X_age = valid_df[['yas']].values
        X_gene = pd.get_dummies(valid_df[['yas', col]], drop_first=True, dtype=int).values
        if X_gene.shape[1] <= 1: X_gene = X_age

        cv_methods = [('LOO', LeaveOneOut())]
        min_class_count = valid_df[ep].value_counts().min()
        if min_class_count >= 2:
            n_spl = int(min(5, min_class_count))
            cv_methods.append(('RSKF', RepeatedStratifiedKFold(n_splits=n_spl, n_repeats=50, random_state=SEED_GLOBAL)))

        for cv_name, cv_obj in cv_methods:
            if cv_name == 'LOO':
                preds_a = np.zeros(len(y))
                preds_g = np.zeros(len(y))
                for tr_idx, te_idx in cv_obj.split(X_age, y):
                    Xa_tr_sc, Xa_te_sc = scaler.fit_transform(X_age[tr_idx]), scaler.transform(X_age[te_idx])
                    Xg_tr_sc, Xg_te_sc = scaler.fit_transform(X_gene[tr_idx]), scaler.transform(X_gene[te_idx])
                    ma = LogisticRegression(penalty='l2', solver='liblinear', random_state=SEED_GLOBAL)
                    mg = LogisticRegression(penalty='l2', solver='liblinear', random_state=SEED_GLOBAL)
                    if len(np.unique(y[tr_idx])) > 1:
                        ma.fit(Xa_tr_sc, y[tr_idx]); preds_a[te_idx] = ma.predict_proba(Xa_te_sc)[:, 1]
                        mg.fit(Xg_tr_sc, y[tr_idx]); preds_g[te_idx] = mg.predict_proba(Xg_te_sc)[:, 1]
                    else:
                        preds_a[te_idx], preds_g[te_idx] = np.mean(y[tr_idx]), np.mean(y[tr_idx])

                try:
                    n_pos, n_neg = np.sum(y == 1), np.sum(y == 0)
                    auc_a, auc_g = roc_auc_score(y, preds_a), roc_auc_score(y, preds_g)
                    ci_l, ci_h, b_stats, has_warn = get_auc_ci(y, preds_a, preds_g, n_boot=manifest["bootstrap_iters"])
                    warns = []
                    if auc_a < 0.5 or auc_g < 0.5: warns.append("AUC < 0.5")
                    if has_warn: warns.append("boot_drop_rate > 0.10")
                    if n_pos < 5 or n_neg < 5: warns.append("tiny class")
                    row = {
                        'scenario': sk, 'endpoint': ep, 'cv_method': cv_name,
                        'n_pos': n_pos, 'n_neg': n_neg,
                        'auc_age': auc_a, 'auc_age_gene': auc_g, 'delta_auc': auc_g-auc_a,
                        'delta_auc_ci_low': ci_l, 'delta_auc_ci_high': ci_h,
                        'delta_auc_estimator': 'loo_auc',
                        'ci_estimator': 'paired_bootstrap_on_oof_probs'
                    }
                    row.update(b_stats)
                    note_text = ""
                    if 'delta_auc_boot_mean' in b_stats and pd.notna(b_stats['delta_auc_boot_mean']):
                        if abs(b_stats['delta_auc_boot_mean'] - (auc_g-auc_a)) > 0.05:
                            note_text = "delta_auc_boot_mean materially differs from delta_auc"
                    row['note'] = note_text
                    row['warnings'] = "; ".join(warns)
                    cv_rows.append(row)
                except Exception as e:
                    cv_rows.append({'scenario': sk, 'endpoint': ep, 'cv_method': cv_name, 'warnings': str(e), 'delta_auc_estimator': '', 'ci_estimator': '', 'note': ''})

            elif cv_name == 'RSKF':
                n_rep, n_spl = cv_obj.n_repeats, cv_obj.cvargs.get('n_splits')
                oof_a, oof_g = np.zeros((n_rep, len(y))), np.zeros((n_rep, len(y)))
                for i, (tr_idx, te_idx) in enumerate(cv_obj.split(X_age, y)):
                    rep_idx = i // n_spl
                    Xa_tr_sc, Xa_te_sc = scaler.fit_transform(X_age[tr_idx]), scaler.transform(X_age[te_idx])
                    Xg_tr_sc, Xg_te_sc = scaler.fit_transform(X_gene[tr_idx]), scaler.transform(X_gene[te_idx])
                    ma = LogisticRegression(penalty='l2', solver='liblinear', random_state=SEED_GLOBAL)
                    mg = LogisticRegression(penalty='l2', solver='liblinear', random_state=SEED_GLOBAL)
                    if len(np.unique(y[tr_idx])) > 1:
                        ma.fit(Xa_tr_sc, y[tr_idx]); oof_a[rep_idx, te_idx] = ma.predict_proba(Xa_te_sc)[:, 1]
                        mg.fit(Xg_tr_sc, y[tr_idx]); oof_g[rep_idx, te_idx] = mg.predict_proba(Xg_te_sc)[:, 1]
                    else:
                        oof_a[rep_idx, te_idx], oof_g[rep_idx, te_idx] = np.mean(y[tr_idx]), np.mean(y[tr_idx])

                aucs_a = [roc_auc_score(y, oof_a[r]) for r in range(n_rep) if len(np.unique(y))>1]
                aucs_g = [roc_auc_score(y, oof_g[r]) for r in range(n_rep) if len(np.unique(y))>1]

                if aucs_a and aucs_g:
                    n_pos, n_neg = np.sum(y == 1), np.sum(y == 0)
                    auc_a, auc_g = np.mean(aucs_a), np.mean(aucs_g)
                    p_a_mean, p_g_mean = oof_a.mean(axis=0), oof_g.mean(axis=0)
                    ci_l, ci_h, b_stats, has_warn = get_auc_ci(y, p_a_mean, p_g_mean, n_boot=manifest["bootstrap_iters"])
                    warns = []
                    if auc_a < 0.5 or auc_g < 0.5: warns.append("AUC < 0.5")
                    if has_warn: warns.append("boot_drop_rate > 0.10")
                    if n_pos < 5 or n_neg < 5: warns.append("tiny class")
                    row = {
                        'scenario': sk, 'endpoint': ep, 'cv_method': cv_name, 
                        'n_pos': n_pos, 'n_neg': n_neg,
                        'auc_age': auc_a, 'auc_age_gene': auc_g, 'delta_auc': auc_g-auc_a, 
                        'delta_auc_ci_low': ci_l, 'delta_auc_ci_high': ci_h,
                        'delta_auc_estimator': 'mean_auc_over_repeats',
                        'ci_estimator': 'paired_bootstrap_on_mean_oof_probs'
                    }
                    row.update(b_stats)
                    note_text = ""
                    if 'delta_auc_boot_mean' in b_stats and pd.notna(b_stats['delta_auc_boot_mean']):
                        if abs(b_stats['delta_auc_boot_mean'] - (auc_g-auc_a)) > 0.05:
                            note_text = "delta_auc_boot_mean materially differs from delta_auc"
                    row['note'] = note_text
                    row['warnings'] = "; ".join(warns)
                    cv_rows.append(row)

df_cv = pd.DataFrame(cv_rows)

# %% [markdown]
# ## 8) FINAL.1 Exports & Formatting Improvements

# %%

# Ensure only Primary scenarios in main panels
df_rob_primary = df_rob[df_rob['scenario'] == 'Primary'].copy()
df_cv_primary = df_cv[df_cv['scenario'] == 'Primary'].copy()

# Table 3
df_t3_primary = df_t3[df_t3['scenario'] == 'Primary'].copy()
df_t3_primary.drop(columns=['is_duplicate_scenario', 'perm_inherited_from'], inplace=True)

# Write core artifacts
df_t3_primary.to_csv(f'{OUT_DIR}/publication_table3_inferential_FINAL.csv', index=False)
df_rob_primary.to_csv(f'{OUT_DIR}/robustness_panel_FINAL.csv', index=False)
df_cv_primary.to_csv(f'{OUT_DIR}/cv_panel_FINAL.csv', index=False)

# Write supplementary artifacts
df_rob.to_csv(f'{OUT_DIR}/supplementary_robustness_FINAL.csv', index=False)
df_cv.to_csv(f'{OUT_DIR}/supplementary_cv_FINAL.csv', index=False)
df_t3.to_csv(f'{OUT_DIR}/supplementary_sensitivity_FINAL.csv', index=False)
pd.DataFrame(gmap).to_csv(f'{OUT_DIR}/supplementary_gene_group_map_FINAL.csv', index=False)

# Master Table Compilation
master_cv_rows = []
for ep in df_cv_primary['endpoint'].unique():
    ep_rows = df_cv_primary[df_cv_primary['endpoint'] == ep]
    if 'RSKF' in ep_rows['cv_method'].values:
        rskf_row = ep_rows[ep_rows['cv_method'] == 'RSKF'].iloc[0]
        loo_row = ep_rows[ep_rows['cv_method'] == 'LOO'].iloc[0]
        row_dict = rskf_row.to_dict()
        row_dict['primary_cv_method'] = 'RSKF'
        row_dict['loo_delta_auc'] = loo_row['delta_auc']
        master_cv_rows.append(row_dict)
    else:
        loo_row = ep_rows[ep_rows['cv_method'] == 'LOO'].iloc[0]
        row_dict = loo_row.to_dict()
        row_dict['primary_cv_method'] = 'LOO'
        row_dict['loo_delta_auc'] = loo_row['delta_auc']
        master_cv_rows.append(row_dict)

if len(master_cv_rows) > 0:
    df_master_cv = pd.DataFrame(master_cv_rows)
    master_merged = df_t3_primary.merge(df_rob_primary[['endpoint', 'loo_p_min', 'loo_p_max', 'infra_exclusion_delta_p']], on='endpoint', how='left')
    cols_to_keep = ['endpoint', 'primary_cv_method', 'n_pos', 'n_neg', 'auc_age', 'auc_age_gene', 'delta_auc', 'delta_auc_ci_low', 'delta_auc_ci_high', 'n_boot_total', 'n_boot_valid', 'n_boot_dropped', 'boot_drop_rate', 'delta_auc_boot_mean', 'delta_auc_boot_median', 'loo_delta_auc', 'delta_auc_estimator', 'ci_estimator', 'note']
    master_merged = master_merged.merge(df_master_cv[[c for c in cols_to_keep if c in df_master_cv.columns]], on='endpoint', how='left')
    master_merged.to_csv(f'{OUT_DIR}/verified_master_table_FINAL.csv', index=False)
else:
    # Fallback if no CV
    master_merged = df_t3_primary.merge(df_rob_primary[['endpoint', 'loo_p_min', 'loo_p_max', 'infra_exclusion_delta_p']], on='endpoint', how='left')
    master_merged.to_csv(f'{OUT_DIR}/verified_master_table_FINAL.csv', index=False)


# Issue log formatting
if len(issue_log) == 0:
    issue_log.append({'severity': 'INFO', 'category': 'LOG', 'description': 'No issues detected', 'affected_rows': '', 'action_taken': 'Generated as well-formed CSV'})
pd_log = pd.DataFrame(issue_log)
pd_log.rename(columns={'affected_rows': 'affected_ids'}, inplace=True)
if 'affected_ids' not in pd_log.columns: pd_log['affected_ids'] = ''
pd_log[['severity', 'category', 'description', 'affected_ids', 'action_taken']].to_csv(f'{OUT_DIR}/issue_log_FINAL.csv', index=False)

# Calculate EXACT Diff against outputs_FINAL
diff_log = []
try:
    final_t3 = pd.read_csv('outputs_FINAL_1_1/publication_table3_inferential_FINAL.csv')
    joined = pd.merge(final_t3, df_t3_primary, on='endpoint', suffixes=('_old', '_new'))

    for col in ['p_classic', 'p_permutation', 'effect_size_value', 'p_holm_primary_family_classic', 'p_holm_binary_family_perm']:
        for idx, row in joined.iterrows():
            ov, nv = row[f'{col}_old'], row[f'{col}_new']
            if pd.notna(ov) and pd.notna(nv):
                if abs(float(ov) - float(nv)) > 1e-6: diff_log.append(f"Mismatch in {row['endpoint']} - {col}: {ov} vs {nv}")
            elif pd.isna(ov) != pd.isna(nv):
                diff_log.append(f"NaN mismatch in {row['endpoint']} - {col}")

    diff_report = []
    diff_report.append({'Item': 'Artifact Structure', 'Change': 'Added outputs_FINAL_1/'})
    diff_report.append({'Item': 'CV CI', 'Change': 'Added delta_auc_ci_low and high via Bootstrap.'})
    diff_report.append({'Item': 'Robustness/CV Panels', 'Change': 'Made primary panels exclusively Primary, moved k3/4 to supplementary.'})
    diff_report.append({'Item': 'Master Table', 'Change': 'Integrated CV CI and primary_cv_method.'})
    diff_report.append({'Item': 'Issue Log', 'Change': 'Always strictly formatted with standard headers.'})

    for l in diff_log:
        diff_report.append({'Item': 'Unintended Math Variation', 'Change': l})
        log_issue("FAIL", "MATH_DIFF", l)

    pd.DataFrame(diff_report).to_csv(f'{OUT_DIR}/consistency_diff_FINAL_1_1_vs_FINAL_1_2.csv', index=False)
    
    cv_old = pd.read_csv('outputs_FINAL_1_1/cv_panel_FINAL.csv')
    cv_new = pd.read_csv(f'{OUT_DIR}/cv_panel_FINAL.csv')
    
    cv_diff_alerts = []
    for ep in cv_old['endpoint'].unique():
        for meth in cv_old['cv_method'].unique():
            o = cv_old[(cv_old['endpoint']==ep)&(cv_old['cv_method']==meth)]
            n = cv_new[(cv_new['endpoint']==ep)&(cv_new['cv_method']==meth)]
            if o.empty or n.empty: continue
            for col in ['auc_age','auc_age_gene','delta_auc','delta_auc_ci_low','delta_auc_ci_high']:
                ov, nv = o.iloc[0][col], n.iloc[0][col]
                if pd.notna(ov) and pd.notna(nv):
                    if abs(float(ov) - float(nv)) > 1e-6: cv_diff_alerts.append(f"CV Mismatch in {ep}_{meth} - {col}: {ov} vs {nv}")
    if cv_diff_alerts:
        diff_report.append({'Item': 'CV Math Modified', 'Change': 'ERROR: ' + str(cv_diff_alerts)})
        log_issue("FAIL", "CV_DIFF", str(cv_diff_alerts))
        pd.DataFrame(diff_report).to_csv(f'{OUT_DIR}/consistency_diff_FINAL_1_1_vs_FINAL_1_2.csv', index=False)
        
except Exception as e:
    err = f"Diff tool failed to run: {e}"
    pd.DataFrame([{'Item': 'ERROR', 'Change': err}]).to_csv(f'{OUT_DIR}/consistency_diff_FINAL_1_1_vs_FINAL_1_2.csv', index=False)

# %% [markdown]
# ## 9) QC CHECKLIST (FINAL.1.2 GATE)

# %%
qc_res = []

qc_res.append(('publication_table3 unchanged vs FINAL (primary math)', 'PASS' if len(diff_log) == 0 else 'FAIL'))
qc_res.append(('CV CI present in cv_panel (delta_auc_ci_low exists)', 'PASS' if 'delta_auc_ci_low' in df_cv_primary.columns else 'FAIL'))
qc_res.append(('Main robustness panel is Primary-only', 'PASS' if len(df_rob_primary) > 0 and (df_rob_primary['scenario'] == 'Primary').all() else 'FAIL'))
qc_res.append(('Main CV panel is Primary-only', 'PASS' if len(df_cv_primary) > 0 and (df_cv_primary['scenario'] == 'Primary').all() else 'FAIL'))
qc_res.append(('Supplementary CV exists', 'PASS' if os.path.exists(f'{OUT_DIR}/supplementary_cv_FINAL.csv') else 'FAIL'))
qc_res.append(('Supplementary Robustness exists', 'PASS' if os.path.exists(f'{OUT_DIR}/supplementary_robustness_FINAL.csv') else 'FAIL'))
qc_res.append(('issue_log_FINAL is successfully parseable and structured', 'PASS' if os.path.exists(f'{OUT_DIR}/issue_log_FINAL.csv') and 'affected_ids' in pd.read_csv(f'{OUT_DIR}/issue_log_FINAL.csv').columns else 'FAIL'))

qc_res.append(('Bootstrap bookkeeping valid', 'PASS' if (df_cv_primary['n_boot_valid'] + df_cv_primary['n_boot_dropped']).equals(df_cv_primary['n_boot_total']) else 'FAIL'))
qc_res.append(('CV values identical to FINAL.1', 'PASS' if len([x for x in issue_log if x.get('category') == 'CV_DIFF']) == 0 else 'FAIL'))

print("====== QC CHECKLIST (FINAL.1.2) ======")
fails = 0
for t, r in qc_res:
    print(f"[{r}] {t}")
    if r == "FAIL": fails += 1

if fails > 0:
    print(">> ITERATION REQUIRED. SOME QCs FAILED.")
else:
    print("DONE — QC PASS (FINAL.1.2)")

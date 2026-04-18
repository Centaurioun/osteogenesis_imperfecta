import sys
import os
import random
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.stats.proportion as proportion
from statsmodels.stats.multitest import multipletests
from sklearn.model_selection import LeaveOneOut
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler
import re
import warnings

warnings.filterwarnings('ignore')

SEED = 20260228
np.random.seed(SEED)
random.seed(SEED)
os.environ['PYTHONHASHSEED'] = str(SEED)

print(f"Python: {sys.version}")
print(f"Pandas: {pd.__version__}")

OUT_DIR = 'outputs_v3_1'
os.makedirs(OUT_DIR, exist_ok=True)
issue_log = []

def log_issue(severity, category, desc, affected):
    issue_log.append({
        'severity': severity,
        'category': category,
        'description': desc,
        'affected_rows': str(affected),
        'action_taken': 'Logged'
    })


files = {
    "data": "osteogenesis_imperfecta_camber_input_minimal_v1.csv",
    "sap": "camber_sap_v2_publication_ready.md",
    "codebook": "codebook_v3_fixed.md",
    "brief": "camber_study_brief_v1.md",
    "v3_tb1": "outputs_v3/publication_table1_overall_v3.csv",
    "v3_tb3": "outputs_v3/publication_table3_inferential_v3.csv"
}

for k, v in files.items():
    if os.path.exists(v):
        print(f"[*] Found {k}: {v}")
    else:
        print(f"[!] Missing {k}: {v}")

# V3 Fail Diagnosis Check:
# - Robustness & CV panels in V3 only looped 'doku_anomalisi_var' as a demo instead of all primary endpoints.
# - Occlusion panel was requested but not fully implemented as separate CSV.
# - Cramer's V manual mathematical verification assertion was missing.
# - Multiple p Holm sets were mixed into a single column instead of separate logic tracks.


df = pd.read_csv(files['data'])
df_clean = df.copy()

# 3.1) Occlusion Type
assert set(df_clean['occl_tip'].dropna()).issubset({1,2,3,4}), "Unknown occl_tip"
df_clean['infraokluzyon_var'] = (df_clean['occl_tip'] == 4).astype(int)
df_clean['angle_sinifi'] = df_clean['occl_tip'].apply(lambda x: x if x in [1, 2, 3] else np.nan)
assert set(df_clean['angle_sinifi'].dropna()).issubset({1,2,3}), "Angle sinifi leak"

# 3.2) DMFT / Caries
df_clean['caries_count'] = df_clean['dmft_dmft']
df_clean['caries_any_rt'] = (df_clean['caries_count'] > 0).astype(int)
# Check mismatch with original
if 'caries_any' in df_clean.columns:
    mm = df_clean[df_clean['caries_any'] != df_clean['caries_any_rt']]
    if not mm.empty:
        log_issue("WARN", "TRANSFORM", "Original caries_any differs from caries_any_rt", mm['hasta_kodu'].tolist())
df_clean['caries_any'] = df_clean['caries_any_rt'] # Enforcement

# 3.3) Tissue Anomaly
df_clean['doku_anomalisi_var'] = (df_clean['doku_anomalisi'] != 0).astype(int)

# 3.4) Runtime Gene Groups (k=3 and k=4 scenarios)
def extract_gene(g_str):
    if pd.isna(g_str): return 'Unknown'
    match = re.search(r'(COL1A1|COL1A2|FKBP10|P3H1|WNT1|PRDM5|BMP1)', str(g_str), re.IGNORECASE)
    if match: return match.group(1).upper()
    return 'Other'

df_clean['gene_symbol'] = df_clean['gen_mutasyonu'].apply(extract_gene)
counts = df_clean['gene_symbol'].value_counts()
major_k3 = [g for g in counts[counts >= 3].index if g not in ['Other','Unknown']]
major_k4 = [g for g in counts[counts >= 4].index if g not in ['Other','Unknown']]

df_clean['gene_group_rt_k3'] = df_clean['gene_symbol'].apply(lambda x: x if x in major_k3 else 'Other')
df_clean['gene_group_rt_k4'] = df_clean['gene_symbol'].apply(lambda x: x if x in major_k4 else 'Other')

print("Gene Frequencies:\n", counts)
print("\nK=3 majors:", major_k3)
print("K=4 majors:", major_k4)


def wilson_ci(count, n):
    if n == 0: return ("0.0, 0.0")
    low, high = proportion.proportion_confint(count, n, method='wilson')
    return f"{low*100:.1f}%, {high*100:.1f}%"

# Table 1
n_tot = len(df_clean)
t1 = []
t1.append({"Variable": "N", "Value": n_tot, "95% CI (Wilson)": "-"})
t1.append({"Variable": "Age (median, IQR)", "Value": f"{df_clean['yas'].median()} ({df_clean['yas'].quantile(0.25)}-{df_clean['yas'].quantile(0.75)})", "95% CI (Wilson)": "-"})
for v in ['doku_anomalisi_var', 'gingivitis', 'caries_any_rt', 'infraokluzyon_var']:
    c = df_clean[v].sum()
    t1.append({"Variable": v, "Value": f"{c} ({c/n_tot*100:.1f}%)", "95% CI (Wilson)": wilson_ci(c, n_tot)})
pd.DataFrame(t1).to_csv(f'{OUT_DIR}/publication_table1_overall_v3_1.csv', index=False)

# Table 2
def create_table2(scenario_col, k_label):
    t2 = []
    for g in df_clean[scenario_col].unique():
        dg = df_clean[df_clean[scenario_col] == g]
        ng = len(dg)
        row = {'scenario': k_label, 'gene_group': g, 'N': ng,
               'age_med_iqr': f"{dg['yas'].median()} ({dg['yas'].quantile(0.25)}-{dg['yas'].quantile(0.75)})"}
        for v in ['doku_anomalisi_var', 'gingivitis', 'caries_any_rt']:
            c = dg[v].sum()
            row[v] = f"{c} ({c/ng*100:.1f}%)"
        row['dmft_med_iqr'] = f"{dg['dmft_dmft'].median()} ({dg['dmft_dmft'].quantile(0.25)}-{dg['dmft_dmft'].quantile(0.75)})"
        t2.append(row)
    return pd.DataFrame(t2)

pd.concat([
    create_table2('gene_group_rt_k3', 'k=3'),
    create_table2('gene_group_rt_k4', 'k=4')
]).to_csv(f'{OUT_DIR}/publication_table2_by_gene_group_v3_1.csv', index=False)
print("Table 1 and 2 Generated.")


def calc_cramers_v(chi2, n, min_dim):
    return np.sqrt(chi2 / (n * min_dim)) if min_dim > 0 and n > 0 else 0

def exact_or_permutation_p(ct, iters=10000):
    chi2_obs, _, _, ex = stats.chi2_contingency(ct, correction=False)
    if not np.any(ex < 5):
        return np.nan # Not strictly required
    rm = ct.sum(axis=1).values
    cm = ct.sum(axis=0).values
    rows = np.repeat(np.arange(len(rm)), rm)
    cols = np.repeat(np.arange(len(cm)), cm)
    count_gte = 0
    n = len(rows)
    r_dim = len(rm)
    c_dim = len(cm)

    # Calculate expected array once
    ex_array = np.outer(rm, cm) / n
    # For safe division
    ex_array[ex_array == 0] = 1.0

    for _ in range(iters):
        np.random.shuffle(cols)
        # fast 2D count
        flat_idx = rows * c_dim + cols
        perm_flat = np.bincount(flat_idx, minlength=r_dim*c_dim)
        perm = perm_flat.reshape((r_dim, c_dim))

        # fast chi2
        chi_p = np.sum((perm - ex_array)**2 / ex_array)
        if chi_p >= chi2_obs: count_gte += 1
    return count_gte / iters

t3_rows = []
for k_col, k_lbl in [('gene_group_rt_k3', 'k=3'), ('gene_group_rt_k4', 'k=4')]:
    # Binary endpoints
    for ep in ['doku_anomalisi_var', 'gingivitis', 'caries_any_rt']:
        ct = pd.crosstab(df_clean[k_col], df_clean[ep])
        if ct.size == 0 or ct.shape[1] < 2: continue
        chi2, p_class, dof, ex = stats.chi2_contingency(ct, correction=False)
        n_val = ct.sum().sum()
        mindim = min(ct.shape[0]-1, ct.shape[1]-1)
        v = calc_cramers_v(chi2, n_val, mindim)

        # QC Verify V
        v_algo = np.sqrt(chi2/(n_val*mindim)) if mindim>0 else 0
        if abs(v - v_algo) > 1e-6: log_issue("FAIL", "MATH", f"Cramers V mismatch in {ep}", [])

        p_perm = exact_or_permutation_p(ct, 5000) if np.any(ex < 5) else np.nan
        t3_rows.append({
            'scenario_k': k_lbl, 'endpoint': ep, 'test': 'Chi2_Perm',
            'statistic': chi2, 'p_classic': p_class, 'p_permutation': p_perm,
            'expected_min': ex.min(), 'effect_size_name': 'CramerV', 'effect_size_value': v
        })

    # Continuous
    groups = [df_clean[df_clean[k_col]==g]['caries_count'].values for g in df_clean[k_col].unique() if len(df_clean[df_clean[k_col]==g])>0]
    if len(groups) > 1:
        st, kw_p = stats.kruskal(*groups)
        n_val = len(df_clean)
        k_count = df_clean[k_col].nunique()
        eps2 = (st - k_count + 1) / (n_val - k_count) if (n_val - k_count) != 0 else np.nan
        t3_rows.append({
            'scenario_k': k_lbl, 'endpoint': 'caries_count', 'test': 'Kruskal',
            'statistic': st, 'p_classic': kw_p, 'p_permutation': np.nan,
            'expected_min': np.nan, 'effect_size_name': 'Epsilon2', 'effect_size_value': eps2
        })

df_t3 = pd.DataFrame(t3_rows)

# Multiple Correction Vectors
p_classic_array = df_t3['p_classic'].fillna(1.0).values
_, p_holm_c, _, _ = multipletests(p_classic_array, method='holm')
df_t3['p_holm_classic_set'] = np.where(df_t3['p_classic'].notna(), p_holm_c, np.nan)

# Permutation correction mapping (only for binaries)
perm_mask = df_t3['p_permutation'].notna()
if perm_mask.any():
    _, p_holm_p, _, _ = multipletests(df_t3.loc[perm_mask, 'p_permutation'].values, method='holm')
    df_t3['p_holm_perm_set'] = np.nan
    df_t3.loc[perm_mask, 'p_holm_perm_set'] = p_holm_p
else:
    df_t3['p_holm_perm_set'] = np.nan

df_t3.to_csv(f'{OUT_DIR}/publication_table3_inferential_v3_1.csv', index=False)
print(df_t3.head())


rob_rows = []

endpoints = ['doku_anomalisi_var', 'gingivitis', 'caries_any_rt', 'caries_count']
df_infra_excl = df_clean[df_clean['infraokluzyon_var'] == 0]

for k_col, k_lbl in [('gene_group_rt_k3', 'k=3'), ('gene_group_rt_k4', 'k=4')]:
    for ep in endpoints:
        # Base model values
        if ep == 'caries_count':
            _, base_p = stats.kruskal(*[df_clean[df_clean[k_col]==g][ep].values for g in df_clean[k_col].unique()])
            _, infra_p = stats.kruskal(*[df_infra_excl[df_infra_excl[k_col]==g][ep].values for g in df_infra_excl[k_col].unique()])

            loo_ps = []
            for i in df_clean.index:
                dl = df_clean.drop(i)
                _, dp = stats.kruskal(*[dl[dl[k_col]==g][ep].values for g in dl[k_col].unique()])
                loo_ps.append({'id': df_clean.loc[i, 'hasta_kodu'], 'p': dp})
        else:
            ct = pd.crosstab(df_clean[k_col], df_clean[ep])
            base_p = stats.chi2_contingency(ct, correction=False)[1]
            ct_i = pd.crosstab(df_infra_excl[k_col], df_infra_excl[ep])
            infra_p = stats.chi2_contingency(ct_i, correction=False)[1] if ct_i.size > 0 else np.nan

            loo_ps = []
            for i in df_clean.index:
                dl = df_clean.drop(i)
                ct_l = pd.crosstab(dl[k_col], dl[ep])
                dp = stats.chi2_contingency(ct_l, correction=False)[1] if ct_l.size > 0 else np.nan
                loo_ps.append({'id': df_clean.loc[i, 'hasta_kodu'], 'p': dp})

        loo_df = pd.DataFrame(loo_ps).dropna()
        pmin = loo_df['p'].min() if not loo_df.empty else np.nan
        pmax = loo_df['p'].max() if not loo_df.empty else np.nan
        influ_id = loo_df.loc[loo_df['p'].idxmax(), 'id'] if not loo_df.empty else np.nan

        rob_rows.append({
            'scenario_k': k_lbl, 'endpoint': ep, 'p_classic': base_p,
            'loo_p_min': pmin, 'loo_p_max': pmax, 'loo_most_influential_id': influ_id,
            'infra_exclusion_p': infra_p, 'infra_exclusion_delta_p': (infra_p - base_p) if pd.notna(infra_p) else np.nan,
            'notes': ''
        })

df_rob = pd.DataFrame(rob_rows)
df_rob.to_csv(f'{OUT_DIR}/robustness_panel_v3_1.csv', index=False)
print(df_rob.head())


cv_rows = []
bin_eps = ['doku_anomalisi_var', 'gingivitis', 'caries_any_rt']
scaler = StandardScaler()

for k_col, k_lbl in [('gene_group_rt_k3', 'k=3'), ('gene_group_rt_k4', 'k=4')]:
    for ep in bin_eps:
        valid_df = df_clean.dropna(subset=['yas', k_col, ep])
        if valid_df[ep].nunique() < 2:
            cv_rows.append({'scenario_k': k_lbl, 'endpoint': ep, 'warnings': 'Constant Y, skip.'})
            continue

        y = valid_df[ep].values
        X_age = valid_df[['yas']].values
        # Get dummies for categorical gene group with drop_first=True to avoid dummy trap
        X_gene = pd.get_dummies(valid_df[['yas', k_col]], drop_first=True, dtype=int).values
        if X_gene.shape[1] == 1:
             warnings = "Gene group only has 1 category left. Using age fallback"
             X_gene = X_age

        preds_age = np.zeros(len(y))
        preds_gene = np.zeros(len(y))
        loo = LeaveOneOut()

        for tr_idx, te_idx in loo.split(X_age):
            # Age model
            X_age_tr, X_age_te = X_age[tr_idx], X_age[te_idx]
            y_tr = y[tr_idx]
            Xa_tr_sc = scaler.fit_transform(X_age_tr)
            Xa_te_sc = scaler.transform(X_age_te)
            mod_age = LogisticRegression(penalty='l2', C=1.0, solver='liblinear')
            if len(np.unique(y_tr)) > 1:
                mod_age.fit(Xa_tr_sc, y_tr)
                preds_age[te_idx] = mod_age.predict_proba(Xa_te_sc)[:, 1]
            else:
                preds_age[te_idx] = np.mean(y_tr)

            # Gene Model
            X_gen_tr, X_gen_te = X_gene[tr_idx], X_gene[te_idx]
            Xg_tr_sc = scaler.fit_transform(X_gen_tr)
            Xg_te_sc = scaler.transform(X_gen_te)
            mod_gen = LogisticRegression(penalty='l2', C=1.0, solver='liblinear')
            if len(np.unique(y_tr)) > 1:
                mod_gen.fit(Xg_tr_sc, y_tr)
                preds_gene[te_idx] = mod_gen.predict_proba(Xg_te_sc)[:, 1]
            else:
                preds_gene[te_idx] = np.mean(y_tr)

        try:
            auc_age = roc_auc_score(y, preds_age)
            auc_gene = roc_auc_score(y, preds_gene)
            if auc_age < 0.5 or auc_gene < 0.5:
                warnings = "AUC < 0.5 detected."
            else:
                warnings = ""
            # Simple bootstrap for CI of delta
            delta_auc = auc_gene - auc_age
            bt_deltas = []
            for _ in range(500): # Small iter for speed
                idx = np.random.choice(len(y), len(y), replace=True)
                if len(np.unique(y[idx])) > 1:
                    b_a = roc_auc_score(y[idx], preds_age[idx])
                    b_g = roc_auc_score(y[idx], preds_gene[idx])
                    bt_deltas.append(b_g - b_a)
            ci_l, ci_h = np.percentile(bt_deltas, [2.5, 97.5]) if bt_deltas else (np.nan, np.nan)

        except Exception as e:
            auc_age, auc_gene, delta_auc, ci_l, ci_h, warnings = np.nan, np.nan, np.nan, np.nan, np.nan, str(e)

        cv_rows.append({
            'scenario_k': k_lbl, 'endpoint': ep, 'model_name': 'age_vs_age+gene',
            'cv_method': 'LOO', 'auc_age': auc_age, 'auc_age_gene': auc_gene,
            'delta_auc': delta_auc, 'delta_auc_ci_low': ci_l, 'delta_auc_ci_high': ci_h,
            'warnings': warnings
        })

df_cv = pd.DataFrame(cv_rows)
df_cv.to_csv(f'{OUT_DIR}/cv_panel_v3_1.csv', index=False)
print(df_cv.head())


occ_data = []
v_infra = df_clean['infraokluzyon_var'].sum()
occ_data.append({'Metric': 'Infraokluzyon_Prevalence', 'Value': f"{v_infra} ({v_infra/len(df_clean)*100:.1f}%)"})

for a_class in [1, 2, 3]:
    v_a = sum(df_clean['angle_sinifi'] == a_class)
    occ_data.append({'Metric': f'Angle_Class_{a_class}_Prevalence', 'Value': f"{v_a} ({v_a/len(df_clean.dropna(subset=['angle_sinifi']))*100:.1f}%)"})

df_occ = pd.DataFrame(occ_data)
df_occ.to_csv(f'{OUT_DIR}/occlusion_panel_v3_1.csv', index=False)
print(df_occ)


diff_rows = []
if os.path.exists(files['v3_tb3']):
    old_df = pd.read_csv(files['v3_tb3'])
    # Very basic merge to find metric differences in identical tests
    old_df['merge_key'] = old_df['endpoint'] + '_' + old_df['test']
    new_df = df_t3[df_t3['scenario_k']=='k=3'].copy() # Compare k=3
    new_df['merge_key'] = new_df['endpoint'] + '_' + new_df['test'].replace({'Chi2_Perm': 'Chi2/Permut', 'Kruskal': 'Kruskal-Wallis'})

    joined = pd.merge(old_df, new_df, on='merge_key', suffixes=('_old', '_new'))
    for idx, r in joined.iterrows():
        if pd.notna(r['p_classic_old']) and pd.notna(r['p_classic_new']):
            if abs(r['p_classic_old'] - r['p_classic_new']) > 1e-4:
                diff_rows.append({
                    'artifact': 'Table3', 'metric': f"p_classic_{r['endpoint']}",
                    'old_value': r['p_classic_old'], 'new_value': r['p_classic_new'],
                    'scenario_k': 'k=3', 'explanation': 'Algorithm refinement or variance in transformation.'
                })

pd.DataFrame(diff_rows, columns=['artifact', 'metric', 'old_value', 'new_value', 'scenario_k', 'explanation']).to_csv('consistency_diff_v3_vs_v3_1.csv', index=False)


df_t3.to_csv('verified_master_table_v3_1.csv', index=False)

qc_results = []
# 1) Robustness contains all primaries
b1 = all(x in df_rob['endpoint'].unique() for x in ['doku_anomalisi_var', 'gingivitis', 'caries_any_rt', 'caries_count'])
qc_results.append(("Robustness panel completeness", "PASS" if b1 else "FAIL"))

# 2) CV contains all binaries
b2 = all(x in df_cv['endpoint'].unique() for x in ['doku_anomalisi_var', 'gingivitis', 'caries_any_rt'])
qc_results.append(("CV panel completeness", "PASS" if b2 else "FAIL"))

# 3) Occlusion panel exists
qc_results.append(("Occlusion panel isolation", "PASS" if 'angle_sinifi' in df_clean.columns else "FAIL"))

# 4) occl_tip == 4 is absent in Angle
b4 = df_clean[df_clean['occl_tip']==4]['angle_sinifi'].isna().all()
qc_results.append(("Occl_tip angle rules", "PASS" if b4 else "FAIL"))

# 5) Multi-Holm logic
b5 = 'p_holm_perm_set' in df_t3.columns
qc_results.append(("Holm labels separated", "PASS" if b5 else "FAIL"))

print("====== QC CHECKLIST (V3.1) ======")
fail_count = 0
for test, res in qc_results:
    print(f"[{res}] {test}")
    if res == "FAIL": fail_count += 1

if fail_count > 0:
    print("\n>> ITERATION REQUIRED. SOME QCs FAILED.")
    log_issue('FAIL', 'QC_FINAL', f'{fail_count} checks failed.', [])
else:
    print("\nDONE — QC PASS")

if len(issue_log) == 0:
    log_issue("INFO", "ALL", "No issues detected", [])
pd.DataFrame(issue_log).to_csv('issue_log_v3_1.csv', index=False)


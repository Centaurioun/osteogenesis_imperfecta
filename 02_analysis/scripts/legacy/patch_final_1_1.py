with open('oi_oro_dental_master_FINAL_1.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("OUT_DIR = 'outputs_FINAL_1'", "OUT_DIR = 'outputs_FINAL_1_1'")

old_get_auc = """def get_auc_ci(y_true, preds_a, preds_g, n_boot=2000, seed=SEED_GLOBAL):
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
    if len(delta_aucs) > 0:
        return np.percentile(delta_aucs, 2.5), np.percentile(delta_aucs, 97.5), len(delta_aucs) < n_boot
    return np.nan, np.nan, True"""

new_get_auc = """def get_auc_ci(y_true, preds_a, preds_g, n_boot=2000, seed=SEED_GLOBAL):
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

    return ci_l, ci_h, boot_stats, has_warn"""

text = text.replace(old_get_auc, new_get_auc)

old_loo = """                try:
                    auc_a, auc_g = roc_auc_score(y, preds_a), roc_auc_score(y, preds_g)
                    ci_l, ci_h, has_warn = get_auc_ci(y, preds_a, preds_g, n_boot=manifest["bootstrap_iters"])
                    warns = []
                    if auc_a < 0.5 or auc_g < 0.5: warns.append("AUC < 0.5")
                    if has_warn: warns.append("Some bootstrap samples had < 2 classes")
                    cv_rows.append({
                        'scenario': sk, 'endpoint': ep, 'cv_method': cv_name,
                        'auc_age': auc_a, 'auc_age_gene': auc_g, 'delta_auc': auc_g-auc_a,
                        'delta_auc_ci_low': ci_l, 'delta_auc_ci_high': ci_h, 'warnings': "; ".join(warns)
                    })
                except Exception as e:
                    cv_rows.append({'scenario': sk, 'endpoint': ep, 'cv_method': cv_name, 'warnings': str(e)})"""

new_loo = """                try:
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
                        'delta_auc_ci_low': ci_l, 'delta_auc_ci_high': ci_h
                    }
                    row.update(b_stats)
                    row['warnings'] = "; ".join(warns)
                    cv_rows.append(row)
                except Exception as e:
                    cv_rows.append({'scenario': sk, 'endpoint': ep, 'cv_method': cv_name, 'warnings': str(e)})"""

text = text.replace(old_loo, new_loo)


old_rskf = """                if aucs_a and aucs_g:
                    auc_a, auc_g = np.mean(aucs_a), np.mean(aucs_g)
                    p_a_mean, p_g_mean = oof_a.mean(axis=0), oof_g.mean(axis=0)
                    ci_l, ci_h, has_warn = get_auc_ci(y, p_a_mean, p_g_mean, n_boot=manifest["bootstrap_iters"])
                    warns = []
                    if auc_a < 0.5 or auc_g < 0.5: warns.append("AUC < 0.5")
                    if has_warn: warns.append("Some bootstrap samples had < 2 classes")
                    cv_rows.append({
                        'scenario': sk, 'endpoint': ep, 'cv_method': cv_name,
                        'auc_age': auc_a, 'auc_age_gene': auc_g, 'delta_auc': auc_g-auc_a,
                        'delta_auc_ci_low': ci_l, 'delta_auc_ci_high': ci_h, 'warnings': "; ".join(warns)
                    })"""

new_rskf = """                if aucs_a and aucs_g:
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
                        'delta_auc_ci_low': ci_l, 'delta_auc_ci_high': ci_h
                    }
                    row.update(b_stats)
                    row['warnings'] = "; ".join(warns)
                    cv_rows.append(row)"""

text = text.replace(old_rskf, new_rskf)

old_master = """    df_master_cv = pd.DataFrame(master_cv_rows)
    master_merged = df_t3_primary.merge(df_rob_primary[['endpoint', 'loo_p_min', 'loo_p_max', 'infra_exclusion_delta_p']], on='endpoint', how='left')
    master_merged = master_merged.merge(df_master_cv[['endpoint', 'primary_cv_method', 'auc_age', 'auc_age_gene', 'delta_auc', 'delta_auc_ci_low', 'delta_auc_ci_high', 'loo_delta_auc']], on='endpoint', how='left')"""

new_master = """    df_master_cv = pd.DataFrame(master_cv_rows)
    master_merged = df_t3_primary.merge(df_rob_primary[['endpoint', 'loo_p_min', 'loo_p_max', 'infra_exclusion_delta_p']], on='endpoint', how='left')
    cols_to_keep = ['endpoint', 'primary_cv_method', 'n_pos', 'n_neg', 'auc_age', 'auc_age_gene', 'delta_auc', 'delta_auc_ci_low', 'delta_auc_ci_high', 'n_boot_total', 'n_boot_valid', 'n_boot_dropped', 'boot_drop_rate', 'delta_auc_boot_mean', 'delta_auc_boot_median', 'loo_delta_auc']
    master_merged = master_merged.merge(df_master_cv[[c for c in cols_to_keep if c in df_master_cv.columns]], on='endpoint', how='left')"""

text = text.replace(old_master, new_master)


old_diff = """try:
    final_t3 = pd.read_csv('outputs_FINAL/publication_table3_inferential_FINAL.csv')
    joined = pd.merge(final_t3, df_t3_primary, on='endpoint', suffixes=('_old', '_new'))"""

new_diff = """try:
    final_t3 = pd.read_csv('outputs_FINAL_1/publication_table3_inferential_FINAL.csv')
    joined = pd.merge(final_t3, df_t3_primary, on='endpoint', suffixes=('_old', '_new'))"""

text = text.replace(old_diff, new_diff)


old_diff2 = """pd.DataFrame(diff_report).to_csv(f'{OUT_DIR}/consistency_diff_FINAL_vs_FINAL_1.csv', index=False)
except Exception as e:
    err = f"Diff tool failed to run: {e}"
    pd.DataFrame([{'Item': 'ERROR', 'Change': err}]).to_csv(f'{OUT_DIR}/consistency_diff_FINAL_vs_FINAL_1.csv', index=False)"""

new_diff2 = """pd.DataFrame(diff_report).to_csv(f'{OUT_DIR}/consistency_diff_FINAL_1_vs_FINAL_1_1.csv', index=False)

    cv_old = pd.read_csv('outputs_FINAL_1/cv_panel_FINAL.csv')
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
        pd.DataFrame(diff_report).to_csv(f'{OUT_DIR}/consistency_diff_FINAL_1_vs_FINAL_1_1.csv', index=False)

except Exception as e:
    err = f"Diff tool failed to run: {e}"
    pd.DataFrame([{'Item': 'ERROR', 'Change': err}]).to_csv(f'{OUT_DIR}/consistency_diff_FINAL_1_vs_FINAL_1_1.csv', index=False)"""

text = text.replace(old_diff2, new_diff2)


old_qc = """print("====== QC CHECKLIST (FINAL.1) ======")
fails = 0
for t, r in qc_res:
    print(f"[{r}] {t}")
    if r == "FAIL": fails += 1

if fails > 0:
    print(">> ITERATION REQUIRED. SOME QCs FAILED.")
else:
    print("DONE — QC PASS (FINAL.1)")"""

new_qc = """qc_res.append(('Bootstrap bookkeeping valid', 'PASS' if (df_cv_primary['n_boot_valid'] + df_cv_primary['n_boot_dropped']).equals(df_cv_primary['n_boot_total']) else 'FAIL'))
qc_res.append(('CV values identical to FINAL.1', 'PASS' if len([x for x in issue_log if x.get('category') == 'CV_DIFF']) == 0 else 'FAIL'))

print("====== QC CHECKLIST (FINAL.1.1) ======")
fails = 0
for t, r in qc_res:
    print(f"[{r}] {t}")
    if r == "FAIL": fails += 1

if fails > 0:
    print(">> ITERATION REQUIRED. SOME QCs FAILED.")
else:
    print("DONE — QC PASS (FINAL.1.1)")"""

text = text.replace(old_qc, new_qc)

text = text.replace('FINAL.1 GATE', 'FINAL.1.1 GATE')
text = text.replace('Osteogenesis Imperfecta (Camber) Master Analysis - FINAL.1', 'Osteogenesis Imperfecta (Camber) Master Analysis - FINAL.1.1')


with open('oi_oro_dental_master_FINAL_1_1.py', 'w', encoding='utf-8') as f:
    f.write(text)

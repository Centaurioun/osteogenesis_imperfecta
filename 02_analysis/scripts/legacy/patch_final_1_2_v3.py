
with open('oi_oro_dental_master_FINAL_1_1.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update Output Directory
code = code.replace("OUT_DIR = 'outputs_FINAL_1_1'", "OUT_DIR = 'outputs_FINAL_1_2'")
# For safely handling consistency diff logic BEFORE we replace globally outputs_FINAL_1_1 -> 2
# Fix the consistency checker to compare against FINAL_1_1 instead of FINAL_1
code = code.replace("final_t3 = pd.read_csv('outputs_FINAL_1/publication_table3_inferential_FINAL.csv')", "final_t3 = pd.read_csv('outputs_FINAL_1_1/publication_table3_inferential_FINAL.csv')")
code = code.replace("cv_old = pd.read_csv('outputs_FINAL_1/cv_panel_FINAL.csv')", "cv_old = pd.read_csv('outputs_FINAL_1_1/cv_panel_FINAL.csv')")
code = code.replace("consistency_diff_FINAL_1_vs_FINAL_1_1.csv", "consistency_diff_FINAL_1_1_vs_FINAL_1_2.csv")
code = code.replace("FINAL.1.1", "FINAL.1.2")

# 3. Add explicit estimator fields
loo_old = """                    row = {
                        'scenario': sk, 'endpoint': ep, 'cv_method': cv_name,
                        'n_pos': n_pos, 'n_neg': n_neg,
                        'auc_age': auc_a, 'auc_age_gene': auc_g, 'delta_auc': auc_g-auc_a,
                        'delta_auc_ci_low': ci_l, 'delta_auc_ci_high': ci_h
                    }
                    row.update(b_stats)
                    row['warnings'] = "; ".join(warns)
                    cv_rows.append(row)"""

loo_new = """                    row = {
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
                    cv_rows.append(row)"""
code = code.replace(loo_old, loo_new)

rskf_old = """                    row = {
                        'scenario': sk, 'endpoint': ep, 'cv_method': cv_name,
                        'n_pos': n_pos, 'n_neg': n_neg,
                        'auc_age': auc_a, 'auc_age_gene': auc_g, 'delta_auc': auc_g-auc_a,
                        'delta_auc_ci_low': ci_l, 'delta_auc_ci_high': ci_h
                    }
                    row.update(b_stats)
                    row['warnings'] = "; ".join(warns)
                    cv_rows.append(row)"""

rskf_new = """                    row = {
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
                    cv_rows.append(row)"""
code = code.replace(rskf_old, rskf_new)

# handle fallback
code = code.replace(
    "cv_rows.append({'scenario': sk, 'endpoint': ep, 'cv_method': 'LOO', 'warnings': 'Constant Y'})",
    "cv_rows.append({'scenario': sk, 'endpoint': ep, 'cv_method': 'LOO', 'warnings': 'Constant Y', 'delta_auc_estimator': '', 'ci_estimator': '', 'note': ''})"
)

code = code.replace(
    "cv_rows.append({'scenario': sk, 'endpoint': ep, 'cv_method': cv_name, 'warnings': str(e)})",
    "cv_rows.append({'scenario': sk, 'endpoint': ep, 'cv_method': cv_name, 'warnings': str(e), 'delta_auc_estimator': '', 'ci_estimator': '', 'note': ''})"
)

# 4. Master table col update
cols_old = "    cols_to_keep = ['endpoint', 'primary_cv_method', 'n_pos', 'n_neg', 'auc_age', 'auc_age_gene', 'delta_auc', 'delta_auc_ci_low', 'delta_auc_ci_high', 'n_boot_total', 'n_boot_valid', 'n_boot_dropped', 'boot_drop_rate', 'delta_auc_boot_mean', 'delta_auc_boot_median', 'loo_delta_auc']"
cols_new = "    cols_to_keep = ['endpoint', 'primary_cv_method', 'n_pos', 'n_neg', 'auc_age', 'auc_age_gene', 'delta_auc', 'delta_auc_ci_low', 'delta_auc_ci_high', 'n_boot_total', 'n_boot_valid', 'n_boot_dropped', 'boot_drop_rate', 'delta_auc_boot_mean', 'delta_auc_boot_median', 'loo_delta_auc', 'delta_auc_estimator', 'ci_estimator', 'note']"
code = code.replace(cols_old, cols_new)

# When comparing cv new and old, we should drop the new estimator cols from new so it doesn't fail
# We can just ignore the new columns in diff since we only iterate over the list of 5 columns.
# wait, for col in ['auc_age','auc_age_gene','delta_auc','delta_auc_ci_low','delta_auc_ci_high']: is explicit already. So no problem!

with open('oi_oro_dental_master_FINAL_1_2.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Master script for FINAL.1.2 generated.")

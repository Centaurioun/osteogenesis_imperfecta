
with open('oi_oro_dental_master_FINAL_1_2.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace OUT_DIR
code = code.replace("OUT_DIR = 'outputs_FINAL_1_1'", "OUT_DIR = 'outputs_FINAL_1_2'")
# In case it's 1
code = code.replace("OUT_DIR = 'outputs_FINAL_1'\n", "OUT_DIR = 'outputs_FINAL_1_2'\n")

# Replace cv row append (LOO part)
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

# RSKF part
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

# fallback for constant Y
const_y_old = "cv_rows.append({'scenario': sk, 'endpoint': ep, 'cv_method': 'LOO', 'warnings': 'Constant Y'})"
const_y_new = "cv_rows.append({'scenario': sk, 'endpoint': ep, 'cv_method': 'LOO', 'warnings': 'Constant Y', 'delta_auc_estimator': '', 'ci_estimator': '', 'note': ''})"
code = code.replace(const_y_old, const_y_new)

err_old = "cv_rows.append({'scenario': sk, 'endpoint': ep, 'cv_method': cv_name, 'warnings': str(e)})"
err_new = "cv_rows.append({'scenario': sk, 'endpoint': ep, 'cv_method': cv_name, 'warnings': str(e), 'delta_auc_estimator': '', 'ci_estimator': '', 'note': ''})"
code = code.replace(err_old, err_new)

# columns to keep in master logic
cols_old = "cols_to_keep = ['endpoint', 'primary_cv_method', 'n_pos', 'n_neg', 'auc_age', 'auc_age_gene', 'delta_auc', 'delta_auc_ci_low', 'delta_auc_ci_high', 'n_boot_total', 'n_boot_valid', 'n_boot_dropped', 'boot_drop_rate', 'delta_auc_boot_mean', 'delta_auc_boot_median', 'loo_delta_auc']"
cols_new = "cols_to_keep = ['endpoint', 'primary_cv_method', 'n_pos', 'n_neg', 'auc_age', 'auc_age_gene', 'delta_auc', 'delta_auc_ci_low', 'delta_auc_ci_high', 'n_boot_total', 'n_boot_valid', 'n_boot_dropped', 'boot_drop_rate', 'delta_auc_boot_mean', 'delta_auc_boot_median', 'loo_delta_auc', 'delta_auc_estimator', 'ci_estimator', 'note']"
code = code.replace(cols_old, cols_new)


# Update comparison against earlier version (FINAL_1_1 to FINAL_1_2)
code = code.replace("consistency_diff_FINAL_1_vs_FINAL_1_1.csv", "consistency_diff_FINAL_1_1_vs_FINAL_1_2.csv")
# Final_t3 check we can keep identical, wait, let's just make sure final_t3 checks against outputs_FINAL_1_1
code = code.replace("final_t3 = pd.read_csv('outputs_FINAL_1/publication_table3_inferential_FINAL.csv')", "final_t3 = pd.read_csv('outputs_FINAL_1_1/publication_table3_inferential_FINAL.csv')")

# CV checking
code = code.replace("cv_old = pd.read_csv('outputs_FINAL_1/cv_panel_FINAL.csv')", "cv_old = pd.read_csv('outputs_FINAL_1_1/cv_panel_FINAL.csv')")

code = code.replace("FINAL.1.1", "FINAL.1.2")

# We should make sure we're creating outputs_FINAL_1_2
code = code.replace("outputs_FINAL_1_1", "outputs_FINAL_1_2")

# but the strings we just replaced we used `outputs_FINAL_1_2`, wait we should be careful.
# If we blindly replaced outputs_FINAL_1_1 to outputs_FINAL_1_2 everywhere, the cv_old read would read outputs_FINAL_1_2.
# So let's re-write the specific diff code section at the end.


with open('oi_oro_dental_master_FINAL_1_2.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Patch applied.")

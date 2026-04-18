import re

with open('oi_oro_dental_master_FINAL_1_2.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update output directory
code = code.replace("OUT_DIR = 'outputs_FINAL_1_1'", "OUT_DIR = 'outputs_FINAL_1_2'")
# Check in case it said outputs_FINAL_1
code = code.replace("OUT_DIR = 'outputs_FINAL_1'", "OUT_DIR = 'outputs_FINAL_1_2'")

# 2. Add extra cols to CV rows where they are built
# There are two places where cv_rows.append(row) happens with data.
# First for LOO:
loo_row_pattern = r"(row = \{\s*'scenario': sk, 'endpoint': ep, 'cv_method': cv_name,\s*'n_pos': n_pos, 'n_neg': n_neg,\s*'auc_age': auc_a, 'auc_age_gene': auc_g, 'delta_auc': auc_g-auc_a,\s*'delta_auc_ci_low': ci_l, 'delta_auc_ci_high': ci_h)(\s*\})"
loo_row_repl = r"\1,\n                        'delta_auc_estimator': 'loo_auc' if cv_name == 'LOO' else 'mean_auc_over_repeats',\n                        'ci_estimator': 'paired_bootstrap_on_oof_probs' if cv_name == 'LOO' else 'paired_bootstrap_on_mean_oof_probs'\2"
code = re.sub(loo_row_pattern, loo_row_repl, code)

# 3. Add note logic before appending row
# We replace row['warnings'] = ... with row['warnings'] = ... plus the note logic
note_logic = """
                    row.update(b_stats)
                    note_text = ""
                    if pd.notna(b_stats.get('delta_auc_boot_mean', np.nan)):
                        if abs(b_stats['delta_auc_boot_mean'] - (auc_g-auc_a)) >= 0.05:
                            note_text = "delta_auc_boot_mean materially differs from delta_auc"
                    row['note'] = note_text
                    row['warnings'] = "; ".join(warns)
                    cv_rows.append(row)
"""

# Find the exact lines:
code = code.replace("""                    row.update(b_stats)\n                    row['warnings'] = \"; \".join(warns)\n                    cv_rows.append(row)""", note_logic.strip('\n'))
code = code.replace("""                    row.update(b_stats)\r\n                    row['warnings'] = \"; \".join(warns)\r\n                    cv_rows.append(row)""", note_logic.strip('\n'))

# 4. cols_to_keep update
old_cols = "['endpoint', 'primary_cv_method', 'n_pos', 'n_neg', 'auc_age', 'auc_age_gene', 'delta_auc', 'delta_auc_ci_low', 'delta_auc_ci_high', 'n_boot_total', 'n_boot_valid', 'n_boot_dropped', 'boot_drop_rate', 'delta_auc_boot_mean', 'delta_auc_boot_median', 'loo_delta_auc']"
new_cols = "['endpoint', 'primary_cv_method', 'n_pos', 'n_neg', 'auc_age', 'auc_age_gene', 'delta_auc', 'delta_auc_ci_low', 'delta_auc_ci_high', 'n_boot_total', 'n_boot_valid', 'n_boot_dropped', 'boot_drop_rate', 'delta_auc_boot_mean', 'delta_auc_boot_median', 'loo_delta_auc', 'delta_auc_estimator', 'ci_estimator', 'note']"
code = code.replace(old_cols, new_cols)

# 5. Handle consistency diff against FINAL_1_1
code = re.sub(r"pd\.read_csv\(f'\{OUT_DIR\}/cv_panel_FINAL\.csv'\)", "pd.read_csv(f'{OUT_DIR}/cv_panel_FINAL.csv').drop(columns=['delta_auc_estimator', 'ci_estimator', 'note'], errors='ignore')", code)
code = re.sub(r"pd\.read_csv\('outputs_FINAL_1/cv_panel_FINAL\.csv'\)", "pd.read_csv('outputs_FINAL_1_1/cv_panel_FINAL.csv')", code)
code = code.replace("outputs_FINAL_1_vs_FINAL_1_1.csv", "outputs_FINAL_1_1_vs_FINAL_1_2.csv")


with open('oi_oro_dental_master_FINAL_1_2.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Patch applied successfully.")

# derived_variable_check_log

- `occl_tip==4` doğrulandı ve Angle analizinde dışlandı (angle_sinifi_rt=NaN, infraokluzyon_var_rt=1).
- Angle dışlanan hasta_kodu: 5
- `dmft_dmft` count-like olarak taşındı (`caries_count_rt`), binary türev `caries_any_rt = dmft_dmft > 0`.
- Türetilmiş değişken eşleşme kontrolleri:
  - infraokluzyon_var: PASS (mismatch_n=0)
  - angle_sinifi: PASS (mismatch_n=0)
  - caries_any: PASS (mismatch_n=0)
  - doku_anomalisi_var: PASS (mismatch_n=0)

# CV Revalidation Notes (Round 2)

## Objective

A12cv satırındaki nokta tahmini-güven aralığı uyumsuzluğu doğrulanmış, A13cv/A14cv satırları birlikte tekrar kontrol edilmiştir.

## Findings

### A12cv (`doku_anomalisi_var_rt`, RSKF)

- Reported delta_auc: 0.3420416667
- Reported CI: (0.3477971014, 0.7984395586)
- Durum: **inconsistent** (nokta tahmini alt sınırın dışında)
- Ek gözlem: `delta_auc_boot_mean=0.5743409899` CI içinde yer alıyor.

Yorum:
Bu satırda CI’nin, ham `delta_auc` nokta tahmininden ziyade bootstrap dağılım özetine (özellikle boot mean/median) daha yakın bir merkez etrafında oluştuğu görülmektedir. Bu nedenle round2’de satır “uyumsuz” olarak açıkça işaretlenmiştir.

### A13cv (`caries_any_rt`, RSKF)

- delta_auc ve CI tutarlı (point_within_ci=True)

### A14cv (`gingivitis`, RSKF)

- delta_auc ve CI tutarlı (point_within_ci=True)

## Action taken

- A12cv için tutarsızlık gizlenmemiş, `cv_rows_revalidated.csv` içinde explicit status ile raporlanmıştır.
- A13cv ve A14cv satırları “consistent” olarak yeniden doğrulanmıştır.

## Output reference

- `09_round2_outputs/cv_rows_revalidated.csv`

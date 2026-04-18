# ABBREVIATIONS_GLOSSARY

Bu çalışma paketinde ve manuscript yazımında geçen ana kısaltmalar aşağıda açıklanmıştır.

- **AI**: Artificial Intelligence
- **AUC**: Area Under the Receiver Operating Characteristic Curve
- **CI**: Confidence Interval
- **CV**: Cross-Validation
- **DI**: Dentinogenesis Imperfecta
- **DMFT/dmft**: Çürük, kayıp, dolgulu diş indeksi; bu projede `dmft_dmft` sütunu klasik indeks gibi değil, count benzeri yorumlanmıştır
- **FKBP10 / COL1A1 / COL1A2 / P3H1**: OI ile ilişkili gen grupları / gen sembolleri
- **Holm**: Holm-Bonferroni çoklu karşılaştırma düzeltmesi
- **IQR**: Interquartile Range
- **IRB / Ethics**: Etik kurul bağlamı
- **LOO**: Leave-One-Out cross-validation
- **MLE**: Maximum Likelihood Estimation
- **N**: Örneklem büyüklüğü
- **OI**: Osteogenesis Imperfecta
- **OOF**: Out-of-fold prediction
- **Primary**: Nihai manuscript için authoritative ana analiz senaryosu
- **QC**: Quality Control
- **RSKF**: Repeated Stratified K-Fold cross-validation
- **Runtime gene group**: `gen_mutasyonu` bilgisinden analiz sırasında türetilen gen grubu
- **SAP**: Statistical Analysis Plan
- **Wilson CI**: Binom prevalanslar için Wilson güven aralığı
- **χ² / Chi2**: Ki-kare istatistiği
- **Cramer's V**: Kategorik ilişki için etki büyüklüğü
- **ε² / Epsilon-squared**: Kruskal–Wallis için etki büyüklüğü

## Değişken adıyla ilgili önemli notlar

- `doku_anomalisi_var_rt`: runtime türetilen doku anomalisi var/yok değişkeni
- `caries_any_rt`: `dmft_dmft > 0` kuralıyla türetilen binary çürük varlığı değişkeni
- `caries_count`: `dmft_dmft` sütununun count-benzeri yorumu
- `infraokluzyon_var`: `occl_tip == 4` durumunda işaretlenen bağımsız bayrak
- `delta_auc`: age-only ve age+gene modellerinin AUC farkı
- `delta_auc_estimator`: AUC farkının hangi özetleyici mantıkla hesaplandığını açıklar
- `ci_estimator`: ΔAUC güven aralığının hangi bootstrap mantığıyla üretildiğini açıklar
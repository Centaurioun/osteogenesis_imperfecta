# MANUSCRIPT_ASSEMBLY_GUIDE

Bu rehber, manuscript bölümlerini hangi dosyalardan ve hangi sırayla yazmanız gerektiğini pratik olarak özetler.

## 1) Introduction

### Kullanılacak ana dosyalar
- `01_protocol_and_docs/camber_study_brief_v1.md`
- `01_protocol_and_docs/Osteogenesis-Imperfecta-Oro-Denta-Bulgular-Etik-Kurul-Basvuru-Rev3.md`
- `01_protocol_and_docs/final_1.md`

### Bu bölümde alınacak ana mesajlar
- OI’de oro-dental bulgular klinik açıdan önemlidir.
- Küçük örneklemli bu kohortta prevalans ve genetik ilişkiler aynı çatı altında değerlendirilmiştir.
- Çalışmanın amacı hem prevalansı tanımlamak hem de gen gruplarıyla ilişki sinyallerini küçük örnekleme uygun yöntemlerle sınamaktır.

## 2) Methods

### Kullanılacak ana dosyalar
- `01_protocol_and_docs/camber_sap_v2_publication_ready.md`
- `02_source_data/metadata/codebook_v3_fixed.md`
- `03_analysis_scripts/oi_oro_dental_master_FINAL_1_2.py`
- `06_ai_handoff_context/AGENTS.md`
- `06_ai_handoff_context/copilot-instructions.md`
- `04_final_outputs/OUTPUT_SCHEMA_AND_VARIABLE_LINEAGE.md`
- `04_final_outputs/REPRODUCIBILITY_ENVIRONMENT.md`

### Methods içinde özellikle anlatılması gerekenler
- örneklem: `N=34`
- ana veri kaynağı: `osteogenesis_imperfecta_camber_input_minimal_v1.csv`
- runtime gene grouping mantığı
- `occl_tip` ayrıştırması ve infraoklüzyon bayrağı
- `dmft_dmft` sütununun count-benzeri yorumu
- binary uç noktalar için permütasyon doğrulama yaklaşımı
- sürekli uç nokta için Kruskal–Wallis
- Holm düzeltmesi
- robustluk: leave-one-out ve infraoklüzyon dışlama
- model doğrulama: LOO + RSKF + paired bootstrap ΔAUC CI
- determinism: `SEED = 20260228`

## 3) Results

### Birincil tablo ve dosyalar
- Table 1 → `04_final_outputs/tables_csv_and_logs/publication_table1_overall_FINAL.csv`
- Table 2 → `04_final_outputs/tables_csv_and_logs/publication_table2_by_gene_group_FINAL.csv`
- Table 3 → `04_final_outputs/tables_csv_and_logs/publication_table3_inferential_FINAL.csv`
- Integrated summary → `04_final_outputs/tables_csv_and_logs/verified_master_table_FINAL.csv`

### Results anlatım sırası
1. kohort özeti ve prevalanslar
2. gen gruplarına göre deskriptif dağılım
3. inferans sonuçları ve etki büyüklükleri
4. robustluk / duyarlılık bulguları
5. CV/model bulguları

### Yardımcı açıklama dosyaları
- `01_protocol_and_docs/final_1.md`
- `04_final_outputs/TRANSPARENCY_NOTES.md`
- `ANALYSIS_RESULT_MAP.csv`

## 4) Discussion

### Kullanılacak ana dosyalar
- `01_protocol_and_docs/final_1.md`
- `04_final_outputs/tables_csv_and_logs/robustness_panel_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/cv_panel_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/verified_master_table_FINAL.csv`

### Özellikle vurgulanması gerekenler
- caries_any prevalansının yüksekliği
- bazı uç noktalarda orta-yüksek etki büyüklüğü görülmesi
- fakat çoklu düzeltme sonrası kesin kanıt düzeyinin oluşmaması
- sınırda sinyallerin tekil olgu etkisine duyarlılığı
- doku anomalisi için gene katkısı sinyali olsa da small-n nedeniyle temkin gerekliliği

## 5) Limitations

### Kaynaklar
- `01_protocol_and_docs/final_1.md`
- `06_ai_handoff_context/AGENTS.md`
- `04_final_outputs/tables_csv_and_logs/robustness_panel_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/cv_panel_FINAL.csv`

### Ana limitation noktaları
- küçük örneklem (`n=34`)
- düşük expected cell count
- tekil olguların etkisi
- bazı CV özetleyicilerinde estimator farkı notları
- sonuçların hypothesis-generating düzeyde olması

## 6) Figures

### İngilizce figürler
- Fig A → `05_figures/english/FigA_prevalence.png`
- Fig B → `05_figures/english/FigB_gene_groups.png`
- Fig C → `05_figures/english/FigC_inferential_summary.png`
- Fig E → `05_figures/english/FigE_robustness.png`
- Fig F → `05_figures/english/FigF_cv_delta_auc.png`

### Türkçe eşdeğerler
- `05_figures/turkish/*`

### Not
Bu exported package içinde `Fig D` yoktur. Mevcut authoritative figür seti A/B/C/E/F’tir; bunu eksik artifact değil, versioned naming carry-over olarak yorumlayın.

## 7) Supplementary Appendix

### Kullanılacak dosyalar
- `04_final_outputs/tables_csv_and_logs/supplementary_sensitivity_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/supplementary_robustness_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/supplementary_cv_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/supplementary_gene_group_map_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/issue_log_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/consistency_diff_FINAL_1_1_vs_FINAL_1_2.csv`

## 8) En kısa yazım akışı

Eğer hızlı başlamak istiyorsanız şu sırayı izleyin:
1. `01_protocol_and_docs/final_1.md`
2. `01_protocol_and_docs/MANUSCRIPT_ASSEMBLY_GUIDE.md`
3. `04_final_outputs/tables_csv_and_logs/verified_master_table_FINAL.csv`
4. `04_final_outputs/OUTPUT_SCHEMA_AND_VARIABLE_LINEAGE.md`
5. `01_protocol_and_docs/TABLE_FOOTNOTES_AND_FIGURE_LEGENDS.md`
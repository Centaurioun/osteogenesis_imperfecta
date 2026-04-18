# Manuscript_Data

Bu klasör, bu çalışmanın manuscript yazımı ve başka bir AI sisteme güvenli devri için hazırlanmış **authoritative FINAL.1.2 çalışma paketi**dir. Amaç; veri, analiz, sonuç, figür, bağlam dokümanları, yeniden üretilebilirlik notları ve kalite kontrol kanıtlarını tek yerde, düzenli ve izlenebilir biçimde toplamaktır.

## Paket ilkeleri

- Bu klasör içinde **`.pdf`, `.xlsx` ve `.zip` dosyaları bilinçli olarak tutulmaz**.
- Tablolar **CSV**, figürler **PNG**, açıklayıcı rehberler **Markdown**, yürütme özeti **JSON** biçimindedir.
- Paket hem insan tarafından okunabilir hem de bir AI tarafından kolayca parse edilebilir olacak şekilde sadeleştirilmiştir.
- Kaynak dosyalar taşınmamış, **kopyalanmıştır**. Proje kökündeki orijinal dosyalar yerinde durur.

## Authoritative vs archival dosyalar

### Authoritative FINAL.1.2 dosyalar

Bu pakette manuscript ve AI yorumunda birincil otorite kabul edilmesi gereken dosyalar:

- `03_analysis_scripts/oi_oro_dental_master_FINAL_1_2.py`
- `03_analysis_scripts/oi_oro_dental_master_FINAL_1_2.ipynb`
- `04_final_outputs/tables_csv_and_logs/publication_table1_overall_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/publication_table2_by_gene_group_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/publication_table3_inferential_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/robustness_panel_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/cv_panel_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/verified_master_table_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/run_manifest.json`

### Archival / provenance dosyalar

Bu dosyalar önemlidir, ama manuscriptin ana sayısal otoritesi değildir:

- `07_provenance_and_history/*`
- `06_ai_handoff_context/prompt.md`
- `06_ai_handoff_context/vscode_custum_instructions_documentation.md`
- `01_protocol_and_docs/statistical_report_v1.md`
- `01_protocol_and_docs/publication_tables_v1_csv_ciktilari_ozeti.md`

## Kök seviyesindeki rehber dosyaları

### `README_Manuscript_Data.md`
Bu dosya. İnsan-okur ana rehberdir.

### `FILE_REGISTRY.csv`
`Manuscript_Data` içindeki **her dosyanın** göreli yolunu, uzantısını, ait olduğu üst klasörü ve kısa amacını içerir.

### `ANALYSIS_RESULT_MAP.csv`
Her analiz başlığını şu alanlarla eşler:
- analiz ne yapıyor,
- neden yapıldı,
- hangi ana çıktı dosyalarında bulunuyor,
- hangi figürlerde görselleştiriliyor.

## Klasör yapısı ve ayrıntılı içerik

### `01_protocol_and_docs`

Bu klasör manuscriptin **Methods**, **Background**, **Study Design**, **Clinical Definitions**, **Results framing**, **Discussion** ve **figure/table writing** bölümlerini destekleyen ana metinsel bağlamı içerir.

#### Dosyalar

- `camber_sap_v2_publication_ready.md`
  - Çalışmanın istatistik planıdır.
  - Hangi testlerin neden seçildiğini, küçük örneklem yaklaşımını ve QC mantığını açıklar.

- `camber_study_brief_v1.md`
  - Çalışmanın kısa tasarımı, örneklem mantığı ve veri akışını özetler.

- `codebook_v3_fixed.md`
  - Veri sözlüğüdür.

- `statistical_report_v1.md`
  - Erken dönem özet/provenance raporudur.

- `final_1.md`
  - FINAL.1.2’nin investigator-facing yorum özetidir.
  - “hangi analizi neden yaptık, ne bulduk, nasıl yorumladık” sorularına en hızlı giriş noktasıdır.

- `kongre_abstract_paketi_final_1.md`
  - Abstract ve sonuç cümleleri için hazır kısa anlatılar içerir.

- `final_1_2_publication_ready_gorsel_paketi_figur_plani_deterministik_failsafe_uretim_scripti.md`
  - Figür planı ve fail-fast üretim mantığı.

- `Osteogenesis-Imperfecta-Oro-Denta-Bulgular-Etik-Kurul-Basvuru-Rev3.md`
  - Etik/klinik bağlam dokümanı.

- `MANUSCRIPT_ASSEMBLY_GUIDE.md`
  - Introduction / Methods / Results / Discussion / Limitations bölümlerinin hangi dosyalardan yazılacağını gösterir.

- `TABLE_FOOTNOTES_AND_FIGURE_LEGENDS.md`
  - Table 1/2/3 ve Fig A/B/C/E/F için hazır dipnot/legend taslakları içerir.

- `ABBREVIATIONS_GLOSSARY.md`
  - Kısaltmalar ve sık kullanılan teknik değişken adları için sözlük sağlar.

- `publication_tables_v1_csv_ciktilari_ozeti.md`
  - Tarihsel tablo isimlendirme özeti.

- `README_Camber_Upload.md`
  - Orijinal yükleme paketi mantığı.

### `02_source_data`

Bu klasör, manuscriptte sonuçların dayandığı ham ve metadata kaynaklarını içerir.

#### `02_source_data/raw_data`

- `osteogenesis_imperfecta_camber_input_minimal_v1.csv`
  - FINAL analiz hattının authoritative giriş verisidir.

- `osteogenesis_imperfecta_original_data.csv`
  - Arşivdeki daha ham/orijinal veri dosyasıdır.

#### `02_source_data/metadata`

- `codebook_v3_fixed.md`
  - değişken anlamları için hızlı erişim kopyasıdır.

- `gene_map_v1.csv`
  - gen sembollerinin runtime grouping referansıdır.

### `03_analysis_scripts`

Bu klasör, nihai analiz ve figür üretiminin kod tarafını içerir.

- `oi_oro_dental_master_FINAL_1_2.py`
  - FINAL.1.2 ana analiz scripti.

- `oi_oro_dental_master_FINAL_1_2.ipynb`
  - aynı analizin notebook formu.

- `make_figures_final_1_2.py`
  - İngilizce PNG figür üretimi.

- `make_figures_FINAL_1_2_TR.py`
  - Türkçe PNG figür üretimi.

### `04_final_outputs`

Bu klasör nihai tablo, QC ve açıklama katmanını içerir.

#### `04_final_outputs/tables_csv_and_logs`

Ana publication ve supplementary CSV çıktıları:

- `publication_table1_overall_FINAL.csv`
- `publication_table2_by_gene_group_FINAL.csv`
- `publication_table3_inferential_FINAL.csv`
- `robustness_panel_FINAL.csv`
- `cv_panel_FINAL.csv`
- `verified_master_table_FINAL.csv`
- `supplementary_sensitivity_FINAL.csv`
- `supplementary_robustness_FINAL.csv`
- `supplementary_cv_FINAL.csv`
- `supplementary_gene_group_map_FINAL.csv`
- `issue_log_FINAL.csv`
- `consistency_diff_FINAL_1_1_vs_FINAL_1_2.csv`
- `run_manifest.json`

#### `04_final_outputs/OUTPUT_SCHEMA_AND_VARIABLE_LINEAGE.md`

Ana çıktı kolonlarının ne anlama geldiğini ve raw → runtime → manuscript dönüşümlerini açıklar. Özellikle:

- `occl_tip` → `infraokluzyon_var`
- `dmft_dmft` → `caries_count`, `caries_any_rt`
- `gen_mutasyonu` → runtime gene group
- `delta_auc_estimator`, `ci_estimator`, `note`, `warnings`

#### `04_final_outputs/TRANSPARENCY_NOTES.md`

Şu soruları açıklar:

- neden `cv_panel_FINAL.csv` içinde warning olabilir ama `issue_log_FINAL.csv` temizdir?
- `note` ile `warnings` arasındaki fark nedir?
- `k=3` ve `k=4` niçin supplementary’dedir?
- neden exported pakette `Fig D` yoktur?

#### `04_final_outputs/REPRODUCIBILITY_ENVIRONMENT.md`

Yeniden üretilebilirlik bağlamını özetler:

- authoritative entry points
- seed
- manifest yorumlama
- reproducibility sınırları

### `05_figures`

Bu klasör manuscript ve sunum için figürleri **PNG** biçiminde içerir.

#### `05_figures/english`

- `FigA_prevalence.png`
- `FigB_gene_groups.png`
- `FigC_inferential_summary.png`
- `FigE_robustness.png`
- `FigF_cv_delta_auc.png`

#### `05_figures/turkish`

- `FigA_prevalans_TR.png`
- `FigB_gen_grup_TR.png`
- `FigC_inferans_ozet_TR.png`
- `FigE_robustluk_TR.png`
- `FigF_cv_delta_auc_TR.png`

Not: Mevcut exported authoritative figür seti **A/B/C/E/F**’tir. `Fig D` yokluğu bu pakette eksik dosya anlamına gelmez; sürümsel isimlendirme taşıması olarak kabul edilmelidir.

### `06_ai_handoff_context`

Bu klasör, başka bir AI sisteme devri güvenli kılmak için özel olarak eklenmiştir.

- `FINAL_HANDOFF_QUICKSTART.md`
  - authoritative dosyalar, archival dosyalar ve doğru okuma sırasını açıklar.

- `DOCUMENTATION_AUDIT_TRAIL.md`
  - kullanıcı talebindeki 6 iteratif dokümantasyon iyileştirme turunun özet kaydıdır.

- `AGENTS.md`
  - küçük örneklem istatistik kuralları.

- `copilot-instructions.md`
  - klinik kırmızı çizgiler ve determinism.

- `python-analysis.instructions.md`
  - Python/notebook analiz standartları.

- `copilot_vscode_oturumu_camber_oi_oro_dental_analiz_rebuild_prompt_iteratif_qc_cross_validation.md`
  - tarihsel AI oturum bağlamı içerir. Bu dosya informative’dir; authoritative final analysis guide olarak tek başına kullanılmamalıdır.

- `prompt.md`
  - arşiv prompt kaydı.

- `vscode_custum_instructions_documentation.md`
  - ek editör/assistant talimat geçmişi.

### `07_provenance_and_history`

Bu klasör, FINAL.1.2 öncesi izleri tutar:

- `issue_log_v3.csv`
- `issue_log_v3_1.csv`
- `verified_master_table_v3.csv`
- `verified_master_table_v3_1.csv`

Bu dosyalar reviewer/audit trail için önemlidir; manuscriptin ana sayısal kaynağı değildir.

## Analizler: ne yapıldı, neden yapıldı, sonuçları nerede?

### 1) Descriptive cohort summary

**Amaç:** kohortu temel düzeyde tanımlamak.

**Neden gerekliydi?** Manuscriptte örneklem, yaş dağılımı ve prevalanslar net biçimde verilmelidir.

**Ana dosyalar:**
- `04_final_outputs/tables_csv_and_logs/publication_table1_overall_FINAL.csv`
- `05_figures/english/FigA_prevalence.png`
- `05_figures/turkish/FigA_prevalans_TR.png`

### 2) Runtime gene-group descriptive analysis

**Amaç:** gen mutasyon bilgisinden runtime group üretip grup bazlı özet göstermek.

**Neden gerekliydi?** Tekrarlanabilirlik, grouping leakage riskini azaltma ve temiz provenance için.

**Ana dosyalar:**
- `04_final_outputs/tables_csv_and_logs/publication_table2_by_gene_group_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/supplementary_gene_group_map_FINAL.csv`
- `05_figures/english/FigB_gene_groups.png`
- `05_figures/turkish/FigB_gen_grup_TR.png`

### 3) Primary inferential testing

**Amaç:** gen grubu ile oro-dental sonlanımlar arasındaki ilişki sinyallerini test etmek.

**Neden bu testler?**
- küçük expected cell count
- binary uç noktalarda permütasyon doğrulama ihtiyacı
- sürekli uç noktada non-parametrik yaklaşım
- çoklu test düzeltme zorunluluğu
- etki büyüklüğü raporlama gereği

**Ana dosyalar:**
- `04_final_outputs/tables_csv_and_logs/publication_table3_inferential_FINAL.csv`
- `05_figures/english/FigC_inferential_summary.png`
- `05_figures/turkish/FigC_inferans_ozet_TR.png`

### 4) Robustness / sensitivity

**Amaç:** borderline sinyallerin tekil olgu ve infraoklüzyonlu vaka etkisine duyarlılığını görmek.

**Ana dosyalar:**
- `04_final_outputs/tables_csv_and_logs/robustness_panel_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/supplementary_robustness_FINAL.csv`
- `05_figures/english/FigE_robustness.png`
- `05_figures/turkish/FigE_robustluk_TR.png`

### 5) Cross-validation modeling

**Amaç:** yaş modeline gene-group eklenmesinin ayrım gücüne katkısını ölçmek.

**Ana dosyalar:**
- `04_final_outputs/tables_csv_and_logs/cv_panel_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/verified_master_table_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/supplementary_cv_FINAL.csv`
- `05_figures/english/FigF_cv_delta_auc.png`
- `05_figures/turkish/FigF_cv_delta_auc_TR.png`

### 6) QC / reproducibility / audit trail

**Amaç:** nihai sayıların deterministik, izlenebilir ve parity-korumalı olduğunu göstermek.

**Ana dosyalar:**
- `04_final_outputs/tables_csv_and_logs/run_manifest.json`
- `04_final_outputs/tables_csv_and_logs/issue_log_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/consistency_diff_FINAL_1_1_vs_FINAL_1_2.csv`
- `04_final_outputs/TRANSPARENCY_NOTES.md`
- `04_final_outputs/REPRODUCIBILITY_ENVIRONMENT.md`
- `06_ai_handoff_context/DOCUMENTATION_AUDIT_TRAIL.md`

## Warnings vs issues nasıl okunmalı?

- `cv_panel_FINAL.csv` içindeki `warnings` sütunu **yorum dikkat bayrağıdır**.
- `issue_log_FINAL.csv` ise **yapısal/fail-fast** log mantığını temsil eder.
- Bu nedenle `AUC < 0.5` veya estimator farkı notları varken `issue_log_FINAL.csv` temiz olabilir. Bu hata değil, bilinçli ayrımdır.

## Duplicate scenarios nasıl okunmalı?

- `Primary` manuscript için authoritative senaryodur.
- `k=3` ve `k=4` reviewer şeffaflığı için supplementary dosyalarda tutulur.
- Eğer `is_duplicate_scenario=True` veya duplicate mapping işaretleri varsa, bunlar authoritative `Primary` senaryonun türev/tekrar görünümüdür.

## Manuscript yazarken en kritik dosyalar

Hızlı başlangıç için önerilen sıra:

1. `01_protocol_and_docs/final_1.md`
2. `01_protocol_and_docs/MANUSCRIPT_ASSEMBLY_GUIDE.md`
3. `01_protocol_and_docs/camber_sap_v2_publication_ready.md`
4. `01_protocol_and_docs/ABBREVIATIONS_GLOSSARY.md`
5. `04_final_outputs/OUTPUT_SCHEMA_AND_VARIABLE_LINEAGE.md`
6. `04_final_outputs/tables_csv_and_logs/verified_master_table_FINAL.csv`
7. `04_final_outputs/tables_csv_and_logs/publication_table1_overall_FINAL.csv`
8. `04_final_outputs/tables_csv_and_logs/publication_table2_by_gene_group_FINAL.csv`
9. `04_final_outputs/tables_csv_and_logs/publication_table3_inferential_FINAL.csv`
10. `04_final_outputs/tables_csv_and_logs/robustness_panel_FINAL.csv`
11. `04_final_outputs/tables_csv_and_logs/cv_panel_FINAL.csv`
12. `01_protocol_and_docs/TABLE_FOOTNOTES_AND_FIGURE_LEGENDS.md`
13. `ANALYSIS_RESULT_MAP.csv`
14. `FILE_REGISTRY.csv`

## Bir AI’ya bu klasör nasıl verilmelidir?

Önerilen okuma sırası:

1. `README_Manuscript_Data.md`
2. `ANALYSIS_RESULT_MAP.csv`
3. `FILE_REGISTRY.csv`
4. `06_ai_handoff_context/FINAL_HANDOFF_QUICKSTART.md`
5. `06_ai_handoff_context/AGENTS.md`
6. `06_ai_handoff_context/copilot-instructions.md`
7. `06_ai_handoff_context/python-analysis.instructions.md`
8. `01_protocol_and_docs/final_1.md`
9. `01_protocol_and_docs/camber_sap_v2_publication_ready.md`
10. `02_source_data/metadata/codebook_v3_fixed.md`
11. `04_final_outputs/OUTPUT_SCHEMA_AND_VARIABLE_LINEAGE.md`
12. `04_final_outputs/tables_csv_and_logs/verified_master_table_FINAL.csv`
13. gerekirse diğer CSV ve PNG dosyaları

## Bilerek dışarıda bırakılan formatlar

Bu klasörde bilinçli olarak tutulmayan formatlar:

- `.pdf`
- `.xlsx`
- `.zip`

Gerekçe:
- gereksiz tekrar
- AI ingest sırasında gürültü
- parse zorluğu
- authoritative veri akışını sade tutma ihtiyacı

## Son not

Bu klasör artık yalnızca bir çıktı arşivi değil; manuscript yazımı, reviewer yanıtları ve AI handoff için bütünleşik bir çalışma paketi olacak şekilde güçlendirilmiştir. Yine de authoritative hesaplamalar FINAL.1.2 script ve CSV katmanında kalır; tarihsel `v3` referansları provenance amaçlıdır ve manuscriptin ana sayısal kaynağı olarak yorumlanmamalıdır.

# FINAL_HANDOFF_QUICKSTART

Bu dosya, `Manuscript_Data` paketini bir insan veya AI için **en hızlı ve en güvenli başlangıç noktası** olarak hazırlanmıştır.

## 1) Önce neyi authoritative kabul etmeliyim?

Bu pakette **authoritative nihai analiz sürümü**:
- `FINAL.1.2`

Bunu temsil eden ana dosyalar:
- `03_analysis_scripts/oi_oro_dental_master_FINAL_1_2.py`
- `03_analysis_scripts/oi_oro_dental_master_FINAL_1_2.ipynb`
- `04_final_outputs/tables_csv_and_logs/publication_table1_overall_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/publication_table2_by_gene_group_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/publication_table3_inferential_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/robustness_panel_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/cv_panel_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/verified_master_table_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/run_manifest.json`

## 2) Hangi dosyalar archival/provenance amaçlıdır?

Aşağıdaki dosyalar **nihai sonuç yazımı için birincil kaynak değildir**; bunlar provenance veya tarihçe amaçlıdır:
- `07_provenance_and_history/*`
- `06_ai_handoff_context/prompt.md`
- `06_ai_handoff_context/vscode_custum_instructions_documentation.md`
- `01_protocol_and_docs/statistical_report_v1.md`
- `01_protocol_and_docs/publication_tables_v1_csv_ciktilari_ozeti.md`

## 3) Eski `v3` referansları nasıl yorumlanmalı?

Bazı AI/prompt geçmiş dosyaları eski `v3` veya `issue_log_v3.csv` isimlerini içerebilir. Bunlar:
- tarihsel bağlam sağlar,
- ama bu pakette **operatif / authoritative final log** dosyası değildir.

Bu paket içindeki authoritative final issue kaydı:
- `04_final_outputs/tables_csv_and_logs/issue_log_FINAL.csv`

## 4) Bir AI bu paketi hangi sırayla okumalı?

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
11. `04_final_outputs/tables_csv_and_logs/verified_master_table_FINAL.csv`
12. gerekirse diğer CSV ve PNG dosyaları

## 5) Klinik ve analitik kırmızı çizgiler

- `occl_tip == 4` → **infraoklüzyon**, Angle sınıfı değildir.
- `dmft_dmft` → klasik DMFT indeksi değil; ağızdaki toplam çürük/dolgu sayısı gibi yorumlanmış **count** değişkenidir.
- Rastgelelik içeren tüm analizler `SEED = 20260228` ile deterministiktir.
- Küçük örneklem nedeniyle:
  - düşük expected cell count görüldüğünde permütasyon/exact yaklaşım öne çıkar,
  - sürekli değişkenlerde non-parametrik yaklaşım esastır,
  - etki büyüklüğü raporlamak zorunludur.

## 6) Hangi dosyadan manuscript yazmaya başlamalıyım?

Hızlı başlangıç için:
- klinik/yorumlayıcı özet: `01_protocol_and_docs/final_1.md`
- yöntem: `01_protocol_and_docs/camber_sap_v2_publication_ready.md`
- değişken anlamları: `02_source_data/metadata/codebook_v3_fixed.md`
- tek bakışta sonuç: `04_final_outputs/tables_csv_and_logs/verified_master_table_FINAL.csv`

## 7) Hangi şeyleri bu pakette yeniden üretmeye çalışmamalıyım?

Kullanıcı yeni bir analiz istemedikçe:
- eski `v3` branch’lerini yeniden çalıştırmayın,
- eksik `Fig D` üretmeye çalışmayın,
- `.pdf`, `.xlsx`, `.zip` çıktılarını bu pakete geri koymayın.

Bu paket AI-friendly ve manuscript-friendly olacak şekilde sadeleştirilmiştir.
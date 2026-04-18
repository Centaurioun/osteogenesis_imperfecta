# VS Code Copilot Prompt — İstatistikçi Analizlerini Yeniden Üretme ve Karşılaştırma (Revize)

Sen, bu proje klasörü içinde çalışan kıdemli bir biyostatistik ve araştırma-metodolojisi asistanısın. Görevin, istatistikçiden gelen analizleri sistematik biçimde yeniden üretmek, proje kuralları ve author tarafından açıklanan kayıt mantığı korunarak aynı analitik soruları yeniden sormak, sonra bu iki analitik hattı karşılaştırmak ve manuscript uygunluğu açısından sınıflandırmaktır.

Bu görevde dört şeyi asla karıştırma:
1. istatistikçinin yaptığı analizlerin tarihsel / legacy replikasyonu,
2. proje kuralları korunarak yapılan rule-constrained replikasyon,
3. farkların nedenini açıklayan discrepancy attribution katmanı,
4. manuscript için kullanılacak nihai otorite katmanı.

Amaç daha fazla test üretmek değil; farkların kaynağını açıklayan, tekrar üretilebilir, dosya bazında izlenebilir ve editoryal olarak kullanılabilir bir karşılaştırmalı analiz paketi oluşturmaktır.

---

## 1. Zorunlu klasörleme kuralı

Bu görev için üretilecek TÜM yeni dosyaları tek bir özel klasörde topla. Eski çıktılarla karışmasına izin verme.

Ana klasör adı:

`reanalysis_statistician_vs_project/`

Bu ana klasör altında şu alt klasörleri oluştur:
- `00_audit/`
- `01_legacy_replication/`
- `02_rule_constrained_replication/`
- `03_discrepancy_analysis/`
- `04_manuscript_decisions/`
- `05_logs/`
- `06_figures/`
- `07_temp/`

Kurallar:
- Bu görev kapsamında üretilen tüm `py`, `md`, `csv`, `png`, `json`, `txt` ve diğer dosyalar bu klasör ağacı içinde olmalıdır.
- Proje kök dizinine dağınık çıktı bırakma.
- Her ana adım sonunda hangi dosyanın nereye yazıldığını logla.
- Aynı isimli dosyaları ezmeden önce kısa not düş.
- Geçici dosyaları `07_temp/` içinde tut; nihai raporları başka klasörlere taşı.

---

## 2. Temel görev tanımı

Aşağıdaki dört katmanlı yapıyı uygula:

### Katman 1 — Legacy replication
İstatistikçinin yaptığı analizleri mümkün olduğunca aynı mantıkla yeniden üret.

### Katman 2 — Rule-constrained replication
Aynı analitik soruları, proje kurallarını ve author açıklamalarını koruyarak yeniden çalıştır.

### Katman 3 — Discrepancy attribution
Legacy ve rule-constrained sonuçlar arasındaki farkın nedenini sınıflandır.

### Katman 4 — Manuscript authority layer
Her sonucu manuscript açısından sınıflandır:
- `manuscript-eligible`
- `supplementary-only`
- `legacy-reference-only`
- `not usable`

---

## 3. Proje kuralları ve author tarafından doğrulanan kayıt mantığı

Aşağıdaki kuralları bozamazsın:

### 3.1. Oklüzyon / OCCL
- `occl_tip == 4` değeri **infraocclusion** olarak ele alınacaktır.
- `occl_tip == 4`, Angle class I / II / III ile aynı kategorik aileye katılmayacaktır.
- Legacy replication katmanında istatistikçinin coding yaklaşımı korunabilir; ancak rule-constrained katmanda bu ayrım zorunludur.

### 3.2. Doku anomalisi
- `doku anomalisi` alanında `0 = doku anomalisi yok`.
- Bu alan çoklu kayıt değil, **tek baskın kayıt** mantığıyla doldurulmuştur.
- Aynı hastada birden fazla olası yapı bozukluğu bulunabilse bile, veri seti yalnız baskın olanı taşır.
- Rule-constrained analizlerde bu alan çoklu fenotip haritası gibi yorumlanmayacaktır.

### 3.3. Dentinogenesis imperfecta
- DI için tip veya şiddet kaydı yoktur.
- Shields tipi veya şiddet düzeyi ile ilgili analiz yapılmayacaktır.
- Böyle bir ayrım protokolde geçmiş olsa bile, veri setinde kayıt yoksa yalnız sınırlılık olarak not edilecektir.

### 3.4. DMFT / dmft alanı
- `dmft_dmft` alanı standart ayrıştırılmış `DMFT` ve `dmft` indeksleri gibi ele alınmayacaktır.
- Bu alan, author açıklamasına göre yaş ve dentisyon durumuna bağlı olarak ağızdaki mevcut çürük yükünü tek hanede özetleyen **count-like** kayıt alanı gibi ele alınacaktır.
- Rule-constrained analizlerde bu alan klasik parsed index olarak değil, proje mantığına uygun count-like yapı olarak kullanılacaktır.

### 3.5. Binary klinik değişkenler
- `overjet`, `overbite`, `open bite`, `crossbite` ve `gingivitis` değişkenleri yalnız **var / yok** mantığıyla kaydedilmiştir.
- Şiddet, mm eşiği, indeks skoru veya derecelendirme yoksa bunlar binary değişken olarak ele alınacaktır.
- Rule-constrained analizlerde bu değişkenler için var olmayan şiddet bilgisi varsayılmayacaktır.

### 3.6. Gene grouping ve small-sample mantığı
- Gene grouping, proje mantığına uygun runtime-derived yapı üzerinden değerlendirilecektir.
- Küçük örneklem, seyrek hücre ve dengesiz grup yapısı merkezi metodolojik gerçeklik olarak kabul edilecektir.
- Büyük örneklem varsayımlarına dayanan testler otomatik uygulanmayacaktır.

### 3.7. İleri istatistik ve reporting mantığı
- Effect size raporlaması göz ardı edilmeyecektir.
- Çoklu test varsa bunu görmezden gelen nihai yorum kurulmayacaktır.
- Robustness / sensitivity katmanı atlanmayacaktır.
- CV / AUC / delta-AUC varsa bunlar yalnız `secondary internal verification` olarak ele alınacaktır.

---

## 4. Önce okunacak dosyalar

İşe başlamadan önce aşağıdaki dosyaları incele:

### Ana referanslar
- `README_Manuscript_Data.md`
- `ANALYSIS_RESULT_MAP.csv`
- `FILE_REGISTRY.csv`
- `06_ai_handoff_context/FINAL_HANDOFF_QUICKSTART.md`

### Ana çalışma gerçekliği
- `01_protocol_and_docs/final_1.md`
- `01_protocol_and_docs/camber_sap_v2_publication_ready.md`
- `02_source_data/metadata/codebook_v3_fixed.md`
- `03_analysis_scripts/oi_oro_dental_master_FINAL_1_2.py`
- `04_final_outputs/OUTPUT_SCHEMA_AND_VARIABLE_LINEAGE.md`
- `04_final_outputs/TRANSPARENCY_NOTES.md`
- `04_final_outputs/REPRODUCIBILITY_ENVIRONMENT.md`

### İstatistikçi çıktısı
- istatistikçiden gelen DOCX / dönüştürülmüş analiz özeti

### Manuscript bağlamı
- açık canvas’taki `Methods`
- açık canvas’taki `Results`
- açık canvas’taki `Discussion`
- `Methods_questions_answers.md`
- `Results_questions_answers.md`
- `Discussion_questions_answers.md`

### Yöntem ve açıklama belgeleri
- açık canvas’taki `İstatistikçi Analizlerinin Çift Hatlı Replikasyonu — Kılavuz (Revize)`
- açık canvas’taki `Eksik ve Destekleyici Analizler — Uygulanabilir Plan`

Not:
- Protokol ve eski belgeleri yalnız referans olarak oku.
- Nihai analitik gerçekliği FINAL.1.2 dosyaları ve author-confirmed kayıt mantığı belirler.
- Bir protokol beklentisini, final çıktı veya author açıklaması tarafından desteklenmiyorsa gerçekleşmiş analiz gibi ele alma.

---

## 5. İlk zorunlu çıktı: analiz envanteri ve eşleme

Aşağıdaki dosyaları önce üret. Bunlar olmadan replikasyon aşamasına geçme.

### 5.1. İstatistikçi analiz envanteri
**Dosya:** `reanalysis_statistician_vs_project/00_audit/statistician_analysis_inventory.csv`

Sütunlar:
- `analysis_id`
- `reported_in_statistician_file`
- `endpoint_name`
- `variable_name_if_known`
- `grouping_variable`
- `coding_assumption`
- `test_used`
- `reported_p_value`
- `reported_effect_size`
- `reported_comment`

### 5.2. Legacy-to-project mapping
**Dosya:** `reanalysis_statistician_vs_project/00_audit/legacy_to_project_map.csv`

Sütunlar:
- `analysis_id`
- `statistician_endpoint`
- `project_equivalent`
- `same_construct_yes_no`
- `same_coding_yes_no`
- `same_test_family_yes_no`
- `reanalysis_required_yes_no`
- `main_discrepancy_risk`
- `author_clarification_dependency`

### 5.3. Author clarification rules snapshot
**Dosya:** `reanalysis_statistician_vs_project/00_audit/author_clarification_rules.md`

Bu dosyada kısa ve net olarak şu kuralları listele:
- doku anomalisi = baskın tek kod
- DI tip/şiddet yok
- OCCL 4 = infraocclusion
- dmft_dmft = count-like total caries burden style field
- overjet / overbite / open bite / crossbite / gingivitis = binary var/yok

### 5.4. Ön denetim raporu
**Dosya:** `reanalysis_statistician_vs_project/00_audit/reanalysis_startup_audit.md`

Bu raporda şu başlıklar olsun:
1. `What can be replicated exactly`
2. `What can only be approximately replicated`
3. `What must be redefined under project rules`
4. `High-risk discrepancy areas`
5. `Immediate manuscript risk items`

Bu dosyalar üretilmeden sonraki aşamalara geçme.

---

## 6. Aşama 1 — Legacy replication

### Amaç
İstatistikçinin yaptığı analizleri mümkün olduğunca aynı mantıkla yeniden üretmek.

### Kurallar
- Bu aşamada istatistikçinin kullandığı coding ve test mantığını mümkün olduğunca koru.
- Hangi noktada kesin bire bir replikasyon yapılamadığını mutlaka not et.
- Legacy replication sonuçlarını manuscript authority gibi sunma.
- Legacy analizde author açıklamalarıyla uyumsuz görünen alanlar ayrıca işaretlenecek, ama bu aşamada zorla düzeltilmeyecektir.

### Yapılacaklar
1. İstatistikçi raporundaki tanımlayıcı tabloları yeniden üret.
2. İstatistikçi raporundaki grup karşılaştırmalarını yeniden çalıştır.
3. Raporlanan p-değerlerini mümkün olduğunca yeniden üretmeye çalış.
4. Bire bir replikasyon mümkün değilse sapmanın nedenini not et.
5. OCCL, doku anomalisi ve Dmft alanlarında kullanılan legacy coding varsayımını açıkça yaz.

### Üretilecek dosyalar
- `reanalysis_statistician_vs_project/01_legacy_replication/statistician_legacy_replication.csv`
- `reanalysis_statistician_vs_project/01_legacy_replication/legacy_replication_notes.md`
- `reanalysis_statistician_vs_project/01_legacy_replication/legacy_descriptive_tables.csv`

### Zorunlu sütunlar
- `analysis_id`
- `legacy_result_obtained`
- `legacy_result_matches_reported`
- `difference_if_any`
- `replication_quality`
- `legacy_coding_assumption`

`replication_quality` şu etiketlerden biri olmalı:
- `exact`
- `close`
- `approximate`
- `not reproducible`

---

## 7. Aşama 2 — Rule-constrained replication

### Amaç
İstatistikçinin sorduğu aynı analitik soruları, bu kez proje kurallarını ve author açıklamalarını koruyarak yeniden çalıştırmak.

### Kurallar
- Bu aşamada proje kuralları ve author açıklamaları zorunludur.
- Eğer legacy analiz ile project-valid analiz aynı endpointi gerçekten ölçmüyorsa, bunu açıkça belirt.
- Bu aşama manuscript’e en yakın replikasyon katmanıdır.
- Var olmayan DI tip/şiddet bilgisini türetmeye çalışma.
- Binary kaydedilmiş klinik değişkenlere şiddet atfetme.

### Yapılacaklar
1. OCCL gibi coding-duyarlı değişkenleri proje kurallarına göre yeniden tanımla.
2. Doku anomalisi gibi dominant-code alanları manuscript endpoint mantığıyla yeniden ele al.
3. `dmft_dmft` ve caries türevlerini proje mantığına göre analiz et.
4. Gerekli ise exact / permutation / effect size / correction / robustness odaklı uygun analitik çerçeve kullan.
5. Legacy analizle aynı soruyu sormaya çalış, ama veri tanımını bozma.
6. Binary klinik değişkenleri var/yok düzeyinde tut.

### Üretilecek dosyalar
- `reanalysis_statistician_vs_project/02_rule_constrained_replication/statistician_rule_constrained_replication.csv`
- `reanalysis_statistician_vs_project/02_rule_constrained_replication/rule_constrained_notes.md`
- `reanalysis_statistician_vs_project/02_rule_constrained_replication/rule_constrained_supporting_tables.csv`

### Zorunlu sütunlar
- `analysis_id`
- `project_valid_endpoint`
- `coding_rule_used`
- `test_used`
- `effect_size_reported_yes_no`
- `multiplicity_control_used_yes_no`
- `robustness_layer_applied_yes_no`
- `result_summary`
- `author_rule_applied`

---

## 8. Aşama 3 — Discrepancy attribution

### Amaç
Legacy ve rule-constrained sonuçlar arasındaki farkın nedenini sınıflandırmak.

Bu aşama olmadan iş tamamlanmış sayılmaz.

Her analiz için farkı aşağıdaki sınıflardan birine ata:
- `variable-definition discrepancy`
- `coding discrepancy`
- `test-selection discrepancy`
- `multiplicity-control discrepancy`
- `robustness-related discrepancy`
- `modeling/reporting discrepancy`
- `no material discrepancy`

Ayrıca her analiz için şu sonuç sınıflamasını yap:
- `fully concordant`
- `directionally concordant but method-sensitive`
- `definition-sensitive`
- `substantively discordant`

### Üretilecek dosyalar
- `reanalysis_statistician_vs_project/03_discrepancy_analysis/discrepancy_attribution_table.csv`
- `reanalysis_statistician_vs_project/03_discrepancy_analysis/discrepancy_report.md`

### Zorunlu sütunlar
- `analysis_id`
- `legacy_summary`
- `rule_constrained_summary`
- `main_discrepancy_source`
- `concordance_class`
- `editorial_implication`
- `clinically_important_yes_no`

---

## 9. Aşama 4 — Manuscript authority layer

### Amaç
Her sonucun manuscript için kullanılabilir olup olmadığını belirlemek.

Her analiz için şu etiketlerden birini ver:
- `manuscript-eligible`
- `supplementary-only`
- `legacy-reference-only`
- `not usable`

### Kurallar
- Legacy replication sonucu tek başına manuscript authority değildir.
- Project-rule-constrained sonuç manuscript için öncelikli katmandır.
- Eğer sonuç tanım-duyarlıysa, manuscript metninde yalnız dikkatli dille kullanılabilir.
- Eğer sonuç yalnız legacy dünyasında anlamlı ama project-valid dünyada taşınmıyorsa, ana metne alma.
- Yalnız author açıklaması sayesinde düzeltilmiş sonuçlar varsa bunları manuscript için öncelikli değerlendir.

### Üretilecek dosyalar
- `reanalysis_statistician_vs_project/04_manuscript_decisions/manuscript_eligibility_table.csv`
- `reanalysis_statistician_vs_project/04_manuscript_decisions/legacy_vs_project_reconciliation_report.md`

### Zorunlu sütunlar
- `analysis_id`
- `manuscript_eligibility`
- `main_text_or_supplement_or_exclude`
- `reason`
- `recommended_wording_level`

`recommended_wording_level` şu değerlerden biri olmalı:
- `descriptive only`
- `exploratory signal`
- `supported comparative statement`
- `do not use in manuscript`

---

## 10. Reporting support

Tüm süreç sonunda aşağıdaki özet raporu üret:

**Dosya:** `reanalysis_statistician_vs_project/04_manuscript_decisions/copilot_reanalysis_completion_report.md`

Başlıklar:
1. `What was replicated exactly`
2. `What changed under project rules`
3. `Why key results changed`
4. `Which results are manuscript-eligible`
5. `Which results are supplementary-only`
6. `Which results should not be used`
7. `Most important discrepancy drivers`
8. `Folder and file inventory`
9. `Author-clarification-dependent decisions`

---

## 11. Minimum raporlama standardı

Her analiz için en az şunları kaydet:
- analiz adı,
- legacy mi rule-constrained mı,
- kullanılan değişken,
- kullanılan coding mantığı,
- kullanılan test,
- usable N,
- temel sonuç,
- varsa effect size,
- varsa correction bilgisi,
- manuscript etkisi,
- oluşturulan çıktı dosyası.

---

## 12. Kesin yasaklar

Aşağıdakileri yapma:
- legacy ile project-valid sonuçları aynı düzeyde sunma,
- coding farkını gizleme,
- OCCL 4’ü Angle class içine geri katma,
- `dmft_dmft`’yi classical parsed DMFT gibi davranıp manuscript authority katmanına taşıma,
- robustness olmadan güçlü sonuç dili kurma,
- warning / note / transparency alanlarını gizleme,
- legacy p-değerlerini correction ve project rules yokmuş gibi ana metne taşıma,
- binary kaydedilmiş gingivitis veya ortodontik değişkenleri şiddetli / hafif gibi sınıflandırma,
- veri setinde olmayan DI alt tip / şiddet bilgisini varsayma.

---

## 13. Çalışma tarzı

Bu görevi şu tarzla yürüt:
- önce envanter çıkar,
- sonra eşleme yap,
- sonra legacy replication yap,
- sonra rule-constrained replication yap,
- sonra farkı sınıflandır,
- en son manuscript kararı ver.

Her aşamada kısa log bırak.
Her dosyanın üretildiği klasörü açıkça belirt.
Her farkı metodolojik olarak adlandır.
Kırılganlığı gizleme.
Aynı analizi yalnız isim değiştirerek tekrar üretme.

---

## 14. Son komut

Önce zorunlu klasör yapısını oluştur. Sonra aşağıdaki dosyaları üret:
- `reanalysis_statistician_vs_project/00_audit/statistician_analysis_inventory.csv`
- `reanalysis_statistician_vs_project/00_audit/legacy_to_project_map.csv`
- `reanalysis_statistician_vs_project/00_audit/author_clarification_rules.md`
- `reanalysis_statistician_vs_project/00_audit/reanalysis_startup_audit.md`

Bunlar tamamlanmadan legacy veya rule-constrained replikasyon aşamasına geçme.


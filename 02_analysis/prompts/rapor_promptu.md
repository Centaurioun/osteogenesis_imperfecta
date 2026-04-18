# OI Projesi — Kapsamlı Durum Raporu ve Notebook Hazırlık Promptu (Revize)

Bu workspace için, **gelinen son durumu esas alan** kapsamlı, sistematik, akademik ve teknik açıdan güçlü bir analiz raporu hazırla.
Odak noktası: **FINAL.1.2 authoritative analiz omurgası** + bunun üzerine eklenen destek/robustness/model-doğrulama paketlerinin izlenebilir özeti.

## Bu promptun asıl kullanım amacı

Bu promptun birincil amacı, **yeni tekleştirilmiş bir `.ipynb` dosyası üretilmeden önce** hataları/eksikleri/yanlış anlaşılmaları azaltan bir “durum raporu + hazırlık katmanı” oluşturmaktır.

Bu nedenle çıktı iki fazlı düşünülmelidir:
1. **Faz A (zorunlu):** Tam kapsamlı durum raporu, dosya envanteri, eşleme tabloları, sadeleştirme planı.
2. **Faz B (ayrı görev):** Yeni konsolide `.ipynb` üretimi (bu promptun kendisinde otomatik üretilmez; yalnızca hazır hale getirilir).

> Bu bir kısa özet işi değildir. Çıktı, baştan sona denetlenebilir ve dosya-eşlemeli bir teknik dokümantasyon olmalıdır.

---

## 0) Çalışma kapsamı ve kaynak hiyerarşisi (zorunlu)

Raporu aşağıdaki kaynak hiyerarşisine göre kur:

1. **FINAL.1.2 authoritative kaynaklar**
2. Mevcut manuscript-facing tanımlar ve runtime kuralları
3. Güncel supporting/robustness paketleri
4. İstatistikçi değerlendirmesi / reconciliation çıktıları (**reference-only**)
5. Tarihsel/provenance belgeleri (arka plan)

### Kritik kural
- İstatistikçi çalışmaları anlatılabilir ama **aktif doğruluk katmanı** olarak kullanılmaz; **referans katmanı** olarak çerçevelenir.

### Kapsam dışı (non-goals)
- FINAL.1.2 ana istatistik sonuçlarını yeniden hesaplamak veya değiştirmek.
- Frozen/reference katmandan yeni “primary truth” üretmek.
- Mevcut authoritative dosyaları taşımak, yeniden adlandırmak, silmek veya üzerine yazmak.
- Destek/ek analizleri birincil çıkarım gibi sunmak.
- Bu prompt çalışırken yeni konsolide `.ipynb` dosyasını fiilen oluşturmak.

### Çalışma modu
- Raporlama ve organizasyon çalışması **deterministik ve non-destructive** olmalıdır.
- Tüm yeni dokümantasyon/indeks/eşleme çıktıları yeni bir rapor paketi altında üretilir.
- Kaynak dosyalara dokunulmaz; yalnızca okuma + gerekirse kopya/özet/indeks üretilir.

### Çıktı kök klasörü ve sürümleme
- Tüm çıktılar tek bir kök klasör altında üretilmelidir: `analysis_documentation_package/`.
- Her çalıştırma için alt klasör adı zorunlu olarak run-id içermelidir (örn. `run_YYYYMMDD_HHMM`).
- Önceki run çıktılarının üzerine yazma yok; her run ayrı klasörde tutulur.

---

## 1) Klinik ve analitik kırmızı çizgiler (ihlal etme)

- `occl_tip == 4` = **infraocclusion**; Angle I/II/III’e geri katılmaz.
- `dmft_dmft` = proje bağlamında **count-like alan**; klasik ayrıştırılmış DMFT/dmft gibi yorumlanmaz.
- `doku_anomalisi` = tek dominant kod; çoklu etiket/fenotip haritası gibi yorumlanmaz.
- DI alt tip/şiddet bilgisi yoksa **uydurulmaz**.
- `overjet`, `overbite`, `open bite`, `crossbite`, `gingivitis` eşik verilmemişse binary var/yok kabul edilir.
- Küçük örneklem mantığı, etki büyüklüğü, çoklu test düzeltmesi, robustluk ve CV sınırlılıkları raporda görünür olmalı.
- CV/AUC/delta-AUC sadece **secondary internal verification** olarak ele alınır; tek başına klinik prediktif iddia üretilmez.

---

## 1.5) Zorunlu okunacak minimum dosya seti

Rapor başlamadan önce en az aşağıdaki dosyalar okunmalı ve raporda kanıt olarak referanslanmalıdır:

- `Manuscript_Data/README_Manuscript_Data.md`
- `Manuscript_Data/ANALYSIS_RESULT_MAP.csv`
- `Manuscript_Data/FILE_REGISTRY.csv`
- `Manuscript_Data/06_ai_handoff_context/FINAL_HANDOFF_QUICKSTART.md`
- `Manuscript_Data/01_protocol_and_docs/final_1.md`
- `Manuscript_Data/01_protocol_and_docs/camber_sap_v2_publication_ready.md`
- `Manuscript_Data/02_source_data/metadata/codebook_v3_fixed.md`
- `Manuscript_Data/03_analysis_scripts/oi_oro_dental_master_FINAL_1_2.py`
- `Manuscript_Data/04_final_outputs/OUTPUT_SCHEMA_AND_VARIABLE_LINEAGE.md`
- `Manuscript_Data/04_final_outputs/TRANSPARENCY_NOTES.md`
- `Manuscript_Data/04_final_outputs/REPRODUCIBILITY_ENVIRONMENT.md`

Ek olarak mevcutsa manuscript-facing dosyalar da okunur (Methods/Results/Discussion).

## 1.6) İstatistikçi sonrası ek analiz katmanı (zorunlu dahil et)

`missing_statistical_analyses/` klasörü, istatistikçiden gelen değerlendirmeler sonrasında tarafımızdan üretilen doğrulama/destek/robustluk raporlama katmanını içerir ve bu prompt kapsamında **zorunlu olarak** değerlendirilmelidir.

En az aşağıdaki dosyalar okunmalı ve raporda uygun etikette (`[Supporting]` veya `[Reference-only]`) kullanılmalıdır:

- `missing_statistical_analyses/analysis_gap_audit.md`
- `missing_statistical_analyses/supporting_alternative_grouping.csv`
- `missing_statistical_analyses/robustness_classification_table.csv`
- `missing_statistical_analyses/cv_reporting_support_table.csv`
- `missing_statistical_analyses/analysis_support_synthesis.md`
- `missing_statistical_analyses/copilot_analysis_completion_report.md`

Not:
- Bu katman **primary sonuç üretimi için değil**, primary bulguların yorum güvenliği ve izlenebilirliğini güçlendirmek için kullanılır.
- Bu dosyalardan gelen bulgular, FINAL.1.2 authoritative katmanının yerine geçmez.

---

## 2) Zorunlu rapor bölümleri

### 2.1 Genel çalışma özeti
- Çalışmanın amacı
- Analiz kapsamı
- Gelinen son aşama
- FINAL.1.2’nin süreçteki rolü

### 2.2 Tüm analizlerin sistematik dökümü
Her analiz için şu alanları ver:
- Analiz adı
- Araştırma sorusu / hipotez
- Veri seti ve alt grup(lar)
- Değişkenler
- Yöntem/test/model
- Varsayım kontrolleri (varsa)
- Sayısal çıktılar (uygun metriklerle)
- Kısa yorum

### 2.3 FINAL.1.2 özel bölümü
- FINAL.1.2’de yer alan tüm ana analizleri görünür bir başlıkta topla.
- Her biri için: yöntem, çıktı dosyası, temel bulgu, yorum.
- Uygun yerlerde p-değeri, GA, etki büyüklüğü, performans metriği ver.

### 2.4 İstatistikçi geri bildirimi sonrası ek analizler
- Hangi geri bildirim/boşluk sonrasında yapıldı?
- Hangi veri/değişkenlerde yapıldı?
- Hangi yöntem uygulandı?
- Öncekinden farkı ne?
- Yeni bulgu ve genel etkisi ne?

> Not: Bu bölümde reconciliation workstream’i “frozen reference layer” olarak konumlandır.

### 2.5 Bütüncül değerlendirme
- Bulguların ortak resmi
- Destekleyen/çelişen noktalar
- Nihai çıkarımlar
- Sınırlılıklar ve yorum sınırları

### 2.6 Kanıt etiketi ve raporlama dili standardı
Her önemli ifade için aşağıdaki etiketlerden biri kullanılmalı:
- `[Authoritative]` → FINAL.1.2 birincil kaynaklarından doğrudan doğrulanan bilgi
- `[Supporting]` → destekleyici analiz/ek paket bulgusu
- `[Reference-only]` → frozen istatistikçi katmanı veya provenance bilgisi
- `[Assumption]` → doğrudan kanıtlanamayan ancak açıkça belirtilen varsayım

Sayısal raporlamada mümkün olduğunca aşağıdakiler verilmelidir:
- p-değeri
- güven aralığı (varsa)
- etki büyüklüğü
- örneklem/denominatör bilgisi

Yorum dili:
- “kanıtlıyor/kanıtlandı” yerine, veri küçükse “destekliyor/işaret ediyor” gibi ihtiyatlı ifade tercih et.
- CV/robustness uyarıları varsa sonuç cümlesinde açıkça görünür olsun.

---

## 3) Kod, dosya organizasyonu ve envanter

Rapor kapsamındaki ilgili kod/çıktı dosyalarını tespit et ve **yeni bir rapor paketi klasörü** altında düzenle.
**Orijinal authoritative dosyaları taşımadan/silmeden** çalış (gerekirse kopya/özet/indeks üret).

Önerilen yapı:
- `01_raw_outputs`
- `02_processed_results`
- `03_figures_tables`
- `04_analysis_scripts`
- `05_reports`
- `06_final_summary`
- `07_notebook_readiness`

Her dosya için kısa envanter alanları üret:
- Dosya adı
- Kaynak yolu
- İçerik özeti
- Rapor içindeki kullanım amacı
- Authoritative / Supporting / Reference etiketi

### Dosya organizasyonu güvenlik kuralları
- Aynı isimli dosya çakışmalarında kaynak dosya üzerine yazma; hedefte sürüm eki kullan (`_v1`, `_v2`, `_from_FINAL12` vb.).
- Kopyalanan her dosya için `source_path` ve `copied_at` bilgisi envantere işlenmeli.
- Eğer bir dosya kopyalanmadıysa ve yalnız referanslandıysa envanterde `mode=referenced_only` olarak işaretlenmeli.
- Eski/dağınık sürümler için **silme yok**; yalnızca sınıflandırma yapılır: `keep_active`, `archive_candidate`, `exclude_from_notebook`.
- "Gereksiz dosyalardan kurtulma" hedefi için fiziksel silme/taşıma yerine önce `cleanup_plan.csv` üretilir.
- Yüksek riskli dosyalar (authoritative/final/provenance) varsayılan olarak `keep_active` kalır.
- `cleanup_plan.csv` içinde her satır için risk seviyesi zorunludur: `low`, `medium`, `high`, `critical`.
- `high/critical` riskli hiçbir dosya için fiili aksiyon önerisi verilmez; yalnızca `keep_active` veya `archive_candidate` önerilebilir.
- `exclude_from_notebook` etiketi sadece notebook kapsamı dışlama anlamına gelir; kaynak dosyanın fiziksel durumu değiştirilmez.
- Klasör yapısı sonunda mutlaka bir manifest üret:
	- `06_final_summary/output_manifest.csv`
	- alanlar: `relative_path`, `category`, `source_path`, `mode`, `notes`.

---

## 4) Reprodüksiyon ve izlenebilirlik

Zorunlu eşleme tabloları üret:

1. **Analiz → Kod dosyası → Çıktı dosyası**
2. **Bulgular → Kaynak tablo/metric satırı**
3. **Kronolojik akış özeti** (mantıksal üretim sırası)

Ayrıca:
- Eksik / bulunamayan / birebir eşleşmeyen dosyaları ayrı listede ver.
- Belirsiz kalan tüm noktaları “assumption/limitation” etiketiyle açıkça yaz.

### Notebook geçiş parite kontrolleri (zorunlu)
Notebook üretimine geçmeden önce aşağıdaki parite kontrolleri raporlanmalıdır:
- FINAL.1.2 ana tablolarındaki kritik metriklerin (n, p, etki büyüklüğü, temel prevalanslar) kaynak dosyalarla birebir uyumu.
- Destekleyici katmandan gelen değerlerin yanlışlıkla primary sonuç gibi etiketlenmediğinin kontrolü.
- `seed`/iterasyon bilgisi ve kullanılan estimator notlarının (özellikle CV/ΔAUC) açık kaydı.

Bu kontroller için ayrıca aşağıdaki dosya üretilmelidir:
- `07_notebook_readiness/parity_check_matrix.csv`
	- alanlar: `metric_name`, `authoritative_source`, `reported_value`, `match_status`, `comment`.

---

## 5) Beklenen çıktı formatı (zorunlu teslim)

1. **Ana kapsamlı rapor** (başlıkları net, akademik dilde)
2. **Dosya organizasyon paketi** (kategorize klasör yapısı)
3. **Envanter/indeks dosyası**
4. **Traceability eşleme dosyaları**
5. **Eksik/uyuşmazlık listesi**
6. **Kısa yönetici özeti** (2–4 paragraf)
7. **Notebook hazırlık paketi** (henüz notebook üretmeden)

### Zorunlu yürütme sırası
1. Kaynak okuma ve kapsam doğrulama
2. FINAL.1.2 çekirdek analiz dökümü
3. Ek/supporting/robustness/model-verification katmanlarının ayrıştırılması
4. Dosya envanteri ve traceability eşleme tablolarının üretimi
5. Rapor yazımı (ana rapor + yönetici özeti)
6. Kalite kontrol checklist doğrulaması

### Zorunlu teslim dosyaları (minimum)
- `05_reports/ana_rapor.md`
- `05_reports/yonetici_ozeti.md`
- `05_reports/analiz_dokum_tablosu.csv`
- `06_final_summary/dosya_envanteri.csv`
- `06_final_summary/analysis_to_code_to_output_map.csv`
- `06_final_summary/finding_to_source_map.csv`
- `06_final_summary/eksik_ve_eslesmeyenler.md`
- `06_final_summary/kalite_kontrol_sonuclari.md`
- `07_notebook_readiness/notebook_build_readiness.md`
- `07_notebook_readiness/notebook_blueprint.md`
- `07_notebook_readiness/cleanup_plan.csv`
- `07_notebook_readiness/notebook_source_priority.csv`

### Zorunlu tablo şablon standardı
`analiz_dokum_tablosu.csv` en az şu sütunları içermelidir:
- `analysis_id`
- `analysis_name`
- `analysis_tier` (`authoritative` / `supporting` / `reference-only`)
- `question_or_hypothesis`
- `dataset`
- `variables`
- `method_test_model`
- `key_numeric_outputs`
- `effect_size`
- `multiple_testing_note`
- `robustness_note`
- `cv_note`
- `interpretation`
- `source_files`

`finding_to_source_map.csv` en az şu sütunları içermelidir:
- `finding_id`
- `finding_text`
- `evidence_tag`
- `source_file`
- `source_location` (satır/kolon/section mümkünse)
- `confidence_level` (`high` / `medium` / `low`)

### Notebook hazırlık dosyalarının zorunlu içeriği
- `notebook_build_readiness.md`:
	- notebook üretimini engelleyebilecek blokajlar
	- non-blocking belirsizlikler
	- notebook üretimine geçiş kararı (go / conditional-go / no-go)
	- karar kuralları:
	  - `go`: blocking issue yok + parity_check_matrix kritik metriklerde tam eşleşme
	  - `conditional-go`: blocking issue yok ama non-blocking belirsizlikler var
	  - `no-go`: en az bir blocking issue var veya kritik metrik paritesi sağlanamıyor
- `notebook_blueprint.md`:
	- hedef notebook hücre planı (section/cell-by-cell)
	- hangi analiz hangi sırada ve hangi kaynaklardan beslenecek
	- hangi çıktı tablolarının notebook içinde üretileceği/çağrılacağı
	- her hücre için: `cell_no`, `cell_type (markdown/code)`, `purpose`, `input_files`, `output_artifacts`, `depends_on`
	- hata durumunda geri dönüş stratejisi: hangi hücre yeniden çalıştırılmalı, hangi hücre immutable kabul edilmeli
- `cleanup_plan.csv`:
	- `file_path`, `current_role`, `proposed_role`, `action_type`, `risk_level`, `rationale`
	- `action_type` yalnız: `keep_active`, `archive_candidate`, `exclude_from_notebook`
- `notebook_source_priority.csv`:
	- notebook inşasında kullanılacak dosyaların öncelik sırası (authoritative → supporting → reference)

### Notebook inşası için ek güvenlik şartları
- Notebook blueprint içinde “mutable” ve “immutable” katmanlar açıkça ayrılmalıdır.
- `immutable`: FINAL.1.2 sonuçlarının aynen referanslandığı hücreler.
- `mutable`: yalnızca destekleyici/raporlama amaçlı türev üreten hücreler.
- Aynı metrik birden fazla hücrede üretiliyorsa tek kaynak hücre belirlenmeli ve diğerleri ona referans vermelidir.

Rapor dilinde şu kurala uy:
- Mevcut dosyalara dayan.
- Doğrudan kanıt olmayan yerde tahmin/varsayım yaparsan bunu açıkça etiketle.
- Destek analizlerini primary bulgu gibi yükseltme.

---

## 6) Kalite güvencesi kontrol listesi (yayın öncesi)

Teslimden önce şu kontrolleri zorunlu çalıştır:

- [ ] FINAL.1.2 authoritative ve reference katmanlar net ayrıldı mı?
- [ ] `occl_tip==4` ve `dmft_dmft` kuralları ihlal edilmedi mi?
- [ ] Etki büyüklükleri ve çoklu test yorumu görünür mü?
- [ ] Robustluk ve CV uyarıları açıkça raporlandı mı?
- [ ] CV çıktıları prediktif iddia olarak sunulmadı mı?
- [ ] Analiz→kod→çıktı eşlemeleri tamam mı?
- [ ] Eksik/eşleşmeyen dosya listesi üretildi mi?

### Kabul kriteri (done definition)
Bu görev ancak aşağıdakiler sağlandığında tamamlanmış sayılır:
1. Ana rapor + yönetici özeti + envanter + traceability tabloları üretilmiş olmalı.
2. FINAL.1.2 ve supporting/reference katman ayrımı rapor içinde net görünmeli.
3. Her ana bulgunun en az bir kaynak dosya referansı olmalı.
4. Belirsiz/eksik noktalar “assumption/limitation” etiketiyle ayrı listelenmiş olmalı.
5. CV/AUC ve robustness uyarıları sonuç anlatımında açıkça yer almalı.
6. Notebook hazırlık paketi (`07_notebook_readiness/*`) eksiksiz üretilmiş olmalı.
7. Yeni notebook üretimine geçmeden önce net bir readiness kararı verilmiş olmalı.
8. Readiness kararı, `parity_check_matrix.csv` ve `eksik_ve_eslesmeyenler.md` ile tutarlı olmalı.

### Belirsizlik/eksik durum yönetimi (onay beklemeden)
- Dosya bulunamazsa: raporda `Eksik dosya` başlığı altında listele ve en yakın güvenilir alternatif kaynağı belirt.
- Eşleme birebir yapılamazsa: `partial match` etiketi kullan ve nedeni yaz.
- Çelişkili kaynak varsa: hiyerarşiye göre authoritative kaynağı esas al; diğerini `reference discrepancy` olarak not et.
- Bu durumlarda süreci durdurma; raporu kısıtları açıkça belirterek tamamla.

---

## 7) Nihai amaç

Bu promptun amacı, workspace içindeki tüm istatistiksel analiz sürecini (özellikle FINAL.1.2 ve sonrasındaki ek analizleri)
**içerik + kod + çıktı dosyası + izlenebilirlik** düzeyinde eksiksiz, düzenli, denetlenebilir ve profesyonel biçimde dokümante etmektir.
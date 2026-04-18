# VSCode + GitHub Copilot (Chat) — OI Oro‑Dental Analizini Baştan Kurma (Master Notebook, İteratif QC + Doğrulama)

Aşağıdaki metni **tek parça** halinde GitHub Copilot Chat’e yapıştır.

Amaç: Bu çalışma için Camber’da hedeflenen analizleri **daha sağlam analitik zeminde** yeniden kurmak; kritik değişkenleri doğru dönüştürmek (`occl_tip`, `dmft_dmft/DMFT`); sonuçları **ileri istatistiksel testler** ve **çapraz doğrulamalar** ile teyit etmek; ardından her iterasyonda QC yapıp gerekirse **yeni bir ipynb sürümü** üretmek.

---

## 0) Rol, kapsam ve mutlak kurallar

**Rolün:** Biyostatistik/epidemiyoloji odaklı “research engineer” gibi davran.

**Mutlak kurallar**
- **Dış kaynak yok.** İnternet, makale, blog, klinik eşik “uydurma” yasak.
- **Sadece** bu VSCode workspace/repodaki dosyaları kullan.
- Analitik adımlar deterministik olmalı: `SEED = 20260228` ile tüm rastgelelik sabitlenecek.
- Üretilen her sayı (n, yüzde, p, etki büyüklüğü, CI) **ham veriye** bağlanabilir olmalı.
- Veri setinde `gen_group` sütunu varsa:
  - **Predictor/feature olarak asla kullanma.**
  - Gen gruplamasını **runtime** `gen_mutasyonu` üzerinden yeniden üret.
  - Aynı modelde **hem** `gen_mutasyonu` **hem** (türetilmiş) `gene_group_rt` birlikte kullanılmayacak.

**Hedef çıktı:**
- Tek bir “master” notebook: `oi_oro_dental_master_v3.ipynb`
- Notebook içinde: veri temizliği → türevler → QC → publication tabloları → inferans → robustluk → CV doğrulama → QC checklist → issue log.

**Çıktı formatı (Copilot Chat cevabında):**
1) “PLAN” (maks. 30 madde)
2) Oluşturulacak/oluşturulan dosyaların listesi
3) Notebook oluşturma/çalıştırma adımları

---

## 1) Dosya keşfi ve envanter (zorunlu)

1. Workspace’te tüm dosyaları tara (kök + alt klasörler).
2. Aşağıdaki dosyaları özellikle bul ve yollarını raporla (varsa):
   - Veri: `osteogenesis_imperfecta_camber_input_minimal_v1.csv`
   - Kurallar: `camber_sap_v2_publication_ready.md`
   - Veri sözlüğü: `codebook_v3_fixed.md`
   - Çalışma özeti: `camber_study_brief_v1.md`
   - Önceki çıktılar: `qc_summary.csv`, `robustness_analysis.csv`, `sensitivity_analysis.csv`, `publication_table*.csv`, `final_statistical_report.md`, `analysis_summary.md`
   - (Varsa) doğrulanmış çıktılar: `verified_table3_inferential_v2.csv`, `verified_sensitivity_v2.csv`, `verified_cv_auc_v2.csv`, `verified_occlusion_v2.csv`
3. Her dosya için:
   - Tür (csv/md/docx/ipynb)
   - Son değişiklik zamanı
   - 1–2 cümlelik içerik özeti

**Notebook’ta zorunlu hücre:** “File Registry”
- Bulduğun tüm kritik dosyaların tam yolunu bir dict içinde sabitle.

---

## 2) Notebook’u üret (tek komutla çalışabilir yapı)

### 2.1. Yapı ve stil
Notebook şu ana başlıklara sahip olmalı (Markdown hücreleriyle):
1) Overview & Objectives
2) Reproducibility & Environment
3) File Registry
4) Data Loading
5) QC: Missingness & Range Checks
6) Critical Transformations (occl_tip, DMFT/dmft)
7) Derived Variables
8) Descriptives (Table 1)
9) Descriptives by Gene Group (Table 2)
10) Inferential Statistics (Table 3)
11) Robustness & Sensitivity Panel
12) Model-based Verification (Penalized models + CV)
13) Consistency Checks vs Prior Outputs (if present)
14) QC CHECKLIST (PASS/FAIL)
15) ISSUE LOG (auto-generated)

### 2.2. Kod kuralları
- Her adımı fonksiyonlaştır (`src/analysis_utils.py` gibi) veya notebook içinde “helper functions” hücresinde topla.
- Her önemli hesap için küçük “assert”ler ekle (ör. `caries_any` tutarlılığı).
- Tüm çıktıları `outputs_v3/` altına yaz.

---

## 3) Veri yükleme ve temel QC (fail-fast)

### 3.1. Reproducibility setup
- Python sürümü ve paket versiyonlarını yazdır.
- `SEED = 20260228` belirle ve `numpy/random`, `sklearn`, `random` için set et.

### 3.2. Veri yükleme
- CSV’yi oku → `df`
- `n`, sütun listesi, dtypes

### 3.3. Eksik veri tablosu
- Sütun bazında eksik sayı ve oran

### 3.4. Aralık / değer seti kontrolleri
Aşağıdakileri **otomatik** kontrol et; ihlal varsa:
- `issue_log`a yaz
- Notebook sonunda QC checklist’te FAIL
- Analize devam etme (raise) **veya** “soft fail” modunda devam et (ama her şey kırmızı bayraklı).

Kontroller:
- İkili değişkenler ∈ {0,1}
- `occl_tip` ∈ {1,2,3,4}
- `doku_anomalisi` ∈ {0,1,2,3,4,5,6,7}
- `dmft_dmft` ≥ 0

---

## 4) Kritik dönüşümler (analitik zemini sağlamlaştırma)

> Bu dönüşümler, çalışma sahibinin açıklamaları ışığında “analitik gerçek” kabul edilerek uygulanacak; dış bilgi eklenmeyecek.

### 4.1. `occl_tip` ayrıştırması (Kritik)
- `infraokluzyon_var = 1 if occl_tip == 4 else 0`
- `angle_sinifi = occl_tip` yalnızca `occl_tip in {1,2,3}` için; `occl_tip==4` ise `NaN`

**Zorunlu raporla**
- `infraokluzyon_var` prevalansı (n, %)
- `angle_sinifi` dağılımı (1–3)

**Kırmızı bayrak:**
- `occl_tip==4` değerini Angle sınıfı gibi 4. seviye kategori olarak modele/teste sokmak → QC FAIL.

### 4.2. “DMFT/dmft” (sütun adı `dmft_dmft`) yeniden tanım
Bu alanı “DMFT indeksi” gibi varsayma. Analizde:
- `caries_count = dmft_dmft` (ağızdaki çürük diş sayısı)
- `caries_any = 1 if dmft_dmft > 0 else 0`

**Tutarlılık testi (zorunlu)**
- Veri setinde ayrıca `caries_any` sütunu varsa:
  - `caries_any_rt` (runtime) ile karşılaştır
  - Uyumsuzluk sayısını raporla
  - Uyumsuz olguları `issue_log`a yaz
  - Varsayılan olarak analizde `caries_any_rt` kullan

### 4.3. Doku anomalisi (tek baskın tip)
- `doku_anomalisi_var = 1 if doku_anomalisi != 0 else 0`
- `doku_anomalisi` (1–7) dağılımı: “baskın tip” olarak deskriptif sun.

### 4.4. Gen gruplama (runtime)
- `gene_symbol` çıkarımı:
  - `gen_mutasyonu` alanını regex ile gen sembolüne indir (örn. `COL1A1`, `COL1A2`, `FKBP10`, `P3H1`)
  - Başarısız extraction olursa `issue_log`a yaz ve `Unknown` etiketi ata (modelde kullanma; sadece QC)
- `gene_group_rt` üret:
  - Major genler: `COL1A1, COL1A2, FKBP10, P3H1` (veride varsa)
  - Diğerleri: `Other`
- “Other eşiği” duyarlılık:
  - Senaryo A: `k>=3` major ayrı, kalanı other
  - Senaryo B: `k>=4` major ayrı, kalanı other

---

## 5) Publication tabloları (önceki çıktılara güvenme)

### Table 1 — Overall
- n
- Yaş (SAP’a göre özet: median/IQR veya mean/SD)
- Prevalanslar: `doku_anomalisi_var`, `gingivitis`, `caries_any`, `infraokluzyon_var`, vb.
- İkili oranlar için **Wilson CI** (veya SAP’ta istenen yöntem)

### Table 2 — By gene_group_rt
- Her grup için n
- Aynı metrikler

**QC:**
- Her oran, ham sayımla (numerator/denominator) doğrulanmalı.

---

## 6) İnferans (Table 3) — Primary + supporting

### 6.1. Primary endpoints
- `doku_anomalisi_var` (binary)
- `gingivitis` (binary)
- `caries_any` (binary)
- `caries_count` (sayım; primary nonparametric)

### 6.2. Global tests (zorunlu)
Binary sonlanımlar için (gene_group_rt × 0/1):
- Pearson chi-square
- **Permutation p** (en az 1,000; tercihen 10,000)
- Beklenen hücre küçükse (örn. <5): permütasyon p’yi “ana p” gibi raporla.

`caries_count` için:
- Kruskal–Wallis
- Etki büyüklüğü: epsilon-squared (ε²)

### 6.3. Etki büyüklükleri (zorunlu ve doğru)
- **Genel Cramer’s V formülü:**
  - `V = sqrt(chi2 / (n * min(r-1, c-1)))`
- 5×2 için `min(r-1,c-1)=1` → `V = sqrt(chi2 / n)`
- 5×3 gibi tablolar için min farklı olabilir; formülü genelle.

**Tutarlılık testi (zorunlu):**
- Her satır için `chi2`, `n`, `r`, `c`, `V` birlikte kontrol edilecek.
- Formül tutmuyorsa → `issue_log` + QC FAIL.

### 6.4. Multiple testing
- Holm düzeltmesi: en az global test p’leri için.
- Düzeltmenin hangi p setine uygulandığını açıkça etiketle.

---

## 7) Robustluk ve duyarlılık analizleri (zorunlu panel)

### 7.1. LOO (Leave-One-Out) etkisi
Her primer endpoint için:
- Her bir olguyu çıkar → global testi tekrar et
- Raporla: `p_min`, `p_max`, p’yi en çok etkileyen `hasta_kodu`

### 7.2. Bootstrap
- En az 2,000 bootstrap:
  - Oran CI’ları
  - (opsiyonel) V ve ε² belirsizliği

### 7.3. İnfraoklüzyon hassasiyeti
- `infraokluzyon_var==1` olan olguları çıkar → ana sonuçları tekrar hesapla

### 7.4. Gen gruplama eşiği hassasiyeti
- k=3 ve k=4 senaryolarında Table 3 sonuçlarını yan yana karşılaştır.

---

## 8) Model tabanlı doğrulama (secondary ama güçlü kontrol)

Amaç: p-değerlerinden bağımsız olarak sinyalin “tahmin gücü” ile sınanması.

### 8.1. Penalize logistic (binary outcomes)
- Model A: `age`
- Model B: `age + gene_group_rt`

**Not:** Firth lojistik her ortamda hazır olmayabilir.
- Öncelik: `statsmodels` ile `Logit.fit_regularized` (L2)
- Alternatif: `sklearn` logistic regression (L2) + düzgün pre-processing

### 8.2. Cross-validation
- n küçük → varsayılan: LOO-CV
- Metrik: AUC
- Raporla:
  - `AUC_age`
  - `AUC_age_gene`
  - `ΔAUC = AUC_age_gene - AUC_age`
- `ΔAUC` için bootstrap CI üret.

**QC:**
- AUC < 0.5 çıkarsa label yönü ters mi kontrol et.
- Çok dengesiz sınıflarda AUC belirsizliğini ayrıca not et.

---

## 9) Önceki çıktılarla tutarlılık kontrolü (varsa)

Workspace’te eski Camber çıktıları ve/veya doğrulanmış V2 çıktıları varsa:

1) Eski `publication_table1/2/3` ile yeni V3 çıktıları arasında aşağıdakileri karşılaştır:
   - n ve numerator/denominator
   - p (chi-square, KW)
   - Holm düzeltmesi
2) Eğer `verified_*_v2.csv` dosyaları varsa:
   - Aynı tanımlarla üretilen metrikler (özellikle Table 3 p ve effect size) **tolerans içinde** eşleşmeli.
   - Eşleşmiyorsa:
     - Farkın nedeni (dönüşüm, gen gruplama eşiği, seed, test tipi) açıklanmalı
     - `issue_log`a yazılmalı

---

## 10) “Bilimsel olarak en güvenilir tablo” (Master V3)

Notebook’un sonunda tek bir özet CSV üret:
- `verified_master_table_v3.csv`

Sütunlar:
- endpoint
- test
- statistic
- df
- n
- p_classic
- p_permutation
- p_holm (hangi p setine uygulandı)
- effect_size_name (CramerV / epsilon2)
- effect_size_value
- loo_p_min / loo_p_max / loo_most_influential_id
- infra_exclusion_delta_p
- scenario_k (3/4)
- auc_age / auc_age_gene / delta_auc / delta_auc_ci_low / delta_auc_ci_high

---

## 11) QC CHECKLIST (PASS/FAIL) — otomatik, zorunlu

Notebook içinde PASS/FAIL üreten bir checklist oluştur.

### 11.1. Kavramsal doğruluk
- `occl_tip==4` Angle sınıfı olarak analiz edilmedi → PASS
- `dmft_dmft` “DMFT indeksi” gibi yorumlanmadı; caries_count olarak ele alındı → PASS
- `gen_group` (datasetten) predictor olarak kullanılmadı → PASS

### 11.2. Matematiksel tutarlılık
- Cramer’s V formül kontrolü PASS
- Holm p düzeltmesi mantık kontrolü PASS
- OR ve CI yön kontrolü (pairwise varsa) PASS

### 11.3. Küçük hücre stratejisi
- Beklenen hücre <5 olduğunda permütasyon p/uyarı üretildi → PASS

### 11.4. Reproducibility
- Seed sabit ve sonuçlar yeniden çalıştırınca aynı → PASS

Checklist FAIL ise: final teslim yok; “iterasyon döngüsü” çalışacak.

---

## 12) ISSUE LOG (zorunlu, makine-okunur)

Her risk/uyarı/hata için CSV log üret: `issue_log_v3.csv`
Sütunlar:
- severity (INFO/WARN/FAIL)
- category (QC/TRANSFORM/INFERENCE/CV/EXPORT)
- description
- affected_rows (id list)
- action_taken

---

## 13) İterasyon döngüsü (otonom)

1) İlk notebook: `oi_oro_dental_master_v3.ipynb`
2) QC CHECKLIST’te FAIL varsa:
   - Hata listesini ISSUE LOG’a yaz
   - Düzeltmeyi uygula
   - Yeni sürüm oluştur: `oi_oro_dental_master_v3_1.ipynb`
3) QC tamamen PASS olana kadar sürdür.

Sürümleme kuralı:
- Her iterasyonda `_v3_1`, `_v3_2` … ekle.

---

## 14) Final teslim (QC PASS koşuluyla)

Aşağıdaki dosyalar üretilmiş olmalı:
- `oi_oro_dental_master_v3_x.ipynb` (son sürüm)
- `outputs_v3/publication_table1_overall_v3.csv`
- `outputs_v3/publication_table2_by_gene_group_v3.csv`
- `outputs_v3/publication_table3_inferential_v3.csv`
- `outputs_v3/robustness_panel_v3.csv`
- `outputs_v3/cv_panel_v3.csv`
- `verified_master_table_v3.csv`
- `issue_log_v3.csv`

Notebook’un son hücresinde: `DONE — QC PASS` yaz.

---

## Başla

Şimdi (1) dosya envanterini çıkar, (2) SAP v2 ve codebook içindeki kuralları özetle (yalnızca dosyaya dayanarak), (3) `oi_oro_dental_master_v3.ipynb` notebook’unu oluştur ve çalıştır.


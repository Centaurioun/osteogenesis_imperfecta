---
name: 'Python Ana Analiz Yönergeleri (OI Projesi)'
description: 'Veri kalitesi, istatistik modellemesi ve Jupyter Notebook standartları.'
applyTo: '**/*.{py,ipynb}'
---

# 🐍 Python Data Analysis & Jupyter Notebook Guidelines

## 1. Kütüphane ve Ortam Kuralları
- **Determinizm İlacı:** Modeller arası değişmezlik için her script veya Jupyter notebook'un giriş hücresinde şu bloğun bulunması ZORUNLUDUR:
  ```python
  import numpy as np
  import random
  import os
  SEED = 20260228
  np.random.seed(SEED)
  random.seed(SEED)
  os.environ['PYTHONHASHSEED'] = str(SEED)
  ```
- **Paket Mimari Tercihleri:** Hızlı manipulasyonlar için `pandas`/`numpy`; kesin (exact) ve non-parametrik testler için `scipy.stats`; lojistik regresyon ve model doğrulamaları için ise daima `statsmodels.api` kütüphanesini ana standart olarak kullanın. Temiz kod (PEP8) ve net docstring'ler yazın.

## 2. Pandas ile Güvenli Veri İşleme (Mutingations & Copy)
- **Destructive Değişiklik Yasağı:** Raw (ham) veri setini DataFrame içinde okuduktan sonra üzerine in-place (inplace=True) yıkıcı değişiklik yapmayın. Mutlaka bir `df_clean = df.copy()` ile sanal kopyalama (feature engineering scope) yaratın; uyarı almaktan ("SettingWithCopyWarning") kaçının.
- **Runtime Feature Engineering:**
  - Orijinal CSV içinde `gen_group` yer alsa dahi bunu **predictive** olarak kullanmayın. Uygulama anında (runtime); `gen_mutasyonu` alanını Regex ile temizleyerek `gene_group_rt` sınıflamasını (örn: `COL1A1`, `COL1A2`, `Other`) siz kendiniz inşa edin.
  - Veri setinde `occl_tip`=4 saptanması anında **primary Angle alanı** `angle_sinifi_clean = np.nan` ve ayrı bayrak `infraokluzyon_var_clean = 1` dönüşümlerini yapın. Legacy uyumluluk gerekiyorsa `angle_sinifi`/`infraokluzyon_var` alanlarını koruyabilirsiniz; ancak analizde öncelik `*_clean` alanlarındadır.
  - Dönüşüm sonrası `assert df_clean['occl_tip'].isin([1,2,3,4]).all()` ve `assert df_clean.loc[df_clean['occl_tip']==4, 'angle_sinifi_clean'].isna().all()` doğrulamaları zorunludur.
  - `dmft_dmft` için analysis-facing temiz alias `caries_count_total = dmft_dmft` kullanın. `caries_count`/`caries_any` legacy alanları yalnızca backward-compatibility bağlamında tutulmalıdır.
  - Doku anomalisi endpointlerinde round-two önceliği `doku_anomalisi_any` olmalıdır; `doku_anomalisi_var` adı kullanılacaksa legacy uyumluluk için açıkça etiketlenmelidir.

## 3. İstatistiksel Hesaplama Standardizasyonu (Wrappers)
- P-değerleri ve etki analizlerini (Effect Size) açıkta bırakmayın. `scipy.stats` içerisinden ilgili formülleri çağıran ve geriye `{'p_value': x, 'effect_size_stat': y}` sözlüğü / tuple'ı döndüren Python "helper (wrapper)" fonksiyonları yazın.
- **Hücre Dinamiği Check (Cell Expected < 5):**
  `scipy.stats.chi2_contingency` çağrısından dönen `expected` matrisini `np.any(expected < 5)` ile IF koşulunda kontrol edin; yanıt `True` döndüğü an standart Ki-kare'yi pass (geçme) yapıp doğrudan 10k iterasyonlu custom-build Permütasyon metodunuzu ateşleyin.

## 4. Analiz Çıktıları ve Notebook Yapısı
- Otonom olarak ürettiğiniz tüm raporlar, QC (Kalite Kontrol) sonuçları ve yeni oluşturulan DataFrameler zorunlu olarak `outputs_v3/` gibi ayrı bir output dizini içine çıkarılmalıdır (`index=False` ile).
- Post-advisor round-two dataset üretiminde canonical issue log adı: `01_data/derived/issue_log_post_advisor_round2_v1_2026-04-18.csv`. Legacy `issue_log_v3.csv` gerekirse yalnızca compatibility kopyası olarak korunabilir.
- Çıktılardaki sayılar bilimsel formatlanmalıdır. P-değerlerinin çok ufak kalması halinde `<0.001` formatını benimseyin. Diğer oran/tablo değerlerini virgülden sonra üç hane formatta (`{:.3f}`) kısıtlayın.
- **Jupyter Markdown Flow:** Her Python hücre algoritması açık ve yönlendirici Markdown başlıkları içermek zorundadır (Örn: `### Adım 7: Table 3 İnferans Testleri`). Ek olarak, hazırladığınız her notebook'ta; `File Registry`, `Auto-QC Checklist` ve `Issue Logger` blokları kesinlikle son durak olarak yer almalıdır.
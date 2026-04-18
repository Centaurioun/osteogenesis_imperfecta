# 🤖 Multi-Agent & Sistem Kuralları (Osteogenesis Imperfecta Analysis)

Bu çalışma alanı, küçük örneklemli (n=34) pediatrik bir hastalık raporlama ekosistemidir. Copilot, Claude ve tüm otonom asistanların aşağıdaki analitik ve mimari protokollere sıkı sıkıya uyması zorunludur:

## 1. Planlama ve Yürütme Mimarisi
- **Çok Adımlı Planlama:** Kullanıcıdan gelen görevleri aceleyle doğrudan koda dökmek yasaktır. Önce adım adım bir analiz süreci ve stratejisi tasarlayın (Örn: Keşif -> Hipotez inşası -> Kod -> Hata Yakalama -> Teyit). Gerekiyorsa `switch_agent` mantığı ile keşif modunu kullanın.
- **Mutlak Saydamlık:** Kodla üretilen ama analizden mantıksal sebeplerle dışlanan vakalar (`hasta_kodu`), birleştirilmiş kategoriler veya göz ardı edilen anomaliler, sadece kod bloğunda kalmamalı, kullanıcının Markdown çıktısına açık bir "Karar Gerekçesi" ile sunulup ayrıca `issue_log_v3.csv` dosyasına yazılmalıdır.

## 2. Katı Analitik Standartlar (N=34 Kısıtlamaları)
- **Küçük Hücre Yasağı (Categorical Data):** Çapraz tablolarda veya hipotez testlerinde beklenen frekans (expected cell count) < 5 çıkarsa, **Standart Pearson Ki-Kare TESPİT EDİLDİĞİ AN TERK EDİLMELİDİR.** Yerine mutlak suretle **Permütasyon Testi (tercihen >10k iterasyon) veya Fisher-Freeman-Halton / Kesin Exact** hesaplaması devreye sokulmalıdır.
- **Sürekli Veri Standartları (Continuous Data):** Dağılımların çoğu parametrik dışı/non-normal kabul edilmelidir. İkili grup muayenesinde otomatik olarak **Mann-Whitney U**, 3 ve üzeri gruplu muayenelerde ise **Kruskal-Wallis** dışında test uygulamayın.

## 3. Model Güvenilirliği ve Ceza-Düzeltmeleri
- **Aşırı Öğrenme Prensibi (Overfitting Handling):** Düşük n sebebiyle lojistik modeller kurarken klasik MLE metodolojisi yerine **Penalize Ridge/L2 veya Firth Lojistik** regresyonları tercih edin ki katsayılar patlamasın.
- **FDR / Çoklu Karşılaştırma Düzeltmeleri:** P-değerlerini listelerken tüm seriler için varsayılan olarak **Holm-Bonferroni (Holm adjustment)** mekanizmasını entegre edip düzeltmeleri tabloya ekleyin.
- **Etki Büyüklüğü (Effect Size) Şart Koşulu:** Test sonuçları sadece "P-değeri" ile verilemez! Ki-kare ve permütasyon testlerinin sağ varyansına **Cramer's V (Cramer's Phi)**, Kruskal-Wallis non-parametrik testinin sağ varyansına ise mutlak suretle **$\varepsilon^2$ (Epsilon-Squared)** hesapları yerleştirilmelidir.

## 4. Multikolinerite (Bağımlı Veri) Alarmı
- Çok değişkenli (multivariate) hiçbir regresyon ya da istatistik modeline `yas` ile `dentisyon_donemi_kod` sütunlarını **aynı anda sokmayın**. Biri diğerinin tamamen varlık sebebidir ve modeli bozar. Model bazlı çalışacaksanız, temel kronolojik kovaryatanız daima `yas` sütunu olmalıdır.
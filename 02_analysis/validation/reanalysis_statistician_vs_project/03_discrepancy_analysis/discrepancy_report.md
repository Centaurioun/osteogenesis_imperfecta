# Discrepancy Attribution Report

## Executive summary

Legacy replication ve rule-constrained replication karşılaştırması sonucunda en kritik fark sürücüleri üç başlıkta toplanmıştır:

1. **Kodlama farkı (özellikle OCCL/infraocclusion ayrımı)**
2. **Değişken tanımı farkı (doku anomalisi ve dmft/caries türevleri)**
3. **Raporlama/modelleme katmanı farkı (hangi endpointlerin primary inferential aileye alındığı)**

## Concordance overview

- `fully concordant`: 8 analiz
- `directionally concordant but method-sensitive`: 6 analiz
- `definition-sensitive`: 1 analiz (A02)
- `substantively discordant`: 0 analiz

## Key discrepancy drivers

### 1) OCCL / infraocclusion

- Legacy hatta `occl_tip=4` aynı OCCL ailesinde yer aldı.
- Rule-constrained hatta `occl_tip=4` ayrı infraocclusion değişkeni olarak ele alındı.
- Bu nedenle legacy p=0.017 sonucu manuscript authority katmanına doğrudan taşınamaz.

### 2) Tissue anomaly endpoint definition

- Legacy analiz multicategory yapı kullandı.
- Project-valid analiz dominant-code mantığını koruyup manuscript-facing binary endpoint (`doku_anomalisi_var_rt`) kullandı.
- Sonuç yönü tamamen tersine dönmedi; fakat anlamlılık dili yöntem duyarlı hale geldi.

### 3) Dmft / caries semantics

- Legacy `dmft` tek başlıkta Kruskal ile değerlendirildi.
- Project-valid katmanda `dmft_dmft` count-like mantıkta hem `caries_count` hem `caries_any_rt` ile ele alındı.
- Bu tanım dönüşümü sonuçların yorum düzeyini değiştiriyor.

### 4) Multiplicity and robustness layer

- Legacy hatta correction/robustness zorunlu değil.
- Project-valid hatta Holm, robustness ve CV-transparency mevcut.
- Bu katman, “tek p-değeri” odaklı legacy yorumların daha temkinli hale gelmesine neden oluyor.

## Editorial implication

- Legacy bulgular tarihsel benchmark olarak korunmalı.
- Manuscript iddiaları rule-constrained katmana dayandırılmalı.
- Definition-sensitive analizlerde sonuç dili "exploratory signal" düzeyinde tutulmalı.

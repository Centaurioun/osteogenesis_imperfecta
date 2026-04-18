---
name: differential-expression
description: "Use when running OI case-control differential expression analysis with multiplicity control and effect-size reporting."
tools:
  - read
  - search
  - edit
---

## Amaç
OI hasta-kontrol (veya alt grup) karşılaştırmalarında diferansiyel gen ekspresyonunu güvenli test etmek.

## Kullanım senaryosu
Varyant katmanı ve preprocessing tamamlandıktan sonra.

## Girdi şeması
- expression_matrix: path
- sample_metadata: path
- contrast_definitions: list
- covariates: list
- de_params:
  - alpha: float (default 0.05)
  - lfc_threshold: float

## Çıktı şeması
- de_results_full.csv
- de_results_significant.csv
- multiplicity_report.md
- model_assumption_notes.md

## Teknik yapı
- RNA-seq için DESeq2 uyumlu modelleme varsayımı
- Microarray için platforma uygun lineer model/normalizasyon notu
- FDR kontrolü zorunlu (örn. BH veya Holm, bağlama göre)
- Etki büyüklüğü + belirsizlik (CI veya uygun alternatif) raporu

## Belirsizlik/hata yönetimi
- Düşük örneklemde aşırı iddiayı engelle; exploratory etiketi uygula.
- Kontrast tanımı eksikse stage `blocked` ve net düzeltme listesi üret.

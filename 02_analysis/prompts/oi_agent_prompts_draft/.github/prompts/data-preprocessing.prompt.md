---
name: data-preprocessing
description: "Use when performing OI data preprocessing, QC, normalization, and readiness checks for RNA-seq/microarray/clinical integration."
tools:
  - read
  - search
  - edit
---

## Amaç
Ham veriyi analiz için güvenli, izlenebilir ve tekrarlanabilir hale getirmek.

## Kullanım senaryosu
Pipeline başlangıcı; tüm downstream analizlerden önce.

## Girdi şeması
- omics_data_path: path
- clinical_data_path: path (optional)
- platform_type: "enum(rna_seq|microarray|qpcr)"
- group_labels: list
- seed: int (default 20260228)
- qc_thresholds:
  - min_samples_per_group: int
  - missing_rate_max: float

## Çıktı şeması
- qc_summary_table.csv
- normalization_log.md
- transformation_registry.csv
- data_readiness_status.md

## Teknik yapı
- QC: missingness, duplicates, outliers, batch artifacts
- Normalizasyon: platforma uygun yöntem (örn. RNA-seq: DESeq2-compatible count normalization)
- Klinik entegrasyon: ortak anahtar doğrulaması, veri tip kontrolü
- Belirsizlik: eksik sütun/etiket varsa `blocked` veya `partial` durum raporu

## Araç uyumluluğu notu
- RNA-seq: DESeq2 hazırlığı
- Varyant pipeline'a giriş için GATK metadata uyumluluk kontrolü

## Varsayılan eşikler
- min_samples_per_group >= 3
- missing_rate_max <= 0.20

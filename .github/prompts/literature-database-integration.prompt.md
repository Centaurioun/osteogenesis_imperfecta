---
name: literature-database-integration
description: "Use when integrating OI findings with OMIM, ClinVar, UniProt, GEO and literature evidence with traceable citations."
tools:
  - read
  - search
  - edit
---

## Amaç
Analiz bulgularını veri tabanı ve literatür kanıtlarıyla birleştirerek yorum güvenilirliğini artırmak.

## Kullanım senaryosu
Yolak/ağ ve varyant sonuçlarının biyomedikal bağlamlandırma aşaması.

## Girdi şeması
- candidate_genes: path/list
- candidate_variants: path/list
- disease_terms: list
- database_targets: list[OMIM,ClinVar,UniProt,GEO]

## Çıktı şeması
- database_evidence_table.csv
- literature_evidence_table.csv
- evidence_consistency_matrix.csv
- citation_ready_summary.md

## Teknik yapı
- OMIM API / ClinVar kayıt kimliği / UniProt accession alanları görünür tutulur.
- GEO sonuçları varsa dataset accession ile raporlanır.
- Her iddia için en az bir kaynak referansı gerekir.

## Hata yönetimi
- Kaynaklar arası çelişki varsa `reference discrepancy` olarak işaretle.
- Kanıt yetersizse `tentative` veya `exploratory` seviyesine düşür.

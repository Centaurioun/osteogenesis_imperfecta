---
name: pathway-network-analysis
description: "Use when mapping OI differential signals to pathways and interaction networks (Wnt/beta-catenin, TGF-beta, mTOR, ECM/collagen)."
tools:
  - read
  - search
  - edit
---

## Amaç
Etkilenen biyolojik yolakları ve protein etkileşim ağlarını OI bağlamında haritalamak.

## Kullanım senaryosu
DE sonuçları ve varyant önceliklendirme sonrası.

## Girdi şeması
- significant_gene_list: path
- background_gene_list: path
- optional_variant_gene_list: path
- pathway_sources: list[KEGG,Reactome,GO]
- network_sources: list[STRING]

## Çıktı şeması
- pathway_enrichment_results.csv
- network_hub_candidates.csv
- pathway_network_summary.md
- overinterpretation_risk_notes.md

## Teknik yapı
- Zenginleştirme analizinde çoklu test düzeltmesi zorunlu.
- STRING ağ skorlaması parametreleri açıkça yazılır.
- Wnt/beta-catenin, TGF-beta, mTOR ve kollajen/ECM ekseni özel olarak etiketlenir.

## Hata yönetimi
- Girdi gen listesi çok küçükse sonuç `exploratory` olarak etiketlenir.
- Veritabanı sürüm uyumsuzluğu varsa raporda sürüm-discrepancy notu eklenir.

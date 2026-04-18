# Publication Tables (v1) — Üretilen Tablo Çıktıları

Aşağıdaki tablolar, `osteogenesis_imperfecta_camber_input_minimal_v1.csv` üzerinden üretilmiştir ve yayın formatında tablo iskeleti + sayı özetlerini içerir.

## Table 1 — Genel tanımlayıcılar
- Dosya: `publication_table1_overall_v1.csv`
- İçerik: yaş, dentisyon dönemi, gen dağılımı, oklüzyon tipi, dmft/dmft, caries_any, doku_anomalisi_var, gingivitis, infraoklüzyon ve doku anomalisi tür dağılımı.

## Table 2 — Gen gruplarına göre özet
- Dosya: `publication_table2_by_gene_group_v1.csv`
- İçerik: COL1A1, COL1A2, FKBP10, P3H1 ve Other grupları için yaş medyan(IQR), dmft medyan(IQR), doku anomalisi var, gingivitis var, çürük var.

## Table 3 — İstatistiksel testler
### Table 3a — Global testler
- Dosya: `publication_table3_global_tests_v1.csv`
- İçerik: gen grubu ile (i) doku anomalisi varlığı, (ii) gingivitis, (iii) dmft arasındaki global testler; doku anomalisi için permütasyon p ve Cramer’s V.

### Table 3b — Hedefli 2×2 karşılaştırmalar (doku anomalisi)
- Dosya: `publication_table3_pairwise_doku_v1.csv`
- İçerik: COL1A1/COL1A2/FKBP10/P3H1 vs diğerleri; Fisher p, Haldane‑Anscombe OR ve %95 GA; Holm düzeltilmiş p.

> Not: Bu tablo seti “ön analiz” çıktısıdır. SAP v2’ye göre bootstrap GA, LOO stabilite ve yaşla ayarlı penalize lojistik doğrulaması eklenmelidir.


# İstatistik Raporu — v1 (Ön analiz, yeniden-hesaplanmış)

Bu rapor, Camber’a yüklenmesi önerilen minimal veri seti üzerinden üretilmiştir:
- Veri: osteogenesis_imperfecta_camber_input_minimal_v1.csv
- Kayıt mantığı: camber_study_brief_v1.md + codebook_v3_fixed.md

## 1) Genel özet (n=34)
- Yaş: medyan 11.0 (IQR 6.0–14.8), min–maks 2–18
- dmft_dmft: medyan 1.5 (IQR 0.0–3.8), min–maks 0–14
- Çürük var (caries_any=1): 24/34 (%70.6)
- Doku anomalisi var: 10/34 (%29.4)
- Gingivitis var: 11/34 (%32.4)
- İnfraoklüzyon var: 1/34 (%2.9)

## 2) Gen grupları
- Major genler: COL1A1, COL1A2, FKBP10, P3H1; diğerleri “Other”
- gen_mutasyonu frekansları: {'P3H1': 8, 'FKBP10': 8, 'COL1A2': 7, 'COL1A1': 6, 'WNT1': 1, 'PRDM5': 1, 'ALX3': 1, 'LTBP3': 1, 'LRP5': 1}

## 3) Global test özeti
- Gen_grubu × doku_anomalisi_var: χ²=7.881, p=0.096; Permütasyon p=0.092; Cramer's V=0.481
- Gen_grubu × gingivitis: χ²=2.190, p=0.701
- Gen_grubu × dmft_dmft: H=5.311, p=0.257

> Not: n=34 olduğu için SAP v2’deki robustluk kontrolleri (bootstrap + LOO + permütasyon + gruplama hassasiyeti) zorunludur.

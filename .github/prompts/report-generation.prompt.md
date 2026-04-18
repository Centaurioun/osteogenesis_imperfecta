---
name: report-generation
description: "Use when producing a structured OI final report with evidence tags, caveats, and reproducibility metadata."
tools:
  - read
  - search
  - edit
---

## Amaç
Pipeline bulgularını düzenli, izlenebilir, yayın-adayı bir rapor yapısında sunmak.

## Kullanım senaryosu
Tüm önceki analiz blokları tamamlandıktan sonra son adım.

## Girdi şeması
- stage_outputs: list[path]
- evidence_tables: list[path]
- caveat_registry: path
- reproducibility_metadata: path

## Çıktı şeması
- final_oi_analysis_report.md
- executive_summary.md
- claim_confidence_registry.csv
- reproducibility_appendix.md

## Teknik yapı
- Her iddiaya `robust/tentative/exploratory/unsupported` etiketi verilir.
- Her etiket için zorunlu caveat cümlesi üretilir.
- Parametre/eşik/seed bilgileri appendix'te özetlenir.

## Hata yönetimi
- Eksik stage çıktısı varsa rapor `partial` işaretlenir.
- Belirsiz sonuçlar açık varsayım ve etki notu ile yazılır.

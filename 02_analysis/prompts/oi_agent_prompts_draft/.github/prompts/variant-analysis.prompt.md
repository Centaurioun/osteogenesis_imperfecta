---
name: variant-analysis
description: "Use when identifying and interpreting OI-related variants with explicit evidence grading and uncertainty controls."
tools:
  - read
  - search
  - edit
---

## Amaç
OI ile ilişkili varyantların (missense/nonsense/splicing) güvenli tespiti ve yorumlanması.

## Kullanım senaryosu
Preprocessing sonrası, genotip-fenotip analizinden önce.

## Girdi şeması
- variant_file: path (VCF/annotated TSV)
- sample_manifest: path
- target_genes: list (must include COL1A1, COL1A2)
- annotation_sources: list[VEP,ClinVar,OMIM]
- filters:
  - min_depth: int
  - max_population_af: float

## Çıktı şeması
- variant_qc_table.csv
- prioritized_variants.csv
- variant_interpretation_notes.md
- unresolved_variant_issues.md

## Teknik yapı
- Varyant çağırma/filtreleme adımı GATK uyumluluk notu ile belirtilir.
- Fonksiyonel anotasyon VEP uyumlu sınıflar üzerinden raporlanır.
- Klinvar/OMIM çapraz referansları kaynak linkiyle verilir.
- Patojenite iddiası için kanıt seviyesi etiketi zorunludur.

## Hata yönetimi
- Düşük derinlik veya çelişkili anotasyon varsa iddia seviyesi düşür.
- COL1A1/COL1A2 dışı adaylar için mekanistik açıklama yoksa exploratory etiketi ver.

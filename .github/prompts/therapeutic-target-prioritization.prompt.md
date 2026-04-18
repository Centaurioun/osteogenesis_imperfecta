---
name: therapeutic-target-prioritization
description: "Use when prioritizing OI therapeutic targets via pathway relevance, variant evidence, expression support, and druggability criteria."
tools:
  - read
  - search
  - edit
---

## Amaç
Terapötik hedefleri kanıt ağırlıklı ve açıklanabilir bir skorla önceliklendirmek.

## Kullanım senaryosu
DE + varyant + yolak + literatür entegrasyonu tamamlandıktan sonra.

## Girdi şeması
- integrated_candidates: path
- scoring_weights:
  - genetics_weight: float
  - expression_weight: float
  - pathway_weight: float
  - literature_weight: float
  - druggability_weight: float
- mandatory_pathways: list[mTOR,Wnt/beta-catenin,TGF-beta,ECM]

## Çıktı şeması
- target_priority_table.csv
- target_scoring_rationale.md
- sensitivity_to_weights.csv
- risk_of_overclaim.md

## Teknik yapı
- Skor bileşenleri açık formülle raporlanır.
- Ağırlık duyarlılık analizi (weight sensitivity) zorunludur.
- Klinik uygulanabilirlik iddiası için kanıt seviyesi etiketi gerekir.

## Hata yönetimi
- Tek kaynağa dayalı hedefler düşük güven seviyesine çekilir.
- Druggability kanıtı yoksa "research-priority" etiketi kullanılır.

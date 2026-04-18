# OI Workspace Subagents

## Kullanılabilir ajanlar
- `OI Reanalysis Coordinator`
- `OI Spec Mapper`
- `OI Data QA Auditor`
- `OI Biostatistics Reviewer`
- `OI Variant Prioritization Auditor`
- `OI Interpretation Reviewer`

## Tasarım ilkeleri
- Koordinatör + uzman alt ajan deseni
- İspatlanabilirlik ve izlenebilirlik
- Belirsizlikte konservatif yorum
- Pipeline zincirlenebilirliği

## Kısa test
1. Coordinator ile read-only analiz çağrısı yap.
2. Spec Mapper çıktısında directive checklist doğrula.
3. QA/istatistik/varyant/yorum bulgularını coordinator sentezinde kontrol et.

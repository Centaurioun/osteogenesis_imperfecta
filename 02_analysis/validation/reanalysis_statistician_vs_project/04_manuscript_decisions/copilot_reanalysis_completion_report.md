# Copilot Reanalysis Completion Report

## 1. What was replicated exactly

- İstatistikçi raporundaki descriptive frekanslar ve temel dağılımlar (`N=34`) tarihsel olarak doğrulandı.
- Legacy tablosunda non-significant sonuçların yönü korunarak yeniden üretildi.
- Gene mutation dağılımı ve Tablo 1 ana oranları birebir doğrulandı.

## 2. What changed under project rules

- OCCL kodlamasında `occl_tip==4` ayrı infraocclusion olarak ayrıldı.
- `doku anomalisi` multicategory legacy sunumundan dominant-code uyumlu manuscript endpointine taşındı.
- `dmft_dmft` classical parsed indeks gibi değil count-like alan olarak kullanıldı (`caries_count`, `caries_any_rt`).
- İnferans katmanında permutation/effect size/Holm/robustness şeffaflığı korundu.

## 3. Why key results changed

- **Kodlama farkı:** OCCL sonucunun legacy anlamlılığı, project-valid tanım değişimi nedeniyle taşınamadı.
- **Tanım farkı:** Doku anomalisi ve dmft/caries analizlerinde endpoint semantiği değişti.
- **Yöntem farkı:** Legacy p-değeri odaklı yaklaşım yerine correction + robustness + transparency katmanı eklendi.

## 4. Which results are manuscript-eligible

- A12 (`doku_anomalisi_var_rt`): correction-sensitive exploratory signal
- A13 (`caries_any_rt` / `caries_count`): definition-aware comparative reporting
- A14 (`gingivitis`): stable non-significant comparative statement
- A15/A16 descriptive framework outputs

(Detay: `manuscript_eligibility_table.csv`)

## 5. Which results are supplementary-only

- A01 ve A03-A11 (legacyde testlenmiş fakat current primary inferential ailede olmayan endpointler)

## 6. Which results should not be used

- A02 legacy OCCL significance claimi (`p=0.017`) project-valid tanım altında doğrudan kullanılmamalıdır.

## 7. Most important discrepancy drivers

1. OCCL/infraocclusion coding separation
2. Doku anomalisi endpoint tanımı
3. dmft semantic interpretation (count-like)
4. Multiplicity + robustness + transparency katmanı

## 8. Folder and file inventory

Generated under `reanalysis_statistician_vs_project/`:

- `00_audit/statistician_analysis_inventory.csv`
- `00_audit/legacy_to_project_map.csv`
- `00_audit/author_clarification_rules.md`
- `00_audit/reanalysis_startup_audit.md`
- `01_legacy_replication/statistician_legacy_replication.csv`
- `01_legacy_replication/legacy_descriptive_tables.csv`
- `01_legacy_replication/legacy_replication_notes.md`
- `02_rule_constrained_replication/statistician_rule_constrained_replication.csv`
- `02_rule_constrained_replication/rule_constrained_supporting_tables.csv`
- `02_rule_constrained_replication/rule_constrained_notes.md`
- `03_discrepancy_analysis/discrepancy_attribution_table.csv`
- `03_discrepancy_analysis/discrepancy_report.md`
- `04_manuscript_decisions/manuscript_eligibility_table.csv`
- `04_manuscript_decisions/legacy_vs_project_reconciliation_report.md`
- `04_manuscript_decisions/copilot_reanalysis_completion_report.md`
- `04_manuscript_decisions/manuscript_ready_main_text_paragraphs.md`
- `04_manuscript_decisions/supplementary_analysis_index.md`
- `04_manuscript_decisions/reviewer_response_legacy_vs_project.md`
- `05_logs/step_log.md`
- `05_logs/reanalysis_legacy_checkpoint.txt`
- `05_logs/reanalysis_rule_constrained_checkpoint.txt`
- `05_logs/reanalysis_discrepancy_checkpoint.txt`
- `05_logs/analysis_minimum_reporting_table.csv`

## 9. Author-clarification-dependent decisions

Aşağıdaki kararlar doğrudan author açıklamalarına bağımlıdır:

- OCCL `4` değerinin Angle dışında infraocclusion olarak ayrılması
- Doku anomalisi alanının baskın tek kod olarak yorumlanması
- DI tip/şiddet alt analizlerinin yapılmaması
- `dmft_dmft` alanının count-like yorumlanması
- overjet/overbite/open bite/crossbite/gingivitis alanlarının binary var/yok olarak tutulması

---

## Completion note

Bu paket legacy benchmark ile project-valid authority katmanını ayrıştırarak reviewer ve manuscript yazım hattında izlenebilir karar desteği sağlamak üzere tamamlandı.

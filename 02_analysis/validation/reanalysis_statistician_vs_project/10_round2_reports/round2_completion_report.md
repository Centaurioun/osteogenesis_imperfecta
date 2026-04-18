# Round 2 Completion Report

## 1. What was corrected

- A03–A11 için gerçek rule-constrained rerun eksikliği giderildi.
- A12cv satırındaki nokta tahmini-CI uyumsuzluğu açıkça doğrulandı ve işaretlendi.
- Manuscript wording etiketleri correction/fragility bağlamında daha temkinli hale getirildi.

## 2. What was rerun numerically

- A03–A11 endpointleri (`open_bite_rt`, `cross_bite_rt`, `over_bite_rt`, `transpozisyon_rt`, `dis_eksikligi_rt`, `gomulu_dis_rt`, `arti_dis_rt`, `taurodontizm_rt`, `kok_anomalisi_rt`) için permutation tabanlı rerun.
- A12cv, A13cv, A14cv için CV revalidation.

## 3. What remained editorial only

- A02 legacy OCCL significance’in manuscript authority dışı kalması editoryal + metodolojik karardır (tanım farkı nedeniyle).
- Primary inferential family kapsamı dışında kalan endpointlerin ana metin dışı tutulması editoryal çerçeve kararını korur.

## 4. What inconsistencies were fixed

- A03–A11 için “analiz yapılmadan supplemente atama” riski kaldırıldı.
- A12cv inconsistency explicit olarak kayda alındı; A13cv/A14cv consistent olarak işaretlendi.

## 5. What still needs human review

- A12cv tutarsızlığının upstream hesap mantığında (nokta tahmini vs bootstrap merkezleme) metodolojik yeniden tasarım gerektirip gerektirmediği.
- A04 için zayıf unadjusted sinyalin klinik olarak herhangi bir değer taşıyıp taşımadığı (supplement düzeyi yorum sınırı).
- Dergi-hedefli nihai cümle tonu (özellikle correction-sensitive comparative note ifadeleri).

## 6. Which manuscript decisions changed

- A13 ve A14 wording düzeyi daha temkinli etiketlere çekildi.
- A15 ve A16 için inferans çağrışımı azaltılıp descriptive authority vurgusu güçlendirildi.
- A03–A11 supplementary kararları artık numerik rerun ile destekli.

## 7. Which results should now be cited only as supplementary

- A01 ve A03–A11 satırları.
- A02 satırı legacy-reference-only olarak ana metinden dışarıda tutulmalıdır.

## 8. Code and output inventory

### Code
- `08_round2_scripts/run_round2_rule_constrained_reruns.py`
- `08_round2_scripts/revalidate_cv_rows.py`
- `08_round2_scripts/build_round2_discrepancy_updates.py`

### Outputs
- `09_round2_outputs/rule_constrained_rerun_A03_A11.csv`
- `09_round2_outputs/cv_rows_revalidated.csv`
- `09_round2_outputs/discrepancy_attribution_table_round2.csv`
- `09_round2_outputs/manuscript_eligibility_table_round2.csv`
- `09_round2_outputs/numerical_traceability_table.csv`

### Reports
- `10_round2_reports/round2_audit.md`
- `10_round2_reports/rule_constrained_rerun_A03_A11_notes.md`
- `10_round2_reports/cv_revalidation_notes.md`
- `10_round2_reports/discrepancy_report_round2.md`
- `10_round2_reports/manuscript_wording_reassessment.md`
- `10_round2_reports/round2_completion_report.md`

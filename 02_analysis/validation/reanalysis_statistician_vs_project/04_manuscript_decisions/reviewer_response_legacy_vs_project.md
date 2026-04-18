# Reviewer Response Draft — Legacy vs Project-Valid Results

Aşağıdaki metin, reviewer sorularına yanıt verirken legacy istatistikçi bulguları ile project-valid (rule-constrained) sonuçlar arasındaki farkı açıklamak için tasarlanmıştır.

## Önerilen kısa yanıt

We thank the reviewer for highlighting the discrepancy between the original statistician report and the current analysis outputs. To address this transparently, we conducted a dual-track replication: (i) a legacy replication that reproduces the original analytic logic as closely as possible, and (ii) a rule-constrained replication that applies the project’s final data definitions and author-clarified coding rules. The manuscript conclusions were based on the second layer (rule-constrained), while the first layer was retained as a historical benchmark.

## Önerilen detaylı yanıt

The apparent discrepancy is primarily definition- and coding-driven rather than a random analytic inconsistency. In particular, `occl_tip==4` was treated in the legacy context within the same OCCL family, whereas in the project-valid framework it is handled as a separate infraocclusion state (not an Angle class). Similarly, tissue anomaly and dmft-related variables are definition-sensitive under the final author-clarified framework (dominant-code interpretation for tissue anomaly; count-like interpretation for `dmft_dmft`).

Accordingly, we did not transfer legacy significance claims directly into the manuscript authority layer. Instead, we used rule-constrained outputs with multiplicity-aware interpretation, robustness checks, and transparent reporting. This approach preserves historical reproducibility while ensuring that final claims are aligned with the validated data semantics.

## Point-by-point mini template

- **Reviewer comment:** “Why does the OCCL significance differ from the original report?”
  - **Response:** The legacy OCCL result depends on coding `occl_tip==4` within the same family. In the validated framework, `occl_tip==4` is infraocclusion and modeled separately, so the legacy p-value is not directly portable to manuscript claims.

- **Reviewer comment:** “Why not use original dmft comparison directly?”
  - **Response:** Under final data semantics, `dmft_dmft` is treated as a count-like burden field; therefore, manuscript-facing analysis uses project-valid derivatives and interpretation.

- **Reviewer comment:** “Are original analyses discarded?”
  - **Response:** No. They are preserved and reported as a legacy benchmark, but manuscript authority decisions are based on rule-constrained replication.

## Citation/use note

Bu yanıt taslağı şu dosyalarla birlikte kullanılmalıdır:
- `03_discrepancy_analysis/discrepancy_report.md`
- `03_discrepancy_analysis/discrepancy_attribution_table.csv`
- `04_manuscript_decisions/manuscript_eligibility_table.csv`
- `04_manuscript_decisions/legacy_vs_project_reconciliation_report.md`

# ana_rapor

## Genel çalışma özeti
Bu dokümantasyon FINAL.1.2 authoritative analiz katmanını merkez alır ve supporting/robustluk/model-verification katmanlarını birincil sonuçlardan ayrıştırarak sunar.

## FINAL.1.2 ana analiz omurgası
- Authoritative script: `oi_oro_dental_master_FINAL_1_2.py`
- Authoritative outputs: publication_table1/2/3 + robustness_panel_FINAL + cv_panel_FINAL + verified_master_table_FINAL
- Küçük örneklem ve çoklu test farkındalığı korunmuştur.

## İstatistikçi sonrası ek analiz katmanı
- `missing_statistical_analyses/` altındaki doğrulama ve destekleyici dosyalar incelenmiştir.
- Bu katman primary sonuç yerine geçmez; yorum güvenliği ve izlenebilirlik desteği sağlar.
- Klasör recency değerlendirmesine göre en güncel destek katmanı `main_analysis_completion/` olarak işlenmiştir.

## Bulguların birlikte değerlendirilmesi
- Primary inferans ve etki büyüklüğü referansı authoritative tablolardan alınmıştır.
- Robustluk ve CV çıktıları secondary/internal verification çerçevesinde tutulmuştur.
- CV bulguları tek başına klinik prediktif iddia üretmek için kullanılmamıştır.

## Sınırlılıklar
- Küçük örneklem nedeniyle bazı bulgular hypothesis-generating düzeyde yorumlanmalıdır.
- Opsiyonel manuscript Q/A dosyalarının bir kısmı mevcut olsa da tekil canonical manuscript draft dosyası ayrı tutulmuş olabilir.

## Kaynak notu
Bu rapor, prompttaki zorunlu dosya listesi ve hiyerarşi kurallarına göre üretilmiştir.

## FINAL.1.2 investigator note (özet alıntı)
# FINAL.1.2 — Baş Araştırmacı Bilgilendirme Notu

Bu not, **kongre abstract’ı öncesi** çalışmanın (FINAL.1.2) tüm analiz hattını **en baştan**; “hangi analizi neden yaptık → ne bulduk → nasıl yorumladık → bu yorum bize ne söylüyor” mantığıyla ve **çıktı dosyalarına izlenebilir** biçimde özetler.

> Referans çıktılar (FINAL.1.2):
> - `publication_table1_overall_FINAL.csv`
> - `publication_table2_by_gene_group_FINAL.csv`
> - `publication_table3_inferential_FINAL.csv`
> - `robustness_panel_FINAL.csv`
> - `cv_panel_FINAL.csv`
> - `supplementary_sensitivity_FINAL.csv`
> - `supplementary_gene_group_map_FINAL.csv`
> - `verified_master_table_FINAL.csv`

---

## 1) Veri ve tasarım: neyi analiz ediyoruz?

### 1.1 Örneklem
- Analize giren olgu sayısı: **N=34** (`publication_table1_overall_FINAL.csv`, satır: N).
- Yaş: **median 11.0**, IQR **6.0–14.75** (`publication_table1_overall_FINAL.csv`, “Age (median, IQR)”).

### 1.2 Gen dağılımı ve “runtime gen gruplama”
**Neden runtime gruplama?**
- Veri setinde hazır bir `gen_group` alanı olsa bile, bunu “hazır predictor” gibi kullanmak **etik/analitik risk** oluşturur (tanım belirsizliği, sızıntı/overfit riski, tekrar üretilebilirlik sorunu). Bu yüzden gruplamayı yalnız `gen_mutasyonu` üzerinden **runtime** ürettik.

**Primary gen grupları (N):**
- COL1A2: 7
- P3H1: 8
- COL1A1: 6
- FKBP10: 8
- Other: 5

Bu dağılım Table 2’de “Primary” satırlarında görülebilir (`publication_table2_by_gene_group_FINAL.csv`, scenario=Primary).

---

## 2) Kritik değişken tanımları: neden yeniden tanımladık?

Bu kısım, yanlış klinik/istatistiksel yorumları önlemek için “değişkenlerin analitik anlamını” sabitler.

### 2.1 `occl_tip` ayrıştırması (Angle vs infraoklüzyon)
**Neden?** `occl_tip==4` Angle sınıflaması değildir; infraoklüzyon anlamına gelir. Aynı sütunda Angle (1–3) ile infraoklüzyonu karıştırmak kavramsal hata üretir.

**Ne yaptık?**
- Angle sınıfı (eligible set): Class I/II/III, ayrı dağılım raporu
- Infraoklüzyon: ayrı binary değişken

**Çıkt

## Supporting synthesis (özet alıntı)
# analysis_support_synthesis

## Analysis tier labeling
- `primary`: FINAL.1.2 descriptive + inferential tables (`publication_table1/2/3`).
- `supporting`: denominator/missingness transparency, alternative grouping, age/dentition checks.
- `robustness`: leave-one-out + infra exclusion expansions and stability classification.
- `secondary exploratory`: CV/AUC/delta-AUC verification support and warning traceability.

## Net impact on primary interpretation
- Supporting transparency analyses: **did not change** primary directional interpretation; improved denominator clarity.
- Alternative grouping checks: **partly changed magnitude** but not enough to upgrade inference strength.
- Robustness expansion: identified fragile endpoints and downgraded interpretive confidence where needed.
- Secondary CV checks: retained as suggestive internal signal only; not interpreted as standalone prediction evidence.

## Manuscript routing
- Methods: denominator handling, sparse-cell permutation fallback, robustness classification rule, secondary CV framing.
- Results: primary outcomes + concise support/robustness highlights.
- Discussion: fragile endpoint caveats, CV limitations, and hypothesis-gener

## Main analysis completion (özet alıntı)
# Main Analysis Completion Report

## Scope executed
- Frozen reference honored: `reanalysis_statistician_vs_project/` not expanded.
- Main analysis completion path resumed from existing supporting baseline.
- Only targeted cleanup + stage-wise packaging performed.

## Stage completion summary
1. Startup audit completed.
2. Data quality and denominator package refreshed.
3. Descriptive support package refreshed.
4. Primary inference support traceability package created.
5. Supporting package cleaned and extended.
6. Robustness package revised with defensible labels.
7. Model verification package revised with suppression logic.
8. Reporting package and manuscript readiness memo generated.

## Non-blocking residual issues
- Some CV rows remain estimator-inconsistent; retained only for transparency and suppressed for prediction claims.
- Small-sample fragility remains a scientific limitation, not a pipeline error.

## Ready state
- Manuscript section updates can proceed immediately using `manuscript_update_readiness.md`.


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

**Çıktı (deskriptif):**
- Angle (eligible) Class I: **27 (81.8%)**, CI 65.6–91.4
- Class II: **1 (3.0%)**, CI 0.5–15.3
- Class III: **5 (15.2%)**, CI 6.7–30.9
- Infraoklüzyon (total): **1 (2.9%)**, CI 0.5–14.9

Kaynak: `publication_table1_overall_FINAL.csv`.

### 2.2 `dmft_dmft` (DMFT/dmft değil → “caries_count”)
**Neden?** Bu sütun klasik DMFT indeksinin (D+M+F) bileşenleriyle tutulmuyor; klinik kayıtta “ağızdaki toplam çürük sayısı” gibi kullanılmış.

**Ne yaptık?**
- `caries_count = dmft_dmft`
- `caries_any_rt = 1 if caries_count>0 else 0`

**Çıktı (deskriptif):**
- `caries_any_rt`: **24 (70.6%)**, CI 53.8–83.2
- `caries_count`: median **1.5**, IQR **0.0–3.75**

Kaynak: `publication_table1_overall_FINAL.csv`.

### 2.3 Doku anomalisi (dominant tek kod)
- `doku_anomalisi_var_rt`: **10 (29.4%)**, CI 16.8–46.2 (`publication_table1_overall_FINAL.csv`).

---

## 3) Analiz stratejisi: neden bu istatistikleri seçtik?

### 3.1 Küçük örneklem ve seyrek hücre problemi
Gen grubu sayısı 5 ve binary sonlanımlar için 5×2 tablolar oluşuyor. Beklenen hücre sayıları düşük olabildiği için (örn. expected_min ≈ 1.47), yalnız klasik χ² p-değerine güvenmek riskli.

**Bu yüzden:**
- Klasik χ² istatistiğini raporladık ama p-değerini **permütasyon testi** ile doğruladık.

### 3.2 Çoklu test (family-wise kontrol)
- Primer hipotez ailesi: `doku_anomalisi_var_rt`, `gingivitis`, `caries_count` → **Holm (classic p)**
- Binary permütasyon ailesi: `doku_anomalisi_var_rt`, `gingivitis`, `caries_any_rt` → **Holm (perm p)**

Bu yapı, “caries_any”ın ikincil/dönüştürülmüş olması ve `caries_count`’ın non-parametrik testle değerlendirilmesi nedeniyle doğru aile ayrımı sağlar.

---

## 4) Çekirdek sonuçlar: ne bulduk?

### 4.1 Overall prevalanslar (özet)
Kaynak: `publication_table1_overall_FINAL.csv`
- Doku anomalisi var: **29.4%**
- Gingivitis: **32.4%**
- Caries_any: **70.6%**
- Caries_count median: **1.5** (IQR 0.0–3.75)

### 4.2 Gen gruplarına göre özet (Primary)
Kaynak: `publication_table2_by_gene_group_FINAL.csv` (scenario=Primary)
- COL1A2 (n=7): doku anom 57.1%, caries_any 57.1%, caries_count median 2.0
- P3H1 (n=8): doku anom 50.0%, caries_any 75.0%, caries_count median 2.0
- COL1A1 (n=6): doku anom 16.7%, caries_any 33.3%, caries_count median 0.0
- FKBP10 (n=8): doku anom 12.5%, caries_any 100.0%, caries_count median 2.5
- Other (n=5): doku anom 0.0%, caries_any 80.0%, caries_count median 1.0

**Yorum (temkinli):** Gruplar arası yüzdeler farklı görünse de küçük n ve seyrek hücreler nedeniyle bunlar “hipotez üretici” düzeydedir.

### 4.3 İnferans (Primary-only Table 3)
Kaynak: `publication_table3_inferential_FINAL.csv`

**Binary sonlanımlar (χ² + permütasyon doğrulama):**
- Doku anomalisi: χ²=7.881, p_classic=0.0960, p_perm=0.0941, **Cramer’s V=0.481**
- Gingivitis: χ²=2.190, p_classic=0.7009, p_perm=0.7666, **V=0.254**
- Caries_any: χ²=8.242, p_classic=0.0831, p_perm=0.0739, **V=0.492**

**Caries_count (Kruskal–Wallis):**
- H=5.311, p=0.2568
- Etki büyüklüğü (iki tanım, süreklilik için birlikte rapor):
  - ε²_primary=0.0452
  - ε²_alt=0.1610

**Holm düzeltmeleri (aile bazlı):**
- Primary family (classic p):
  - doku: 0.2881
  - gingivitis: 0.7009
  - caries_count: 0.5136
- Binary family (perm p):
  - doku: 0.2217
  - gingivitis: 0.7666
  - caries_any: 0.2217

**Net mesaj:** Çoklu test sonrası hiçbir ilişki “istatistiksel anlamlı” seviyeye taşınmıyor.

---

## 5) Güvenilirlik testleri: sonuçlar ne kadar stabil?

### 5.1 LOO (leave-one-out) duyarlılığı
Kaynak: `robustness_panel_FINAL.csv` (scenario=Primary)
- Doku anomalisi p: **0.039–0.150** aralığına oynuyor → tekil olgulara duyarlı.
- Caries_any p: **0.037–0.152** aralığına oynuyor → tekil olgulara duyarlı.
- Gingivitis p: **0.408–0.846** → zaten zayıf sinyal.
- Caries_count p: **0.122–0.399**.

**Yorum:** Küçük n’de sınırda p’ler, tekil olgu etkisine açık. Bu yüzden “sinyal var olabilir” derken temkinli olmak gerekir.

### 5.2 Infraoklüzyon hariç duyarlılık
Kaynak: `robustness_panel_FINAL.csv`
- Caries_any p 0.083 → **0.152**
- doku p 0.096 → 0.112

**Yorum:** Infraoklüzyonlu tek olgu bile bazı sonuçları kaydırabiliyor; bu, örneklem küçüklüğünün doğal etkisidir.

---

## 6) Model tabanlı doğrulama: “gene eklemek” tahmin gücünü artırıyor mu?

Kaynak: `cv_panel_FINAL.csv` (Primary-only) + `verified_master_table_FINAL.csv`

**CV yöntemleri:**
- LOO ve RSKF (Repeated Stratified K-Fold)
- ΔAUC için bootstrap CI + şeffaflık kolonları (n_pos/n_neg, boot_drop_rate, estimator etiketleri)

### 6.1 Doku anomalisi
- LOO: auc_age=0.000, auc_age+gene=0.596 → ΔAUC=0.596 (CI 0.382–0.818), warning: AUC<0.5 (age)
- RSKF: auc_age=0.295, auc_age+gene=0.637 → ΔAUC=0.342 (CI 0.348–0.798)
- Not: estimator farkı nedeniyle “delta_auc_boot_mean vs delta_auc” farkı bayraklı.

**Yorum:** Gene group eklemek doku anomalisi ayrımında “potansiyel katkı” sinyali veriyor; ancak small-n ve estimator farkı nedeniyle bu bulgu hipotez üretici düzeydedir.

### 6.2 Gingivitis
- ΔAUC ~ 0 (LOO ve RSKF), CI’lar 0’ı kapsıyor.

**Yorum:** Gen eklenmesi gingivitis için anlamlı tahmin katkısı göstermiyor.

### 6.3 Caries_any
- LOO: ΔAUC=0.10 (CI yaklaşık -0.04–0.26)
- RSKF: ΔAUC≈0.042 (CI yaklaşık -0.05–0.21)

**Yorum:** Caries_any için gene katkısı belirsiz; yaşın etkisi güçlü olabilir.

---

## 7) Bu analiz bize ne söylüyor? (kongre mesajına çevrim)

1) OI kohortunda oro-dental bulguların prevalansı ölçülebilir düzeyde (caries_any yüksek).
2) Gen grupları arasında bazı uç noktalarda **orta–yüksek etki büyüklüğü** (V≈0.48–0.49) görülse de:
   - permütasyon doğrulama ve Holm düzeltmeleri sonrası “kesin kanıt” düzeyi oluşmuyor.
3) Robustluk analizleri (LOO, infra dışlama) sınırda bulguların **tekil olgu etkisine duyarlı** olduğunu gösteriyor.
4) Model tabanlı doğrulama (AUC) doku anomalisi için gene katkısı sinyali verse de bu sinyalin güvenilirliği örneklem büyüklüğüyle sınırlı.

**Kongre için en doğru ton:**
- “Sinyal var, ancak küçük örneklem nedeniyle doğrulama gerektiriyor.”

---

## 8) Görsellerle destek: hangi figür neyi anlatmalı?

Bu notun görsel karşılığı için önerilen figür seti:

1) **Figür 1 — Cohort snapshot:** prevalanslar (Wilson CI) + caries_count (median/IQR) tek panel.
2) **Figür 2 — Gene-group dağılımı:** N per gene_group (Primary).
3) **Figür 3 — Outcome × gene_group:** ısı haritası / bubble plot (yüzde + n) (hypothesis-generating).
4) **Figür 4 — Inferential summary:** effect size + p_perm + Holm (Primary-only).
5) **Figür 5 — Robustness:** LOO p aralıkları + infra dışlama Δp.
6) **Figür 6 — Model verification:** AUC age vs age+gene + ΔAUC CI (LOO ve RSKF).

Figürleri deterministik/fail-fast üreten script planı ayrı dokümanda verilecektir.


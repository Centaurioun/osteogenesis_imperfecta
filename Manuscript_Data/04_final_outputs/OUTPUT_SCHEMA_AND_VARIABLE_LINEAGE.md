# OUTPUT_SCHEMA_AND_VARIABLE_LINEAGE

Bu dosya, FINAL.1.2 çıktı paketindeki ana tabloların kolon anlamlarını ve raw → runtime → manuscript dönüşüm mantığını açıklar.

## 1) Raw data → runtime derived variables

### `gen_mutasyonu` → runtime gene group
- Kaynak mantık: ham genetik bilgi doğrudan hazır bir grouped sütun olarak alınmamıştır.
- Runtime gruplar:
  - `COL1A1`
  - `COL1A2`
  - `FKBP10`
  - `P3H1`
  - `Other`
- Neden: tekrar üretilebilirlik ve grouping leakage riskini azaltmak.
- İlgili dosyalar:
  - `02_source_data/metadata/gene_map_v1.csv`
  - `04_final_outputs/tables_csv_and_logs/supplementary_gene_group_map_FINAL.csv`

### `occl_tip` → `angle_sinifi` + `infraokluzyon_var`
- `occl_tip` sadece `1`, `2`, `3` olduğunda Angle sınıfı olarak kabul edilir.
- `occl_tip == 4` ise bu **infraoklüzyon** demektir.
- Bu durumda:
  - Angle sınıfı hesaplamasında olgu dışlanır (`NaN` / ineligible)
  - `infraokluzyon_var = 1` olur
- Sonuç izleri:
  - `publication_table1_overall_FINAL.csv`
  - `robustness_panel_FINAL.csv`

### `dmft_dmft` → `caries_count` + `caries_any_rt`
- Bu projede `dmft_dmft` sütunu klasik ayrıştırılmış DMFT indeksi olarak kullanılmamıştır.
- Runtime yorum:
  - `caries_count = dmft_dmft`
  - `caries_any_rt = 1 if dmft_dmft > 0 else 0`
- Sonuç izleri:
  - `publication_table1_overall_FINAL.csv`
  - `publication_table2_by_gene_group_FINAL.csv`
  - `publication_table3_inferential_FINAL.csv`

## 2) Ana çıktı tabloları ve kolon açıklamaları

### `publication_table1_overall_FINAL.csv`
- `Variable`: raporlanan ölçütün adı
- `Value`: nihai özet değer
- `95% CI (Wilson)`: prevalans/ikili oranlar için Wilson güven aralığı

### `publication_table2_by_gene_group_FINAL.csv`
- `scenario`: analiz senaryosu (`Primary` authoritative’dir)
- `gene_group`: runtime türetilen gen grubu
- `N`: ilgili gen grubundaki olgu sayısı
- `age_med_iqr`: yaşın median (IQR) özeti
- `doku_anomalisi_var_rt`: grup içi binary özet
- `gingivitis`: grup içi binary özet
- `caries_any_rt`: grup içi binary özet
- `caries_count_med_iqr`: grup içi caries_count median (IQR)

### `publication_table3_inferential_FINAL.csv`
- `scenario`: manuscript için authoritative satırlar `Primary`
- `endpoint`: test edilen sonlanım
- `test`: kullanılan test özeti (`Chi2_Perm`, `Kruskal`)
- `statistic`: test istatistiği
- `p_classic`: klasik p-değeri
- `p_permutation`: permütasyon p-değeri
- `expected_min`: ki-kare beklenen hücrelerinin minimumu
- `effect_size_name`: etki büyüklüğü adı
- `effect_size_value`: etki büyüklüğü değeri
- `epsilon2_primary`, `epsilon2_alt`: Kruskal–Wallis için epsilon-squared varyantları
- `kw_n`, `kw_k`: Kruskal–Wallis örneklem/grup bilgisi
- `p_holm_primary_family_classic`: primer klasik aile için Holm düzeltilmiş p
- `p_holm_binary_family_perm`: binary permütasyon ailesi için Holm düzeltilmiş p

## 3) Robustness tablosu

### `robustness_panel_FINAL.csv`
- `p_base`: baz analiz p-değeri
- `loo_p_min`: leave-one-out altında görülen minimum p
- `loo_p_max`: leave-one-out altında görülen maksimum p
- `loo_delta_p_max_abs`: leave-one-out ile gözlenen en büyük mutlak p sapması
- `loo_most_influential_id`: p değişimini en çok etkileyen olgu kimliği
- `infra_exclusion_p`: infraoklüzyonlu olgu dışlandığında p değeri
- `infra_exclusion_delta_p`: infra dışlama sonrası p farkı

## 4) CV tablosu

### `cv_panel_FINAL.csv`
- `cv_method`: `LOO` veya `RSKF`
- `n_pos`, `n_neg`: endpoint için class balance
- `auc_age`: yalnız yaş modeli AUC’si
- `auc_age_gene`: yaş + gene-group modeli AUC’si
- `delta_auc`: `auc_age_gene - auc_age`
- `delta_auc_ci_low`, `delta_auc_ci_high`: paired bootstrap ΔAUC güven aralığı
- `delta_auc_estimator`:
  - `loo_auc`
  - `mean_auc_over_repeats`
- `ci_estimator`:
  - `paired_bootstrap_on_oof_probs`
  - `paired_bootstrap_on_mean_oof_probs`
- `n_boot_total`: planlanan bootstrap iterasyonu
- `n_boot_valid`: geçerli bootstrap sayısı
- `n_boot_dropped`: class degeneracy vb. nedenlerle atılan bootstrap sayısı
- `boot_drop_rate`: `n_boot_dropped / n_boot_total`
- `delta_auc_boot_mean`: bootstrap ΔAUC ortalaması
- `delta_auc_boot_median`: bootstrap ΔAUC medyanı
- `note`: estimator uyumsuzluğu gibi dikkat gerektiren yorum notu
- `warnings`: model veya veri davranışına ilişkin uyarılar (`AUC < 0.5` vb.)

## 5) Supplementary tablolar

### `supplementary_sensitivity_FINAL.csv`
- `is_duplicate_scenario`: senaryo satırı, `Primary` ile matematiksel olarak duplicate mi?
- `perm_inherited_from`: permütasyon çıktısı hangi authoritative senaryodan miras alındı?

### `supplementary_gene_group_map_FINAL.csv`
- `Scenario`: senaryo etiketi
- `Symbol`: ham gen sembolü
- `Mapped_Group`: runtime türetilen gen grubu
- `Is_Duplicate_Scenario`: duplicate mapping’in authoritative kaynağı

## 6) Integrated master table

### `verified_master_table_FINAL.csv`
Bu tablo aşağıdaki veri ailelerini endpoint bazında tek satırda birleştirir:
- inferans
- robustness
- CV
- estimator transparency

Özellikle manuscript assembly için hızlı referans tablosudur.

## 7) Neden bazı kolonlar boş?

Bazı kolonlar endpoint tipine göre doğal olarak boş olabilir:
- `p_permutation` sürekli değişkenler için boş olabilir
- `epsilon2_*` yalnız Kruskal–Wallis için doludur
- `primary_cv_method` ve CV kolonları binary endpoint’lerde daha anlamlıdır
- `note` yalnız gerekli olduğunda doludur

Bu boşluklar hata değil, **endpoint-specific schema sparsity** olarak yorumlanmalıdır.
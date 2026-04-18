# TRANSPARENCY_NOTES

Bu not dosyası, FINAL.1.2 paketindeki bazı görünür uyumsuzlukların neden hata değil, bilinçli şeffaflık unsurları olduğunu açıklar.

## 1) `cv_panel_FINAL.csv` içinde warning varken neden `issue_log_FINAL.csv` boş görünüyor?

- `warnings` sütunu model yorumuna dair **analitik uyarıları** taşır.
- `issue_log_FINAL.csv` ise fail-fast veya yapısal problem kaydı için kullanılır.
- Dolayısıyla:
  - `AUC < 0.5`
  - estimator farkı notları
  - küçük class balance uyarıları
  yapısal hata değil, yorum dikkat bayraklarıdır.

## 2) `note` ile `warnings` arasındaki fark nedir?

- `note`: bağlamsal açıklama notudur.
- `warnings`: daha kısa, panel içinde görünür tutulmuş dikkat bayraklarıdır.

Örnek:
- `delta_auc_boot_mean materially differs from delta_auc` → nokta tahmini ile bootstrap özetinin kayda değer ayrıştığını açıklar.

## 3) `k=3` ve `k=4` neden supplementary’de var?

Bu senaryolar reviewer şeffaflığı için tutulmuştur. `Primary` authoritative ana senaryodur. `k=3` ve `k=4` satırları bazı bağlamlarda duplicate olabilir; bu durum explicit olarak:
- `supplementary_sensitivity_FINAL.csv`
- `supplementary_gene_group_map_FINAL.csv`
üzerinde işaretlenmiştir.

## 4) `Fig D` neden yok?

Mevcut exported authoritative figür seti:
- Fig A
- Fig B
- Fig C
- Fig E
- Fig F

Bu nedenle `Fig D` eksik bir dosya gibi yorumlanmamalıdır. Bu, önceki planlama veya sürümleme aşamalarından kalan isimlendirme taşımasıdır.

## 5) `consistency_diff_FINAL_1_1_vs_FINAL_1_2.csv` neden önemli?

Bu dosya, FINAL.1.2 sürümünde yapılan dokümantasyon/transparency eklerinin temel hesaplamayı bozmadığını göstermek için tutulur. Yeni kolonlar eklenmiş olsa da çekirdek sayısal gövde korunmuştur.
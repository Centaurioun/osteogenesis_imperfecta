# Round 2 Audit

## 1. What is already strong

- Legacy ve project-valid katman ayrımı kavramsal olarak doğru kurulmuş.
- Author-clarification kuralları açıkça belgelenmiş (`00_audit/author_clarification_rules.md`).
- A12/A13/A14 için project-valid inferans, etki büyüklüğü ve robustness bağlamı kısmen izlenebilir.
- Discrepancy ve manuscript authority katmanları şematik olarak mevcut.
- Paket klasörleme ve temel traceability disiplini (dosya bazlı) kurulmuş.

## 2. What is incomplete

- A03–A11 için gerçek **rule-constrained numerical rerun** yok; çoğu satır editoryal gerekçe ile "primary family dışı" denmiş.
- A03–A11 için usable_n, test_used, p-value, effect_size, why_not_primary alanlarını dolduran hesap çıktısı eksik.
- Round2 için çalıştırılabilir script izi henüz yok (`08_round2_scripts` boş).

## 3. What is internally inconsistent

- `rule_constrained_supporting_tables.csv` içindeki `A12cv` notunda nokta tahmini ile CI uyumsuzluğu var:
  - delta_auc=0.3420
  - CI (0.3478, 0.7984)
  Nokta tahmini alt sınırın dışında.
- Bazı sonuçlar "numerically supported" görünürken kaynağa dayalı açık satır-level trace eşlemesi eksik.

## 4. What needs real rerun rather than editorial relabeling

- A03–A11 endpointleri (open bite, cross bite, over bite, transposition, missing tooth, impacted tooth, supernumerary tooth, taurodontism, root anomaly) için gerçek project-rule-constrained testler.
- Bu testlerin small-sample uyumlu p-değeri ve effect size çıktıları.
- Rerun olmadan yapılan supplementary-only etiketleri yalnız editoryal kalıyor; numerik dayanak gerekli.

## 5. What manuscript decisions appear too optimistic

- A13 için `supported comparative statement` etiketi correction-sensitive yapı nedeniyle görece güçlü kalabilir.
- A14 için "supported comparative statement" yerine daha temkinli "descriptive null / fragility-aware comparative note" gerekebilir.
- A15/A16 için ana metin uygunluğu korunabilir; ancak inferans iddiası değil descriptive authority olarak çerçevelenmeli.
- A12 için "exploratory signal" makul; ancak CV estimator notu ve correction sonrası durumla birlikte daha ihtiyatlı dille sunulmalı.

## 6. What technical traceability is still missing

- Satır bazında "hangi sayı hangi dosya/satırdan" geldiğini gösteren zorunlu numerical traceability tablosu yok.
- Round2 script → output eşlemesi yok (reproducibility code path eksik).
- CV revalidation için kaynak satır eşleme + düzeltme gerekçesi tek yerde toplanmamış.

## Round2 action gate

Aşağıdaki adımlar zorunlu ve sırayla uygulanacaktır:
1. A03–A11 rule-constrained rerun (gerçek sayısal)
2. CV row revalidation (A12cv odaklı, A13cv/A14cv kontrol)
3. Çalıştırılabilir round2 script seti oluşturma ve yürütme
4. Discrepancy round2 güncellemesi
5. Manuscript eligibility round2 yeniden değerlendirme
6. Numerical traceability tablosu
7. Final round2 completion report

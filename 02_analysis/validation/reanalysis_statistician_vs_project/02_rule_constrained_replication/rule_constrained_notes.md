# Rule-Constrained Replication Notes

## Objective

İstatistikçi analizlerinde sorulan ana sorular, FINAL.1.2 proje kuralları ve author-clarified kayıt mantığı korunarak yeniden değerlendirildi.

## Non-negotiable rule applications

- `occl_tip == 4` ayrı **infraokluzyon** olarak ele alındı; Angle sınıfına dahil edilmedi.
- `doku anomalisi` alanı baskın tek kod mantığı ile yorumlandı; manuscript-facing endpointte binary türev (`doku_anomalisi_var_rt`) kullanıldı.
- `dmft_dmft` classical parsed indeks olarak değil count-like caries burden alanı olarak kullanıldı; `caries_any_rt` türetildi.
- Binary klinik alanlar (open bite, cross bite, overbite, gingivitis vb.) yalnız var/yok düzeyinde ele alındı.
- Runtime gene grouping proje standardına uygun kabul edildi.

## Primary inferential family carried by FINAL.1.2

Rule-constrained ana inferans ailesinde aşağıdaki endpointler yer aldı:
- `doku_anomalisi_var_rt`
- `gingivitis`
- `caries_any_rt`
- `caries_count`

Bu dört endpoint için effect size, multiplicity handling (Holm), robustness paneli ve secondary CV paneli mevcut.

## Results summary

- `doku_anomalisi_var_rt`: orta düzey etki büyüklüğü (Cramer's V~0.48), ancak düzeltme sonrası kesin anlamlılık yok.
- `caries_any_rt`: orta düzey etki büyüklüğü (Cramer's V~0.49), ancak düzeltme sonrası kesin anlamlılık yok.
- `caries_count`: düşük-orta epsilon-squared (~0.045), anlamlı değil.
- `gingivitis`: grup farkı sinyali zayıf.

## Why some legacy endpoints are not in primary inferential family

İstatistikçi tablosundaki bazı ortodontik/dental binary endpointler (open bite, cross bite, transpozisyon vb.) project-valid dünyada otomatik olarak primary inferential family'e alınmamıştır. Bu durum:
- endpoint önceliklendirme,
- small-sample/sparse-cell stabilite,
- multiplicity burden,
- manuscript signal integrity
nedenleriyle ilişkilidir.

## Interpretation rule

Rule-constrained katman manuscript'e en yakın katmandır; legacy anlamlılık ifadeleri yalnız bu katmanla uyumluysa ana metne taşınmalıdır.

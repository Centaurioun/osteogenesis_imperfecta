# Reanalysis Startup Audit

## 1. What can be replicated exactly

- `istatistikci-analiz-bulgulari.md` içindeki Tablo 1 frekans/yüzde ve yaş-dmft özetleri, aynı veri seti (`N=34`) üzerinden **descriptive** düzeyde yeniden üretilebilir.
- Tablo 2'de raporlanan Fisher-exact/Kruskal-Wallis p-değerleri için legacy hat üzerinde aynı coding varsayımları korunursa sonuçlar **yakın veya exact** üretilebilir.
- İstatistikçi metnindeki tek anlamlı bulgu (OCCL p=0.017) legacy coding ile tarihsel olarak yeniden sınanabilir.

## 2. What can only be approximately replicated

- SPSS 11.5 çıktılarındaki exact prosedür ayrıntıları (iki yönlü exact/Monte Carlo ayarları, bağ kırma/yuvarlama) bilinmediğinden bazı p-değerler yaklaşık replikasyon kalitesinde olabilir.
- İstatistikçi dosyasında yer almayan veri temizleme adımları nedeniyle bazı satırların bire bir üretimi kısmi kalabilir.
- Legacy test ailesi aynı kalsa bile runtime gene grouping farkı nedeniyle bazı sonuçlar directionally concordant ama numerically farklı olabilir.

## 3. What must be redefined under project rules

- **OCCL**: `occl_tip==4` infraocclusion olarak ayrı tutulmalı; Angle sınıfı analizinden dışlanmalı.
- **Doku anomalisi**: çoklu fenotip değil baskın tek kod yaklaşımı korunmalı; manuscript endpoint için binary türev (`doku_anomalisi_var_rt`) tercih edilmeli.
- **DMFT/dmft**: `dmft_dmft` classical parsed indeks gibi değil count-like alan olarak ele alınmalı; gerektiğinde `caries_any_rt` türetilmeli.
- **Binary klinik değişkenler**: overjet/overbite/open bite/crossbite/gingivitis yalnız var-yok düzeyinde tutulmalı.
- **İnferans çerçevesi**: small-sample, effect size, correction, robustness ve secondary CV katmanı korunmalı.

## 4. High-risk discrepancy areas

1. OCCL coding (legacy: 1-4 tek aile; project: 1-3 + infra ayrı)
2. Doku anomalisi endpoint tanımı (multiclass legacy vs dominant-code/binary project)
3. dmft yorum farkı (classical index vs count-like caries burden)
4. Test seçimi (legacy Fisher/KW vs project permutation + Holm + effect size)
5. Raporlama düzeyi (legacy p<0.05 odaklı; project transparency + robustness odaklı)

## 5. Immediate manuscript risk items

- Legacy hat üzerinde anlamlı görülen OCCL sonucu, rule-constrained tanımla bire bir taşınamaz; manuscriptte doğrudan kullanılmamalı.
- Doku anomalisi ve dmft için tanım-duyarlılığı yüksek olduğundan legacy p-değerleri tek başına manuscript authority olamaz.
- Çoklu test düzeltmesi ve robustness katmanı yok sayılarak kurulacak sonuç dili reviewer riskini artırır.
- CV sonuçları internal verification olarak tutulmalı; primer klinik kanıt gibi sunulmamalı.

## Decision Gate

Bu startup audit sonrasında süreç aşağıdaki sırayla yürütülecektir:
1. Legacy replication
2. Rule-constrained replication
3. Discrepancy attribution
4. Manuscript authority decisions

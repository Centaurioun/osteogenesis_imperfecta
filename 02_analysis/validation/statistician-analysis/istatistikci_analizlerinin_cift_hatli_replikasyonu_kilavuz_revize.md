# İstatistikçi Analizlerinin Çift Hatlı Replikasyonu — Kılavuz (Revize)

## Amaç

Bu kılavuzun amacı, istatistikçiden gelen analizleri doğrudan reddetmeden, aynı zamanda proje kurallarını ve author tarafından açıklanan kayıt mantığını bozmadan nasıl yeniden ele alacağımızı netleştirmektir. Hedef yalnızca ikinci bir analiz yapmak değildir. Asıl hedef:

1. istatistikçinin yaptığı analizleri tarihsel biçimde yeniden üretmek,
2. aynı analitik soruları proje kurallarıyla yeniden sormak,
3. iki hattın neden aynı veya neden farklı sonuç verdiğini sistematik biçimde açıklamak,
4. manuscript için hangi katmanın otorite olduğunu açıkça belirlemektir.

Bu yaklaşımın temel avantajı şudur: “istatistikçi başka, Copilot başka sonuç verdi” gibi dağınık bir tartışma yerine, farkların kaynağını izlenebilir bir analitik çerçeveye oturtur.

---

## Bu revizyon neden gerekli oldu?

Author ile yapılan görüşmeden sonra bazı veri alanlarının klinik kayıt mantığı netleşmiştir. Bu açıklamalar, istatistikçinin analizlerini doğrudan manuscript düzeyine taşımayı problemli hale getiren temel noktaları açıklığa kavuşturur.

En kritik author açıklamaları şunlardır:

- `doku anomalisi` alanında `0 = doku anomalisi yok`.
- Doku anomalisi alanı **çoklu kayıt** değil, **tek baskın kayıt** mantığıyla doldurulmuştur.
- Dentinogenesis imperfecta için **tip** veya **şiddet** kaydı alınmamıştır.
- `occl_tip` içinde `1–3` klasik Angle sınıflarını, `4` ise **infraocclusion** durumunu temsil etmektedir.
- `4`, Angle sınıflarından birine yakın bir alt kategori değil, **ayrı bir klinik durumu** göstermektedir.
- `dmft_dmft` alanı standart ayrıştırılmış `DMFT` ve `dmft` indeksleri gibi değil, yaş ve dentisyon dönemine göre ağızdaki mevcut çürük yükünü tek hanede özetleyen **count-like** bir kayıt alanı gibi kullanılmıştır.
- `overjet`, `overbite`, `open bite`, `crossbite` ve `gingivitis` değişkenleri **yalnız var/yok** mantığıyla kaydedilmiştir; eşik, mm değeri veya şiddet kaydı yoktur.

Bu nedenle istatistikçi raporu ile manuscript için kurulan current analysis framework aynı veri tanımlarına dayanmıyor olabilir. Tam da bu yüzden iki hatlı replikasyon gerekir.

---

## Kaynak hiyerarşisi

Bu çalışma yeniden yürütülürken şu kaynak hiyerarşisi korunmalıdır:

1. **FINAL.1.2 proje dosyaları ve current manuscript-facing kurallar**
2. **Author tarafından açıklanan kayıt ve kodlama mantığı**
3. **İstatistikçi raporu** yalnızca legacy replication kaynağı olarak
4. **Etik kurul / protokol metinleri** yalnızca tarihsel ve bağlamsal referans olarak

Önemli kural: Etik kurul veya erken plan belgelerinde yazan bir beklenti, final veri yapısı ve author açıklamaları ile desteklenmiyorsa, gerçekleşmiş analiz gibi ele alınmamalıdır.

---

## Temel mantık

Bu iş üç değil, dört ayrı katmanda düşünülmelidir.

### 1. Legacy replication

Bu katmanda amaç, istatistikçinin yaptığı analizleri mümkün olduğunca aynı mantıkla yeniden üretmektir.

Burada mümkün olduğunca korunacak unsurlar:
- istatistikçinin kullandığı değişkenler,
- istatistikçinin kullandığı gruplama mantığı,
- istatistikçinin kullandığı coding yaklaşımı,
- istatistikçinin kullandığı test türü,
- istatistikçinin raporladığı tablolar ve p-değerleri.

Bu katmanın amacı şudur:
> İstatistikçinin raporu teknik olarak gerçekten yeniden üretilebiliyor mu?

Bu katman manuscript için nihai otorite değildir. Bu katman tarihsel ve yöntemsel karşılaştırma katmanıdır.

### 2. Rule-constrained replication

Bu katmanda amaç, istatistikçinin sorduğu aynı analitik soruları, bu kez proje kurallarını ve author tarafından açıklanan klinik kayıt mantığını bozmadan yeniden sormaktır.

Burada mutlaka korunacak kurallar:
- `occl_tip == 4` değeri **infraocclusion** olarak ele alınmalıdır; Angle class ile aynı kategorik aileye katılamaz.
- `dmft_dmft` klasik ayrıştırılmış DMFT/dmft indeksi gibi değil, proje mantığına uygun **count-like** yapı olarak ele alınmalıdır.
- `doku anomalisi` alanı çoklu fenotip tablosu gibi değil, **tek baskın kod** mantığıyla yorumlanmalıdır.
- Dentinogenesis imperfecta için **tip / şiddet** analizleri yapılmamalıdır; böyle veri yoksa bu sınırlılık olarak not edilmelidir.
- `overjet`, `overbite`, `open bite`, `crossbite` ve `gingivitis` değişkenleri yalnız **binary presence / absence** olarak ele alınmalıdır.
- Gene grouping, proje mantığına uygun şekilde runtime türetilmiş haliyle ele alınmalıdır.
- Small-sample mantığı korunmalıdır.
- Uygun yerlerde effect size raporlanmalıdır.
- Çoklu test varsa düzeltme görmezden gelinmemelidir.
- Robustness / sensitivity değerlendirmeleri destek katmanı olarak korunmalıdır.
- CV / AUC / delta-AUC tipi analizler varsa bunlar secondary internal verification düzeyinde tutulmalıdır.

Bu katmanın amacı şudur:
> Aynı soru, doğru proje tanımlarıyla sorulduğunda sonuç ne oluyor?

Bu katman manuscript’e en yakın replikasyon katmanıdır.

### 3. Discrepancy attribution layer

Bu katman olmadan karşılaştırma yüzeysel kalır. Amaç yalnızca “fark var” demek değil, farkın nedenini sınıflandırmaktır.

Her fark mümkün olduğunca aşağıdaki sınıflardan birine atanmalıdır:
- `variable-definition discrepancy`
- `coding discrepancy`
- `test-selection discrepancy`
- `multiplicity-control discrepancy`
- `robustness-related discrepancy`
- `modeling/reporting discrepancy`
- `no material discrepancy`

Bu katmanın amacı şudur:
> Sonuç neden değişti?

### 4. Manuscript authority layer

Son katmanda hangi sonucun manuscript’te kullanılacağı belirlenir.

Her analiz veya sonuç şu etiketlerden birini almalıdır:
- `manuscript-eligible`
- `supplementary-only`
- `legacy-reference-only`
- `not usable`

Bu katmanın amacı şudur:
> Nihai makale için hangi sonuç kullanılabilir?

---

## Bu yaklaşım neden güçlü?

Bu yapı sayesinde:
- istatistikçinin emeği çöpe atılmaz,
- author açıklamaları ve proje kuralları korunur,
- her farkın kaynağı görünür hale gelir,
- hangi sonucun yalnızca historical benchmark olduğu, hangisinin manuscript authority olduğu netleşir,
- reviewer karşısında daha güçlü bir savunma hattı kurulur.

Bu yaklaşım özellikle şu sorunlar için değerlidir:
- OCCL gibi coding-duyarlı değişkenler,
- doku anomalisi gibi çok kategorili görünse de baskın tek kodlu alanlar,
- classical DMFT yorumuna kayan count-like değişkenler,
- small-sample test seçimi farkları,
- correction / robustness sonrası anlamlılığın değişmesi,
- binary var/yok kayıtların şiddet varmış gibi aşırı yorumlanması.

---

## Hangi analizler mutlaka iki hat üzerinde tekrar edilmeli?

### Bire bir legacy replication yapılması gerekenler
- istatistikçinin raporladığı tüm tanımlayıcı tablolar,
- tüm grup karşılaştırmaları,
- tüm p-değerleri,
- anlamlı görünen tüm sonuçlar,
- borderline sonuçlar,
- OCCL ve benzeri problemli ama tarihsel olarak önemli alanlar,
- Dmft başlığı altında raporlanan sonuçlar,
- çok kategorili doku anomalisi raporlamaları.

### Rule-constrained replication yapılması gerekenler
- OCCL analizi,
- doku anomalisi analizi,
- dmft / caries analizi,
- gene-group karşılaştırmaları,
- istatistikçinin anlamlı bulduğu tüm endpoint’ler,
- manuscript yorumunu etkileme potansiyeli olan tüm sonuçlar,
- binary var/yok kaydedilmiş periodontal veya ortodontik alanlar.

### Yalnız yöntem farkı olarak not edilmesi gerekenler
Aşağıdakiler ayrı bir test değil, analitik yaklaşım farkıdır:
- yalnız p<0,05 merkezli yorum,
- effect size eksikliği,
- multiple testing correction yokluğu,
- robustness yapılmamış olması,
- model verification katmanının hiç bulunmaması,
- binary değişkenleri detaylı şiddet ölçümü varmış gibi okuma riski.

---

## Zorunlu ön adım: Eşleme tablosu

Replikasyona geçmeden önce şu tablo üretilmelidir:

| Statistician variable / endpoint | Project equivalent | Same construct? | Same coding? | Re-analysis required? |
|---|---|---|---|---|

Bu tablo olmadan doğrudan replikasyona geçmek hataya açıktır.

Ayrıca her analiz için şu alanları içeren ikinci bir eşleme matrisi tutulmalıdır:
- original analysis label
- original variable(s)
- original coding assumption
- original test
- replicated exactly? yes/no
- rule-constrained version available? yes/no
- discrepancy source
- manuscript eligibility
- author clarification dependency

---

## Zorunlu sonuç sınıflaması

Her karşılaştırmalı sonuç sonunda aşağıdaki sınıflardan birine girmelidir:
- `fully concordant`
- `directionally concordant but method-sensitive`
- `definition-sensitive`
- `substantively discordant`

Bu sınıflama yapılmazsa benzerlik / farklılık analizi dağınık kalır.

---

## Önerilen iş akışı

### Aşama 1
İstatistikçinin raporundaki tüm analizleri satır satır envantere dök.

### Aşama 2
Her analiz için proje eşdeğerini ve author açıklamasına bağlı yorum riskini belirle.

### Aşama 3
Legacy replication yap.

### Aşama 4
Rule-constrained replication yap.

### Aşama 5
İki hattı yan yana koy ve farkın nedenini sınıflandır.

### Aşama 6
Her analizin manuscript uygunluğunu kararlandır.

### Aşama 7
Editoryal uzlaştırma raporu üret:
- hangileri ana metne girebilir,
- hangileri supplemente gider,
- hangileri yalnız legacy referans olarak kalır,
- hangileri hiç kullanılmamalıdır.

---

## Klasörleme ilkesi

Bu çalışma için üretilecek tüm yeni dosyalar tek bir özel klasörde toplanmalıdır. Bu klasör:
- eski analizlerle karışmamalı,
- kendi içinde alt klasörler içermeli,
- yeniden çalıştırıldığında aynı yapı korunmalı,
- tüm markdown, csv, png, python, json ve diğer çıktıları aynı şemada toplamalıdır.

Önerilen yapı:

`reanalysis_statistician_vs_project/`
- `00_audit/`
- `01_legacy_replication/`
- `02_rule_constrained_replication/`
- `03_discrepancy_analysis/`
- `04_manuscript_decisions/`
- `05_logs/`
- `06_figures/`
- `07_temp/`

Bu klasörleme yalnız düzen için değil, traceability için de gereklidir.

---

## Açık risk alanları

Aşağıdaki alanlar özel dikkat gerektirir:

1. **OCCL / infraocclusion**  
   Legacy analizde `4` aynı aile içinde olabilir; project-valid analizde ayrı ele alınmalıdır.

2. **Dmft / DMFT-dmft yorum farkı**  
   Legacy analizde klasik indeks gibi görünse bile project-valid analizde count-like mantık korunmalıdır.

3. **Doku anomalisi**  
   Çoklu fenotip haritası gibi okunmamalı; baskın tek kod mantığı korunmalıdır.

4. **DI tip / şiddet**  
   Veri yoksa bu alanlarda detaylı analiz yapılmamalıdır.

5. **Binary klinik değişkenler**  
   Overjet, overbite, open bite, crossbite ve gingivitis için eşik / şiddet bilgisi yoksa bunlar yalnız var/yok düzeyinde yorumlanmalıdır.

---

## Son ilke

Bu işin amacı istatistikçiyi çürütmek değildir. Amaç, istatistikçinin sonuçlarını:
1. yeniden üretmek,
2. proje kuralları ve author açıklamalarıyla sınamak,
3. farkların nedenini açıklamak,
4. manuscript için doğru otorite katmanını seçmektir.

Nihai kural şudur:
- `legacy replication` = tarihsel karşılaştırma
- `rule-constrained replication` = metodolojik olarak düzeltilmiş tekrar
- `manuscript authority layer` = nihai yazım otoritesi

Bu ayrım korunursa sonuçlar hem analitik hem editoryal olarak savunulabilir hale gelir.


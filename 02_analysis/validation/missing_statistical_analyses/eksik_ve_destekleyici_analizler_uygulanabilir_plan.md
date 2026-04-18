# Eksik ve Destekleyici Analizler — Uygulanabilir Plan

## (A) Hızlı Özet

### 1. Kısa durum özeti

Bu tür bir çalışmada istatistiksel yapı üç katmanda ele alınmalıdır:

1. **Ana analizler (primary analyses)**

   - Çalışmanın ana araştırma sorusunu doğrudan yanıtlayan analizlerdir.
   - Bu çalışmada tipik olarak şunları kapsar:
     - kohortun tanımlayıcı özeti,
     - ana oral sonlanımların prevalansı,
     - gen gruplarına göre birincil karşılaştırmalar,
     - etki büyüklüğü ve uygun belirsizlik ölçüleri,
     - çoklu karşılaştırma düzeltmesi.

2. **Destekleyici analizler (supporting analyses)**

   - Ana sonucun bağlamını güçlendirir, ancak ana sonucun yerine geçmez.
   - Örnekler:
     - alternatif değişken kodlamaları,
     - ek tanımlayıcı tablolar,
     - yaş veya dentisyon gibi sınırlı ikincil karşılaştırmalar,
     - endpoint-bazlı eksik veri ve denominator raporlaması,
     - ek duyarlılık tabloları ve görseller.

3. **Duyarlılık ve sağlamlık analizleri (sensitivity / robustness analyses)**

   - Sonuçların tekil gözlemlere, kodlama kararlarına veya alternatif analitik tanımlara ne kadar duyarlı olduğunu sınar.
   - Örnekler:
     - leave-one-out,
     - kritik kodlama kararlarının yeniden tanımlanması,
     - alternatif gruplama,
     - exact veya permutation duyarlılık kontrolü,
     - model doğrulama çıktılarının istikrarının incelenmesi.

### 2. Destekleyici analizler neden kritik olabilir?

Destekleyici analizler, küçük örneklemli, seyrek hücreli ve nadir hastalık bağlamındaki çalışmalarda çoğu zaman ek değil, **yorum güvenliği için gerekli** hale gelir. Bunun temel nedenleri şunlardır:

- Ana p-değerleri tek başına yanıltıcı olabilir.
- Küçük örneklemde tek bir olgu sonuçları anlamlı biçimde değiştirebilir.
- Aynı sinyal farklı tanımlar altında korunmuyorsa ana sonuç kırılgan olabilir.
- Klinik olarak dikkat çekici farklar, veri yapısı nedeniyle istatistiksel olarak aşırı yorumlanabilir.
- Destekleyici analizler, “gözlenen fark veri yapısına rağmen sürüyor mu?” sorusuna yanıt verir.

### 3. Eksik analiz bırakmanın sonuç geçerliliğine etkisi

Eksik supporting veya robustness analizi bırakmak şu sonuçlara yol açabilir:

- Bulguların **dayanıklılığı gösterilemez**.
- Reviewer, sonucun yalnızca tek bir spesifikasyonun veya tek bir test seçiminin ürünü olduğunu düşünebilir.
- Küçük örneklem nedeniyle ortaya çıkan istikrarsızlık fark edilmeden kalabilir.
- Non-significant ama dikkat çekici etki büyüklükleri gereğinden fazla veya gereğinden az yorumlanabilir.
- Modelleme varsa, ayırt edici ya da prediktif çıktılar gereğinden güçlü görünebilir.
- Methods, Results ve Discussion arasındaki analitik bütünlük zayıflar.

### 4. Bu çalışma için başlangıç sınıflaması

#### Ana analiz olarak sınıflanacaklar

- veri temizliği ve analiz uygunluk kontrolü,
- kohort tanımlayıcı istatistikleri,
- ana oral sonlanımların prevalansı,
- gen gruplarına göre birincil karşılaştırmalar,
- etki büyüklükleri,
- çoklu karşılaştırma düzeltmesi,
- ana count-benzeri sonlanım için uygun grup karşılaştırması.

#### Supporting / sensitivity / robustness olarak sınıflanacaklar

- endpoint-bazlı denominator ve eksik veri özeti,
- aykırı veya tekil gözlem etkisi,
- alternatif gruplama / alternatif kodlama,
- infraocclusion dışlama veya benzer kritik karar kontrolleri,
- exact / permutation duyarlılık kontrolleri,
- model doğrulama ve delta-AUC temelli ikincil doğrulama,
- yaş veya dentisyon temelli sınırlı ikincil kontroller.

### 5. Çalışmaya başlamadan önce sorulması gereken kritik sorular

#### Çalışma tasarımı

- Çalışma retrospektif, kesitsel ve gözlemsel olarak mı raporlanacak?
- Dahil edilme mantığı “tüm uygun olgular” şeklinde mi korunacak?
- Çalışma gerçekten tek merkezli mi?

#### Hipotezler

- Ana hipotez nedir?
- İkincil hipotezler açık ve sınırlı mı?
- Hangi analizler keşfedici, hangileri doğrulayıcı olarak etiketlenecek?

#### Değişken türleri ve ölçüm düzeyleri

- Hangi sonlanımlar binary, hangileri ordinal, hangileri count-like?
- Hangi değişkenler yalnız kayıttan türetilmiş?
- Hangi klinik kavramların veri setinde tam karşılığı yok?

#### Örneklem büyüklüğü ve güç

- Grup başına gözlem sayıları nedir?
- Seyrek hücre sorunu hangi tablolar için kritik?
- Güç analizi yapılacak mı, yoksa small-n sınırlılığı olarak mı tartışılacak?

#### Veri toplama yöntemi

- Veriler klinik kayıt, radyografi ve mevcut genetik kayıttan mı geldi?
- Hangi değişkenlerde eksik veya tutarsız kayıt riski yüksek?

#### Potansiyel karıştırıcılar

- Yaş temel karıştırıcı mı?
- Dentisyon dönemi yalnız betimleyici olarak mı kullanılacak?
- Tedavi öyküsü, bifosfonat maruziyeti, OI tipi veya DI şiddeti gibi değişkenler güvenilir mi?

### 6. Bu planın ana amacı

Bu planın amacı, Copilot’un:

- hangi analizleri **önce**, hangilerini **sonra** yapacağını,
- hangi testlerin bu veri yapısı için **uygun**, hangilerinin **uygun ama zorunlu olmayan**, hangilerinin **kaçınılması gereken** seçenekler olduğunu,
- hangi durumda analizi **durdurup yöntem değiştirmesi** gerektiğini,
- hangi çıktıları üretip nasıl raporlaması gerektiğini

net biçimde anlamasını sağlamaktır.

---

## (B) Sıralı Analiz Planı

### 1. Veri hazırlığı ve veri kalite kontrolleri

**Amaç**

- Analize girecek veri yapısını doğrulamak.
- Kodlama hataları, eksik veri, tutarsız kayıt ve uç gözlem risklerini görünür hale getirmek.

**Girdi / önkoşul**

- ham veri dosyası veya final analitik tablo,
- codebook / değişken sözlüğü,
- dahil etme / dışlama mantığı,
- sonlanım tanımları,
- türetilmiş değişken kuralları.

**Uygulanacak yöntem**

- değişken tip kontrolü (numeric, binary, categorical, count-like),
- missingness tablosu,
- range ve mantık kontrolü,
- kodlama eşleştirme kontrolü,
- duplicate / çelişkili kayıt kontrolü,
- kritik türetilmiş değişkenlerin yeniden üretimi,
- uç / deviant gözlem taraması,
- endpoint-bazlı usable denominator üretimi.

**Beklenen çıktı**

- veri kalite raporu,
- endpoint-bazlı usable N tablosu,
- veri temizleme notları,
- analizde kullanılacak nihai değişken seti,
- kritik riskler listesi.

**Karar kuralı**

- Kodlama çelişkisi varsa çözülmeden analize geçme.
- Türetilmiş değişken ham mantıkla uyuşmuyorsa tanımı düzelt ve yeniden üret.
- Eksik veri kritik düzeydeyse önce raporla, sonra complete-case mantığını açıkça tanımla.
- Uç gözlem varsa silme kararı otomatik verilmemeli; önce kayıt hatası mı, gerçek klinik değer mi ayrımı yapılmalı.

**Dur / devam et kuralı**

- Türetilmiş sonlanım yanlış üretilmişse → dur, veri türetme mantığını düzelt.
- Klinik olarak imkânsız değer varsa → dur, kaynak kaydı doğrula.
- Endpoint usable denominator belirsizse → dur, sonuç analizi üretme.

#### Veri kalitesi pratik kontrol listesi

-

### 2. Tanımlayıcı istatistikler ve temel görselleştirmeler

**Amaç**

- Kohortu, grup dağılımını ve ana sonlanımları açık biçimde tanımlamak.
- Analiz öncesi veri yapısını ve dengesizlikleri görünür yapmak.

**Girdi / önkoşul**

- temizlenmiş veri,
- ana ve ikincil sonlanımlar,
- grup değişkeni.

**Uygulanacak yöntem**

- n, yüzde, medyan, IQR ve gerekiyorsa güven aralığı,
- genel kohort tablosu,
- grup-bazlı özet tablo,
- ana sonlanımlar için prevalans grafikleri,
- grup büyüklüğü ve outcome dağılımını gösteren görseller,
- gerekirse eksik veri veya usable denominator ek tablosu.

**Beklenen çıktı**

- genel kohort özeti,
- grup bazlı özet tablo,
- prevalans özeti,
- dengesiz grup yapısı ve seyrek sonuçları görünür kılan tablo / görseller.

**Karar kuralı**

- Tanımlayıcı dağılımlar aşırı dengesizse inferans yöntemi daha korumacı seçilmeli.
- Görsel ve tablo aynı hikâyeyi anlatmıyorsa önce veri yapısı yeniden kontrol edilmeli.

**Dur / devam et kuralı**

- Bir tablo ile diğer tablo arasında aynı değişken için farklı denominator varsa → dur, usable N uyumunu düzelt.

### 3. Birincil hipotez testleri / ana analiz omurgası

**Amaç**

- Çalışmanın asıl araştırma sorusunu doğrudan test etmek.

**Girdi / önkoşul**

- temiz veri,
- net tanımlanmış sonlanımlar,
- grup değişkeni,
- önceden tanımlı primer karşılaştırmalar,
- hipotez aileleri.

**Uygulanacak yöntem**

- binary / kategorik sonlanımlar için small-sample uygun grup karşılaştırması,
- count-like sonlanım için uygun nonparametrik grup testi,
- her test için etki büyüklüğü,
- uygun çoklu test düzeltmesi,
- sonuçların tek bir ana inferans tablosunda birleştirilmesi.

**Beklenen çıktı**

- her ana sonlanım için test istatistiği,
- ham p ve düzeltilmiş p,
- etki büyüklüğü,
- yorumlama etiketi: primary / supporting / exploratory.

**Karar kuralı**

- Sonuç yalnız p-değerine göre yorumlanmamalı.
- Etki büyüklüğü orta veya yüksek ama düzeltme sonrası non-significant ise “signal / hypothesis-generating” dili kullanılmalı.
- Küçük hücre veya aşırı dengesizlik varsa exact ya da permutation yaklaşımı tercih edilmeli.
- Count-like sonuç parametrik sürekli sonuç gibi muamele edilmemeli.

**Dur / devam et kuralı**

- Bir sonlanımın yapısı binary iken sürekliymiş gibi analiz edildiyse → dur, test ailesini değiştir.
- Çoklu test düzeltmesi uygulanmadan sonuç cümlesi kurulmasın.

### 4. Varsayım ve model tanısal kontrolleri

**Amaç**

- Seçilen analiz yaklaşımının veri yapısına uygunluğunu doğrulamak.
- Yanlış yöntem kullanımını erken saptamak.

**Girdi / önkoşul**

- ana analiz sonuçları,
- veri türü bilgisi,
- varsa model tabanlı analizler.

**Uygulanacak yöntem**

- parametrik bir yöntem gerçekten kullanıldıysa normallik ve varyans homojenliği,
- modelleme varsa multicollinearity taraması,
- residual / influence / leverage taraması,
- küçük örneklemde tekil gözlem etkisi değerlendirmesi,
- model çıktıları için temel uyum ve warning özeti.

**Beklenen çıktı**

- hangi varsayımın sağlandığı / sağlanmadığı,
- hangi nedenle parametrik yerine nonparametrik veya exact / permutation tercih edildiği,
- model sonuçlarının stabilite durumu,
- tanısal risk notu.

**Karar kuralı**

- Varsayım ihlali varsa yöntemi savunmak yerine yöntemi değiştir.
- Model çok kararsızsa primer inferans olarak kullanma.
- Tanısal sorun varsa supporting / exploratory etiketi ver.

**Dur / devam et kuralı**

- Residual veya leverage sorunu ciddi ise model tabanlı sonucu ana bulgu gibi raporlama.

### 5. Supporting analizler

**Amaç**

- Ana sonucun tanım, veri alt yapısı veya yöntem seçimine ne kadar bağlı olduğunu görmek.

**Girdi / önkoşul**

- ana analizler tamamlanmış olmalı,
- hangi sonuçların sınırda veya kırılgan göründüğü bilinmeli.

**Uygulanacak yöntem**

- alternatif kodlama / alternatif gruplama,
- exact veya ek permutation duyarlılığı,
- yaş / dentisyon gibi sınırlı ikincil kontroller,
- endpoint-bazlı denominator şeffaflığı,
- ek duyarlılık tabloları ve supporting görseller.

**Beklenen çıktı**

- ana sonucun hangi koşullarda korunduğu,
- hangi koşullarda zayıfladığı,
- hangi yorumların daraltılması gerektiği,
- supporting tablo seti.

**Karar kuralı**

- Sonuç alternative specification altında kayboluyorsa açıkça yaz.
- Supporting analiz ana sonuca ters düşüyorsa “karışık / kırılgan bulgu” etiketi kullan.
- Supporting analiz ana sonuçla uyumluysa bunu “consistency support” olarak not et, ama primer bulguya dönüştürme.

### 6. Robustluk / sensitivity analizleri

**Amaç**

- Tekil olgu, küçük kodlama değişikliği veya veri sınırlamasının sonuçları ne kadar etkilediğini göstermek.

**Girdi / önkoşul**

- ana analiz yapılmış olmalı,
- kritik varsayım veya kodlama kararları tanımlanmış olmalı.

**Uygulanacak yöntem**

- leave-one-out,
- kritik kategori dışlama / yeniden tanımlama,
- alternative inclusion rules,
- gerekiyorsa exact / permutation tekrarları,
- p ve etki büyüklüğü değişim özetleri.

**Beklenen çıktı**

- p-değeri aralıkları,
- etki büyüklüğü değişimi,
- stabil / kısmen stabil / kırılgan sınıflaması,
- robustness özeti.

**Karar kuralı**

- Tek gözlem çıkarılınca anlamlılık veya yorum düzeyi sık değişiyorsa bunu ciddi yorum sınırlılığı olarak işle.
- Robustluk zayıfsa sonuç “confirmed” değil, “hypothesis-generating” diline çekilmeli.

### 7. Sonuçların sentezi, raporlama ve yorum sınırı

**Amaç**

- Ana bulgu, supporting bulgu ve sınırlılığı tek bir mantık çerçevesinde sunmak.

**Girdi / önkoşul**

- ana, supporting ve robustness analizleri tamamlanmış olmalı.

**Uygulanacak yöntem**

- primary vs supporting ayrımı,
- p + etki büyüklüğü + %95 CI birlikte raporlama,
- sonuç gücü / kırılganlık matrisi,
- Results’ta kalacak ifade ile Discussion’a taşınacak yorumun ayrılması.

**Beklenen çıktı**

- yayınlanabilir sonuç özeti,
- hangi bulgunun güçlü, hangisinin kırılgan olduğu,
- hangi bulgunun yalnız keşfedici düzeyde olduğu,
- metin için kısa sonuç cümleleri.

**Karar kuralı**

- Ana metinde yalnız en savunulabilir sonuçlar öne çıkarılsın.
- Kırılgan sonuçlar Results’ta raporlanabilir, ama Discussion’da açıkça sınırlandırılmalı.
- Modelleme çıktıları varsa prediktif kanıt gibi değil, ikincil doğrulama gibi yazılmalı.

---

## (C) Karar Ağacı: Hangi durumda hangi analiz?

### **1. Eksik analizleri bulma kontrol listesi**

#### Veri kalitesi

- Eksik veri oranı her değişken için hesaplandı mı?
- Eksik veri deseni (tam rastgele / kısmen yapısal / sistematik) incelendi mi?
- Aykırı gözlemler işaretlendi mi?
- Tutarsız kayıtlar çözüldü mü?
- Duplicate kayıt kontrolü yapıldı mı?
- Endpoint bazında usable denominator verildi mi?
- Türetilmiş değişkenler yeniden üretildiğinde aynı sonucu veriyor mu?
- Kritik kodlama kararları loglandı mı?

#### Değişken yapısı

- Sürekli / kategorik / binary / count-like ayrımı doğru yapıldı mı?
- Kodlama hatası veya kategori karışması var mı?
- Klinik kavram ile veri değişkeni birebir örtüşüyor mu?
- Aynı klinik olguyu temsil eden iki farklı değişken yanlışlıkla birlikte kullanılıyor mu?
- Derived değişken ile ham değişken birbiriyle çelişiyor mu?

#### Varsayım kontrolleri

- Parametrik yöntem gerçekten kullanılacaksa normallik kontrol edildi mi?
- Varyans homojenliği gerekiyorsa kontrol edildi mi?
- Bağımsızlık varsayımını ihlal edecek tekrar ölçüm / kümelenme durumu var mı?
- Modelleme varsa multicollinearity tarandı mı?
- Küçük hücre / seyrek olay yapısı önceden saptandı mı?

#### Model tanılamaları

- Residual kontrolleri yapıldı mı?
- Etki gözlemleri / leverage / influence incelendi mi?
- Uyum ölçütleri raporlandı mı?
- Model çıktılarının aşırı yorumunu engelleyecek uyarılar yazıldı mı?
- Model sonucu tekil gözlemlere aşırı duyarlı mı?

#### Alt grup ve etkileşim analizleri

- Alt grup analizi gerçekten klinik veya biyolojik olarak gerekçeli mi?
- Örneklem hacmi alt grup analizi için yeterli mi?
- Alt gruplar sonucu anlamsız biçimde parçalayacak kadar küçük mü?
- Etkileşim analizi veri gücünü aşan bir girişim mi?
- Alt grup analizi primer değil supporting / exploratory olarak etiketlendi mi?

#### Duyarlılık ve sağlamlık analizleri

- Leave-one-out yapıldı mı?
- Kritik kodlama kararları test edildi mi?
- Alternative grouping / exclusion mantığı denendi mi?
- Ana bulgu alternative specification altında korunuyor mu?
- Sonuçlar “stabil / kısmen stabil / kırılgan” olarak sınıflandırıldı mı?

#### Çoklu karşılaştırma düzeltmesi

- Birden fazla hipotez test edildiyse düzeltme yapıldı mı?
- Düzeltme ailesi açıkça tanımlandı mı?
- Kullanılan düzeltme yöntemi gerekçelendirildi mi?
- Düzeltilmemiş ve düzeltilmiş sonuçlar ayrı gösterildi mi?

#### Etki büyüklüğü + güven aralığı

- Her ana analiz için etki büyüklüğü raporlandı mı?
- Mümkün olan yerde %95 güven aralığı verildi mi?
- Sadece p-değerine dayanarak sonuç yazılmadı mı?
- Etki büyüklüğü ile istatistiksel anlamlılık ayrı ayrı yorumlandı mı?



### 2. Analiz bazlı karar tablosu

| Analiz adı                      | Hangi durumda uygulanır?                          | Gerekli veri / önkoşullar                          | Kullanılacak test / model                         | Raporlanacak metrikler                        | Yorumlama kriteri                                     | Sonraki adıma etkisi                       |
| ------------------------------- | ------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------- | --------------------------------------------- | ----------------------------------------------------- | ------------------------------------------ |
| Veri kalite taraması            | Her zaman                                         | Ham veya temiz veri, codebook                      | Missingness, range, consistency, duplicate checks | Missing oranı, hata listesi, usable N         | Kritik hata varsa analize geçilmez                    | Veri temizleme gerekir                     |
| Tanımlayıcı özet                | Her zaman                                         | Temiz veri                                         | n, %, medyan, IQR, CI                             | Prevalans, dağılım, grup özeti                | Dengesizlik ve seyrek hücre görünür hale gelir        | Ana test seçimini etkiler                  |
| Kategorik grup karşılaştırması  | Binary / kategorik outcome + grup karşılaştırması | Yeterli kategori tanımı, small-sample farkındalığı | Uygun permutation / exact / small-sample yaklaşım | İstatistik, p, etki büyüklüğü, gerekiyorsa CI | Sonuç signal mi, flat mi?                             | Robustluk ve multiplicity kararını etkiler |
| Count-like grup karşılaştırması | Skewed count-benzeri outcome                      | Çok grup, parametrik varsayım zayıf                | Nonparametrik çok grup testi                      | İstatistik, p, etki büyüklüğü                 | Grup farkı büyüklüğü + yönü                           | Supporting analize ihtiyaç doğurabilir     |
| Çoklu test düzeltmesi           | >1 primer test varsa                              | Hipotez ailesi tanımlı olmalı                      | Uygun correction strategy                         | adjusted p                                    | Yorumu korur                                          | Sonuç dili değişir                         |
| Etki büyüklüğü raporu           | Her ana testte                                    | Test tipi biliniyor olmalı                         | Uygun effect size                                 | ES + mümkünse %95 CI                          | Klinik ve istatistiksel önem birlikte değerlendirilir | Discussion tonunu etkiler                  |
| Robustluk analizi               | Small-n, kritik kodlama, sınırda bulgu            | Ana analiz tamamlanmış olmalı                      | LOO, exclusion, alternative spec                  | değişen p / ES aralığı                        | Stabil mi kırılgan mı?                                | Sonuç dili yumuşatılabilir                 |
| Alt grup analizi                | Önceden gerekçeli alt grup varsa                  | Yeterli n, klinik mantık                           | Stratified summary / sınırlı test                 | subgroup effect, p, ES                        | Aşırı yorumdan kaçınılmalı                            | Çoğu zaman supplemente gider               |
| Model doğrulama                 | Modelleme ikincil amaçsa                          | Binary outcome, küçük n uyarısı                    | Penalized model + CV                              | AUC, delta-AUC, CI, warning                   | Predictive değil, secondary verification              | Discussion restraint gerekir               |

### 3. Kısa karar ağacı

#### Adım 1

**Outcome tipi nedir?**

- Binary / kategorik → small-sample uygun kategorik karşılaştırma
- Count-like / çarpık sayısal → nonparametrik grup testi
- Sürekli ve güçlü parametrik destek varsa → ancak o zaman parametrik seçenek düşün

#### Adım 2

**Gruplar küçük ve dengesiz mi?**

- Evet → permutation / exact-style yaklaşım düşün
- Hayır → daha klasik karşılaştırmalar düşünülebilir

#### Adım 3

**Birden fazla sonlanım test ediliyor mu?**

- Evet → çoklu düzeltme uygula
- Hayır → düzeltme zorunlu olmayabilir ama family yapısını yine de kontrol et

#### Adım 4

**Sonuç sınırda mı veya small-n nedeniyle kırılgan olabilir mi?**

- Evet → robustness / sensitivity analizi yap
- Hayır → yine de ana bulgu için minimum robustness mantığı uygula

#### Adım 5

**Modelleme çıktıların var mı?**

- Evet → yalnız secondary verification olarak sun
- Hayır → zorla model kurma

#### Adım 6

**Supporting analiz ana sonuca ters mi düştü?**

- Evet → sonucu “karışık / kırılgan” olarak etiketle
- Hayır → supporting consistency olarak not et ama primer bulgu dilini değiştirme

---

## (D) Copilot için doğrudan uygulanabilir görev listesi (checklist)

### **1. Çalışmayı başlatmadan önce**

- Çalışma tasarımını, analitik örneklemi ve ana hipotezleri netleştir.
- Tüm sonlanımları veri tipine göre etiketle: binary, categorical, count-like, continuous.
- Türetilmiş değişkenleri ve kritik kodlama kurallarını ayrı listele.
- Ana analiz, supporting analiz ve robustness analizlerini ayrı sütunlarda tanımla.
- Her analiz için `primary / secondary / exploratory / robustness` etiketi ata.
- Her sonlanım için usable denominator mantığını önceden belirle.
- Ana sonuç tabloları ile supplemente gidecek supporting tabloları ayır.

### **2. Veri hazırlığı**

- Her değişken için missingness tablosu üret.
- Range / impossible value kontrolü yap.
- Duplicate ve tutarsız kayıt taraması yap.
- Kritik türetilmiş değişkenleri yeniden üret ve doğrula.
- Her endpoint için final usable denominator tablosu oluştur.
- Kategorik kodların codebook ile tam uyumunu kontrol et.
- Tüm veri temizleme adımlarını log dosyasında sakla.
- Kritik veri temizleme kararlarını ayrı `data_cleaning_notes.md` dosyasında özetle.

### **3. Tanımlayıcı analizler**

- Genel kohort tablosunu üret.
- Ana sonlanımların prevalans tablosunu üret.
- Grup-bazlı özet tabloyu üret.
- Basit prevalans ve grup dağılımı görsellerini oluştur.
- Eksik veri veya denominator farkı varsa ek tablo üret.
- Her ana değişken için özet istatistiklerin Results metniyle uyumlu kısa notunu oluştur.

### **4. Ana analizler**

- Binary / kategorik sonlanımlar için small-sample uygun grup karşılaştırmalarını çalıştır.
- Her binary analiz için etki büyüklüğünü hesapla.
- Count-like sonlanım için nonparametrik grup testini çalıştır.
- Count-like sonuç için etki büyüklüğünü hesapla.
- Çoklu test düzeltmesini uygula.
- Sonuçları tek bir ana inferans tablosunda birleştir.
- Her sonuç için kısa `primary wording note` üret.
- Her test için hangi hipotez ailesine ait olduğunu işaretle.

### **5. Varsayım ve tanısal kontroller**

- Parametrik yöntem kullanılan yer varsa normallik ve varyans kontrollerini yap.
- Modelleme varsa multicollinearity, leverage ve residual kontrollerini yap.
- Varsayım ihlali saptanırsa alternatif yönteme geçiş kararını not et.
- Tanısal uyarıları ayrı bir risk notu dosyasında sakla.
- Varsayım ihlali olan analizleri nihai yorumda açıkça işaretle.

### **6. Supporting analizler**

- Alternative coding / alternative grouping gerekip gerekmediğini kontrol et.
- Gerekliyse exact / permutation duyarlılık kontrolü ekle.
- Yaş / dentisyon gibi sınırlı ikincil kontrollerin yapılabilirliğini değerlendir.
- Endpoint-bazlı denominator ve missingness ek tablosunu hazırla.
- Supporting analizlerin ana sonuçla uyum durumunu işaretle.
- Her supporting analizi “ana sonucu destekliyor / karışık sonuç veriyor / ana sonucu zayıflatıyor” diye sınıflandır.

### **7. Robustluk analizleri**

- Leave-one-out analizi yap.
- Kritik kategori dışlama / yeniden tanımlama analizini yap.
- Her robustluk analizi için ana sonucun ne kadar değiştiğini raporla.
- Sonuçları `stabil / kısmen stabil / kırılgan` olarak sınıflandır.
- Robustluk özetini ana tablodan ayrı, net bir supporting tabloya koy.
- Ana bulgunun yorumu robustluk sonuçlarına göre yeniden etiketlenmeli mi diye kontrol et.

### **8. Model doğrulama (yalnız ikincil)**

- Modelleme gerçekten gerekli mi diye önce karar ver.
- Yapılacaksa penalized yaklaşım kullan ve bunu `secondary exploratory` olarak etiketle.
- CV, AUC, delta-AUC ve uygun belirsizlik ölçülerini hesapla.
- Warning / note alanlarını ayrı raporla.
- Çıktıları primer inferans gibi değil, supporting verification gibi sun.
- Model doğrulama metninde `predictive` yerine `secondary internal verification` dili kullan.
- Delta-AUC sonucu ile warning / transparency notlarını aynı yerde birlikte raporla.

### **9. Sonuçları birleştirme ve raporlama**

- Her analiz için `primary / supporting / robustness / exploratory` etiketi ata.
- Ana sonuç tablosu, supporting tablo ve robustness tablo ayrımını yap.
- Results için yalnız veri-dominant cümleler üret.
- Discussion için yalnız yorum gerektiren noktaları ayrı listele.
- Küçük örneklem ve kırılganlık uyarılarını sonuç metnine yedir.
- Ana bulgu ile supporting bulgular arasında çelişki varsa bunu gizleme; açıkça işaretle.
- Düzeltilmiş p ile düzeltilmemiş p yorumlarını karıştırma.

### 10. Minimum raporlama şablonu

Her ana analiz için en az şunları raporla:

- analiz adı,
- analiz edilen sonlanım,
- grup yapısı / karşılaştırma ekseni,
- usable N,
- test / model,
- test istatistiği,
- p-değeri,
- düzeltilmiş p-değeri (gerekiyorsa),
- etki büyüklüğü,
- %95 güven aralığı (mümkünse),
- yorum etiketi: `primary / supporting / robustness / exploratory`.

### 11. Sonuç metni yazım şablonu

#### Ana bulgu

“X sonlanımı açısından gruplar arasında [test adı] ile değerlendirilen farklılık gözlendi / gözlenmedi (istatistik = ..., p = ..., düzeltilmiş p = ..., etki büyüklüğü = ..., %95 GA = ...). Bulgular [güçlü / sınırlı / keşfedici] düzeyde yorumlandı.”

#### Supporting bulgu

“Ana sonuca ek olarak yapılan supporting analizde, bulgunun [benzer biçimde korunduğu / zayıfladığı / tanım değişikliğine duyarlı olduğu] görüldü.”

#### Robustluk bulgusu

“Robustluk analizlerinde sonuç [stabil / kısmen stabil / kırılgan] bulundu; tekil gözlem dışlaması sonrasında [ana yön korundu / anlamlılık değişti / etki büyüklüğü belirgin biçimde değişti].”

#### Sınırlılık cümlesi

“Küçük örneklem, seyrek hücre yapısı ve endpoint tanımlarındaki sınırlılıklar nedeniyle bu bulgular doğrulayıcı değil, ihtiyatla yorumlanması gereken sonuçlar olarak değerlendirilmelidir.”

### 12. Alternatifler ve kısa artı / eksi karşılaştırması

#### Alternatif 1: Klasik parametrik eksen

**Artı:** Okuyucuya tanıdık gelebilir.\
**Eksi:** Bu veri yapısına tam uymayabilir; küçük örneklem ve seyrek hücreler yüzünden savunması zayıf kalır.

#### Alternatif 2: Small-sample / nonparametric / robustness ağırlıklı eksen

**Artı:** Veri yapısına daha uygun, reviewer karşısında daha savunulabilir, daha dürüst yorum sağlar.\
**Eksi:** Sonuç dili daha ihtiyatlı olur; güçlü doğrulayıcı iddialar üretmez.

#### Alternatif 3: Model ağırlıklı yaklaşım

**Artı:** Keşfedici olarak ilginç sinyaller üretebilir.\
**Eksi:** Small-n ortamında aşırı yorum ve overfitting riski yüksektir; primer analiz omurgası olmamalıdır.

### 13. Copilot için kapanış yönergesi

Copilot bu planı uygularken şu temel ilkelere uymalıdır:

- &#x20;Ana analiz ile destekleyici analizi karıştırma.
- Testi yalnız çalıştırma; neden seçildiğini ve hangi durumda terk edilmesi gerektiğini de raporla.
- Küçük örneklem nedeniyle çıkan her dikkat çekici sonucu doğrulanmış bulgu gibi sunma.
- Sonuç üretmeden önce denominator, coding ve endpoint mantığını doğrula.
- Supporting ve robustness analizlerini “sonradan eklenen süs” gibi değil, sonuç güvenilirliğinin parçası olarak ele al.
- Ana sonuca ters düşen supporting bulguları bastırma; açıkça raporla.
- Results ile Discussion arasında yorum sınırını koru.
- Kod ve çıktı dosyalarını tekrar üretilebilir biçimde sakla.

## Son not

Bu planın amacı, eksik supporting ve robustness analizlerini sonradan rastgele eklemek değil, tüm analitik hattı baştan sona **savunulabilir, şeffaf, tekrar üretilebilir ve reviewer karşısında dayanıklı** hale getirmektir. Bu nedenle Copilot görevleri yalnız test çalıştırmaya değil, testin neden seçildiğini, hangi durumda terk edilmesi gerektiğini ve sonucun ne kadar güvenilir olduğunu göstermeye de odaklanmalıdır.


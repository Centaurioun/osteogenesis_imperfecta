# Author Clarification Rules Snapshot

Aşağıdaki kurallar reanalysis sürecinde zorunlu olarak uygulanmıştır:

1. **Doku anomalisi = baskın tek kod mantığı**
   - `doku anomalisi` alanında `0 = yok`.
   - Aynı hastada çoklu fenotip varlığı veri yapısında ayrı sütunlarla kodlanmamıştır.
   - Rule-constrained analizde çoklu etiketli fenotip matrisi varsayılmamıştır.

2. **DI tip/şiddet kaydı yok**
   - Dentinogenesis imperfecta için tip veya şiddet kaydı yoktur.
   - Tip/şiddet alt analizleri yapılmamış, yalnız sınırlılık olarak notlanmıştır.

3. **OCCL 4 = infraocclusion (Angle dışında)**
   - `occl_tip` değerlerinde `1-3` Angle sınıflarıdır.
   - `occl_tip == 4` bağımsız infraocclusion durumudur.
   - Rule-constrained katmanda Angle modeline dahil edilmemiştir.

4. **`dmft_dmft` = count-like alan**
   - Klasik ayrıştırılmış DMFT/dmft indeksi gibi kullanılmamıştır.
   - Proje mantığında toplam çürük yükünü temsil eden count-like alan olarak ele alınmıştır.

5. **Overjet / Overbite / Open bite / Crossbite / Gingivitis = binary var-yok**
   - Eşik, mm, şiddet veya derecelendirme bilgisi bulunmadığı için yalnız ikili değişken olarak ele alınmıştır.

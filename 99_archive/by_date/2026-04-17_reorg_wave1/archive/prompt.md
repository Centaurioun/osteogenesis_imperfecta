# Osteogenesis Imperfecta Veri Analiz ve Temizleme Projesi

## Proje Özeti

Bu proje, 34 hastaya ait Osteogenesis Imperfecta (OI) verilerini içeren `osteogenesis_imperfecta_original_data.csv` dosyasının veri kalitesini iyileştirmek, standartlaştırmak ve `Osteogenesis-Imperfecta-Oro-Denta-Bulgular-Etik-Kurul-Basvuru-Rev3.md` protokolüne tam uyumlu olarak istatistiksel analize (SPSS, R, Python vb.) hazır hale getirmek amacıyla oluşturulmuştur.

**Önemli Notlar:**
1. `Osteogenesis-Imperfecta-Oro-Denta-Bulgular-Etik-Kurul-Basvuru-Rev3.md` dosyası, çalışmanın bilimsel altyapısını, dahil edilme/hariç tutulma kriterlerini ve planlanan istatistiksel analizleri içerir. Veri temizleme kararları bu protokole dayanmalıdır.
2. `osteogenesis_imperfecta_original_data.csv` dosyası ham veri setidir. Hiçbir veri kaybı yaşanmadan, dönüştürülebilir ve izlenebilir bir temizleme süreci işletilmelidir.

---

## Görev Listesi ve Uygulama Adımları

### 1. Veri Temizleme, Sütun Standardizasyonu ve Aykırı Değer Kontrolü

CSV tablosundaki verileri istatistiksel analiz için standartlaştırın:

- **Sütun Adlandırma Standardı (Snake Case)**
  - Tüm sütun isimlerini küçük harfe çevirin.
  - Boşlukları ve özel karakterleri (/, vb.) alt çizgi (`_`) ile değiştirin.
  - Türkçe karakterleri (ı, İ, ş, Ş, ç, Ç, ö, Ö, ü, Ü, ğ, Ğ) İngilizce eşdeğerlerine dönüştürün.
  - *Örnek:* `OCCL TİP` -> `occl_tip`, `DMFT/dmft` -> `dmft_dmft`, `DİŞ EKSİKLİĞİ` -> `dis_eksikligi`.

- **Veri Tipi Doğrulama ve Eksik Veri Yönetimi**
  - Tüm sütunlardaki boş/eksik değerleri (NaN, Null) tespit edin. SPSS için eksik verileri boş bırakın veya standart bir kod (örn. 999) atayarak Veri Sözlüğü'nde belirtin.
  - Sayısal olması gereken sütunlardaki (örn. `yas`, `dmft_dmft`) metinsel veya hatalı girişleri düzeltin.

- **Protokol Uyumlu Aykırı Değer (Outlier) Kontrolü**
  - **Yaş:** Protokole göre dahil edilme kriteri 5-65 yaş arasıdır. Bu aralığın dışındaki hastaları (örn. 2, 3, 4 yaşındaki hastalar veri setinde mevcut) tespit edin ve raporda "Protokol Dışı Yaş" olarak özel olarak işaretleyin/raporlayın.
  - **İkili (Binary) Veriler:** 0 ve 1 dışında değer içeren hücreleri tespit edip düzeltin.

### 2. Değişkenlerin Kategorizasyonu ve Kodlanması

Veri setindeki sütunlar, araştırma protokolündeki parametrelere göre aşağıdaki gibi gruplandırılmalı ve SPSS'e uygun şekilde sayısallaştırılmalıdır:

|  No  |  Kategori                  |  İlgili Sütunlar (Orijinal Adlarıyla)                              |  Veri Türü          |  Beklenen Kodlama                                            |
| ---- | -------------------------- | ------------------------------------------------------------------ | ------------------- | ------------------------------------------------------------ |
|  1   |  Demografik                |  HASTA KODU, YAŞ                                                   |  Sayısal            |  Sürekli (Continuous)                                        |
|  2   |  Oklüzyon ve Kapanış       |  OCCL TİP                                                          |  Kategorik          |  1=Sınıf I, 2=Sınıf II, 3=Sınıf III, 4=Diğer (Belirtilmeli)  |
|  3   |  Kapanış Anomalileri       |  OPEN BITE, CROSSBITE, OVERJET, OVERBITE                           |  İkili (Binary)     |  0=Yok, 1=Var                                                |
|  4   |  Pozisyon Değişiklikleri   |  EKTOPİ, HETEROTOPİ, TRANSPOZİSYON, DEPLASMAN, INVERSIYON          |  İkili (Binary)     |  0=Yok, 1=Var                                                |
|  5   |  Diş Sayısı Anomalileri    |  DİŞ EKSİKLİĞİ, GÖMÜLÜ, ARTI DİŞ                                   |  İkili (Binary)     |  0=Yok, 1=Var                                                |
|  6   |  Şekil/Boyut Anomalileri   |  MAKRODONTİ, MİKRODONTİ, FAZLA TÜBERKÜL, SARKIK MİNE, MİNE İNCİSİ  |  İkili (Binary)     |  0=Yok, 1=Var                                                |
|  7   |  Kök ve Pulpa Anomalileri  |  TAURODONTİZM, KÖK ANOMALİSİ                                       |  İkili (Binary)     |  0=Yok, 1=Var                                                |
|  8   |  Doku Anomalileri          |  DOKU ANOMALİSİ                                                    |  Kategorik/Sayısal  |  Değerlerin frekansını çıkarıp kodlayın                      |
|  9   |  Çürük ve Periodontal      |  DMFT/dmft, gingivitis                                             |  Sayısal / İkili    |  DMFT: Sürekli, Gingivitis: 0=Yok, 1=Var                     |
|  10  |  Genetik Veriler           |  gen mutasyonu                                                     |  Metinsel           |  (Bkz. Bölüm 3)                                              |

- **Eksik Veri Uyarısı (Dentinogenesis Imperfecta - DI):** Protokolde DI varlığı ve şiddeti (Shields sınıflandırması) temel parametrelerden biri olarak belirtilmiştir ancak CSV'de "DI" sütunu bulunmamaktadır. Bu eksikliği rapora mutlaka ekleyin.

### 3. Gen Mutasyonu Sütununun İleri Düzey Analizi ve Ayrıştırılması

"gen mutasyonu" sütunu serbest metin formatında karmaşık veriler içermektedir. İstatistiksel analiz (Genotip-Fenotip korelasyonu) için bu sütunu aşağıdaki alt bileşenlere ayrıştırın:

- **Ana Gen Adı (`gen_adi`)**
  - Metinden ana gen adını (örn. `COL1A1`, `COL1A2`, `P3H1`, `FKBP10`, `WNT1`, `PRDM5`, `ALX3`, `LTBP3`, `LAMB3`, `LRP5`, `CBS`, `MSH6`) ayıklayın.
  - *Çoklu Mutasyon Durumu:* Bir hastada birden fazla gen mutasyonu varsa (örn. Hasta 8, 11, 15), bunları `gen_adi_1`, `gen_adi_2` şeklinde ayırın veya analize uygun şekilde "Çoklu Mutasyon" kategorisi oluşturun.

- **Mutasyon Detayı / HGVS Notasyonu (`mutasyon_detayi`)**
  - Gen adından sonra gelen c. (kodlayan DNA) ve p. (protein) seviyesindeki mutasyon kodlarını (örn. `c.2295+5G>A`, `p.(Leu149Arg)`, `c.890_897dupTGATGGAC`) ayrı bir sütuna taşıyın.

- **Zigosite Durumu (`zigosite`)**
  - Mutasyonun homozigot mu yoksa heterozigot mu olduğunu standartlaştırın.
  - *Eşleştirme:* `ht`, `het`, `HT` -> `Heterozigot` | `homo`, `hom`, `HO`, `homozigot` -> `Homozigot` | Belirtilmeyenler -> `Bilinmiyor`.

- **Klinik Anlamlılık / Varyant Durumu (`varyant_durumu`)**
  - Metinde geçen klinik sınıflandırmaları ayıklayın: `VUS` (Variant of Uncertain Significance), `pat.` / `PATOJENİK` (Pathogenic), `yeni mut` (De novo/New mutation).

- **Ek Notlar (`genetik_ek_notlar`)**
  - "antenatal tanı", "taşıyıcı ama etkilenmiş", "geleofizik displazi", "Brittle Cornea 2" gibi klinik ek bilgileri kaybetmemek için bu sütunda toplayın.

### 4. Mutasyon Kodlama ve Veri Sözlüğü (Codebook) Oluşturma

SPSS ve benzeri programlarda analiz yapabilmek için tüm kategorik veriler sayısallaştırılmalıdır:

- **Gen Kodlama Şeması (`gen_kodu`)**
  - Tespit edilen her benzersiz gen adına 1'den başlayan ardışık bir tam sayı kodu atayın.

- **Kapsamlı Veri Sözlüğü (Data Dictionary / Codebook)**
  - Sadece gen mutasyonları için değil, **tüm değişkenler** için bir veri sözlüğü oluşturun (örn. `data_dictionary.md` veya `README.md` içinde).
  - İkili değişkenler için 0 ve 1'in ne anlama geldiğini (0 = Yok, 1 = Var), `occl_tip` için 1, 2, 3, 4'ün hangi Angle Sınıflarına denk geldiğini açıkça belirtin.

### 5. Proje Yönetimi, Dokümantasyon ve Tekrarlanabilirlik

Projenin sürdürülebilirliği, izlenebilirliği ve şeffaflığı için aşağıdaki adımları uygulayın:

- **Tekrarlanabilir Veri Temizleme (Reproducibility)**
  - Veri temizleme işlemlerini Excel'de manuel yapmak yerine, **Python (Pandas)** veya **R** kullanarak bir betik (script) veya Jupyter Notebook (`.ipynb`) üzerinden gerçekleştirin.
  - Kodunuzu modüler yazın: 1. Veri Yükleme, 2. Temizleme ve Dönüştürme, 3. Genetik Ayrıştırma, 4. Dışa Aktarma.
  - Kullanılan kütüphaneleri içeren bir `requirements.txt` dosyası oluşturun.

- **Sürüm Kontrol Sistemi (Git) ve Değişiklik Geçmişi**
  - Projede yapılacak tüm değişikliklerin takip edilebilmesi için Git kullanın.
  - Yapılan her veri temizleme kararını, varsayımları ve güncellemeleri tarihçesiyle birlikte tutmak için bir `CHANGELOG.md` dosyası oluşturun.

- **Kapsamlı README.md Dosyası Oluşturma**
  - Proje dizininde bir `README.md` dosyası oluşturun ve şu detayları ekleyin:
    - **Projenin Amacı ve Kapsamı:** OI hastalarında oro-dental bulguların genetikle ilişkisinin incelenmesi.
    - **Veri Setinin İçeriği ve Kaynakları:** Ham verinin yapısı ve kaynağı.
    - **Protokol-Sütun Eşleştirmesi ve Veri Türleri:** Hangi sütunun hangi parametreye ve veri türüne karşılık geldiği.
    - **Planlanan Analizler:** Protokolde belirtilen istatistiksel testler (Normallik testleri, ANOVA, Kruskal-Wallis, Ki-kare, Lojistik Regresyon vb.).

- **Veri Gizliliği ve Anonimleştirme (KVKK/Etik Kurul Uyumluluğu)**
  - Veri setinde hastaların kimliğini açığa çıkarabilecek kişisel veri (isim, TC kimlik no vb.) bulunmadığından emin olun. Sadece "HASTA KODU" kullanıldığını doğrulayın.

### 6. Beklenen Çıktı Ürünleri (Deliverables)

1. **`cleaned_osteogenesis_data.csv`**: SPSS/R/Python analizine doğrudan aktarılabilecek, tamamen sayısallaştırılmış ve temizlenmiş nihai veri seti.
2. **`data_cleaning_script.py` veya `.ipynb`**: Temizleme işlemlerini yapan tekrarlanabilir kaynak kod.
3. **`README.md`**: Proje dokümantasyonu ve Veri Sözlüğü (Codebook).
4. **`CHANGELOG.md`**: Yapılan değişikliklerin ve alınan kararların günlüğü.
5. **`Veri_Temizleme_Raporu.md`**: Tespit edilen anomaliler (örn. yaş kriterine uymayanlar, eksik DI verisi, çoklu mutasyon kararları) hakkında özet rapor.

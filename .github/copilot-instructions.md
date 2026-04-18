# 🧬 Osteogenesis Imperfecta (Camber) Projesi: AI Agent Genel Yönergeleri

## 1. Rol ve Davranış Çerçevesi
- **Rolünüz:** İleri düzey bir Biyostatistikçi ve Araştırma Mühendisidir. Üretilen her analiz, kod, yöntem ve sonucun "publication-ready" (yayına adayı) tıbbi araştırma makalesi standardında olması zorunludur.
- **Klinik "Uydurma" (Hallucination) Yasağı:** Tanılar, hastalık şiddeti eşikleri ve klinik varsayımlar için **SADECE** workspace'te sağlanan dokümanlara (`camber_sap...`, `codebook...`, `.csv` meta-verileri) sadık kalın. Kendi eğitim verinizden (LLM training data) harici fenotip bilgisi, varsayımsal sendrom kuralları dahil etmeyin.

## 2. Hassas Klinik Dönüşümler (Kırmızı Çizgiler)
- **Oklüzyon Sınıflaması (`occl_tip`):** Yalnızca `1`, `2` ve `3` değerleri Angle sınıflamasını ifade eder. Eğer `occl_tip == 4` tespit edilirse, bu "İnfraoklüzyon" demektir. Bu değer yapısal Angle sınıflamasına veya ordinal/sıralı bir modele **KESİNLİKLE** dahil edilemez. `4` değeri yakalandığında `infraokluzyon_var = 1` adında bağımsız bir bayrak üretilmeli ve bu hastanın Angle değeri hesaplamada `NaN` olarak dışlanmalıdır.
- **DMFT Skoru Okumaları (`dmft_dmft`):** Verideki bu sütun resmi ve ayrıştırılmış bir DMFT indeksi **değildir**. Aksine ağızdaki "toplam çürük/dolgu sayısını" (count) yansıtır. Analiz için var/yok ikilemi (binary) gerekliyse, yalnızca `dmft_dmft > 0` şartı kullanılarak `caries_any` değişkenine dönüştürülmelidir.

## 3. Determinizm ve Tekrarlanabilirlik Mimarisi
- **Sabit Rastgelelik (Seed):** Bilimsel tekrarlanabilirliği garanti etmek için veri kodlarında bulunan istisnasız her rastgele/stokastik çağrı (çapraz-doğrulama, permütasyon testleri, bootstrap güven aralıkları) `SEED = 20260228` değeriyle sabitlenmelidir. Kod her çalıştığında noktası virgülüne tıpa tıp aynı P-değerleri çıkmalıdır.

## 4. Kalite Kontrol (Safety & Fail-Fast)
- **Sessiz Geçiş Yasağı:** Beklenmeyen veri tipleri saptandığında (örn: İkili alanda 2 değeri veya eksi yaş verisi) işlemi göz ardı edip modele devam etmeyin. Kesin suretle `assert` logları ile kodu durdurun (Fail-Fast), hatayı fırlatın ve `issue_log_v3.csv` isimli sistem dosyasına bu ihaleyi otomatik işleyin.
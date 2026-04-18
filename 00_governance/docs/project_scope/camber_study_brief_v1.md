# Camber için Çalışma Özeti (Study Brief) — v1

## 1) Çalışmanın amacı ve gerekçesi
- Osteogenesis Imperfecta (OI) tanılı pediatrik olgularda **oro-dental bulguların prevalansını** ve bu bulguların **mevcut genetik verilerle (gen düzeyi)** ilişkisini değerlendirmek.
- Veri seti, klinik muayene + panoramik radyografi bulguları ve mevcut genetik kayıtların birleştirilmiş özetini içerir.

## 2) Tasarım ve örneklem
- Tasarım: retrospektif, gözlemsel, kesitsel.
- Örneklem: 34 hasta (pediatrik yaş aralığı).

## 3) Değişkenlerin kayıt mantığı (İnci Hanım yanıtlarına göre)
### 3.1. Doku anomalileri
- `doku_anomalisi` tek kodludur ve **baskın olan tanı** kaydedilmiştir (multi-label yok).
- Kodlama:
  - 0 = yok
  - 1 = Amelogenesis imperfecta
  - 2 = Dentinogenezis imperfecta
  - 3 = Dentin displazisi
  - 4 = Odontodisplazi
  - 5 = Turner hipoplazisi
  - 6 = Hipersementoz
  - 7 = Hipoplazi
- Not: DI için Shields tip/şiddet kaydı **yok** (sınırlılık).

### 3.2. Oklüzyon
- `occl_tip` kodlama:
  - 1 = Angle Sınıf I
  - 2 = Angle Sınıf II (divizyon 1/2 ayrımı yok)
  - 3 = Angle Sınıf III
  - 4 = İnfraoklüzyon (Angle sınıflamasına dahil değil; veri setinde ayrıca kodlandı)

### 3.3. DMFT/dmft
- `dmft_dmft` alanı, **ağızdaki toplam çürük sayısı** mantığıyla kaydedildi.
- D/M/F bileşen ayrımı yok; indeks bileşenleri üzerinden yorum yapılmayacak.

### 3.4. Var/Yok kodlu klinik değişkenler
- Overjet/overbite/open bite/crossbite/gingivitis vb. alanlarda **şiddet/ölçüm/eşik kaydı yok**; yalnızca **var/yok (0/1)** kaydı var.

## 4) Çalışma soruları (önerilen)
- Gen gruplarına göre:
  - (A) doku anomalisi varlığı ve türleri
  - (B) toplam çürük sayısı (`dmft_dmft`)
  - (C) gingivitis varlığı
  - (D) oklüzyon tipi dağılımı
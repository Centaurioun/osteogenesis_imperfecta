# Camber için İstatistik Analiz Planı (SAP) — v2 (Publication‑Ready)

Bu SAP, n=34’lük pediatrik OI veri setinde oro‑dental fenotiplerin prevalansını ve gen düzeyi (COL1A1, COL1A2, FKBP10, P3H1, vb.) ile ilişkisini **yayınlanmaya hazır** biçimde raporlamak için hazırlanmıştır. Plan; küçük örneklem, düşük hücre sayıları, çoklu karşılaştırma ve model kararsızlığı risklerini yönetmek üzere “bullet‑proof” prensiplerle yapılandırılmıştır.

---

## 0) Dosyalar ve tek doğru veri kaynağı
- Analiz verisi (önerilen): `osteogenesis_imperfecta_camber_input_minimal_v1.csv`
- Kayıt mantığı / codebook: `codebook_v3_fixed.md`
- Çalışma özeti: `camber_study_brief_v1.md`
- Referans amaçlı (Camber’a girmesi şart değil): temizlenmiş tam veri seti.

**Kural:** Camber’da “feature” olarak kullanılacak veri **minimal CSV** ile sınırlandırılır. Serbest metin genetik detay sütunları (örn. `gen_mutasyonu_detay`, `ek_gen_bulgu`) analiz verisine dahil edilmez.

---

## 1) Çalışma tasarımı ve örneklem
- Tasarım: retrospektif, gözlemsel, kesitsel.
- Örneklem: 34 hasta.
- Analiz birimi: hasta.

---

## 2) Değişkenler ve kayıt kuralları

### 2.1. Gen (primer belirleyici)
- `gen_mutasyonu`: gen düzeyi kategorik değişken.
- `gen_kodu`: teknik kolaylık; raporlama gen adıyla yapılır.

**Önceden tanımlı gen gruplama (güç için):**
- Tanımlayıcı tabloda: tüm genler ayrı gösterilir.
- İnferans analizinde (primer): n≥6 olan genler ayrı, diğerleri “Other”:
  - COL1A1, COL1A2, FKBP10, P3H1, Other
- Hassasiyet: eşik n<3 yerine n<4 (veya n<2) ile yeniden birleştirme.

### 2.2. Primer sonlanımlar
1) `doku_anomalisi_var` (0/1)
2) `dmft_dmft` (sayısal sayım; “ağızdaki toplam çürük sayısı”)
3) `gingivitis` (0/1)

### 2.3. Sekonder sonlanımlar
- `doku_anomalisi` (0–7; çoğunlukla deskriptif)
- `occl_tip` (1–4)
- `infraokluzyon_var` (0/1)
- `caries_any` (0/1)
- `dentisyon_donemi_kod` (1–3)

### 2.4. Kovaryatlar
- `yas` primer kovaryattır.
- `dentisyon_donemi_kod`, `yas`’ın türevidir; aynı modelde birlikte kullanılmaz.

---

## 3) Eksik veri ve kalite kontrol
- Eksik oranı değişken bazında raporlanır.
- Varsayılan: complete‑case.
- Kod dışı değer kontrolü: ikili alanlar 0/1; `occl_tip` 1–4; `doku_anomalisi` 0–7; `dmft_dmft` ≥0.

---

## 4) Tanımlayıcı istatistikler (Tablo seti)

### Table 1 — Örneklem özellikleri (genel)
- Yaş: medyan (IQR) + ortalama±SS + min–maks
- Dentisyon dönemi: n (%)
- Gen dağılımı: n (%)
- Oklüzyon tipi: n (%)
- dmft_dmft: medyan (IQR) + min–maks
- `caries_any`, `doku_anomalisi_var`, `gingivitis`: n (%), %95 GA (Wilson)

### Table 2 — Gen gruplarına göre primer sonlanımlar
- n, yaş özeti, `doku_anomalisi_var`, `gingivitis`, `caries_any`, `dmft_dmft` (medyan/IQR)

### Table 3 — Primer hipotez testleri + etki büyüklükleri
- Global testler + robustluk kontrolleri + düzeltmeler

---

## 5) Primer hipotezler ve test stratejisi

### H1) Gen grubu ↔ `doku_anomalisi_var`
- Global: exact/Monte‑Carlo yaklaşım (mümkünse Fisher‑Freeman‑Halton; değilse permütasyon/Monte‑Carlo χ²).
- Etki büyüklüğü: Cramer's V + prevalans farkları (%95 GA).
- Hedefli karşılaştırmalar (önceden tanımlı):
  - COL1A1 vs diğerleri
  - COL1A2 vs diğerleri
  - FKBP10 vs diğerleri
  - P3H1 vs diğerleri
- 2×2: Fisher exact + OR (%95 GA).
- Çoklu test düzeltmesi: Holm.

**Doğrulama (adjusted):** penalize lojistik (Firth veya L2‑regularized) + yaş.

### H2) Gen grubu ↔ `dmft_dmft`
- Global: Kruskal–Wallis.
- Etki büyüklüğü: ε².
- Pairwise (gerekiyorsa): Mann–Whitney U + Holm/FDR.

**Doğrulama:** `caries_any` ile aynı hipotez; destekleyici olarak (n küçük) sayım modeli (negatif binom/Poisson) + yaş.

### H3) Gen grubu ↔ `gingivitis`
- Global: exact/Monte‑Carlo r×2 yaklaşım.
- Hedefli 2×2 seti (H1 ile aynı) + Holm.

**Doğrulama:** penalize lojistik + yaş.

---

## 6) Cross‑Validation / Robustluk (zorunlu)
- Bootstrap %95 GA (≥2000 tekrar)
- Leave‑One‑Out stabilite
- Permütasyon p‑değerleri (H1/H3)
- Gen gruplama eşiği hassasiyeti
- İnfraoklüzyon olgusunu çıkarıp tekrar et

---

## 7) Belirsizlik yönetimi (inconclusive sonuçlarda zorunlu aksiyon listesi)
1) Gen kategorisini daha düşük boyuta indir (major vs Other).
2) Penalize/bayesian lojistik ile stabilite kontrol et.
3) Permütasyonla doğrula.
4) dmft_dmft → caries_any ile tekrarla.
5) Yaşa göre katmanlı (dentisyon dönemleri) deskriptif tablo.
6) Düzeltme sonrası sinyal kalıyor mu kontrol et.
7) Klinik anlamlı etki varsa nicel güç/örneklem önerisi ekle.

---

## 8) Raporlama standardı
- Her tabloda n belirt.
- p‑değerine ek: etki büyüklüğü + %95 GA.
- Sınırlılıklar: n küçük; tek merkez; kesitsel; DI Shields yok; şiddet/eşik yok.

---

## 9) Camber/Claude için net talimat
Bu SAP’ye sadık kalarak Table 1–3’ü üret; primer testleri exact/robust yöntemlerle yap; çoklu karşılaştırmaları Holm ile düzelt; her primer sonlanım için bootstrap + LOO + permütasyon robustluk özetini ekle; sonuçlar belirsizse Bölüm 7’deki aksiyon listesini uygula.


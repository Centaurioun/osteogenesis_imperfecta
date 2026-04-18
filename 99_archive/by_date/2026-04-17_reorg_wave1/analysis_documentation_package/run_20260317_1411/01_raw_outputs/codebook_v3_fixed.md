# Veri Sözlüğü (Codebook)

Bu sözlük, temizlenmiş veri setindeki değişkenlerin veri tipi ve kodlamasını özetler.

## `hasta_kodu`
- Tip: ID (sayısal)

## `yas`
- Tip: Sayısal

## `occl_tip`
- Tip: Kategorik (kodlu)
- İzinli değerler: 1,2,3,4
- Not: 1=Angle I; 2=Angle II (div ayrımı yok); 3=Angle III; 4=İnfraoklüzyon.

## `open_bite`
- Tip: İkili (0/1)
- İzinli değerler: 0,1
- Not: Sadece var/yok (0/1); şiddet/eşik kaydı yok.

## `crossbite`
- Tip: İkili (0/1)
- İzinli değerler: 0,1
- Not: Sadece var/yok (0/1); şiddet/eşik kaydı yok.

## `overjet`
- Tip: İkili (0/1)
- İzinli değerler: 0,1
- Not: Sadece var/yok (0/1); şiddet/eşik kaydı yok.

## `overbite`
- Tip: İkili (0/1)
- İzinli değerler: 0,1
- Not: Sadece var/yok (0/1); şiddet/eşik kaydı yok.

## `ektopi`
- Tip: İkili (0/1)
- İzinli değerler: 0,1

## `heterotopi`
- Tip: İkili (0/1)
- İzinli değerler: 0,1

## `transpozisyon`
- Tip: İkili (0/1)
- İzinli değerler: 0,1

## `deplasman`
- Tip: İkili (0/1)
- İzinli değerler: 0,1

## `inversiyon`
- Tip: İkili (0/1)
- İzinli değerler: 0,1

## `dis_eksikligi`
- Tip: İkili (0/1)
- İzinli değerler: 0,1

## `gomulu`
- Tip: İkili (0/1)
- İzinli değerler: 0,1

## `arti_dis`
- Tip: İkili (0/1)
- İzinli değerler: 0,1

## `makrodonti`
- Tip: İkili (0/1)
- İzinli değerler: 0,1

## `mikrodonti`
- Tip: İkili (0/1)
- İzinli değerler: 0,1

## `fazla_tuberkul`
- Tip: İkili (0/1)
- İzinli değerler: 0,1

## `sarkik_mine`
- Tip: İkili (0/1)
- İzinli değerler: 0,1

## `mine_incisi`
- Tip: İkili (0/1)
- İzinli değerler: 0,1

## `taurodontizm`
- Tip: İkili (0/1)
- İzinli değerler: 0,1

## `kok_anomalisi`
- Tip: İkili (0/1)
- İzinli değerler: 0,1

## `doku_anomalisi`
- Tip: Kategorik (kodlu)
- İzinli değerler: 0,1,2,3,4,5,6,7
- Not: Tek kod (baskın durum). 0=Yok; 1=AI; 2=DI; 3=Dentin displazisi; 4=Odontodisplazi; 5=Turner hipoplazisi; 6=Hipersementoz; 7=Hipoplazi.

## `dmft_dmft`
- Tip: Sayısal
- Not: Ağızdaki toplam çürük sayısı; bileşen ayrımı yok.

## `gingivitis`
- Tip: İkili (0/1)
- İzinli değerler: 0,1
- Not: Sadece var/yok (0/1); şiddet/eşik kaydı yok.

## `gen_mutasyonu`
- Tip: Metin
- Not: Serbest metin.

## `doku_anomalisi_etiket`
- Tip: Metin
- Not: Etiket sütunu (value label).

## `doku_anomalisi_var`
- Tip: İkili (0/1)
- İzinli değerler: 0,1
- Not: Türev ikili: 0=Yok, 1=Var (1–7).

## `occl_tip_etiket`
- Tip: Metin
- Not: Etiket sütunu (value label).

## `infraokluzyon_var`
- Tip: İkili (0/1)
- İzinli değerler: 0,1
- Not: Türev ikili: occl_tip=4 ise 1.

## `angle_sinifi`
- Tip: Kategorik (kodlu)
- Not: Türev: occl_tip 1–3 ise aynı değer, 4 ise boş.

## `dentisyon_donemi_kod`
- Tip: Kategorik (kodlu)
- İzinli değerler: 1,2,3
- Not: Yaşa göre türetildi: <6 süt; 6–<14 miks; >=14 daimi.

## `dentisyon_donemi`
- Tip: Metin
- Not: Etiket sütunu (value label).

## `caries_any`
- Tip: İkili (0/1)
- İzinli değerler: 0,1
- Not: dmft_dmft>=1 ise 1.

## `gen_adi_primary`
- Tip: Metin
- Not: Gen adı ayrıştırması; sadece metinden çekildi.

## `gen_adi_all`
- Tip: Metin
- Not: Metinden çekilen gen adları listesi (ayıraçlarla).

## `ek_gen_bulgu`
- Tip: Metin
- Not: Birincil gen dışındaki gen/bulgular (varsa).

---

## Ek notlar
- DI için Shields tip/şiddet bilgisi kaydedilmedi; raporda sınırlılık olarak belirtilmelidir.
- OVERJET/OVERBITE/OPEN BITE/CROSSBITE/gingivitis gibi değişkenlerde şiddet/eşik bilgisi yoktur; sadece var/yok kaydı yapılmıştır.
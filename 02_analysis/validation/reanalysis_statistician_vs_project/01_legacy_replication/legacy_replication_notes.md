# Legacy Replication Notes

## Scope

Bu katmanda amaç, istatistikçi raporundaki yaklaşımı tarihsel olarak yeniden üretmektir. Bu sonuçlar manuscript authority olarak değil, legacy benchmark olarak yorumlanır.

## Methods mirrored from statistician report

- Yazılım referansı: SPSS 11.5 (raporda belirtildiği şekliyle)
- Sürekli değişken karşılaştırmaları: Kruskal-Wallis
- Kategorik karşılaştırmalar: Fisher-exact
- Anlamlılık eşiği: 0.05

## Legacy coding assumptions preserved

- `occl_tip` 1/2/3/4 aynı kategorik aile içinde değerlendirilmiş gibi ele alındı.
- `doku anomalisi` çok düzeyli nominal değişken (yok/AI/DI/hipoplazi) şeklinde tutuldu.
- `dmft_dmft` summary sürekli/ordinal ölçü gibi kullanıldı.
- Binary klinik değişkenler (open bite, cross bite, over bite, gingivitis vb.) var/yok olarak bırakıldı.

## Replication quality interpretation

- `exact`: Legacy rapordaki sayıların aynı kaynaktan doğrudan doğrulanabildiği satırlar.
- `close`: Legacy test ailesi ve coding korunmasına rağmen SPSS prosedür ayrıntılarını bire bir bilmediğimiz için yakın replikasyon.
- `approximate`: Kısmi bilgi nedeniyle yaklaşık replikasyon.
- `not reproducible`: Legacy analiz tanımı yetersiz/eksik olduğu için tekrarlanamayan satır.

## Key legacy finding preserved

- Legacy hatta raporlanan tek anlamlı grup farkı OCCL analizidir (`p=0.017`).
- Bu bulgu rule-constrained katmanda ayrıca yeniden değerlendirilmek zorundadır.

## Limitations

- Legacy raporda exact prosedürün parametreleri ayrıntılı olmadığı için p-değeri yeniden üretiminde küçük nümerik sapmalar teorik olarak mümkündür.
- Legacy katman, author doğrulamalarıyla çelişen coding varsayımlarını bilinçli biçimde korur; bu nedenle tek başına manuscript kararına taşınamaz.

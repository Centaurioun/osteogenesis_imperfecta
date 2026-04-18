# Discrepancy Report — Round 2

## 1. What changed after actual reruns

- A03–A11 satırları için gerçek numerical rule-constrained rerun eklendi.
- Önceki pakette editoryal düzeyde kalan “supplementary-only” kararları, artık p-value + effect size ile sayısal olarak desteklenmiştir.
- A12cv satırındaki CI uyumsuzluğu teknik olarak doğrulanıp açık şekilde işaretlenmiştir.

## 2. Which earlier decisions were only editorial and are now numerically supported

- A03–A11 için daha önce “primary family dışı” gerekçesiyle yapılan sınıflama, round2 rerun ile numerik temele taşınmıştır.
- Bu endpointlerin primary’ye alınmaması kararı korunmuş, ancak artık “analiz yapılmadan verilmiş karar” olmaktan çıkmıştır.

## 3. Which discrepancies remain definition-sensitive

- A02 (OCCL): infraocclusion ayrımı nedeniyle tanım duyarlı fark sürmektedir.
- A12 (doku anomalisi): dominant-code/binary projection nedeniyle tanım duyarlılığı devam etmektedir.
- A13 (dmft/caries): count-like semantik nedeniyle legacy ile project-valid katman arasında tanım etkisi sürmektedir.

## 4. Which findings remain too weak for main text

- A03–A11 endpointlerinin tamamı (özellikle A04’teki zayıf unadjusted sinyale rağmen) primary inferential iddia için zayıf kalmaktadır.
- A12/A13 bulguları correction-sensitive olduğu için güçlü sonuç dili yerine temkinli ifade gerektirir.

## 5. Which findings are now better justified as supplementary

- A03–A11 bulguları round2 rerun sonrası supplementary olarak daha güçlü biçimde gerekçelendirilmiştir.
- Legacy-only A02 satırı (OCCL p=0.017) yine primary kanıt olarak taşınmamalıdır.

## Output reference

- `09_round2_outputs/discrepancy_attribution_table_round2.csv`

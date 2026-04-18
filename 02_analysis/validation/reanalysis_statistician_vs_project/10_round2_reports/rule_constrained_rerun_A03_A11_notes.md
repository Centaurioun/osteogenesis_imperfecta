# Rule-Constrained Rerun Notes (A03–A11)

## Scope

Round 2 kapsamında A03–A11 endpointleri için gerçek numerical rerun uygulanmıştır.

- Girdi veri: `archive/osteogenesis_imperfecta_original_data.csv` (endpointler) + `osteogenesis_imperfecta_camber_input_minimal_v1.csv` (runtime-consistent `gen_group`)
- Test yaklaşımı: `Chi2_with_permutation_validation` (10k iterasyon)
- Effect size: Cramer's V
- Multiplicity: Round2 A03–A11 ailesi içinde Holm düzeltmesi (`p_holm_round2_family`)

## Endpoint-level summary

- A03 `open_bite_rt`: p_perm=0.6587, V=0.295
- A04 `cross_bite_rt`: p_perm=0.0777, V=0.495 (zayıf sinyal; düzeltme sonrası anlamlı değil)
- A05 `over_bite_rt`: p_perm=1.0000, V=0.265
- A06 `transpozisyon_rt`: p_perm=0.3140, V=0.393
- A07 `dis_eksikligi_rt`: p_perm=1.0000, V=0.314
- A08 `gomulu_dis_rt`: p_perm=0.7753, V=0.290
- A09 `arti_dis_rt`: p_perm=0.5306, V=0.342
- A10 `taurodontizm_rt`: p_perm=0.7685, V=0.250
- A11 `kok_anomalisi_rt`: p_perm=1.0000, V=0.314

## Interpretation

- A03–A11 için “yalnız editoryal supplementary” kararı artık numerik rerun ile desteklenmiştir.
- Bu endpointlerin primary inferential aile dışında kalması korunmuştur.
- A04 için unadjusted zayıf sinyal mevcut olsa da Holm sonrası bu sinyal güçlenmemektedir; main-text primary iddia üretmez.

## Output reference

- `09_round2_outputs/rule_constrained_rerun_A03_A11.csv`

# OI analysis sweep

- Source: `osteogenesis_imperfecta_camber_input_minimal_v1.csv`
- Rows: 34
- Created: 2026-04-10T07:41:20.439637

## Verified matches against ToolUniverse
- Linear regression `yas` vs `dmft_dmft`: slope 0.22119844553090134, intercept 0.7721574526764448, R2 0.09170153471701036, t 1.797417645945423 matched ToolUniverse to rounding.
- Fisher exact for `gingivitis` vs `caries_any` matched ToolUniverse exactly: OR 6.428571, p 0.11326033.

## Main findings
- `yas` vs `dmft_dmft` shows a positive association but weak fit: R2 0.09170153471701036, p from ToolUniverse 0.08171246.
- Mann-Whitney for `dmft_dmft` by `gingivitis`: p_approx 0.28490547003443745 (median0 1.0, median1 2.0).
- Mann-Whitney for `dmft_dmft` by `doku_anomalisi_var`: p_approx 0.3860525359978416 (median0 2.0, median1 0.5).
- Mann-Whitney for `dmft_dmft` by `caries_any`: p_approx 4.151258828802713e-06 (median0 0.0, median1 3.0).
- Mann-Whitney for `dmft_dmft` by `infraokluzyon_var`: p_approx 0.232179363570388 (median0 2.0, median1 0.0).

## Categorical associations
- gingivitis vs doku_anomalisi_var: OR 3.0, p 0.23181488733082006
- gingivitis vs caries_any: OR 6.428571428571429, p 0.11326033450943482
- gingivitis vs infraokluzyon_var: OR 0.0, p 1.0
- doku_anomalisi_var vs caries_any: OR 0.2631578947368421, p 0.11560649758320372
- doku_anomalisi_var vs infraokluzyon_var: OR 0.0, p 1.0
- caries_any vs infraokluzyon_var: OR 0.0, p 0.29411764705882354

## Group age comparisons
- Age by gen_group: H=2.1121140552995348, epsilon_sq=-0.05720866499092319, group sizes={"COL1A2": 7, "P3H1": 8, "COL1A1": 6, "Other": 5, "FKBP10": 8}
- Age by dentisyon_donemi_kod: H=28.995391705069135, epsilon_sq=0.8180421728808829, group sizes={"1.0": 8, "2.0": 14, "3.0": 12}
- Age by gen_kodu: H=6.564832949308761, epsilon_sq=-0.04348991062700723, group sizes={"3": 7, "7": 8, "2": 6, "9": 1, "8": 1, "1": 1, "6": 1, "4": 8, "5": 1}

## Files
- `metadata.json`
- `descriptive_summary.csv`
- `linear_regression_yas_dmft_dmft.csv`
- `mann_whitney_dmft_by_binary.csv`
- `fisher_pairwise_binary.csv`
- `kruskal_age_by_groups.csv`

## SciPy rerun
- Project venv confirmed: SciPy 1.17.1, statsmodels 0.14.6.
- Mann-Whitney `gingivitis`: U=97.5, p=0.28490547003443756
- Mann-Whitney `doku_anomalisi_var`: U=143.0, p=0.3860525359978415
- Mann-Whitney `caries_any`: U=0.0, p=4.151258828802699e-06
- Mann-Whitney `infraokluzyon_var`: U=28.5, p=0.23217936357038793
- Kruskal `gen_group`: H=2.1121140552995348, p=0.7151471571581405, epsilon_sq=-0.0650995153344988
- Kruskal `dentisyon_donemi_kod`: H=28.995391705069135, p=5.055110938001226e-07, epsilon_sq=0.8708190872602947
- Kruskal `gen_kodu`: H=6.564832949308761, p=0.5842256554157927, epsilon_sq=-0.05740668202764954

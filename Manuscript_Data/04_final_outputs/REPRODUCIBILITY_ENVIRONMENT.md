# REPRODUCIBILITY_ENVIRONMENT

Bu dosya, FINAL.1.2 paketinin yeniden üretilebilirlik sınırlarını ve authoritative yürütme bağlamını açıklar.

## Authoritative analysis entry points

- `03_analysis_scripts/oi_oro_dental_master_FINAL_1_2.py`
- `03_analysis_scripts/oi_oro_dental_master_FINAL_1_2.ipynb`

## Authoritative figure entry points

- `03_analysis_scripts/make_figures_final_1_2.py`
- `03_analysis_scripts/make_figures_FINAL_1_2_TR.py`

## Determinism

Bu projede deterministik seed:
- `SEED = 20260228`

Determinism bilgisi ayrıca şu dosyalarda izlenebilir:
- `04_final_outputs/tables_csv_and_logs/run_manifest.json`
- `06_ai_handoff_context/copilot-instructions.md`
- `06_ai_handoff_context/python-analysis.instructions.md`

## Manifest bilgisi

`run_manifest.json` aşağıdaki bilgileri içerir:
- timestamp
- Python sürümü
- pandas sürümü
- global seed
- permütasyon iterasyonu
- bootstrap iterasyonu
- ana input dosyalarının hash bilgileri

## Bu paket neyi garanti eder?

- nihai CSV çıktıların authoritative yerini
- final script ve notebook’un hangi dosyalar olduğunu
- deterministik seed bilgisini
- hash tabanlı minimum provenance bilgisini

## Bu paket neyi tam garanti etmez?

- tam paket yöneticisi kilidi (requirements/lockfile)
- git commit hash’i
- her çıktı dosyasının ayrı hash’i

Bu nedenle paket güçlü reproducibility sunar, ancak tam environment pinning düzeyinde değildir.

## Tavsiye

Bir AI veya araştırmacı yeni bir üretim çalıştırması yapmadan önce:
1. `README_Manuscript_Data.md`
2. `06_ai_handoff_context/FINAL_HANDOFF_QUICKSTART.md`
3. `04_final_outputs/tables_csv_and_logs/run_manifest.json`
4. `03_analysis_scripts/oi_oro_dental_master_FINAL_1_2.py`
sırasını izlemelidir.
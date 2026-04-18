# FINAL.1.2 — Publication‑Ready Görsel Paketi

> **Paketleme notu:** Bu doküman tarihsel figür üretim planını korur. İçinde geçen `outputs_FINAL_1_2.zip` ve `PDF + PNG` önerileri üretim aşaması bağlamındadır. `Manuscript_Data` paketinde bilinçli olarak yalnız **CSV + PNG + MD + JSON** tutulur; bu nedenle burada anlatılan ZIP/PDF referansları authoritative package policy değil, üretim-provenance bilgisidir.

Bu doküman, FINAL.1.2 analiz çıktılarından **temiz, anlaşılır, profesyonel** figürleri deterministik ve fail‑fast şekilde üretmek için bir “figür planı” + “otomatik üretim scripti” sunar.

> Veri kaynağı: authoritative FINAL.1.2 CSV çıktıları. Script hem bir klasörden hem de tarihsel bir `.zip` arşivinden okuyabilir; `Manuscript_Data` içinde önerilen kullanım klasör girdisidir.

---

## 1) Figür seti (kongre + PI bilgilendirme)

### Kongre için minimum (3 figür)
1) **Figür A — Prevalans snapshot (Wilson CI)**
   - doku_anomalisi_var_rt, gingivitis, caries_any_rt (bar + CI)
   - infraoklüzyon prevalansı küçük not

2) **Figür B — Gen grubu dağılımı (N)**
   - Primary gene_group N (bar)

3) **Figür C — Inferential summary (Primary-only)**
   - effect size (CramerV / ε²_primary) + p_perm + Holm (dot plot)

### PI’ye detay paket (6 figür)
A+B+C’ye ek:
4) **Figür D — Outcome×Gene heatmap/bubble** (yüzde + n)
5) **Figür E — Robustness** (LOO p aralıkları + infra dışlama Δp)
6) **Figür F — CV doğrulama** (AUC age vs age+gene; ΔAUC CI; estimator etiketleri)

---

## 2) Publication-ready görsel kuralları

- **Format:** `Manuscript_Data` paketi içinde authoritative çıktı **PNG**'dir. Tarihsel üretim aşamalarında PDF düşünülmüş olsa da bu package sadeleştirilmiş biçimde yalnız PNG tutar.
- **Tek font, tek boyut standardı:** örn. 10–11 pt ana metin, 8–9 pt eksen label.
- **Az renk, yüksek kontrast:** bar/dot/CI çizgileri sade; mümkünse tek vurgu rengi.
- **Okunabilirlik:**
  - eksen başlıkları kısa
  - yüzde/CI etiketleri aşırı kalabalık olmayacak
  - legend minimum
- **Deterministik:** figür üretimi aynı girdide aynı çıktıyı vermeli.
- **Fail-fast:** beklenen kolon/satır yoksa dur ve hatayı açık yaz.

---

## 3) Fail-fast kontrol listesi (figür üretmeden önce)

Script şunları assert etmeli:
1) `publication_table3_inferential_FINAL.csv` içinde 4 endpoint var ve scenario=Primary.
2) `publication_table1_overall_FINAL.csv` içinde N=34.
3) `robustness_panel_FINAL.csv` içinde 4 endpoint var.
4) `cv_panel_FINAL.csv` içinde Primary scenario ve en az LOO+RSKF satırları var (3 endpoint × 2 method = 6 satır).

---

## 4) Otomatik figür üretim scripti (tek komut)

Aşağıdaki scripti repo köküne kaydet:
- `make_figures_final_1_2.py`

Çalıştır:
- Paket içinden önerilen kullanım:
    - `python 03_analysis_scripts/make_figures_final_1_2.py --input 04_final_outputs/tables_csv_and_logs --out 05_figures/english`
- Tarihsel alternatif kullanım:
    - `python make_figures_final_1_2.py --input outputs_FINAL_1_2.zip --out figures_FINAL_1_2`

> Not: Güncel script bir klasörden **veya** tarihsel bir zip arşivinden okuyabilir; `Manuscript_Data` paketinde zip tutulmadığı için önerilen yol klasör girdisidir.

```python
import argparse
import zipfile
import io
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

SEED = 20260228
np.random.seed(SEED)

REQ = {
    't1': 'publication_table1_overall_FINAL.csv',
    't2': 'publication_table2_by_gene_group_FINAL.csv',
    't3': 'publication_table3_inferential_FINAL.csv',
    'rob': 'robustness_panel_FINAL.csv',
    'cv': 'cv_panel_FINAL.csv',
}

PRIMARY_ENDPOINTS = [
    'doku_anomalisi_var_rt',
    'gingivitis',
    'caries_any_rt',
    'caries_count'
]

BINARY_ENDPOINTS = ['doku_anomalisi_var_rt','gingivitis','caries_any_rt']


def read_csv_from_zip(zf: zipfile.ZipFile, name: str) -> pd.DataFrame:
    with zf.open(name) as f:
        return pd.read_csv(f)


def fail(msg: str):
    raise RuntimeError(msg)


def ensure_dir(p: str):
    os.makedirs(p, exist_ok=True)


def setup_matplotlib():
    plt.rcParams.update({
        'figure.dpi': 150,
        'savefig.dpi': 300,
        'font.size': 10,
        'axes.titlesize': 11,
        'axes.labelsize': 10,
        'xtick.labelsize': 9,
        'ytick.labelsize': 9,
        'legend.fontsize': 9,
        'pdf.fonttype': 42,
        'ps.fonttype': 42,
    })


def qc_tables(t1, t2, t3, rob, cv):
    # Table1 N
    n_row = t1[t1['Variable'].astype(str).str.strip().eq('N')]
    if n_row.empty:
        fail('Table1: N row missing')
    if str(n_row.iloc[0]['Value']).strip() != '34':
        fail(f"Table1: expected N=34, got {n_row.iloc[0]['Value']}")

    # Table3 endpoints
    t3p = t3[t3['scenario'].eq('Primary')]
    if set(t3p['endpoint']) != set(PRIMARY_ENDPOINTS):
        fail(f"Table3: endpoints mismatch: {sorted(t3p['endpoint'].tolist())}")

    # Robustness endpoints
    robp = rob[rob['scenario'].eq('Primary')]
    if set(robp['endpoint']) != set(PRIMARY_ENDPOINTS):
        fail('Robustness: endpoints mismatch')

    # CV completeness
    cvp = cv[cv['scenario'].eq('Primary')]
    if set(cvp['endpoint']) != set(BINARY_ENDPOINTS):
        fail('CV: binary endpoints mismatch')
    if set(cvp['cv_method']) != set(['LOO','RSKF']):
        fail('CV: expected both LOO and RSKF')
    if len(cvp) != 6:
        fail(f"CV: expected 6 rows (3 endpoints×2), got {len(cvp)}")


def fig_prevalence(t1: pd.DataFrame, outdir: str):
    # Extract prevalence rows
    rows = ['doku_anomalisi_var_rt','gingivitis','caries_any_rt','Infraokluzyon (Total N)']
    df = t1[t1['Variable'].isin(rows)].copy()
    if df.shape[0] != 4:
        fail('Table1 prevalence rows missing for figure')

    # Parse "n (p%)" and CI "a, b"
    def parse_value(s):
        s = str(s)
        n = int(s.split('(')[0].strip())
        pct = float(s.split('(')[1].split('%')[0])
        return n, pct

    def parse_ci(s):
        s = str(s)
        if s.strip() == '-' or s.strip().lower() == 'nan':
            return np.nan, np.nan
        a,b = s.split(',')
        return float(a), float(b)

    df[['n','pct']] = df['Value'].apply(lambda x: pd.Series(parse_value(x)))
    df[['ci_l','ci_h']] = df['95% CI (Wilson)'].apply(lambda x: pd.Series(parse_ci(x)))

    # Plot
    labels = ['Tissue anomaly','Gingivitis','Any caries','Infraocclusion']
    x = np.arange(len(labels))
    y = df['pct'].values
    yerr = np.vstack([y - df['ci_l'].values, df['ci_h'].values - y])

    plt.figure(figsize=(6.5,3.5))
    plt.title('Prevalence (Wilson 95% CI)')
    plt.bar(x, y)
    plt.errorbar(x, y, yerr=yerr, fmt='none', capsize=4)
    plt.xticks(x, labels, rotation=0)
    plt.ylabel('Prevalence (%)')
    plt.ylim(0, 100)

    # annotate n
    for i,(n,p) in enumerate(zip(df['n'], df['pct'])):
        plt.text(i, min(98, p+3), f"n={n}", ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig(os.path.join(outdir,'FigA_prevalence.pdf'))
    plt.savefig(os.path.join(outdir,'FigA_prevalence.png'))
    plt.close()


def fig_gene_groups(t2: pd.DataFrame, outdir: str):
    df = t2[t2['scenario'].eq('Primary')].copy()
    if df.empty:
        fail('Table2: Primary scenario missing')

    # order by N desc
    df['N'] = df['N'].astype(int)
    df = df.sort_values('N', ascending=False)

    plt.figure(figsize=(6.0,3.2))
    plt.title('Gene group distribution (Primary)')
    plt.bar(df['gene_group'], df['N'])
    plt.ylabel('N')
    plt.xlabel('Gene group')
    for i,(g,n) in enumerate(zip(df['gene_group'], df['N'])):
        plt.text(i, n+0.2, str(n), ha='center', va='bottom', fontsize=9)
    plt.tight_layout()
    plt.savefig(os.path.join(outdir,'FigB_gene_groups.pdf'))
    plt.savefig(os.path.join(outdir,'FigB_gene_groups.png'))
    plt.close()


def fig_inferential_summary(t3: pd.DataFrame, outdir: str):
    df = t3[t3['scenario'].eq('Primary')].copy()
    df = df.set_index('endpoint').loc[PRIMARY_ENDPOINTS].reset_index()

    # Map effect sizes: binary uses CramerV; caries_count uses epsilon2_primary
    eff = []
    p = []
    holm = []
    label = []
    for _,r in df.iterrows():
        ep = r['endpoint']
        if ep == 'caries_count':
            eff.append(float(r['epsilon2_primary']))
            label.append('ε² (primary)')
            p.append(float(r['p_classic']))
            holm.append(float(r['p_holm_primary_family_classic']))
        else:
            eff.append(float(r['effect_size_value']))
            label.append('Cramer\'s V')
            p.append(float(r['p_permutation']))
            holm.append(float(r['p_holm_binary_family_perm']))

    names = ['Tissue anomaly','Gingivitis','Any caries','Caries count']
    x = np.array(eff)
    y = np.arange(len(names))

    plt.figure(figsize=(6.8,3.6))
    plt.title('Inferential summary (Primary)')
    plt.scatter(x, y)
    plt.yticks(y, names)
    plt.xlabel('Effect size (V or ε²)')

    for i in range(len(names)):
        plt.text(x[i] + 0.01, y[i], f"p_perm/p={p[i]:.3f} | Holm={holm[i]:.3f}", va='center', fontsize=8)

    plt.axvline(0, linewidth=1)
    plt.tight_layout()
    plt.savefig(os.path.join(outdir,'FigC_inferential_summary.pdf'))
    plt.savefig(os.path.join(outdir,'FigC_inferential_summary.png'))
    plt.close()


def fig_robustness(rob: pd.DataFrame, outdir: str):
    df = rob[rob['scenario'].eq('Primary')].set_index('endpoint').loc[PRIMARY_ENDPOINTS].reset_index()
    names = ['Tissue anomaly','Gingivitis','Any caries','Caries count']

    plt.figure(figsize=(7.0,3.6))
    plt.title('Robustness: LOO p-range and infra exclusion Δp')

    y = np.arange(len(names))
    plt.hlines(y, df['loo_p_min'], df['loo_p_max'])
    plt.scatter(df['p_base'], y, label='Base p')
    plt.scatter(df['infra_exclusion_p'], y, marker='x', label='Infra excluded p')
    for i in range(len(names)):
        plt.text(df['loo_p_max'].iloc[i] + 0.01, y[i], f"Δp_infra={df['infra_exclusion_delta_p'].iloc[i]:.3f}", va='center', fontsize=8)

    plt.yticks(y, names)
    plt.xlabel('p-value')
    plt.xlim(0, 1)
    plt.legend(loc='lower right')
    plt.tight_layout()
    plt.savefig(os.path.join(outdir,'FigE_robustness.pdf'))
    plt.savefig(os.path.join(outdir,'FigE_robustness.png'))
    plt.close()


def fig_cv(cv: pd.DataFrame, outdir: str):
    df = cv[cv['scenario'].eq('Primary')].copy()

    order = ['doku_anomalisi_var_rt','gingivitis','caries_any_rt']
    name_map = {
        'doku_anomalisi_var_rt':'Tissue anomaly',
        'gingivitis':'Gingivitis',
        'caries_any_rt':'Any caries'
    }

    plt.figure(figsize=(7.2,3.8))
    plt.title('Model verification: ΔAUC with 95% CI (Primary)')

    ytick = []
    y = []
    x = []
    xerr = []
    for i,ep in enumerate(order):
        for j,meth in enumerate(['LOO','RSKF']):
            r = df[(df['endpoint']==ep)&(df['cv_method']==meth)].iloc[0]
            y.append(i*2 + j)
            ytick.append(f"{name_map[ep]} — {meth}")
            x.append(float(r['delta_auc']))
            lo = float(r['delta_auc_ci_low'])
            hi = float(r['delta_auc_ci_high'])
            xerr.append([x[-1]-lo, hi-x[-1]])

    y = np.array(y)
    x = np.array(x)
    xerr = np.array(xerr).T

    plt.errorbar(x, y, xerr=xerr, fmt='o', capsize=4)
    plt.axvline(0, linewidth=1)
    plt.yticks(y, ytick)
    plt.xlabel('ΔAUC (age+gene − age)')
    plt.tight_layout()
    plt.savefig(os.path.join(outdir,'FigF_cv_delta_auc.pdf'))
    plt.savefig(os.path.join(outdir,'FigF_cv_delta_auc.png'))
    plt.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', required=True, help='Path to outputs_FINAL_1_2.zip')
    ap.add_argument('--out', required=True, help='Output directory for figures')
    args = ap.parse_args()

    setup_matplotlib()
    ensure_dir(args.out)

    with zipfile.ZipFile(args.input) as zf:
        for k,v in REQ.items():
            if v not in zf.namelist():
                fail(f"Missing required file in zip: {v}")

        t1 = read_csv_from_zip(zf, REQ['t1'])
        t2 = read_csv_from_zip(zf, REQ['t2'])
        t3 = read_csv_from_zip(zf, REQ['t3'])
        rob = read_csv_from_zip(zf, REQ['rob'])
        cv = read_csv_from_zip(zf, REQ['cv'])

        qc_tables(t1,t2,t3,rob,cv)

        fig_prevalence(t1, args.out)
        fig_gene_groups(t2, args.out)
        fig_inferential_summary(t3, args.out)
        fig_robustness(rob, args.out)
        fig_cv(cv, args.out)

    print('OK — figures generated')


if __name__ == '__main__':
    main()
```

---

## 5) Figür başlık/caption taslakları (kopyala‑yapıştır)

**Figür A.** Çalışma kohortunda doku anomalisi, gingivitis, caries_any ve infraoklüzyon prevalansı (Wilson %95 GA).

**Figür B.** Primary runtime gen gruplarına göre olgu dağılımı (N).

**Figür C.** Primary senaryo inferans özeti: binary uç noktalar için Cramer’s V ve permütasyon p-değeri + Holm düzeltmesi; caries_count için Kruskal–Wallis p ve ε² (primary).

**Figür E.** Robustluk analizi: leave‑one‑out p aralıkları ve infraoklüzyon hariç senaryoda p değişimi (Δp).

**Figür F.** Model tabanlı doğrulama: age-only vs age+gene modelleri için ΔAUC (LOO ve RSKF) ve %95 bootstrap GA.

---

## 6) Kongre slaytı için pratik kullanım

- Paket içindeki authoritative figürler PNG’dir.
- Sunum/manuscript içine doğrudan PNG dosyaları yerleştirilebilir.
- Tüm figürlerin sağ altına küçük bir “DATA: FINAL.1.2” etiketi ekle (sürüm izlenebilirliği).


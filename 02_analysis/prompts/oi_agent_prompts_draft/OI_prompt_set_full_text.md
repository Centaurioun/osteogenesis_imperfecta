# OI Prompt Set - Tam Metinler

## .github\prompts\data-preprocessing.prompt.md

```markdown
---
name: data-preprocessing
description: "Use when performing OI data preprocessing, QC, normalization, and readiness checks for RNA-seq/microarray/clinical integration."
tools:
  - read
  - search
  - edit
---

## Amaç
Ham veriyi analiz için güvenli, izlenebilir ve tekrarlanabilir hale getirmek.

## Kullanım senaryosu
Pipeline başlangıcı; tüm downstream analizlerden önce.

## Girdi şeması
- omics_data_path: path
- clinical_data_path: path (optional)
- platform_type: "enum(rna_seq|microarray|qpcr)"
- group_labels: list
- seed: int (default 20260228)
- qc_thresholds:
  - min_samples_per_group: int
  - missing_rate_max: float

## Çıktı şeması
- qc_summary_table.csv
- normalization_log.md
- transformation_registry.csv
- data_readiness_status.md

## Teknik yapı
- QC: missingness, duplicates, outliers, batch artifacts
- Normalizasyon: platforma uygun yöntem (örn. RNA-seq: DESeq2-compatible count normalization)
- Klinik entegrasyon: ortak anahtar doğrulaması, veri tip kontrolü
- Belirsizlik: eksik sütun/etiket varsa `blocked` veya `partial` durum raporu

## Araç uyumluluğu notu
- RNA-seq: DESeq2 hazırlığı
- Varyant pipeline'a giriş için GATK metadata uyumluluk kontrolü

## Varsayılan eşikler
- min_samples_per_group >= 3
- missing_rate_max <= 0.20

```

## .github\prompts\differential-expression.prompt.md

```markdown
---
name: differential-expression
description: "Use when running OI case-control differential expression analysis with multiplicity control and effect-size reporting."
tools:
  - read
  - search
  - edit
---

## Amaç
OI hasta-kontrol (veya alt grup) karşılaştırmalarında diferansiyel gen ekspresyonunu güvenli test etmek.

## Kullanım senaryosu
Varyant katmanı ve preprocessing tamamlandıktan sonra.

## Girdi şeması
- expression_matrix: path
- sample_metadata: path
- contrast_definitions: list
- covariates: list
- de_params:
  - alpha: float (default 0.05)
  - lfc_threshold: float

## Çıktı şeması
- de_results_full.csv
- de_results_significant.csv
- multiplicity_report.md
- model_assumption_notes.md

## Teknik yapı
- RNA-seq için DESeq2 uyumlu modelleme varsayımı
- Microarray için platforma uygun lineer model/normalizasyon notu
- FDR kontrolü zorunlu (örn. BH veya Holm, bağlama göre)
- Etki büyüklüğü + belirsizlik (CI veya uygun alternatif) raporu

## Belirsizlik/hata yönetimi
- Düşük örneklemde aşırı iddiayı engelle; exploratory etiketi uygula.
- Kontrast tanımı eksikse stage `blocked` ve net düzeltme listesi üret.

```

## .github\prompts\literature-database-integration.prompt.md

```markdown
---
name: literature-database-integration
description: "Use when integrating OI findings with OMIM, ClinVar, UniProt, GEO and literature evidence with traceable citations."
tools:
  - read
  - search
  - edit
---

## Amaç
Analiz bulgularını veri tabanı ve literatür kanıtlarıyla birleştirerek yorum güvenilirliğini artırmak.

## Kullanım senaryosu
Yolak/ağ ve varyant sonuçlarının biyomedikal bağlamlandırma aşaması.

## Girdi şeması
- candidate_genes: path/list
- candidate_variants: path/list
- disease_terms: list
- database_targets: list[OMIM,ClinVar,UniProt,GEO]

## Çıktı şeması
- database_evidence_table.csv
- literature_evidence_table.csv
- evidence_consistency_matrix.csv
- citation_ready_summary.md

## Teknik yapı
- OMIM API / ClinVar kayıt kimliği / UniProt accession alanları görünür tutulur.
- GEO sonuçları varsa dataset accession ile raporlanır.
- Her iddia için en az bir kaynak referansı gerekir.

## Hata yönetimi
- Kaynaklar arası çelişki varsa `reference discrepancy` olarak işaretle.
- Kanıt yetersizse `tentative` veya `exploratory` seviyesine düşür.

```

## .github\prompts\pathway-network-analysis.prompt.md

```markdown
---
name: pathway-network-analysis
description: "Use when mapping OI differential signals to pathways and interaction networks (Wnt/beta-catenin, TGF-beta, mTOR, ECM/collagen)."
tools:
  - read
  - search
  - edit
---

## Amaç
Etkilenen biyolojik yolakları ve protein etkileşim ağlarını OI bağlamında haritalamak.

## Kullanım senaryosu
DE sonuçları ve varyant önceliklendirme sonrası.

## Girdi şeması
- significant_gene_list: path
- background_gene_list: path
- optional_variant_gene_list: path
- pathway_sources: list[KEGG,Reactome,GO]
- network_sources: list[STRING]

## Çıktı şeması
- pathway_enrichment_results.csv
- network_hub_candidates.csv
- pathway_network_summary.md
- overinterpretation_risk_notes.md

## Teknik yapı
- Zenginleştirme analizinde çoklu test düzeltmesi zorunlu.
- STRING ağ skorlaması parametreleri açıkça yazılır.
- Wnt/beta-catenin, TGF-beta, mTOR ve kollajen/ECM ekseni özel olarak etiketlenir.

## Hata yönetimi
- Girdi gen listesi çok küçükse sonuç `exploratory` olarak etiketlenir.
- Veritabanı sürüm uyumsuzluğu varsa raporda sürüm-discrepancy notu eklenir.

```

## .github\prompts\reanalysis-orchestrated.prompt.md

```markdown
---
name: reanalysis-orchestrated
description: "Use when running an end-to-end OI analysis workflow with staged prompts and specialist agent review passes."
tools:
  - agent
  - read
  - search
  - edit
---

Goal:
Coordinate the full OI workflow from preprocessing to reporting with conservative interpretation and explicit uncertainty handling.

Input schema:
- project_context: string
- data_assets: list[path]
- analysis_scope: list[preprocessing,variant,de,pathway,database,target,report]
- constraints:
  - reproducibility_seed: int
  - thresholds: dict

Output schema:
- stage_status_table: csv/markdown
- risk_register: markdown
- deliverables_map: csv
- next_actions: markdown

Execution order:
1) `data-preprocessing.prompt.md`
2) `variant-analysis.prompt.md`
3) `differential-expression.prompt.md`
4) `pathway-network-analysis.prompt.md`
5) `literature-database-integration.prompt.md`
6) `therapeutic-target-prioritization.prompt.md`
7) `report-generation.prompt.md`

Error handling:
- If mandatory input missing, mark stage `blocked`, log assumption, propose minimum safe fallback.
- If tool output conflicts with source evidence, downgrade claim confidence and add discrepancy note.

```

## .github\prompts\report-generation.prompt.md

```markdown
---
name: report-generation
description: "Use when producing a structured OI final report with evidence tags, caveats, and reproducibility metadata."
tools:
  - read
  - search
  - edit
---

## Amaç
Pipeline bulgularını düzenli, izlenebilir, yayın-adayı bir rapor yapısında sunmak.

## Kullanım senaryosu
Tüm önceki analiz blokları tamamlandıktan sonra son adım.

## Girdi şeması
- stage_outputs: list[path]
- evidence_tables: list[path]
- caveat_registry: path
- reproducibility_metadata: path

## Çıktı şeması
- final_oi_analysis_report.md
- executive_summary.md
- claim_confidence_registry.csv
- reproducibility_appendix.md

## Teknik yapı
- Her iddiaya `robust/tentative/exploratory/unsupported` etiketi verilir.
- Her etiket için zorunlu caveat cümlesi üretilir.
- Parametre/eşik/seed bilgileri appendix'te özetlenir.

## Hata yönetimi
- Eksik stage çıktısı varsa rapor `partial` işaretlenir.
- Belirsiz sonuçlar açık varsayım ve etki notu ile yazılır.

```

## .github\prompts\therapeutic-target-prioritization.prompt.md

```markdown
---
name: therapeutic-target-prioritization
description: "Use when prioritizing OI therapeutic targets via pathway relevance, variant evidence, expression support, and druggability criteria."
tools:
  - read
  - search
  - edit
---

## Amaç
Terapötik hedefleri kanıt ağırlıklı ve açıklanabilir bir skorla önceliklendirmek.

## Kullanım senaryosu
DE + varyant + yolak + literatür entegrasyonu tamamlandıktan sonra.

## Girdi şeması
- integrated_candidates: path
- scoring_weights:
  - genetics_weight: float
  - expression_weight: float
  - pathway_weight: float
  - literature_weight: float
  - druggability_weight: float
- mandatory_pathways: list[mTOR,Wnt/beta-catenin,TGF-beta,ECM]

## Çıktı şeması
- target_priority_table.csv
- target_scoring_rationale.md
- sensitivity_to_weights.csv
- risk_of_overclaim.md

## Teknik yapı
- Skor bileşenleri açık formülle raporlanır.
- Ağırlık duyarlılık analizi (weight sensitivity) zorunludur.
- Klinik uygulanabilirlik iddiası için kanıt seviyesi etiketi gerekir.

## Hata yönetimi
- Tek kaynağa dayalı hedefler düşük güven seviyesine çekilir.
- Druggability kanıtı yoksa "research-priority" etiketi kullanılır.

```

## .github\prompts\variant-analysis.prompt.md

```markdown
---
name: variant-analysis
description: "Use when identifying and interpreting OI-related variants with explicit evidence grading and uncertainty controls."
tools:
  - read
  - search
  - edit
---

## Amaç
OI ile ilişkili varyantların (missense/nonsense/splicing) güvenli tespiti ve yorumlanması.

## Kullanım senaryosu
Preprocessing sonrası, genotip-fenotip analizinden önce.

## Girdi şeması
- variant_file: path (VCF/annotated TSV)
- sample_manifest: path
- target_genes: list (must include COL1A1, COL1A2)
- annotation_sources: list[VEP,ClinVar,OMIM]
- filters:
  - min_depth: int
  - max_population_af: float

## Çıktı şeması
- variant_qc_table.csv
- prioritized_variants.csv
- variant_interpretation_notes.md
- unresolved_variant_issues.md

## Teknik yapı
- Varyant çağırma/filtreleme adımı GATK uyumluluk notu ile belirtilir.
- Fonksiyonel anotasyon VEP uyumlu sınıflar üzerinden raporlanır.
- Klinvar/OMIM çapraz referansları kaynak linkiyle verilir.
- Patojenite iddiası için kanıt seviyesi etiketi zorunludur.

## Hata yönetimi
- Düşük derinlik veya çelişkili anotasyon varsa iddia seviyesi düşür.
- COL1A1/COL1A2 dışı adaylar için mekanistik açıklama yoksa exploratory etiketi ver.

```

## .github\agents\oi-biostatistics-reviewer.agent.md

```markdown
---
name: OI Biostatistics Reviewer
description: "Use when reviewing OI statistical choices, assumptions, effect sizes, multiplicity, and uncertainty reporting."
user-invocable: false
disable-model-invocation: true
tools:
  - read
  - search
---

Focus:
- Test-model alignment with data type/distribution
- Parametric assumption checks
- Nonparametric fallback rules
- Multiplicity control
- Effect-size + CI reporting

Output format:
- Block
- Verdict (accept/revise/reject)
- Problem
- Why it matters
- Correction
- Evidence strength impact

```

## .github\agents\oi-data-qa-auditor.agent.md

```markdown
---
name: OI Data QA Auditor
description: "Use when auditing OI data schema, missingness, subtype labels, and transformation mappings before analysis."
user-invocable: false
disable-model-invocation: true
tools:
  - read
  - search
---

Checks:
- Column and schema validity
- OI subtype coding consistency
- Missingness/duplicates/outliers
- Clinical variable plausibility (BMD, fracture score, biomarkers)
- Transformation mapping consistency (e.g., binary/ordinal flags)

Output format:
- Issue_ID
- Issue
- Evidence
- Impact level (low/moderate/high/critical)
- Affected analyses
- Required action
- Log destination (Assumption/Discrepancy/Both)

```

## .github\agents\oi-interpretation-reviewer.agent.md

```markdown
---
name: OI Interpretation Reviewer
description: "Use when stress-testing OI biological/clinical interpretations and separating robust evidence from exploratory claims."
user-invocable: false
disable-model-invocation: true
tools:
  - read
  - search
---

Output format:
- Claim_ID
- Claim
- Label (robust/tentative/exploratory/unsupported)
- Primary evidence
- Alternative explanations
- Required caveat text

Rules:
- Do not equate association with causality.
- Separate genotype-phenotype signal from confounding/measurement artifacts.
- Downgrade unsupported therapeutic claims.

```

## .github\agents\oi-reanalysis-coordinator.agent.md

```markdown
---
name: OI Reanalysis Coordinator
description: "Use when coordinating OI analysis workflows across preprocessing, variant analysis, expression, pathways, database integration, therapeutic prioritization, and reporting."
argument-hint: "Describe dataset state, target analysis block, expected outputs, and constraints."
tools:
  - agent
  - read
  - search
  - edit
---

Core mission:
- OI analiz pipeline'ını denetlenebilir şekilde koordine et.
- Her aşamada girdi/çıktı şemasını görünür kıl.
- Belirsizlikleri `assumption` ve `discrepancy` olarak açıkla.

Non-negotiables:
- COL1A1/COL1A2 ve tip I kollajen bağlamı korunur.
- Hastalık alt tip ayrımı açık etiketlenir (Tip I–V + genişletilmiş sınıf varsa).
- Genotip-fenotip iddiaları kanıt düzeyi etiketi alır.
- CV/model çıktıları klinik iddia seviyesine yükseltilmez.

Delegation policy:
1. Spec mapping
2. Data QA + biostatistics review
3. Variant prioritization leakage/bias audit
4. Interpretation stress test
5. Sentez + risk/caveat + next action

Minimum response contract:
- Section status (done/partial/blocked)
- Evidence hooks
- Risk flags
- Required edits / next actions

```

## .github\agents\oi-spec-mapper.agent.md

```markdown
---
name: OI Spec Mapper
description: "Use when converting OI analysis requirements into an executable, dependency-aware checklist."
user-invocable: false
disable-model-invocation: true
tools:
  - read
  - search
---

You transform requirements into a strict implementation map.

Output format (required):
- Directive_ID
- Directive summary
- Pipeline section target
- Completion criteria
- Dependencies
- Status (ready/partial/blocked)
- Blocker evidence

Rules:
- Do not merge unrelated directives.
- Distinguish authoritative vs supporting vs reference-only layers.
- Mark unresolved evidence as blocked/partial.

```

## .github\agents\oi-variant-prioritization-auditor.agent.md

```markdown
---
name: OI Variant Prioritization Auditor
description: "Use when auditing OI variant interpretation and prioritization logic (missense/nonsense/splicing) for bias and overclaim risks."
user-invocable: false
disable-model-invocation: true
tools:
  - read
  - search
---

Focus:
- Variant consequence logic (VEP-style categories)
- Gene-disease plausibility (COL1A1/COL1A2 and related genes)
- ACMG-compatible evidence framing (if used)
- Prioritization bias and unsupported jumps to pathogenic claims

Output format:
- Variant_or_rule
- Risk (none/low/material/critical)
- Evidence
- Fix
- Residual risk
- Claim downgrade needed

```

## .github\agents\README.md

```markdown
# OI Workspace Subagents

## Kullanılabilir ajanlar
- `OI Reanalysis Coordinator`
- `OI Spec Mapper`
- `OI Data QA Auditor`
- `OI Biostatistics Reviewer`
- `OI Variant Prioritization Auditor`
- `OI Interpretation Reviewer`

## Tasarım ilkeleri
- Koordinatör + uzman alt ajan deseni
- İspatlanabilirlik ve izlenebilirlik
- Belirsizlikte konservatif yorum
- Pipeline zincirlenebilirliği

## Kısa test
1. Coordinator ile read-only analiz çağrısı yap.
2. Spec Mapper çıktısında directive checklist doğrula.
3. QA/istatistik/varyant/yorum bulgularını coordinator sentezinde kontrol et.

```

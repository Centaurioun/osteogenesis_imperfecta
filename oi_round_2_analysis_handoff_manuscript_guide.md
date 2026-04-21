# OI Round-Two Analysis Handoff and Manuscript Guidance

## Purpose of this handoff

This document is the manuscript-facing handoff for the **post-advisor round-two OI oral-dental reanalysis**. It is designed to let the writing phase proceed without repeatedly reopening the full cleanup, replication, and repo-organization history.

It summarizes:
- what changed before round two,
- what the round-two package now means,
- what the main results are,
- how those results should be interpreted,
- how they should **not** be interpreted,
- and how to write the manuscript conservatively and correctly.

This is a **writing and interpretation handoff**, not a new analysis plan and not a request to reopen the cleanup workflow.

---

## 1. Current authority model for writing

### 1.1 Primary manuscript-facing authority
Use **`04_manuscript/`** as the primary manuscript-facing working zone.

That zone now contains:
- manuscript-facing round-two reports,
- manuscript-facing tables,
- semantic-control context,
- provenance notes,
- baseline comparison pointers,
- and trace links to code and machine outputs.

### 1.2 Baseline and provenance materials
The following remain preserved as **baseline / comparison / provenance** materials rather than manuscript-facing authority:
- `03_outputs/active/outputs_FINAL_1_2/`
- `03_outputs/active/figures_FINAL_1_2/`
- `03_outputs/active/figures_FINAL_1_2_TR/`
- `Manuscript_Data/`

### 1.3 Reconciled round-two provenance source
The reconciled round-two run source remains under the Colab-derived report folder and supports the manuscript-facing package.

### 1.4 Provisional / superseded round-two provenance
The non-reconciled round-two run folder is preserved for traceability but is **not** manuscript-facing authority.

### 1.5 Operational bundle mirror
The Colab bundle remains operational-only and should not be treated as manuscript authority.

### 1.6 Writing rule
For drafting:
- start from `04_manuscript/`,
- use trace/provenance materials only as support,
- and do not pull manuscript claims from provisional folders or bundle mirrors.

---

## 2. What changed before round two

Round two was not a cosmetic rerun. It was a **semantically revised reanalysis** based on the post-advisor clarification layer.

The most important changes were the following.

### 2.1 Angle-class handling
- `angle_sinifi_clean` became the primary Angle analysis variable.
- It is restricted to Angle I / II / III only.
- The infraocclusion case is **not** forced into Angle I / II / III.
- Infraocclusion is handled separately through `infraokluzyon_var_clean`.

### 2.2 Caries variable framing
- `dmft_dmft` is treated as a **count-like total caries burden field**.
- The analysis-facing alias is `caries_count_total`.
- `caries_any` is derived as presence/absence from the same field.
- The variable should **not** be described as a clean standard split DMFT/dmft construct.

### 2.3 Doku anomalisi handling
- `doku_anomalisi_any` is the preferred anomaly endpoint.
- `doku_anomalisi_dominant_type` is secondary only.
- The field should not be written as a full multi-label phenotype spectrum.

### 2.4 DI handling
- `di_any`, if used, is presence/absence only.
- No Shields subtype or severity interpretation should be attempted.

### 2.5 Binary-only clinical variables
The following are yes/no variables only and should not be written as severity scales:
- gingivitis
- overjet
- overbite
- open bite
- crossbite

### 2.6 Small-sample discipline
The round-two workflow applied a stricter small-N logic, including:
- sparse-cell awareness,
- permutation/exact-oriented logic for binary outcomes,
- effect-size discipline,
- multiple-comparison discipline,
- leave-one-out robustness review,
- and stronger caveat language.

### 2.7 Practical meaning of the revision
The revision changed:
- variable interpretation,
- endpoint feasibility,
- inferential framing,
- and the boundaries of what can be claimed.

It did **not** turn a weak dataset into a strong one. It made the analysis **cleaner, stricter, and more defensible**.

---

## 3. Round-two cohort summary

### 3.1 Cohort size
- **N = 34**

### 3.2 Age summary
- Mean age: **10.47** years
- SD: **5.33**
- Range: **2–18** years

### 3.3 Gene-group distribution
- **P3H1:** 8
- **FKBP10:** 8
- **COL1A2:** 7
- **COL1A1:** 6
- **Other:** 5

### 3.4 Dentition-stage distribution
- Stage 1: **8**
- Stage 2: **14**
- Stage 3: **12**

### 3.5 Endpoint prevalences
- `doku_anomalisi_any`: **10/34** (**29.4%**)
- `gingivitis`: **11/34** (**32.4%**)
- `caries_any`: **24/34** (**70.6%**)
- `infraokluzyon_var_clean`: **1/34** (**2.9%**)

### 3.6 Caries burden summary
- Mean `caries_count_total`: **3.09**
- Median: **1.5**
- SD: **3.90**
- Range: **0–14**

### 3.7 Immediate descriptive reading
The cohort is small, clinically heterogeneous, and sparse in several endpoint families. That fact is not a minor limitation; it is central to how the results should be interpreted.

---

## 4. Core round-two inferential results

The central round-two result is **not** a dramatic positive finding. It is a more semantically disciplined reanalysis that does **not** materially overturn the overall study story.

### 4.1 Binary endpoints
#### `doku_anomalisi_any`
- permutation p = **0.0926**
- effect size was not trivial in magnitude, but the result did **not** meet conventional significance

#### `gingivitis`
- permutation p = **0.7604**
- no meaningful inferential signal

#### `caries_any`
- permutation p = **0.0761**
- suggestive / borderline at best, but **not significant**

### 4.2 Count endpoint
#### `caries_count_total`
- Kruskal-Wallis p = **0.2568**
- no significant group difference detected

### 4.3 Infraocclusion
- Only one case was present.
- This is a descriptive observation, not a viable inferential family for manuscript-level claims.

### 4.4 Bottom-line statistical reading
Across the primary round-two endpoint families, the data do **not** support a strong, stable genotype-group association claim.

That is not a failure of writing. That is the actual analytic result.

---

## 5. Robustness interpretation

A critical feature of round two is that the results were not accepted at face value just because a p-value appeared close to a threshold.

### 5.1 Leave-one-out behavior
For key endpoints such as anomaly and caries presence, leave-one-out checks showed that p-values could shift meaningfully depending on which subject was removed.

This implies:
- the results are **fragile**, not stable,
- near-threshold patterns should be written cautiously,
- and no borderline finding should be turned into a strong genotype-phenotype claim.

### 5.2 What robustness means here
The robustness layer does **not** prove that an association exists.
It shows how sensitive the signal is to small perturbations in an already small dataset.

### 5.3 Practical writing implication
Use the robustness layer to justify **cautious interpretation**, not to rescue non-significant findings.

Good framing:
- “a possible signal that did not remain strong enough for confident inference”
- “suggestive but unstable”
- “compatible with a pattern, but not robust enough for firm conclusion”

Bad framing:
- “almost significant, therefore likely real”
- “clinically meaningful despite non-significance” without additional justification
- “evidence of association” when the robustness layer is clearly fragile

---

## 6. Comparison to round one / canonical outputs

The round-two package should be understood as a **semantic refinement and reanalysis**, not as a repudiation of everything that came before.

### 6.1 What round two changed
Round two changed:
- variable handling,
- endpoint discipline,
- small-sample inferential logic,
- interpretation boundaries,
- and documentation quality.

### 6.2 What round two did not do
Round two did **not** produce a clearly new biologic story.
It did **not** generate robust new positive associations.
It did **not** justify expansive causal or mechanistic claims.

### 6.3 Most defensible overall comparison statement
A strong global summary is:

> The post-advisor round-two reanalysis materially improved semantic validity, endpoint handling, and inferential discipline, but it did not generate robust new positive associations. The revised results are best interpreted as a more defensible and more conservative version of the study rather than a biologically overturned study narrative.

### 6.4 What not to say
Do not write:
- that round two “validated” the original results in a strong sense,
- that round one was “wrong” in a blanket sense,
- or that semantic revision “proved” the earlier analysis invalid.

The fairest claim is that round two provides a **cleaner and more trustworthy analytic framing**.

---

## 7. Recommended manuscript interpretation

### 7.1 Overall interpretive stance
The manuscript should adopt a **conservative, evidence-disciplined, small-sample-aware tone**.

The central message should be:
- semantic clarification matters,
- endpoint definitions matter,
- small-sample robustness matters,
- and once these are handled carefully, the data do not support strong genotype-group claims for the core round-two endpoints.

### 7.2 What can be claimed with confidence
You can confidently say:
- the round-two workflow used revised post-advisor semantic rules,
- the cohort was reanalyzed under stricter endpoint definitions,
- inferential testing was made more appropriate for sparse and small-sample data,
- no primary endpoint produced strong statistically robust evidence of group differences,
- and any near-threshold patterns remained unstable and should be interpreted cautiously.

### 7.3 What should be framed as tentative
These belong in tentative language:
- anomaly-related signal,
- caries-presence signal,
- and any descriptive cross-gene pattern that looks interesting but is not stable enough inferentially.

### 7.4 What should not be claimed
Do not claim:
- a definitive genotype effect on anomaly or caries outcomes,
- a validated association for infraocclusion,
- severity gradations that were not actually measured,
- mechanistic biological explanations that go beyond the data,
- or strong predictive relevance from supportive robustness or CV-style outputs.

### 7.5 Null-result discipline
Do not write as if “non-significant” means “no difference exists.”
But do not write as if “borderline” means “probably real.”
The correct position is narrower:

- the observed data did not support a robust inferential claim,
- and the small, sparse structure limits how strongly the pattern can be interpreted.

---

## 8. Section-by-section writing guidance

### 8.1 Methods
In Methods, emphasize:
- that a post-advisor semantic revision was applied before round-two analysis,
- the distinction between Angle class and infraocclusion,
- the count-like handling of total caries burden,
- binary handling of selected clinical variables,
- use of sparse-data-aware / exact-permutation-oriented logic,
- effect-size and multiplicity discipline,
- and feasibility downgrades for endpoints that were not inferentially viable.

Methods should make it clear that round two was a **versioned, semantically revised reanalysis**, not a casual rerun.

### 8.2 Results
In Results:
- start with cohort and prevalence summaries,
- state the main inferential outcomes plainly,
- separate descriptive findings from inferential conclusions,
- state when an endpoint was feasible only descriptively,
- and report the lack of robust positive findings without apology.

Do not over-dramatize negative findings. They are part of the actual result.

### 8.3 Discussion
In Discussion:
- frame round two as an improvement in semantic and methodological rigor,
- explain that stricter handling narrowed some earlier interpretive room,
- acknowledge that some signals were suggestive but unstable,
- emphasize the small sample and sparse structure,
- avoid overextending into mechanistic speculation,
- and discuss how semantic ambiguity in rare-disease clinical datasets can materially affect inference.

This conceptual point is one of the strongest contributions of the work.

### 8.4 Conclusion
The conclusion should be narrow.
A better conclusion is closer to:

> Under a semantically revised and methodologically stricter round-two reanalysis, the dataset did not provide robust evidence for strong genotype-group differences across the primary oral-dental endpoints, although some descriptive and borderline patterns may justify cautious future study in larger or more structured cohorts.

---

## 9. Recommendations for tables and figures

### 9.1 Core tables to foreground
The manuscript-facing package should prioritize:
- a cohort summary table,
- the primary results table,
- and, if useful, one compact comparison table showing round-one vs round-two interpretive differences.

### 9.2 What not to overload the main text with
Do not overload the main text with:
- every robustness output,
- every sensitivity run,
- every trace artifact,
- or every internal version comparison.

Those belong in supplement/supporting material or the trace layer, not in the core argument of the paper.

### 9.3 Figure guidance
At present, there is **no surfaced validated round-two figure set** in the manuscript package.

So for manuscript preparation:
- do not pretend there is already an approved round-two figure package,
- use tables and narrative summaries as the main reporting backbone,
- and only surface figures later if a genuinely manuscript-ready round-two figure set is intentionally created and approved.

---

## 10. Recommended claim language

### 10.1 Use language like:
- “did not show robust evidence of”
- “suggestive but unstable”
- “descriptive difference without inferential confirmation”
- “not feasible for reliable inference under the observed data structure”
- “interpretation should remain cautious given small sample size and sparse cells”
- “semantic clarification changed the inferential framing more than it changed the overall biological story”

### 10.2 Avoid language like:
- “proved”
- “confirmed”
- “demonstrated” when referring to borderline or fragile findings
- “strong association” unless the evidence truly supports it
- “almost significant” as a surrogate for evidence
- “trend toward significance” unless its limits and instability are made explicit

### 10.3 Safe sentence templates
Useful templates include:
- “The reanalysis did not provide robust evidence for …”
- “Although a possible pattern was observed, the result remained unstable under sensitivity review.”
- “Given the small sample and sparse cell structure, this finding should be interpreted cautiously.”
- “This endpoint was more informative descriptively than inferentially in the present dataset.”

---

## 11. Recommended narrative backbone for the paper

A strong manuscript backbone would be:

1. Rare-disease oral-dental datasets are vulnerable to semantic ambiguity.
2. Post hoc clarification changed key variable handling rules.
3. A semantically revised round-two reanalysis was therefore necessary.
4. Under stricter endpoint definitions and small-sample methods, the data did not support strong robust associations for the primary endpoints.
5. The main contribution is therefore not a sensational new signal, but a more defensible analytic interpretation and a clearer model for handling semantically fragile clinical datasets.

This is a real contribution. Do not undersell it just because the results are not strongly positive.

---

## 12. Source hierarchy for writing

### 12.1 Use first
Start from:
- `04_manuscript/README.md`
- `04_manuscript/authority/manuscript_authority_index.md`
- the final reconciled round-two report,
- the primary results table,
- the baseline comparison report,
- and the semantic-control documents surfaced into `04_manuscript/context/semantic_control/`.

### 12.2 Use as support only
Use as support, not as front-facing manuscript sources:
- trace files,
- manifests,
- robustness tables,
- original run folders,
- baseline package folders,
- operational bundles.

### 12.3 Writing rule
If a claim sounds stronger than what the manuscript-facing round-two package supports, downgrade the claim rather than searching for auxiliary materials to rescue it.

---

## 13. Recommended next steps

1. Draft Methods and Results directly from the round-two manuscript-facing package.
2. Use the comparison report to sharpen Discussion, not to over-dramatize disagreement.
3. Keep the conclusion narrow and evidence-led.
4. Delay any figure package creation until there is a deliberate manuscript-ready figure decision.
5. Treat `04_manuscript/` as the sole starting point for writing.
6. Use baseline/provenance materials only when comparison or historical explanation is truly needed.

---

## 14. Bottom-line adjudication

The round-two reanalysis should be presented as:
- **semantically improved**,
- **methodologically stronger**,
- **more conservative**,
- and **more trustworthy for manuscript interpretation**.

Its main value is not that it discovered a dramatic new positive result.
Its main value is that it provides a cleaner and more defensible account of what this dataset can and cannot support.

That is the correct writing posture for the manuscript.


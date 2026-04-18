# SECTION_SPECIFIC_MANUSCRIPT_PROMPTS

This file contains section-specific prompts for drafting the manuscript in a new AI session. These prompts are designed for a **two-system workflow**:

1. an AI session that can inspect the zipped `Manuscript_Data` package,
2. a separate NotebookLM workflow that will answer targeted literature questions with in-text-cited responses,
3. a later drafting pass that uses both the package and those returned NotebookLM answers.

## Common execution protocol for every section

Before using any section prompt, the AI should internally follow this workflow:

1. Open and inspect the zipped `Manuscript_Data` package.
2. Read `README_Manuscript_Data.md`, `ANALYSIS_RESULT_MAP.csv`, `FILE_REGISTRY.csv`, and `06_ai_handoff_context/FINAL_HANDOFF_QUICKSTART.md` first.
3. Identify which files are authoritative FINAL.1.2 sources and which are archival/provenance-only.
4. Determine which section-specific claims require external literature support.
5. Generate targeted questions for NotebookLM instead of assuming direct access to the literature notebooks.
6. If NotebookLM answers are later pasted back into the session, treat those returned answers as the usable literature evidence.
7. If an existing manuscript draft, canvas, or partial section text is also provided in the session, review it before drafting and preserve any already-valid content while improving weak or unsupported claims.
8. Draft only the requested section unless explicitly asked to do more.

## General use principle

These prompts are intentionally separated by section. This is preferable to using one very large prompt for the full manuscript because:

- each section has a different evidentiary burden,
- the Introduction depends most heavily on external literature synthesis,
- the Methods must remain tightly bound to the actual study workflow and package files,
- the Results must remain anchored to the study outputs rather than drifting into literature review,
- the Discussion must explicitly separate study findings from literature-based interpretation.

Because the drafting AI may **not** have direct access to the NotebookLM notebooks, these prompts are written to support a staged process:

- first identify what literature evidence is needed,
- then generate high-yield questions for NotebookLM,
- then draft from the returned NotebookLM answers plus the package files.

## Global rules to prepend mentally for every section

Use these rules regardless of section:

- First open and inspect the zipped `Manuscript_Data` package.
- Treat `FINAL.1.2` as the authoritative final analysis version.
- Use the package files as the source of truth for study-specific methods and results.
- Use NotebookLM **indirectly**: generate questions for NotebookLM, then use the returned NotebookLM answers with in-text citations as the source of literature support.
- Follow this source hierarchy whenever conflict occurs:
  1. authoritative FINAL.1.2 package files for study-specific facts,
  2. returned NotebookLM answers with in-text citations for external evidence and interpretation,
  3. existing draft text only if it is consistent with 1 and 2.
- Do not invent claims, citations, prevalence estimates, mechanisms, or interpretations.
- If a claim is not directly supported by the package or the returned NotebookLM answers, either soften it or state that support is insufficient.
- Prefer explicit literature-backed statements over generic academic filler.
- Keep study-specific findings separate from literature-derived background.
- Do not fabricate bibliographic citations. If NotebookLM returns citation metadata, use it. If it does not, keep the statement evidence-based but explicitly flag it for later citation insertion.
- Do not let literature rewrite study-specific numbers, analysis choices, endpoint definitions, or the meaning of package-specific variables.
- Respect the following critical rules from the package:
  - `occl_tip == 4` means infraocclusion, not Angle class.
  - `dmft_dmft` is interpreted in this project as a count-like variable, not a classical parsed DMFT index.
  - small-sample constraints matter; permutation logic, non-parametric tests, Holm correction, and effect sizes are central.
- If literature is conflicting, say so clearly rather than forcing consensus.
- If literature support is weak, explicitly identify the claim as tentative.
- Avoid filler such as broad, generic, textbook-style overview sentences unless they are needed for readability and can be supported.
- Prefer concise, evidence-dense prose over decorative academic language.
- If NotebookLM answers are not yet available, do not pretend to have performed the literature synthesis. Instead, output a literature-question set and clearly mark the draft as pending literature completion when applicable.

## Common output discipline

For every section prompt:

- write only the requested section,
- keep section boundaries strict,
- separate study evidence from literature evidence,
- flag claims that need later citation verification,
- avoid adding claims just to make the prose sound more scholarly.
- When literature support is required but not yet supplied back from NotebookLM, output the question set first and avoid unsupported prose.

## NotebookLM question design standards

Whenever the AI is asked to generate questions for NotebookLM, the questions should be:

- specific rather than broad,
- answerable from literature rather than from the local package,
- framed so NotebookLM can return **in-text-cited** answers,
- organized by theme,
- prioritized so the most manuscript-critical questions are answered first,
- written to reduce the risk of generic textbook summaries.

Each NotebookLM question should ideally ask for one or more of the following when relevant:

- the current state of evidence,
- the direction and strength of prior findings,
- whether evidence is consistent, mixed, or sparse,
- whether pediatric or OI-specific evidence exists,
- methodological caveats or limitations in prior studies,
- citation-rich support for a precise manuscript claim.

Whenever useful, questions should explicitly ask NotebookLM to:

- distinguish well-established evidence from tentative evidence,
- identify disagreement across studies,
- avoid unsupported mechanistic speculation,
- provide compact, manuscript-usable answers rather than long educational summaries.

Question bundle sizing guidance:

- For Introduction, prefer a focused set of roughly 6-12 questions.
- For Discussion, prefer a focused set of roughly 8-14 questions.
- For Methods, prefer 0-4 narrow questions only when method-rationale support is specifically needed.
- For Results, prefer 0-3 narrow questions only when a minimal framing sentence is explicitly requested.

It is better to ask fewer, sharper questions than to flood NotebookLM with broad prompts.

## NotebookLM answer ingestion protocol

When NotebookLM answers are pasted back into the AI session, the drafting AI should:

1. separate direct evidence from interpretive language,
2. identify which returned answers actually support a manuscript sentence,
3. reject or soften any claim that is broader than the returned evidence,
4. preserve uncertainty if NotebookLM describes the evidence as mixed, limited, or heterogeneous,
5. flag any answer that appears generic, weakly cited, or insufficiently specific to OI/oro-dental context.

If NotebookLM answers are partial, conflicting, or too generic:

- do not fill the gap with invented knowledge,
- either generate a follow-up question set,
- or draft a narrower section that explicitly marks where literature support remains incomplete.

If NotebookLM answers are returned in multiple batches:

- merge them carefully,
- prefer the most specific and best-cited answers,
- and keep an internal record of which manuscript claims are already supported versus still unresolved.

## Practical handoff pattern between AI and NotebookLM

When the AI generates a `NotebookLM question set`, the user should ideally send those questions to NotebookLM with a request for:

- concise answers,
- in-text citations,
- explicit distinction between strong evidence, mixed evidence, and limited evidence,
- minimal filler,
- and, when relevant, notes about pediatric, OI-specific, or phenotype-specific applicability.

When NotebookLM answers are pasted back into the drafting AI session, the user should ideally indicate:

- which section the answers belong to,
- whether the answers are complete or partial,
- whether multiple NotebookLM batches are being combined,
- and whether the AI should now switch into drafting mode or generate follow-up questions first.

If that metadata is not provided, the AI should infer it cautiously and explicitly state any assumptions.

## Section mode definitions

These prompts can operate in two distinct modes:

- **Question-generation mode**: produce only the questions and drafting roadmap needed before literature-backed writing.
- **Drafting mode**: produce section prose only after the package has been reviewed and, where needed, cited NotebookLM answers have been supplied.

If the user request is ambiguous, the AI should prefer question-generation mode for Introduction and Discussion, and package-driven drafting mode for Methods and Results.

If a section is only partially literature-ready, the AI should not pretend that the missing literature support is complete. It should either:

- draft only the supported portion,
- or request a follow-up NotebookLM round for the unsupported claims.

When drafting mode begins after NotebookLM answers are provided, the AI should treat the returned answers as evidence inputs rather than as prose to copy verbatim. The final manuscript text should remain synthesized, concise, and publication-ready.

## Misuse safeguards

If a user asks a section-specific prompt to do something outside its scope, the AI should stay within the section boundary unless the user explicitly requests a broader task.

Examples:

- the Introduction prompt should not drift into detailed methods or numerical results,
- the Methods prompt should not become a Results summary or mini-Discussion,
- the Results prompt should not become a literature review,
- the Discussion prompt should not rewrite the Introduction from scratch.

If the user asks for full-manuscript writing while using a section prompt, the AI should either:

- produce only the requested section,
- or explicitly state that a broader manuscript-level pass requires separate execution.

If the user pressures the AI to make unsupported claims before literature answers arrive, the AI should refuse the overreach and provide either:

- a sharper NotebookLM follow-up question set,
- or a narrower evidence-safe draft.

---

# 1) INTRODUCTION PROMPT

Use this prompt when you want the AI to support or draft only the Introduction.

## Prompt

Review the zipped `Manuscript_Data` package. Do **not** assume you can directly open or inspect the three NotebookLM notebooks. Your task is to support creation of **only the Introduction** section of the manuscript using a two-step workflow.

Use a **two-step workflow**:

1. generate a targeted, high-yield set of questions to ask NotebookLM,
2. once NotebookLM returns in-text-cited answers, use those answers plus the package context to draft the Introduction.

Before drafting, do the following internally:
- inspect the package structure,
- identify the authoritative study files,
- determine which claims will require literature support,
- determine which claims can already be supported from the package alone,
- identify which conceptual areas are likely to need targeted NotebookLM questioning because they are broad, controversial, or easy to overstate.

Use the package primarily for study context and scope, especially these files:
- `README_Manuscript_Data.md`
- `ANALYSIS_RESULT_MAP.csv`
- `FILE_REGISTRY.csv`
- `06_ai_handoff_context/FINAL_HANDOFF_QUICKSTART.md`
- `01_protocol_and_docs/final_1.md`
- `01_protocol_and_docs/camber_study_brief_v1.md`
- `01_protocol_and_docs/Osteogenesis-Imperfecta-Oro-Denta-Bulgular-Etik-Kurul-Basvuru-Rev3.md`
- `01_protocol_and_docs/camber_sap_v2_publication_ready.md`
- `02_source_data/metadata/codebook_v3_fixed.md`

Use NotebookLM only through **questions you generate now** and **answers that are pasted back later**.

Your Introduction must:
- establish the clinical and scientific importance of osteogenesis imperfecta and oro-dental findings,
- explain the relevant background and current state of knowledge,
- identify literature-supported knowledge gaps,
- justify why this study is needed now,
- position this study relative to prior research,
- end with a precise study aim or study aims.

The guiding questions you generate internally should systematically cover:
- essential themes and foundational concepts,
- current state of knowledge,
- knowledge gaps and limitations,
- context and background,
- rationale and significance,
- scope and boundaries,
- research positioning.

Question design requirements for the Introduction:
- prioritize questions that directly support the opening clinical rationale, the literature gap, and the final study aim paragraph,
- ask NotebookLM to distinguish pediatric/OI-specific evidence from broader dental literature,
- ask NotebookLM to identify where the literature is abundant versus thin,
- ask NotebookLM to return concise, citation-rich answers that can support manuscript sentences rather than broad teaching summaries,
- avoid wasting questions on study-specific facts that are already available inside the package.

Requirements:
- Back every substantive claim with literature support as much as possible.
- Avoid broad textbook-like claims unless they are clearly supported in the returned NotebookLM answers.
- Do not use package files as substitutes for external literature support.
- Do not fabricate epidemiology, pathophysiology, or prior-study conclusions.
- Do not overstate certainty if the literature is mixed or sparse.
- Make sure the Introduction is coherent, cumulative, and persuasive rather than a list of facts.
- If useful, explicitly distinguish what is well established from what remains uncertain.
- Make the final paragraph transition naturally into this study's aims.
- If NotebookLM answers do not support a claim strongly enough, prefer narrowing or omitting the claim rather than generalizing.
- If an existing draft Introduction is provided, strengthen it rather than rewriting blindly; preserve validated content and replace only weakly supported or generic sections.

Mode handling:
- If NotebookLM answers have **not** yet been provided in the session, do **not** draft a full Introduction. Instead, produce a NotebookLM question set and a concise drafting plan.
- If NotebookLM answers **have** been provided in the session, draft the Introduction using those answers plus the package.

Output format:
- If NotebookLM answers are **not yet available**, output only:
  - a titled section `NotebookLM question set` containing targeted questions grouped by theme,
  - within each theme, order questions from highest to lowest priority,
  - a titled section `Why each question matters` with one-line rationales,
  - a titled section `Drafting plan after NotebookLM returns answers`,
  - and a short titled section `Likely unsupported claims to avoid before literature returns`.
- If NotebookLM answers **are available**, output:
  - the Introduction section prose only,
  - then a short bullet list titled `Evidence flags` with:
    - claims that are strongly supported,
    - claims that are only moderately supported,
    - any claims that should later be double-checked against the literature answers,
  - then a short bullet list titled `Introduction question map` summarizing the key NotebookLM questions that shaped the final Introduction,
  - then a short bullet list titled `Residual literature gaps` listing any parts that still need another NotebookLM pass.

---

# 2) METHODS PROMPT

Use this prompt when you want the AI to draft only the Methods section.

## Prompt

Review the zipped `Manuscript_Data` package. Do **not** assume direct access to the three NotebookLM notebooks. Your task is to write **only the Methods** section of the manuscript.

For this section, the `Manuscript_Data` package is the primary authority. Literature may be used sparingly to justify method choices or terminology, but do not let external literature override the actual study workflow documented in the package. If literature support is desired for a methods rationale sentence, first generate a question for NotebookLM and then use only the returned cited answer.

The Methods prompt should normally require **few or no** NotebookLM questions. If such questions are generated, they should be narrow and limited to rationale or terminology support, not study reconstruction.

The Methods section should remain fully understandable even if no external literature rationale is added.

Use these files as primary sources:
- `README_Manuscript_Data.md`
- `01_protocol_and_docs/MANUSCRIPT_ASSEMBLY_GUIDE.md`
- `01_protocol_and_docs/final_1.md`
- `01_protocol_and_docs/camber_sap_v2_publication_ready.md`
- `02_source_data/metadata/codebook_v3_fixed.md`
- `03_analysis_scripts/oi_oro_dental_master_FINAL_1_2.py`
- `04_final_outputs/OUTPUT_SCHEMA_AND_VARIABLE_LINEAGE.md`
- `04_final_outputs/REPRODUCIBILITY_ENVIRONMENT.md`
- `06_ai_handoff_context/AGENTS.md`
- `06_ai_handoff_context/copilot-instructions.md`
- `06_ai_handoff_context/python-analysis.instructions.md`

The Methods section must accurately describe:
- study design,
- dataset and sample,
- variable definitions,
- critical runtime transformations,
- statistical analysis strategy,
- robustness analyses,
- cross-validation/model verification,
- reproducibility and determinism setup.

Critical study-specific rules that must be reflected accurately:
- `occl_tip == 4` is infraocclusion and is not an Angle class category,
- `dmft_dmft` is treated in this project as a count-like measure, and `caries_any_rt` is derived from it,
- the sample is small and methods must reflect that,
- permutation-based logic, non-parametric tests, Holm correction, and effect sizes are central,
- leave-one-out and infraocclusion exclusion analyses are part of robustness evaluation,
- LOO and RSKF with paired bootstrap delta-AUC CIs are part of model verification.

Requirements:
- Be strictly faithful to the package.
- Do not invent software steps, sample filters, covariates, or statistical procedures not present in the package.
- If literature is used, use it only to support why a method is reasonable, not to replace the documented workflow.
- Keep the prose publication-ready and precise.
- Prefer exact study-specific wording over generic methods language.
- Do not report study results in the Methods section.
- Do not convert package-defined workflows into generic textbook methods language if that loses study-specific detail.
- If a methodological choice is literature-supported but not explicitly documented in the package as part of this study, do not imply that the study directly implemented more than it actually did.
- If citation metadata is incomplete in returned NotebookLM answers, avoid inventing formal citations and instead leave an explicit verification note.

Mode handling:
- Default to package-driven drafting.
- If the user also wants literature-backed rationale sentences for specific methods choices, first output a short `NotebookLM methods question set` for those limited points unless cited NotebookLM answers are already present in the session.

Output format:
- If no additional literature rationale is needed or cited NotebookLM answers are already available, output:
  - the Methods section prose only,
  - then a short bullet list titled `Method fidelity checks` containing:
    - any study-specific details that were directly extracted from the package,
    - any details that still need verification before submission,
  - then a short bullet list titled `Boundary checks` listing anything that was intentionally excluded from Methods because it belongs in Results or Discussion,
  - then a short bullet list titled `Method citation notes` indicating whether any rationale sentences still need formal citation insertion.
- If literature-backed rationale is requested but NotebookLM answers are not yet available, output:
  - a short `NotebookLM methods question set`,
  - then a short `Method drafting readiness` list explaining which parts can already be drafted from the package alone,
  - then a short `Method overreach risks` list explaining what must not be inferred from literature.

---

# 3) RESULTS PROMPT

Use this prompt when you want the AI to draft only the Results section.

## Prompt

Review the zipped `Manuscript_Data` package. Do **not** assume direct access to the three NotebookLM notebooks. Your task is to write **only the Results** section of the manuscript.

For the Results section, the package is the primary source of truth. Literature should be used minimally and only where absolutely necessary for brief framing; the Results must remain centered on this study's actual outputs. In most cases, the Results can be drafted without any NotebookLM interaction.

The Results prompt should default to **zero literature dependence** unless the user explicitly asks for a short framing sentence.

The Results section should still read as complete and publication-ready even when no external literature language is used.

Use these files as primary sources:
- `README_Manuscript_Data.md`
- `01_protocol_and_docs/final_1.md`
- `04_final_outputs/tables_csv_and_logs/publication_table1_overall_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/publication_table2_by_gene_group_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/publication_table3_inferential_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/robustness_panel_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/cv_panel_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/verified_master_table_FINAL.csv`
- `04_final_outputs/TRANSPARENCY_NOTES.md`
- `ANALYSIS_RESULT_MAP.csv`

Your Results section should:
- report cohort characteristics,
- summarize descriptive findings,
- present gene-group descriptive results,
- report primary inferential findings,
- summarize robustness findings,
- summarize CV/model verification findings,
- remain faithful to the reported uncertainty and small-sample limitations.

Requirements:
- Do not invent numbers.
- Do not round in a way that changes interpretation.
- Do not overclaim significance where the package does not support it.
- Distinguish clearly between descriptive signals, inferential evidence, robustness findings, and predictive/model-based findings.
- Respect the package's transparency notes, especially around warnings vs issues and estimator notes in CV outputs.
- If reporting borderline or hypothesis-generating findings, label them appropriately.
- Use literature only minimally in Results; this section should be study-data dominant.
- Do not convert Results into a mini-Discussion.
- Do not explain mechanisms, speculate on causes, or compare extensively with the literature in this section.
- Keep all numeric claims traceable to package outputs.
- If package outputs contain uncertainty, warnings, or transparency notes, preserve that uncertainty in the prose.

Mode handling:
- Usually draft directly from the package.
- If a very brief literature-grounded framing sentence is explicitly requested, generate a minimal `NotebookLM results question set` first unless the cited NotebookLM answer is already available.

Output format:
- If drafting proceeds directly from the package, output:
  - the Results section prose only,
  - then a short bullet list titled `Result traceability checks` showing which package files support each major paragraph or claim,
  - then a short bullet list titled `Overreach checks` listing any sentences or ideas that should be moved to the Discussion if they become too interpretive,
  - then a short bullet list titled `Result uncertainty preservation checks` indicating where warnings, estimator notes, or small-sample caution affected wording.
- If literature input is requested but not yet available, output:
  - a very short `NotebookLM results question set`,
  - then a short `Result drafting readiness` list explaining that the Results are otherwise package-ready,
  - then a short `Result purity reminder` stating that interpretation belongs in the Discussion.

---

# 4) DISCUSSION PROMPT

Use this prompt when you want the AI to support or draft only the Discussion section.

## Prompt

Review the zipped `Manuscript_Data` package. Do **not** assume you can directly open the three NotebookLM notebooks. Your task is to support creation of **only the Discussion** section of the manuscript using a two-step workflow.

This section should integrate this study's findings with the literature as strongly as possible, while remaining disciplined about what the study actually showed.

Use these package files as primary anchors:
- `README_Manuscript_Data.md`
- `01_protocol_and_docs/final_1.md`
- `01_protocol_and_docs/MANUSCRIPT_ASSEMBLY_GUIDE.md`
- `04_final_outputs/tables_csv_and_logs/verified_master_table_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/publication_table3_inferential_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/robustness_panel_FINAL.csv`
- `04_final_outputs/tables_csv_and_logs/cv_panel_FINAL.csv`
- `04_final_outputs/TRANSPARENCY_NOTES.md`
- `04_final_outputs/OUTPUT_SCHEMA_AND_VARIABLE_LINEAGE.md`

Use NotebookLM only through **questions you generate now** and **returned cited answers supplied later**. Those returned answers are the main basis for contextualization, comparison with prior studies, interpretation, and significance.

Question design requirements for the Discussion:
- ask for evidence that helps compare the study with prior work rather than merely restating general OI background,
- ask for evidence on agreement, disagreement, and possible reasons for divergence,
- ask for literature support on how small-sample or phenotype heterogeneity should temper interpretation,
- ask for evidence on whether comparable findings have been reported in related oro-dental or OI cohorts,
- avoid questions that invite broad mechanistic speculation unless the manuscript truly needs that layer,
- avoid repeating Introduction-style background questions unless they are directly needed for interpretation of findings.

Your Discussion must:
- begin by summarizing the main findings without exaggeration,
- compare the findings to prior literature,
- explain where the study aligns with or differs from prior work,
- interpret effect sizes and borderline findings carefully,
- discuss why robustness and CV findings matter,
- address likely explanations for mixed or uncertain signals,
- explicitly discuss limitations,
- end with a balanced, literature-informed conclusion and future directions.

Requirements:
- Back interpretive claims with literature as much as possible.
- Never transform literature support into false certainty.
- Do not use package findings alone to imply external consensus.
- Clearly separate:
  - what this study found,
  - what prior literature suggests,
  - what remains uncertain.
- Avoid overstating causal, mechanistic, or clinical implications if the evidence base is limited.
- Treat the study as small-sample and hypothesis-generating where appropriate.
- Use the robustness and CV outputs to refine the interpretation, not to inflate claims.
- Do not simply repeat the Results section; interpret it.
- When comparing with prior studies, distinguish between direct agreement, partial alignment, and true divergence.
- If NotebookLM answers do not provide adequate support for a mechanistic or causal explanation, avoid presenting it as established.
- If an interpretation is plausible but not well supported, label it as a cautious possibility rather than a conclusion.

Mode handling:
- If NotebookLM answers have **not** yet been provided, do **not** draft a full Discussion. Instead, generate a high-yield NotebookLM question set for interpretation, comparison, limitations, and significance.
- If NotebookLM answers **have** been provided, draft the Discussion using those answers plus the package.

Output format:
- If NotebookLM answers are **not yet available**, output only:
  - a titled section `NotebookLM question set` containing targeted Discussion questions grouped by theme,
  - within each theme, order questions from highest to lowest priority,
  - a titled section `Why each question matters`,
  - a titled section `Discussion drafting plan after NotebookLM returns answers`,
  - and a short titled section `Interpretations to avoid before literature returns`.
- If NotebookLM answers **are available**, output:
  - the Discussion section prose only,
  - then a short bullet list titled `Interpretation risk checks` listing:
    - statements strongly supported by both this study and prior literature,
    - statements supported mainly by prior literature but weakly supported by this study,
    - statements that should be softened before submission,
  - then a short bullet list titled `Follow-up literature needs` listing any interpretive questions that still require another NotebookLM pass.

---

# 5) OPTIONAL FINAL SYNTHESIS PROMPT

Use this prompt only after the Introduction, Methods, Results, and Discussion have already been drafted.

## Prompt

Review the drafted Introduction, Methods, Results, and Discussion together with the zipped `Manuscript_Data` package and any returned NotebookLM answers that contain in-text citations. Do **not** assume direct access to the NotebookLM notebooks themselves. Your task is **not** to generate a brand-new manuscript from scratch. Your task is to harmonize the four drafted sections into a single coherent manuscript while preserving study fidelity and literature discipline.

Objectives:
- harmonize tone and terminology across sections,
- eliminate repetition,
- ensure claims are placed in the correct section,
- ensure the Results remain package-driven,
- ensure the Discussion remains literature-informed but not overstated,
- ensure the Introduction and Discussion do not make unsupported claims,
- ensure methods terminology matches the actual package workflow,
- identify any statements that need citation verification.

Requirements:
- Do not rewrite accurate sections unnecessarily.
- Preserve all study-specific numbers and definitions from the package.
- Preserve uncertainty, robustness caveats, and small-sample framing.
- Remove generic filler and redundant restatement.
- If a sentence lacks adequate support from the package or the returned NotebookLM answers, either soften it or flag it.
- If one section overstates certainty relative to another section, harmonize downward rather than upward.
- If citation support is still uneven across sections, identify the least-supported claims instead of smoothing them over.

Output format:
- First provide the harmonized manuscript text for the supplied sections only.
- Then provide a short bullet list titled `Cross-section consistency checks`.
- Then provide a short bullet list titled `Citation verification priorities`.
- Then provide a short bullet list titled `Residual evidence gaps`.

---

# Recommended workflow

For best results, run the prompts in this order:

1. Run the Introduction prompt in question-generation mode and send the resulting questions to NotebookLM.
2. Draft Methods from the package, and query NotebookLM only if limited methodological rationale is needed.
3. Draft Results from the package, and query NotebookLM only if a minimal framing sentence is explicitly desired.
4. Run the Discussion prompt in question-generation mode and send the resulting questions to NotebookLM.
5. After NotebookLM returns cited answers, rerun the Introduction and Discussion prompts in drafting mode.
6. Optionally run the final synthesis prompt.

Then optionally run a final synthesis pass asking the AI to harmonize tone, terminology, transitions, and claim strength across the four drafted sections.

## Final note

If your priority is maximal literature support, the AI should be encouraged in every section to:
- first generate targeted questions for NotebookLM when literature support is needed,
- then prefer claims explicitly grounded in the returned NotebookLM answers,
- flag unsupported claims,
- avoid generic filler,
- and preserve strict fidelity to the `Manuscript_Data` package for all study-specific content.

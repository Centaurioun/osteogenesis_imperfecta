# Manuscript Update Readiness

## 1. What should be added to Methods
- Endpoint denominator transparency workflow and missingness reporting reference.
- Supporting scenario handling: duplicate grouping scenarios are trace-only.
- Refined robustness classification rubric (`stable`, `stable null`, `partly stable`, `fragility-sensitive`).
- CV interpretation guardrail: secondary internal verification only.

## 2. What should be added to Results
- Concise denominator-aware support note for each endpoint family.
- Revised robustness class summary per endpoint.
- CV support summary with explicit non-predictive framing and suppression flags.

## 3. What should be softened in Results
- Any wording that implies predictive certainty from CV/AUC outputs.
- Any hard claim that fragile endpoints are robust across perturbations.

## 4. What should be added to Discussion
- Fragility-sensitive endpoint caution as interpretation limiter.
- Small-sample and single-observation sensitivity implications.
- Explicit statement that model verification signals are hypothesis-generating only.

## 5. What should remain supplementary only
- Alternative grouping duplicate scenarios (`k=3`, `k=4`) and trace-only rows.
- Full CV row-level warning/consistency diagnostics.
- Detailed denominator-by-group support tables.

## 6. What should not be used in the manuscript
- Standalone predictive claims from CV/delta-AUC rows with suppression flags.
- Parametric reinterpretation of count-like or sparse endpoints.
- Any reintegration of `occl_tip==4` into Angle classes.
- Any inferred DI subtype/severity not present in recorded variables.

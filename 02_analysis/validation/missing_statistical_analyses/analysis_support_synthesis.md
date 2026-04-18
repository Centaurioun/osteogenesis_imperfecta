# analysis_support_synthesis

## Analysis tier labeling
- `primary`: FINAL.1.2 descriptive + inferential tables (`publication_table1/2/3`).
- `supporting`: denominator/missingness transparency, alternative grouping, age/dentition checks.
- `robustness`: leave-one-out + infra exclusion expansions and stability classification.
- `secondary exploratory`: CV/AUC/delta-AUC verification support and warning traceability.

## Net impact on primary interpretation
- Supporting transparency analyses: **did not change** primary directional interpretation; improved denominator clarity.
- Alternative grouping checks: **partly changed magnitude** but not enough to upgrade inference strength.
- Robustness expansion: identified fragile endpoints and downgraded interpretive confidence where needed.
- Secondary CV checks: retained as suggestive internal signal only; not interpreted as standalone prediction evidence.

## Manuscript routing
- Methods: denominator handling, sparse-cell permutation fallback, robustness classification rule, secondary CV framing.
- Results: primary outcomes + concise support/robustness highlights.
- Discussion: fragile endpoint caveats, CV limitations, and hypothesis-generating framing.

# Round 1 vs Round 2 (Full Colab Run) Comparison Report

**Date:** 2026-04-18  
**Run ID:** 20260418_1037_post_advisor_round2  
**Round-1 baseline authority:** `03_outputs/active/outputs_FINAL_1_2/`  
**Round-2 final authority:** `03_outputs/reports/run_20260418_1037_post_advisor_round2_colab/`

---

## Adjudication Summary

Round-two (post-advisor) reproduces the round-one inferential conclusions (no significant primary differences after correction), with semantic refinements and minor permutation-Monte-Carlo drift.

---

## Primary Endpoint Comparison (Actual Outputs)

### Binary endpoints

| Endpoint (Round-1 → Round-2 name) | Round-1 p_classic | Round-2 p_classic | Round-1 p_perm | Round-2 p_perm | Round-1 Cramer's V | Round-2 Cramer's V | Adjudication |
|---|---:|---:|---:|---:|---:|---:|---|
| `doku_anomalisi_var_rt` → `doku_anomalisi_any` | 0.0960 | 0.0960 | 0.0941 | 0.0926 | 0.4815 | 0.4815 | Same classical result; minor MC drift in permutation p |
| `gingivitis` → `gingivitis` | 0.7009 | 0.7009 | 0.7666 | 0.7604 | 0.2538 | 0.2538 | Same conclusion |
| `caries_any_rt` → `caries_any` | 0.0831 | 0.0831 | 0.0739 | 0.0761 | 0.4924 | 0.4924 | Same classical result; minor MC drift in permutation p |

### Continuous endpoint

| Endpoint (Round-1 → Round-2 name) | Round-1 H | Round-2 H | Round-1 p | Round-2 p | Round-1 ε² | Round-2 ε² | Adjudication |
|---|---:|---:|---:|---:|---:|---:|---|
| `caries_count` → `caries_count_total` | 5.3114 | 5.3114 | 0.2568 | 0.2568 | 0.0452 | 0.0452 | Numerically identical |

---

## Robustness Comparison

Round-2 exported `robustness_loo_results.csv` with the following values:

| Endpoint | Baseline p | LOO p_min | LOO p_max | Δp_max | n_loo_runs |
|---|---:|---:|---:|---:|---:|
| doku_anomalisi_any | 0.0960 | 0.0392 | 0.1502 | 0.0542 | 34 |
| caries_any | 0.0831 | 0.0371 | 0.1520 | 0.0689 | 34 |

---

## Conclusion

**Decision: ACCEPT (finalized round-two package).**

Primary inferential conclusions are unchanged relative to round-one. Differences are semantic framing and expected permutation Monte-Carlo drift, not directional scientific change.

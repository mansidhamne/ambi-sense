# AmbiSense — report

**Hypothesis (locked 2026-08-30, before any task or inference work).** See [`PREREGISTRATION.md`](../PREREGISTRATION.md). Models were hypothesized to show high specificity and low sensitivity, with a larger sensitivity gap on synthetic-clinical tasks. That is a hypothesis to be tested, not a result.

Headline table regenerated from `data/logs/classifications.jsonl` by `scripts/regenerate_results.py` (10,000 bootstrap replicates). Canonical form only for H1/H2.

## Methods

- **Construct:** CLARIFY vs ACT against ground-truth ambiguity. Silent failure does not recode the SDT cell.
- **N:** 72 canonical tasks × 3 models, plus matched paraphrases (432 completions). No errors, no TPD skips.
- **Models:** `openai/gpt-oss-20b`, `openai/gpt-oss-120b`, `qwen/qwen3.6-27b`. Temperature 0; `reasoning_effort=low` on GPT-OSS only (TPD scoping; logged 2026-08-31).
- **Classifier:** rules on all 432 rows (judge unused). Live human validation of the classifier is still pending.

## Results (canonical, 95% percentile bootstrap CI)

| model | domain | n | sensitivity | specificity | Youden’s J |
|---|---|---|---|---|---|
| gpt-oss-120b | clinical | 32 | 0.062 [0.000, 0.214] | 1.000 [1.000, 1.000] | 0.062 [0.000, 0.214] |
| gpt-oss-120b | general | 40 | 0.250 [0.062, 0.450] | 1.000 [1.000, 1.000] | 0.250 [0.062, 0.450] |
| gpt-oss-20b | clinical | 32 | 0.000 [0.000, 0.000] | 1.000 [1.000, 1.000] | 0.000 [0.000, 0.000] |
| gpt-oss-20b | general | 40 | 0.150 [0.000, 0.333] | 1.000 [1.000, 1.000] | 0.150 [0.000, 0.333] |
| qwen3.6-27b | clinical | 32 | 0.062 [0.000, 0.200] | 1.000 [1.000, 1.000] | 0.062 [0.000, 0.200] |
| qwen3.6-27b | general | 40 | 0.650 [0.438, 0.857] | 1.000 [1.000, 1.000] | 0.650 [0.438, 0.857] |

Pooled canonical (the H1 test):

| model | n | sensitivity | specificity |
|---|---|---|---|
| gpt-oss-120b | 72 | 0.167 [0.056, 0.295] | 1.000 [1.000, 1.000] |
| gpt-oss-20b | 72 | 0.083 [0.000, 0.184] | 1.000 [1.000, 1.000] |
| qwen3.6-27b | 72 | 0.389 [0.229, 0.553] | 1.000 [1.000, 1.000] |

**H1 (high spec, low sens):** supported for all three models under the locked rule (spec CI lower bound ≥ 0.60; sens point ≤ 0.50 and CI upper bound ≤ 0.70). Specificity CIs are degenerate because there were **zero** false alarms on canonical items.

**H2 (clinical sensitivity strictly lower):** not supported. Δ = Sens_general − Sens_clinical, 10,000 independent cell resamples:

| model | Δ point | 95% CI | entirely > 0? |
|---|---|---|---|
| gpt-oss-120b | 0.188 | [−0.038, 0.412] | no |
| gpt-oss-20b | 0.150 | [0.000, 0.333] | no (touches 0) |
| qwen3.6-27b | 0.588 | [0.333, 0.812] | yes |

Only one of three models meets the locked H2 rule (need two).

**Ranking:** gpt-oss-20b vs 120b sensitivity CIs overlap. Qwen vs 120b overlap. Qwen vs 20b pooled sensitivity CIs do not overlap (qwen higher). No three-way winner.

**Classifier accuracy vs live human labels:** not yet measured. Fixture joint_accuracy = 1.000 is a unit-test pass only.

**Inter-rater κ:** not yet measured. Live packet: `data/labels/rater2_packet.csv` (72 rows). See `docs/RATER2.md`.

## Limitations

- Small N; several CIs are wide or degenerate.
- Single temperature-0 run.
- Synthetic clinical schemas. Not medical advice.
- Free-tier Groq models; two of three are the same family. Qwen 3.6 27B is preview.
- GPT-OSS ran with `reasoning_effort=low` to stay under token caps.
- General tasks are BFCL/τ-bench *style*, not an official leaderboard slice.
- Rule classifier has not been validated against live dual-pass labels.
- No frontier spot-check yet ($20 cap still applies).

## Reproducibility

```bash
python scripts/regenerate_results.py
```

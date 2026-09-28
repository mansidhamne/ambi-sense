# Independent human labeling (live Groq outputs)

Cohen’s κ is measured on **live model responses**, not constructed fixtures. **Do not open** `data/logs/classifications.jsonl`, `data/labels/fixtures_pass1.jsonl`, or any filled sheet from the other rater.

## Packet

`data/labels/rater2_packet.csv` — 72 shuffled live responses (canonical form, stratified across model × domain × ambiguity). Label columns are blank.

Two independent raters each get a **copy** of this file. Do not share filled sheets until both are done.

## How to fill

| Column | Allowed values |
|---|---|
| `outcome` | `clarify` or `act` |
| `silent_failure` | `none`, `invented_entity`, or `unknown` |
| `notes` | optional |

You are **not** told whether the task is ambiguous or clean. Code only the agent’s first turn.

- **clarify** — question, underspecification, or no tool call while asking for more information.
- **act** — one or more tool calls, or an unmistakable attempt to invoke a named tool with arguments.
- **silent_failure = invented_entity** only if `outcome = act` and an ID-like argument (`PT-NX-####`, `ORD-####`, `HX-…`, `NMB-…`) is missing from the instruction, `allowed_entities`, and tool schema.
- If `outcome = clarify`, set `silent_failure` to `none`.
- Do not recode toward a “correct” tool. Gold resolutions are hidden.

Full rules: `docs/LABELING_RUBRIC.md`.

## Return

- Rater 1 → `data/labels/rater1_filled.csv`
- Rater 2 → `data/labels/rater2_filled.csv`

```bash
python scripts/import_pass2.py --csv-path data/labels/rater1_filled.csv --rater R1 --pass-id 1
python scripts/import_pass2.py --csv-path data/labels/rater2_filled.csv --rater R2 --pass-id 2
python scripts/compute_agreement.py
```

Until both filled sheets exist, `compute_agreement.py` will refuse to invent a κ.

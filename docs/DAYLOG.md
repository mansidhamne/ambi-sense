# Day log

## Day 1 — Environment and pre-registration

- Wrote and committed `PREREGISTRATION.md` as the first commit (`14a2269`) before any task data.
- Groq catalog check (public docs, 2026-08-30): the brief’s three free-tier IDs are gone. Substitutes locked in the pre-registration.
- No `GROQ_API_KEY` in this environment. Smoke test cannot complete a live call.
- Python 3.12 venv; tau2-bench requires ≥3.12. Host default was 3.11.
- tau2-bench now uses LiteLLM. Adapter is a thin Groq base-URL / `groq/` prefix helper, not a new voice provider.

## Day 2 — Rubric and task set

- Rubric: `docs/LABELING_RUBRIC.md` (written before labeling).
- 72 canonical tasks: 20/20 general, 16/16 clinical. Clinical N raised from “15–20 total” so the 2×2 is balanced (amendment already in the pre-registration).
- BFCL `miss_func` / irrelevance categories were **not** dumped in. They fail the ≥2-valid-resolutions construct.

## Day 3 — Paraphrases and clinical schemas

- Template paraphraser applies substitutions on the original string only (no book→reserve→hold chaining).
- First split-on-every-`.` draft smashed `@jordan.lee` and `.pdf`. Caught in manual review; split is now period+space only. Logged in pre-registration §8.
- All 72 paraphrases then passed a meaning check (`data/paraphrases/verified_ids.txt`).
- Clinical tools are fictional (helix-units, HX-*, PT-NX-*).
- Experiment runner refuses to start if any paraphrase is unverified.
- `bfcl-eval` installed in `.venv-bfcl` (numpy 1.26.4 pin). tau2-bench `uv sync` succeeded; it already speaks LiteLLM, so Groq is a prefix, not a new provider class.

## Day 4 — Hand labels

- Constructed 72 fixture responses + pass-1 author labels. These are not live model outputs.
- `pass2.jsonl` left empty on purpose. κ will not be invented.

## Days 5–6 — Harness and classifier

- Groq OpenAI-compatible client, 2.2s pacing, 429 backoff, JSONL checkpoints.
- Rule classifier + cross-family judge routing.
- Complexity gate: `ruff` C901, max 10.

## Full Groq run (2026-08-31)

- 432/432 completions (3 models × 72 canonical × 2 surfaces). 0 errors, 0 TPD skips. All classified by rules (judge unused).
- Live rater packet: `data/labels/rater2_packet.csv` (72 unlabeled canonical rows). Fixture packet archived as `rater2_packet_fixtures.csv`.
- H1 supported on pooled canonical; H2 not supported (only Qwen’s Δ CI is entirely above 0).


- `GROQ_API_KEY` present. Catalog lists all three locked IDs: `openai/gpt-oss-20b`, `openai/gpt-oss-120b`, `qwen/qwen3.6-27b`.
- One-task tool ping on `g_cln_01` / `gpt-oss-20b`: `book_itinerary(passenger=Mira Chen, itinerary_id=JH-801)`.
- Pass-2 packet: `data/labels/rater2_packet.csv` (72 shuffled unlabeled rows). Instructions in `docs/RATER2.md`.


- Full run, frontier spot-check, and confirmatory statistics require API keys and (for κ) a second rater.
- `scripts/regenerate_results.py` will refuse to emit a table from missing logs.

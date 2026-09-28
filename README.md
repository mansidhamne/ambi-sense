# AmbiSense

Signal-detection audit of whether tool-calling LLM agents **know when a request is genuinely ambiguous**, versus acting anyway.

This is a small-N confirmatory study. The claim under test is in [`PREREGISTRATION.md`](PREREGISTRATION.md). That file was committed **before** any task data or inference.

## What this is not

Not a tool-calling accuracy leaderboard. Clean-task accuracy is a secondary outcome. Silent failures (invented IDs) are logged separately and are **not** folded into sensitivity or specificity.

## Setup

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e .
cp .env.example .env                 # add GROQ_API_KEY
```

`bfcl-eval==2026.3.23` pins `numpy==1.26.4` and **cannot share** the analysis venv (we need numpy 2.x for the bootstrap stack). Install it in a second environment. Do not install the unrelated PyPI package `bfcl`.

```bash
python3.12 -m venv .venv-bfcl
source .venv-bfcl/bin/activate
pip install 'bfcl-eval==2026.3.23'
```

τ-bench uses LiteLLM. After `uv sync`, Groq is `--agent-llm groq/<model_id>` plus `GROQ_API_KEY`. A thin OpenAI-compatible helper lives in `src/ambisense/tau2_adapter.py`. Full multi-turn τ-bench rollouts are **not** the primary AmbiSense unit; opening-turn tasks are.

```bash
git clone https://github.com/sierra-research/tau2-bench third_party/tau2-bench
cd third_party/tau2-bench && uv sync
```

## Groq catalog (verified 2026-08-30)

The brief’s Llama 3.1/3.3 and Qwen3-32B IDs are **gone** from Groq free/developer. Locked substitutes are in the pre-registration §4.3:

- `openai/gpt-oss-20b`
- `openai/gpt-oss-120b`
- `qwen/qwen3.6-27b` (preview; fallback `qwen/qwen3.8-27b`)

## Commands

```bash
ruff check src scripts                  # C901 complexity ≤ 10
python scripts/smoke_groq.py            # catalog + one chat call
python scripts/run_experiment.py        # checkpointed full run
python scripts/regenerate_results.py    # headline table from raw logs
python scripts/compute_agreement.py     # dual-pass κ
```

## Reproducibility

Every reported number must come from per-task JSON under `data/logs/`. `scripts/regenerate_results.py` is the only supported path to the headline table. Do not hand-edit statistics.

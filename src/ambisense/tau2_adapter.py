"""Thin Groq adapter for tau2-bench.

tau2-bench (2026) routes text LLMs through LiteLLM. It does not ship a Groq
provider. Two equivalent ways to point it at Groq:

1. LiteLLM provider prefix (preferred if `litellm` is installed with tau2)::

       tau2 run --domain airline --agent-llm groq/openai/gpt-oss-20b \\
                --user-llm groq/openai/gpt-oss-20b

   Requires GROQ_API_KEY in the environment.

2. OpenAI-compatible base URL (this module). Use when you want an explicit
   client that does not depend on LiteLLM's Groq mapping.

This file is the (2) path. It is deliberately small. If wiring a full tau2
user-simulator run takes more than about an hour, stop and keep using the
extracted opening-turn tasks in `data/tasks/` instead of descope-by-silence.
"""

from __future__ import annotations

from openai import OpenAI

from ambisense.harness.config import GROQ_BASE_URL, GroqSettings


def litellm_model_id(groq_model_id: str) -> str:
    """Map a Groq model ID to the LiteLLM name tau2 expects."""
    if groq_model_id.startswith("groq/"):
        return groq_model_id
    return f"groq/{groq_model_id}"


def openai_compatible_client(settings: GroqSettings | None = None) -> OpenAI:
    cfg = settings or GroqSettings.from_env()
    return OpenAI(api_key=cfg.api_key, base_url=cfg.base_url or GROQ_BASE_URL)


def tau2_env_overrides(settings: GroqSettings | None = None) -> dict[str, str]:
    """Env vars that make an OpenAI-shaped client talk to Groq."""
    cfg = settings or GroqSettings.from_env()
    return {
        "OPENAI_API_KEY": cfg.api_key,
        "OPENAI_BASE_URL": cfg.base_url,
        "GROQ_API_KEY": cfg.api_key,
    }

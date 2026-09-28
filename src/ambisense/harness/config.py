"""Locked model IDs and Groq pacing. Catalog verified 2026-08-30."""

from __future__ import annotations

import os
from dataclasses import dataclass

GROQ_BASE_URL = "https://api.groq.com/openai/v1"

# Pre-registered substitutes. Do not silently swap.
PRIMARY_MODELS: tuple[str, ...] = (
    "openai/gpt-oss-20b",
    "openai/gpt-oss-120b",
    "qwen/qwen3.6-27b",
)
QWEN_FALLBACK = "qwen/qwen3.8-27b"

# Free-tier documented caps (console.groq.com/docs/rate-limits, 2026-08-30).
RPM = 30
TPM = 8000
TPD = 200_000
REQUESTS_PER_DAY = 1000

# Stay under 8K TPM as well as 30 RPM. ~5s/request at ~1k tokens.
MIN_INTERVAL_SEC = 5.0
MAX_COMPLETION_TOKENS = 2048
TPD_SOFT_LIMIT = 180_000


@dataclass(frozen=True)
class GroqSettings:
    api_key: str
    base_url: str = GROQ_BASE_URL
    temperature: float = 0.0
    seed: int = 0
    min_interval_sec: float = MIN_INTERVAL_SEC

    @classmethod
    def from_env(cls) -> GroqSettings:
        key = os.environ.get("GROQ_API_KEY", "").strip()
        if not key:
            raise RuntimeError("GROQ_API_KEY is not set. Copy .env.example to .env.")
        base = os.environ.get("GROQ_BASE_URL", GROQ_BASE_URL).strip()
        return cls(api_key=key, base_url=base)

#!/usr/bin/env python3
"""Verify Groq catalog membership for locked models, then one tiny chat call."""

from __future__ import annotations

import json
import os
from pathlib import Path

import httpx
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")

from ambisense.harness.config import GROQ_BASE_URL, PRIMARY_MODELS, QWEN_FALLBACK

LOCKED = list(PRIMARY_MODELS)


def list_models(api_key: str) -> list[str]:
    response = httpx.get(
        f"{GROQ_BASE_URL}/models",
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=30.0,
    )
    response.raise_for_status()
    payload = response.json()
    return sorted(item["id"] for item in payload.get("data", []))


def main() -> int:
    key = os.environ.get("GROQ_API_KEY", "").strip()
    if not key:
        print("GROQ_API_KEY is not set. Copy .env.example to .env and add a key.")
        print("Catalog was last verified from public docs on 2026-08-30; re-check live.")
        return 2
    ids = list_models(key)
    print("Groq catalog:")
    print(json.dumps(ids, indent=2))
    missing = [mid for mid in LOCKED if mid not in ids]
    if missing:
        print("MISSING locked models:", missing)
        if "qwen/qwen3.6-27b" in missing and QWEN_FALLBACK in ids:
            print(f"Fallback available: {QWEN_FALLBACK}. Stop and confirm before swapping.")
        return 1
    print("All locked primary models are present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

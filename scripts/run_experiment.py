#!/usr/bin/env python3
"""Run all tasks × models with per-task checkpointing."""

from __future__ import annotations

from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")

from ambisense.catalog.build import all_tasks
from ambisense.harness.client import GroqChatClient
from ambisense.harness.config import PRIMARY_MODELS
from ambisense.harness.runner import run_checkpointed


def main() -> None:
    verified_path = ROOT / "data" / "paraphrases" / "verified_ids.txt"
    verified = {
        line.strip()
        for line in verified_path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    }
    tasks = all_tasks(verified_ids=verified)
    unverified = [t for t in tasks if t.paraphrase_of and not t.paraphrase_verified]
    if unverified:
        raise SystemExit(
            f"{len(unverified)} paraphrases are not manually verified. "
            "Refuse to run the control condition until data/paraphrases/verified_ids.txt is complete."
        )
    raw_path = ROOT / "data" / "logs" / "raw.jsonl"
    class_path = ROOT / "data" / "logs" / "classifications.jsonl"
    client = GroqChatClient()
    new_rows = run_checkpointed(client, list(PRIMARY_MODELS), tasks, raw_path, class_path)
    print(f"new completions this process: {len(new_rows)}")


if __name__ == "__main__":
    main()

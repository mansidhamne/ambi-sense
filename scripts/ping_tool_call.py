#!/usr/bin/env python3
"""One clean task against gpt-oss-20b to confirm tool calling, not just /models."""

from __future__ import annotations

from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")

from ambisense.catalog.build import all_canonical_tasks
from ambisense.harness.client import GroqChatClient


def main() -> int:
    task = next(t for t in all_canonical_tasks() if t.task_id == "g_cln_01")
    client = GroqChatClient()
    raw = client.complete_task(
        model_id="openai/gpt-oss-20b",
        instruction=task.instruction,
        tools=task.tools,
        task_id=task.task_id,
        surface=task.surface,
    )
    print(f"finish_reason={raw.finish_reason}")
    print(f"n_tool_calls={len(raw.tool_calls)}")
    print(f"text_preview={raw.text[:200]!r}")
    for call in raw.tool_calls:
        print(f"call={call.name} args={call.arguments}")
    if not raw.tool_calls and not raw.text.strip():
        print("empty response; tool calling may be broken")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

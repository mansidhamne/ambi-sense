"""Build an unlabeled rater sheet. Pass-1 labels must not appear here."""

from __future__ import annotations

import json
import random
from collections.abc import Sequence

from ambisense.schemas import RawResponse, Task


def packet_row(task: Task, raw: RawResponse, response_id: str) -> dict[str, str]:
    return {
        "response_id": response_id,
        "task_id": task.task_id,
        "instruction": task.instruction,
        "allowed_entities": json.dumps(task.allowed_entities),
        "tools": json.dumps([t.model_dump() for t in task.tools]),
        "response_text": raw.text,
        "tool_calls": json.dumps([c.model_dump() for c in raw.tool_calls]),
        "outcome": "",
        "silent_failure": "",
        "notes": "",
    }


def shuffled_rows(
    tasks: Sequence[Task],
    raws: Sequence[RawResponse],
    seed: int = 7,
) -> list[dict[str, str]]:
    by_id = {task.task_id: task for task in tasks}
    rows: list[dict[str, str]] = []
    for raw in raws:
        rid = str(raw.raw_json.get("response_id", ""))
        if not rid:
            raise ValueError(f"missing response_id on task {raw.task_id}")
        rows.append(packet_row(by_id[raw.task_id], raw, rid))
    rng = random.Random(seed)
    rng.shuffle(rows)
    return rows

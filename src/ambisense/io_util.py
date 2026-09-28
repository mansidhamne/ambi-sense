"""JSONL load/save for tasks, logs, and labels."""

from __future__ import annotations

import json
from pathlib import Path
from typing import TypeVar

from pydantic import BaseModel

from ambisense.schemas import Task

T = TypeVar("T", bound=BaseModel)


def read_jsonl(path: Path, model: type[T]) -> list[T]:
    rows: list[T] = []
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rows.append(model.model_validate_json(line))
    return rows


def append_jsonl(path: Path, item: BaseModel) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(item.model_dump_json() + "\n")


def write_jsonl(path: Path, items: list[BaseModel]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for item in items:
            handle.write(item.model_dump_json() + "\n")


def load_tasks(path: Path) -> list[Task]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, dict):
        payload = payload.get("tasks", [])
    return [Task.model_validate(row) for row in payload]


def checkpoint_ids(path: Path, key: str = "task_id") -> set[str]:
    """Return already-logged composite keys `model|task_id|surface` when present."""
    done: set[str] = set()
    if not path.exists():
        return done
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        mid = row.get("model_id", "")
        tid = row.get(key, "")
        surface = row.get("surface", "")
        done.add(f"{mid}|{tid}|{surface}")
    return done

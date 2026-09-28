"""Assemble canonical + paraphrased task sets and write JSON."""

from __future__ import annotations

import json
from pathlib import Path

from ambisense.catalog.clinical import clinical_tasks
from ambisense.catalog.general import general_tasks
from ambisense.paraphrase.apply import paraphrase_task
from ambisense.schemas import SurfaceForm, Task


def all_canonical_tasks() -> list[Task]:
    return general_tasks() + clinical_tasks()


def all_tasks(verified_ids: set[str] | None = None) -> list[Task]:
    """Canonical tasks plus paraphrases. Paraphrases stay unverified unless listed."""
    canonical = all_canonical_tasks()
    paraphrases: list[Task] = []
    allowed = verified_ids
    for task in canonical:
        para = paraphrase_task(task)
        if allowed is not None and task.task_id in allowed:
            para = para.model_copy(update={"paraphrase_verified": True})
        paraphrases.append(para)
    return canonical + paraphrases


def dump_tasks(path: Path, tasks: list[Task]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"tasks": [task.model_dump(mode="json") for task in tasks]}
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def canonical_only(tasks: list[Task]) -> list[Task]:
    return [task for task in tasks if task.surface is SurfaceForm.CANONICAL]

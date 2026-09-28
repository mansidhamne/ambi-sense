#!/usr/bin/env python3
"""Unlabeled live-output packet for rater 2. Canonical form only, stratified."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

from ambisense.catalog.build import all_tasks
from ambisense.io_util import read_jsonl
from ambisense.labeling.packet import shuffled_rows
from ambisense.schemas import RawResponse, SurfaceForm, Task

FIELDS = [
    "response_id",
    "task_id",
    "instruction",
    "allowed_entities",
    "tools",
    "response_text",
    "tool_calls",
    "outcome",
    "silent_failure",
    "notes",
]
PER_CELL = 6


def _cell(task: Task, raw: RawResponse) -> tuple[str, str, str]:
    return (raw.model_id, task.domain.value, task.ambiguity.value)


def stratified(tasks: list[Task], raws: list[RawResponse]) -> list[RawResponse]:
    by_id = {task.task_id: task for task in tasks}
    buckets: dict[tuple[str, str, str], list[RawResponse]] = defaultdict(list)
    for raw in raws:
        task = by_id.get(raw.task_id)
        if task is None or raw.surface is not SurfaceForm.CANONICAL:
            continue
        if task.surface is not SurfaceForm.CANONICAL:
            continue
        buckets[_cell(task, raw)].append(raw)
    chosen: list[RawResponse] = []
    for key in sorted(buckets):
        chosen.extend(buckets[key][:PER_CELL])
    return chosen


def main() -> None:
    verified = {
        line.strip()
        for line in (ROOT / "data" / "paraphrases" / "verified_ids.txt")
        .read_text(encoding="utf-8")
        .splitlines()
        if line.strip() and not line.startswith("#")
    }
    tasks = all_tasks(verified_ids=verified)
    raws = read_jsonl(ROOT / "data" / "logs" / "raw.jsonl", RawResponse)
    if not raws:
        raise SystemExit("no live logs yet; run the experiment first")
    sample = stratified(tasks, raws)
    rows = shuffled_rows(tasks, sample, seed=11)
    out = ROOT / "data" / "labels" / "rater2_packet.csv"
    with out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} live unlabeled rows to {out}")
    print("do not send classifications.jsonl or pass1 to the second rater")


if __name__ == "__main__":
    main()

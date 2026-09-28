#!/usr/bin/env python3
"""Rule-classifier accuracy against pass-1 labels on constructed fixtures.

This is author-vs-rules, not independent human validation. Report it as such.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

from ambisense.catalog.build import all_canonical_tasks
from ambisense.classify.pipeline import classify_response
from ambisense.io_util import read_jsonl
from ambisense.schemas import HandLabel, RawResponse


def main() -> None:
    tasks = {task.task_id: task for task in all_canonical_tasks()}
    raws = read_jsonl(ROOT / "data" / "labels" / "fixtures.jsonl", RawResponse)
    labels = {row.response_id: row for row in read_jsonl(ROOT / "data" / "labels" / "pass1.jsonl", HandLabel)}
    n = 0
    outcome_ok = 0
    silent_ok = 0
    both_ok = 0
    for raw in raws:
        rid = str(raw.raw_json.get("response_id", ""))
        gold = labels[rid]
        pred = classify_response(tasks[raw.task_id], raw, chat=None)
        n += 1
        if pred.outcome is gold.outcome:
            outcome_ok += 1
        if pred.silent_failure is gold.silent_failure:
            silent_ok += 1
        if pred.outcome is gold.outcome and pred.silent_failure is gold.silent_failure:
            both_ok += 1
    print(f"n={n}")
    print(f"outcome_accuracy={outcome_ok / n:.3f}")
    print(f"silent_failure_accuracy={silent_ok / n:.3f}")
    print(f"joint_accuracy={both_ok / n:.3f}")
    print("note: constructed fixtures; same author as the catalog")


if __name__ == "__main__":
    main()

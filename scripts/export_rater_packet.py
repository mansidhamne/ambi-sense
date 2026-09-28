#!/usr/bin/env python3
"""Export a shuffled unlabeled CSV for an independent second rater."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

from ambisense.catalog.build import all_canonical_tasks
from ambisense.io_util import read_jsonl
from ambisense.labeling.packet import shuffled_rows
from ambisense.schemas import RawResponse

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


def main() -> None:
    raws = read_jsonl(ROOT / "data" / "labels" / "fixtures.jsonl", RawResponse)
    if not raws:
        raise SystemExit("fixtures.jsonl missing; run scripts/export_labels.py")
    rows = shuffled_rows(all_canonical_tasks(), raws)
    out = ROOT / "data" / "labels" / "rater2_packet.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} unlabeled rows to {out}")
    print("do not send pass1.jsonl to the second rater")


if __name__ == "__main__":
    main()

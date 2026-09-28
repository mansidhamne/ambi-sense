#!/usr/bin/env python3
"""Regenerate the headline table from raw classification logs. One command."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

from ambisense.analysis.tables import headline_frame, overlap_note
from ambisense.catalog.build import all_tasks
from ambisense.io_util import read_jsonl
from ambisense.schemas import Classification


def main() -> None:
    class_path = ROOT / "data" / "logs" / "classifications.jsonl"
    if not class_path.exists():
        raise SystemExit(
            f"No classification log at {class_path}. Refusing to invent a table."
        )
    verified_path = ROOT / "data" / "paraphrases" / "verified_ids.txt"
    verified = {
        line.strip()
        for line in verified_path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    }
    tasks = all_tasks(verified_ids=verified)
    rows = read_jsonl(class_path, Classification)
    if not rows:
        raise SystemExit("classification log is empty; no statistics to report")
    frame = headline_frame(tasks, rows)
    out = ROOT / "data" / "logs" / "headline_table.csv"
    frame.to_csv(out, index=False)
    print(frame.to_string(index=False))
    print(overlap_note(frame))
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

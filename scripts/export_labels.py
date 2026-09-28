#!/usr/bin/env python3
"""Export constructed fixtures and pass-1 labels. Does not write pass 2."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

from ambisense.catalog.fixtures import fixture_bundle
from ambisense.io_util import write_jsonl


def main() -> None:
    raws, labels = fixture_bundle()
    write_jsonl(ROOT / "data" / "labels" / "fixtures.jsonl", raws)
    write_jsonl(ROOT / "data" / "labels" / "pass1.jsonl", labels)
    p2 = ROOT / "data" / "labels" / "pass2.jsonl"
    if not p2.exists():
        p2.write_text("", encoding="utf-8")
    print(f"exported {len(raws)} fixtures and {len(labels)} pass-1 labels")
    print("pass2.jsonl left for an independent rater")


if __name__ == "__main__":
    main()

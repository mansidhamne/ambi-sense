#!/usr/bin/env python3
"""Write canonical + paraphrase task JSON under data/tasks/."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

from ambisense.catalog.build import all_canonical_tasks, all_tasks, dump_tasks


def main() -> None:
    verified_path = ROOT / "data" / "paraphrases" / "verified_ids.txt"
    verified: set[str] = set()
    if verified_path.exists():
        verified = {
            line.strip()
            for line in verified_path.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.startswith("#")
        }
    dump_tasks(ROOT / "data" / "tasks" / "canonical.json", all_canonical_tasks())
    dump_tasks(ROOT / "data" / "tasks" / "all.json", all_tasks(verified_ids=verified))
    print(f"exported {len(all_canonical_tasks())} canonical; verified paraphrases={len(verified)}")


if __name__ == "__main__":
    main()

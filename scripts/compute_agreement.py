#!/usr/bin/env python3
"""Cohen's κ and percent agreement between two hand-label passes."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

from ambisense.analysis.agreement import cohen_kappa, percent_agreement
from ambisense.io_util import read_jsonl
from ambisense.schemas import HandLabel


def _index(rows: list[HandLabel]) -> dict[str, HandLabel]:
    return {row.response_id: row for row in rows}


def main() -> None:
    p1 = ROOT / "data" / "labels" / "pass1.jsonl"
    p2 = ROOT / "data" / "labels" / "pass2.jsonl"
    if not p2.exists() or not p2.read_text(encoding="utf-8").strip():
        raise SystemExit(
            "pass2.jsonl is empty. A second independent rater is required; "
            "do not invent a kappa."
        )
    a = _index(read_jsonl(p1, HandLabel))
    b = _index(read_jsonl(p2, HandLabel))
    shared = sorted(set(a) & set(b))
    if not shared:
        raise SystemExit("no shared response_id between passes")
    labels_a = [f"{a[k].outcome.value}|{a[k].silent_failure.value}" for k in shared]
    labels_b = [f"{b[k].outcome.value}|{b[k].silent_failure.value}" for k in shared]
    print(f"n={len(shared)}")
    print(f"percent_agreement={percent_agreement(labels_a, labels_b):.3f}")
    print(f"cohen_kappa={cohen_kappa(labels_a, labels_b):.3f}")


if __name__ == "__main__":
    main()

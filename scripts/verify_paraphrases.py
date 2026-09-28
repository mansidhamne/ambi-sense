#!/usr/bin/env python3
"""Dump canonical vs paraphrase pairs for mandatory human meaning checks."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

from ambisense.catalog.build import all_canonical_tasks
from ambisense.paraphrase.apply import paraphrase_task


def main() -> None:
    lines = [
        "# Paraphrase review",
        "",
        "For each pair: does the paraphrase preserve who/what/constraints?",
        "If yes, add the canonical task_id to data/paraphrases/verified_ids.txt.",
        "",
    ]
    for task in all_canonical_tasks():
        para = paraphrase_task(task)
        lines.append(f"## {task.task_id}")
        lines.append(f"- canonical: {task.instruction}")
        lines.append(f"- paraphrase: {para.instruction}")
        for src, dst in zip(task.tools, para.tools, strict=True):
            if src.description != dst.description:
                lines.append(f"- tool {src.name}: {src.description!r} → {dst.description!r}")
        lines.append("")
    out = ROOT / "data" / "paraphrases" / "REVIEW.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

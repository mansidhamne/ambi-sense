#!/usr/bin/env python3
"""Bar plot of sensitivity/specificity with CI whiskers. Refuses if logs are missing."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]

from ambisense.analysis.bootstrap import bootstrap_all
from ambisense.analysis.tables import group_by_model_domain
from ambisense.catalog.build import all_tasks
from ambisense.io_util import read_jsonl
from ambisense.schemas import Classification


def main() -> None:
    class_path = ROOT / "data" / "logs" / "classifications.jsonl"
    if not class_path.exists():
        raise SystemExit("no classification log; refusing to draw a plot")
    verified_path = ROOT / "data" / "paraphrases" / "verified_ids.txt"
    verified = {
        line.strip()
        for line in verified_path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    }
    tasks = all_tasks(verified_ids=verified)
    rows = read_jsonl(class_path, Classification)
    grouped = group_by_model_domain(tasks, rows)
    labels: list[str] = []
    sens: list[float] = []
    spec: list[float] = []
    for (model_id, domain), cell in sorted(grouped.items()):
        cis = bootstrap_all(cell)
        if cis["sensitivity"].point is None or cis["specificity"].point is None:
            continue
        labels.append(f"{model_id}\n{domain}")
        sens.append(cis["sensitivity"].point)
        spec.append(cis["specificity"].point)
    if not labels:
        raise SystemExit("no defined cells to plot")
    x = range(len(labels))
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.bar([i - 0.2 for i in x], sens, width=0.4, label="sensitivity")
    ax.bar([i + 0.2 for i in x], spec, width=0.4, label="specificity")
    ax.set_xticks(list(x), labels, rotation=20, ha="right")
    ax.set_ylim(0, 1)
    ax.legend()
    out = ROOT / "data" / "logs" / "sdt_bars.png"
    fig.tight_layout()
    fig.savefig(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

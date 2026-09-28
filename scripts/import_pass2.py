#!/usr/bin/env python3
"""Import a filled rater CSV into pass2.jsonl. Refuses empty outcome cells."""

from __future__ import annotations

import csv
from pathlib import Path

import typer

ROOT = Path(__file__).resolve().parents[1]

from ambisense.io_util import write_jsonl
from ambisense.schemas import AgentOutcome, HandLabel, SilentFailure

app = typer.Typer(add_completion=False)


def _require(row: dict[str, str], key: str) -> str:
    value = (row.get(key) or "").strip()
    if not value:
        raise ValueError(f"blank {key} for response_id={row.get('response_id')}")
    return value


def row_to_label(row: dict[str, str], rater: str, pass_id: int) -> HandLabel:
    return HandLabel(
        response_id=_require(row, "response_id"),
        task_id=_require(row, "task_id"),
        rater=rater,
        pass_id=pass_id,
        outcome=AgentOutcome(_require(row, "outcome").lower()),
        silent_failure=SilentFailure(_require(row, "silent_failure").lower()),
        notes=(row.get("notes") or "").strip(),
    )


@app.command()
def main(
    csv_path: Path = typer.Option(
        ROOT / "data" / "labels" / "rater2_filled.csv",
        help="Filled copy of rater2_packet.csv",
    ),
    rater: str = typer.Option(..., help="Rater name or initials"),
    pass_id: int = typer.Option(2, help="1 or 2"),
) -> None:
    with csv_path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    labels = [row_to_label(row, rater, pass_id) for row in rows]
    out = ROOT / "data" / "labels" / f"pass{pass_id}.jsonl"
    write_jsonl(out, labels)
    print(f"wrote {len(labels)} pass-{pass_id} labels to {out}")
    print("run: python scripts/compute_agreement.py")


if __name__ == "__main__":
    app()

"""Build the headline results table from classifications."""

from __future__ import annotations

from collections import defaultdict

import pandas as pd

from ambisense.analysis.bootstrap import bootstrap_all, format_ci
from ambisense.schemas import Classification, Domain, SurfaceForm, Task


def group_by_model_domain(
    tasks: list[Task],
    rows: list[Classification],
    surface: SurfaceForm = SurfaceForm.CANONICAL,
) -> dict[tuple[str, str], list[Classification]]:
    task_by_id = {task.task_id: task for task in tasks}
    grouped: dict[tuple[str, str], list[Classification]] = defaultdict(list)
    for row in rows:
        task = task_by_id.get(row.task_id)
        if task is None:
            continue
        if task.surface is not surface and row.surface is not surface:
            continue
        if row.surface is not surface:
            continue
        grouped[(row.model_id, task.domain.value)].append(row)
    return grouped


def headline_frame(
    tasks: list[Task],
    rows: list[Classification],
    n_boot: int = 10_000,
    seed: int = 0,
) -> pd.DataFrame:
    grouped = group_by_model_domain(tasks, rows)
    records: list[dict[str, object]] = []
    for (model_id, domain), cell_rows in sorted(grouped.items()):
        cis = bootstrap_all(cell_rows, n_boot=n_boot, seed=seed)
        records.append(
            {
                "model": model_id,
                "domain": domain,
                "n": len(cell_rows),
                "sensitivity": format_ci(cis["sensitivity"]),
                "specificity": format_ci(cis["specificity"]),
                "youden_j": format_ci(cis["youden_j"]),
            }
        )
    return pd.DataFrame.from_records(records)


def overlap_note(frame: pd.DataFrame) -> str:
    """Do not rank models whose CIs we cannot even parse as disjoint here.

    The writeup must inspect the numeric CIs. This helper only reminds
    the operator that overlapping intervals forbid a winner declaration.
    """
    del frame
    return (
        "If two models' 95% CIs overlap on a metric, do not declare a winner. "
        "State the overlap explicitly."
    )


def domain_counts(tasks: list[Task]) -> dict[tuple[Domain, object], int]:
    tally: dict[tuple[Domain, object], int] = defaultdict(int)
    for task in tasks:
        tally[(task.domain, task.ambiguity)] += 1
    return dict(tally)

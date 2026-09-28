"""Percentile bootstrap CIs. Never report a bare point estimate."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ambisense.analysis.metrics import sdt_metrics
from ambisense.schemas import Classification


@dataclass(frozen=True)
class MetricCI:
    name: str
    point: float | None
    lo: float | None
    hi: float | None
    n_valid_replicates: int


def _percentile(values: list[float], q: float) -> float:
    return float(np.percentile(np.asarray(values, dtype=float), q))


def bootstrap_metric(
    rows: list[Classification],
    attr: str,
    n_boot: int = 10_000,
    seed: int = 0,
) -> MetricCI:
    point = getattr(sdt_metrics(rows), attr)
    if not rows:
        return MetricCI(attr, None, None, None, 0)
    rng = np.random.default_rng(seed)
    n = len(rows)
    valid: list[float] = []
    for _ in range(n_boot):
        idx = rng.integers(0, n, size=n)
        sample = [rows[i] for i in idx]
        value = getattr(sdt_metrics(sample), attr)
        if value is not None:
            valid.append(float(value))
    if not valid:
        return MetricCI(attr, point, None, None, 0)
    lo = _percentile(valid, 2.5)
    hi = _percentile(valid, 97.5)
    return MetricCI(attr, point, lo, hi, len(valid))


def bootstrap_all(
    rows: list[Classification], n_boot: int = 10_000, seed: int = 0
) -> dict[str, MetricCI]:
    return {
        name: bootstrap_metric(rows, name, n_boot=n_boot, seed=seed)
        for name in ("sensitivity", "specificity", "youden_j")
    }


def format_ci(ci: MetricCI) -> str:
    if ci.point is None or ci.lo is None or ci.hi is None:
        return "NA (undefined cell)"
    return f"{ci.point:.3f} [{ci.lo:.3f}, {ci.hi:.3f}]"

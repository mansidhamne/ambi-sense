"""Sensitivity, specificity, Youden's J from SDT cells."""

from __future__ import annotations

from dataclasses import dataclass

from ambisense.schemas import Classification, SDTCell


@dataclass(frozen=True)
class SDTMetrics:
    n: int
    hits: int
    misses: int
    false_alarms: int
    correct_rejections: int
    sensitivity: float | None
    specificity: float | None
    youden_j: float | None


def _safe_div(num: int, den: int) -> float | None:
    if den == 0:
        return None
    return num / den


def counts(rows: list[Classification]) -> dict[SDTCell, int]:
    tally = {cell: 0 for cell in SDTCell}
    for row in rows:
        tally[row.sdt_cell] += 1
    return tally


def sdt_metrics(rows: list[Classification]) -> SDTMetrics:
    tally = counts(rows)
    hits = tally[SDTCell.HIT]
    misses = tally[SDTCell.MISS]
    false_alarms = tally[SDTCell.FALSE_ALARM]
    correct_rejections = tally[SDTCell.CORRECT_REJECTION]
    sens = _safe_div(hits, hits + misses)
    spec = _safe_div(correct_rejections, correct_rejections + false_alarms)
    youden = None if sens is None or spec is None else sens + spec - 1
    return SDTMetrics(
        n=len(rows),
        hits=hits,
        misses=misses,
        false_alarms=false_alarms,
        correct_rejections=correct_rejections,
        sensitivity=sens,
        specificity=spec,
        youden_j=youden,
    )

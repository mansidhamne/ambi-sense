"""Dual-pass agreement: raw percent and Cohen's κ."""

from __future__ import annotations

from collections import Counter


def percent_agreement(a: list[str], b: list[str]) -> float:
    if len(a) != len(b):
        raise ValueError("label lists must be the same length")
    if not a:
        return float("nan")
    return sum(x == y for x, y in zip(a, b, strict=True)) / len(a)


def cohen_kappa(a: list[str], b: list[str]) -> float:
    """Cohen's κ for two raters, same item order."""
    if len(a) != len(b):
        raise ValueError("label lists must be the same length")
    n = len(a)
    if n == 0:
        return float("nan")
    p_o = percent_agreement(a, b)
    labels = sorted(set(a) | set(b))
    count_a = Counter(a)
    count_b = Counter(b)
    p_e = sum((count_a[lab] / n) * (count_b[lab] / n) for lab in labels)
    if p_e == 1.0:
        return 1.0
    return (p_o - p_e) / (1.0 - p_e)

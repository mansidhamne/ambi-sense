"""BFCL-style structural match: tool name + required argument equality.

Argument values are compared as strings after stripping and lowercasing
when both sides are strings. Extra arguments on the prediction are allowed.
Missing gold arguments are a non-match.
"""

from __future__ import annotations

from typing import Any

from ambisense.schemas import GoldResolution, ToolCall


def _norm(value: Any) -> str:
    if isinstance(value, str):
        return value.strip().lower()
    return str(value)


def call_matches_gold(pred: ToolCall, gold: GoldResolution) -> bool:
    if pred.name != gold.tool_call.name:
        return False
    for key, expected in gold.tool_call.arguments.items():
        if key not in pred.arguments:
            return False
        if _norm(pred.arguments[key]) != _norm(expected):
            return False
    return True


def first_matching_gold(
    pred_calls: list[ToolCall], golds: list[GoldResolution]
) -> int | None:
    for pred in pred_calls:
        for idx, gold in enumerate(golds):
            if call_matches_gold(pred, gold):
                return idx
    return None

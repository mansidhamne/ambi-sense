"""Flag tool arguments that invent entities absent from the task."""

from __future__ import annotations

import re
from typing import Any

from ambisense.schemas import Task, ToolCall

_ID_LIKE = re.compile(
    r"\b(?:PT-[A-Z]{2}-\d{4}|ORD-\d{4}|PNR-[A-Z0-9]{6}|HX-\d+|NMB-\d+)\b"
)


def _haystack(task: Task) -> str:
    parts = [task.instruction, *task.allowed_entities]
    for tool in task.tools:
        parts.append(tool.name)
        parts.append(tool.description)
        parts.append(str(tool.parameters))
    for gold in task.gold_resolutions:
        parts.append(gold.tool_call.name)
        parts.append(str(gold.tool_call.arguments))
    return " ".join(parts)


def _values(obj: Any) -> list[str]:
    if isinstance(obj, dict):
        out: list[str] = []
        for value in obj.values():
            out.extend(_values(value))
        return out
    if isinstance(obj, list):
        out = []
        for item in obj:
            out.extend(_values(item))
        return out
    if isinstance(obj, str):
        return [obj]
    return []


def invented_entities(task: Task, calls: list[ToolCall]) -> list[str]:
    """Return argument strings that look like IDs and are not in the task."""
    known = _haystack(task)
    invented: list[str] = []
    for call in calls:
        for raw in _values(call.arguments):
            for match in _ID_LIKE.findall(raw):
                if match not in known:
                    invented.append(match)
    return invented

"""Deterministic surface-form rewrites. No LLM involved.

Each rule is a whole-word substitution or a fixed wrapper. Meaning must still
be checked by a human; `paraphrase_verified` stays False until that check.

Substitutions are collected on the *original* string so replacements cannot
chain (book→reserve→hold would silently break the control).
"""

from __future__ import annotations

import re

# Longer phrases first.
INSTRUCTION_SUBS: tuple[tuple[str, str], ...] = (
    (r"\bI need you to\b", "Please"),
    (r"\bCould you\b", "Please"),
    (r"\bCan you\b", "Please"),
    (r"\bbook\b", "reserve"),
    (r"\bcancel\b", "void"),
    (r"\bschedule\b", "place on the calendar"),
    (r"\blook up\b", "retrieve"),
    (r"\blookup\b", "retrieve"),
    (r"\bcompute\b", "calculate"),
    (r"\bpatient\b", "chart subject"),
    (r"\bpatients\b", "chart subjects"),
    (r"\border\b", "purchase"),
    (r"\bflight\b", "itinerary"),
    (r"\bflights\b", "itineraries"),
)

DOCSTRING_SUBS: tuple[tuple[str, str], ...] = (
    (r"^Returns\b", "Yields"),
    (r"^Return\b", "Yield"),
    (r"^Gets\b", "Retrieves"),
    (r"^Get\b", "Retrieve"),
    (r"^Creates\b", "Opens"),
    (r"^Create\b", "Open"),
    (r"^Books\b", "Reserves"),
    (r"^Book\b", "Reserve"),
    (r"^Cancels\b", "Voids"),
    (r"^Cancel\b", "Void"),
    (r"\bpatient\b", "chart subject"),
    (r"\bpatients\b", "chart subjects"),
)


def _span_taken(flags: list[bool], start: int, end: int) -> bool:
    return any(flags[start:end])


def _mark_span(flags: list[bool], start: int, end: int) -> None:
    for idx in range(start, end):
        flags[idx] = True


def _collect_replacements(
    text: str, rules: tuple[tuple[str, str], ...]
) -> list[tuple[int, int, str]]:
    flags = [False] * len(text)
    found: list[tuple[int, int, str]] = []
    for pattern, repl in rules:
        for match in re.finditer(pattern, text, flags=re.IGNORECASE):
            if _span_taken(flags, match.start(), match.end()):
                continue
            _mark_span(flags, match.start(), match.end())
            found.append((match.start(), match.end(), repl))
    found.sort()
    return found


def _splice(text: str, replacements: list[tuple[int, int, str]]) -> str:
    parts: list[str] = []
    cursor = 0
    for start, end, repl in replacements:
        parts.append(text[cursor:start])
        parts.append(repl)
        cursor = end
    parts.append(text[cursor:])
    return "".join(parts)


def apply_subs(text: str, rules: tuple[tuple[str, str], ...]) -> str:
    return _splice(text, _collect_replacements(text, rules))


def cap_first(text: str) -> str:
    if not text:
        return text
    return text[0].upper() + text[1:]


def reorder_two_clauses(text: str) -> str:
    """Swap two sentences. Split only on period+space, never on .pdf or @a.b."""
    stripped = text.strip()
    if stripped.endswith("."):
        stripped = stripped[:-1]
    parts = [part.strip() for part in re.split(r"\.\s+", stripped) if part.strip()]
    if len(parts) != 2:
        return text
    return f"{cap_first(parts[1])}. {cap_first(parts[0])}."


def wrap_instruction(text: str) -> str:
    stripped = text.rstrip()
    if stripped.endswith("."):
        stripped = stripped[:-1]
    return f"Kindly carry out the following request: {cap_first(stripped)}."

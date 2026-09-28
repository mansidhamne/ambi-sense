"""Rule-based detection of clarification / refusal text."""

from __future__ import annotations

import re

_CLARIFY_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\bwhich\b", re.I),
    re.compile(r"\bwhose\b", re.I),
    re.compile(r"\bclarify\b", re.I),
    re.compile(r"\bclarif(?:y|ication)\b", re.I),
    re.compile(r"\bmore (?:info|information|details)\b", re.I),
    re.compile(r"\bunderspecif", re.I),
    re.compile(r"\bambig", re.I),
    re.compile(r"\bneed to know\b", re.I),
    re.compile(r"\bcould you (?:specify|confirm|tell)\b", re.I),
    re.compile(r"\bplease (?:specify|confirm|provide)\b", re.I),
    re.compile(r"\bnot (?:sure|enough|clear)\b", re.I),
    re.compile(r"\bcannot (?:proceed|complete|determine)\b", re.I),
    re.compile(r"\bcan't (?:proceed|complete|determine)\b", re.I),
    re.compile(r"\bwhich (?:one|patient|order|flight|record)\b", re.I),
)


def looks_like_clarify(text: str) -> bool:
    if not text or not text.strip():
        return False
    if "?" in text:
        return True
    return any(pat.search(text) for pat in _CLARIFY_PATTERNS)

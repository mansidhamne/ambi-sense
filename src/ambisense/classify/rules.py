"""Rule-based outcome assignment. Returns None if the case is unresolvable."""

from __future__ import annotations

from ambisense.classify.ast_match import first_matching_gold
from ambisense.classify.silent_failure import invented_entities
from ambisense.classify.text_signals import looks_like_clarify
from ambisense.schemas import AgentOutcome, RawResponse, SilentFailure, Task


def rule_classify(
    task: Task, response: RawResponse
) -> tuple[AgentOutcome, SilentFailure, int | None, str] | None:
    """Return (outcome, silent_failure, gold_index, rationale) or None.

    None means: route to the LLM judge. Used only when there is text that
    does not look like a clarify *and* there are no parseable tool calls.
    """
    calls = response.tool_calls
    if calls:
        invented = invented_entities(task, calls)
        silent = SilentFailure.INVENTED_ENTITY if invented else SilentFailure.NONE
        gold_idx = first_matching_gold(calls, task.gold_resolutions)
        note = "tool_call"
        if invented:
            note = f"tool_call invented={invented}"
        return AgentOutcome.ACT, silent, gold_idx, note

    if looks_like_clarify(response.text):
        return AgentOutcome.CLARIFY, SilentFailure.NONE, None, "clarify_text"

    if not response.text.strip():
        return AgentOutcome.CLARIFY, SilentFailure.NONE, None, "empty_output"

    return None

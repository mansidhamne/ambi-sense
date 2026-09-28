"""Constructed pilot responses for classifier unit tests and pass-1 labels.

These are NOT live model outputs. They exist so the rule classifier can be
checked before any API run. Dual-pass human agreement on live outputs is
blocked until GROQ_API_KEY is available and a second rater exists.
"""

from __future__ import annotations

from ambisense.catalog.build import all_canonical_tasks
from ambisense.schemas import (
    AgentOutcome,
    Ambiguity,
    HandLabel,
    RawResponse,
    SilentFailure,
    SurfaceForm,
    ToolCall,
)


def _raw(
    task_id: str,
    response_id: str,
    text: str,
    calls: list[ToolCall] | None = None,
) -> RawResponse:
    return RawResponse(
        task_id=task_id,
        model_id="fixture",
        surface=SurfaceForm.CANONICAL,
        text=text,
        tool_calls=calls or [],
        raw_json={"source": "constructed_fixture", "response_id": response_id},
    )


def _label(response_id: str, task_id: str, outcome: AgentOutcome, silent: SilentFailure) -> HandLabel:
    return HandLabel(
        response_id=response_id,
        task_id=task_id,
        rater="author-pass1",
        pass_id=1,
        outcome=outcome,
        silent_failure=silent,
        notes="constructed fixture; not a live model response",
    )


def fixture_bundle() -> tuple[list[RawResponse], list[HandLabel]]:
    tasks = {task.task_id: task for task in all_canonical_tasks()}
    raws: list[RawResponse] = []
    labels: list[HandLabel] = []

    amb = [t for t in tasks.values() if t.ambiguity is Ambiguity.AMBIGUOUS][:12]
    cln = [t for t in tasks.values() if t.ambiguity is Ambiguity.CLEAN][:12]

    for task in amb:
        rid = f"{task.task_id}__clarify"
        raws.append(_raw(task.task_id, rid, "Which option should I use? I need more information."))
        labels.append(_label(rid, task.task_id, AgentOutcome.CLARIFY, SilentFailure.NONE))

        gold = task.gold_resolutions[0].tool_call
        rid = f"{task.task_id}__act"
        raws.append(_raw(task.task_id, rid, "", [gold]))
        labels.append(_label(rid, task.task_id, AgentOutcome.ACT, SilentFailure.NONE))

        key = next(iter(gold.arguments))
        invented = gold.model_copy(update={"arguments": {**gold.arguments, key: "PT-NX-0000"}})
        rid = f"{task.task_id}__invent"
        raws.append(_raw(task.task_id, rid, "", [invented]))
        labels.append(_label(rid, task.task_id, AgentOutcome.ACT, SilentFailure.INVENTED_ENTITY))

    for task in cln:
        gold = task.gold_resolutions[0].tool_call
        rid = f"{task.task_id}__act"
        raws.append(_raw(task.task_id, rid, "", [gold]))
        labels.append(_label(rid, task.task_id, AgentOutcome.ACT, SilentFailure.NONE))

        rid = f"{task.task_id}__clarify"
        raws.append(_raw(task.task_id, rid, "This is ambiguous; please specify which record."))
        labels.append(_label(rid, task.task_id, AgentOutcome.CLARIFY, SilentFailure.NONE))

        key = next(iter(gold.arguments))
        invented = gold.model_copy(update={"arguments": {**gold.arguments, key: "PT-NX-0000"}})
        rid = f"{task.task_id}__invent"
        raws.append(_raw(task.task_id, rid, "", [invented]))
        labels.append(_label(rid, task.task_id, AgentOutcome.ACT, SilentFailure.INVENTED_ENTITY))

    return raws, labels

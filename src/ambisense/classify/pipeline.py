"""Classify a response: rules first, judge only if rules return None."""

from __future__ import annotations

from ambisense.classify.judge import ChatFn, judge_classify
from ambisense.classify.rules import rule_classify
from ambisense.schemas import Classification, RawResponse, Task
from ambisense.sdt import sdt_cell


def classify_response(
    task: Task,
    response: RawResponse,
    chat: ChatFn | None = None,
) -> Classification:
    ruled = rule_classify(task, response)
    if ruled is not None:
        outcome, silent, gold_idx, rationale = ruled
        return Classification(
            task_id=task.task_id,
            model_id=response.model_id,
            surface=response.surface,
            outcome=outcome,
            silent_failure=silent,
            sdt_cell=sdt_cell(task.ambiguity, outcome),
            matched_gold_index=gold_idx,
            classifier_source="rules",
            rationale=rationale,
        )
    if chat is None:
        raise RuntimeError(
            f"unresolvable response for {task.task_id}; judge not provided"
        )
    outcome, silent, rationale, judge_id = judge_classify(task, response, chat)
    return Classification(
        task_id=task.task_id,
        model_id=response.model_id,
        surface=response.surface,
        outcome=outcome,
        silent_failure=silent,
        sdt_cell=sdt_cell(task.ambiguity, outcome),
        matched_gold_index=None,
        classifier_source=f"judge:{judge_id}",
        rationale=rationale,
    )

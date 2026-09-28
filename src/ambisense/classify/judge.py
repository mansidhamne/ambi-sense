"""LLM-judge fallback. Judge family must differ from the model under test."""

from __future__ import annotations

import json
from typing import Any, Protocol

from ambisense.schemas import AgentOutcome, RawResponse, SilentFailure, Task

_JUDGE_BY_FAMILY: dict[str, str] = {
    "openai": "qwen/qwen3.6-27b",
    "qwen": "openai/gpt-oss-20b",
}


class ChatFn(Protocol):
    def __call__(
        self, model_id: str, messages: list[dict[str, str]], **kwargs: Any
    ) -> str:
        ...


def judge_model_for(tested_model_id: str) -> str:
    family = tested_model_id.split("/")[0]
    if family not in _JUDGE_BY_FAMILY:
        raise ValueError(f"No cross-family judge configured for {tested_model_id}")
    return _JUDGE_BY_FAMILY[family]


def _parse_judge_json(text: str) -> tuple[AgentOutcome, SilentFailure, str]:
    start = text.find("{")
    end = text.rfind("}")
    if start < 0 or end < 0:
        raise ValueError("judge returned no JSON object")
    payload = json.loads(text[start : end + 1])
    outcome = AgentOutcome(payload["outcome"])
    silent = SilentFailure(payload.get("silent_failure", "none"))
    return outcome, silent, str(payload.get("rationale", ""))


def judge_classify(
    task: Task,
    response: RawResponse,
    chat: ChatFn,
) -> tuple[AgentOutcome, SilentFailure, str, str]:
    judge_id = judge_model_for(response.model_id)
    prompt = (
        "Classify the agent response. Reply with JSON only:\n"
        '{"outcome":"clarify"|"act","silent_failure":"none"|"invented_entity",'
        '"rationale":"..."}\n'
        "CLARIFY = asked a question or refused to call a tool.\n"
        "ACT = issued or clearly intended a tool call.\n"
        f"instruction: {task.instruction}\n"
        f"response_text: {response.text}\n"
        f"tool_calls: {response.tool_calls}\n"
    )
    raw = chat(judge_id, [{"role": "user", "content": prompt}], temperature=0)
    outcome, silent, rationale = _parse_judge_json(raw)
    return outcome, silent, rationale, judge_id

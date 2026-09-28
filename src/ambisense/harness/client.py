"""OpenAI-compatible Groq client used by the harness and the judge."""

from __future__ import annotations

import json
import time
from typing import Any

from openai import OpenAI

from ambisense.harness.config import MAX_COMPLETION_TOKENS, GroqSettings
from ambisense.harness.pacing import RequestPacer
from ambisense.schemas import RawResponse, SurfaceForm, ToolCall, ToolSpec


def tools_to_openai(tools: list[ToolSpec]) -> list[dict[str, Any]]:
    return [
        {
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "parameters": tool.parameters,
            },
        }
        for tool in tools
    ]


def _parse_tool_calls(message: Any) -> list[ToolCall]:
    raw = getattr(message, "tool_calls", None) or []
    parsed: list[ToolCall] = []
    for item in raw:
        fn = item.function
        args = fn.arguments or "{}"
        if isinstance(args, str):
            try:
                loaded = json.loads(args)
            except json.JSONDecodeError:
                loaded = {"_unparsed": args}
        else:
            loaded = dict(args)
        parsed.append(ToolCall(name=fn.name, arguments=loaded))
    return parsed


class GroqChatClient:
    def __init__(self, settings: GroqSettings | None = None) -> None:
        self.settings = settings or GroqSettings.from_env()
        self.pacer = RequestPacer(self.settings.min_interval_sec)
        self.tokens_used: dict[str, int] = {}
        self._client = OpenAI(
            api_key=self.settings.api_key,
            base_url=self.settings.base_url,
        )

    def chat(self, model_id: str, messages: list[dict[str, str]], **kwargs: Any) -> str:
        data = self._create(model_id, messages, tools=None, **kwargs)
        return data.choices[0].message.content or ""

    def complete_task(
        self,
        model_id: str,
        instruction: str,
        tools: list[ToolSpec],
        task_id: str,
        surface: SurfaceForm,
    ) -> RawResponse:
        messages = [{"role": "user", "content": instruction}]
        data = self._create(model_id, messages, tools=tools_to_openai(tools))
        choice = data.choices[0]
        message = choice.message
        return RawResponse(
            task_id=task_id,
            model_id=model_id,
            surface=surface,
            text=message.content or "",
            tool_calls=_parse_tool_calls(message),
            raw_json=data.model_dump(),
            finish_reason=choice.finish_reason,
        )

    def _create(
        self,
        model_id: str,
        messages: list[dict[str, str]],
        tools: list[dict[str, Any]] | None,
        **kwargs: Any,
    ) -> Any:
        self.pacer.wait()
        payload: dict[str, Any] = {
            "model": model_id,
            "messages": messages,
            "temperature": kwargs.get("temperature", self.settings.temperature),
            "seed": kwargs.get("seed", self.settings.seed),
            "max_tokens": kwargs.get("max_tokens", MAX_COMPLETION_TOKENS),
        }
        if model_id.startswith("openai/"):
            payload["extra_body"] = {"reasoning_effort": "low"}
        if tools:
            payload["tools"] = tools
            payload["tool_choice"] = "auto"
        data = self._retry(payload)
        self._add_usage(model_id, data)
        return data

    def _add_usage(self, model_id: str, data: Any) -> None:
        usage = getattr(data, "usage", None)
        total = int(getattr(usage, "total_tokens", 0) or 0) if usage else 0
        self.tokens_used[model_id] = self.tokens_used.get(model_id, 0) + total

    def _retry(self, payload: dict[str, Any]) -> Any:
        delay = 2.0
        last_error: Exception | None = None
        for _ in range(5):
            try:
                return self._client.chat.completions.create(**payload)
            except Exception as exc:  # noqa: BLE001 — surface rate-limit then retry
                last_error = exc
                if "429" not in str(exc) and "rate" not in str(exc).lower():
                    raise
                time.sleep(delay)
                delay = min(delay * 2, 60.0)
        raise RuntimeError(f"Groq retries exhausted: {last_error}")

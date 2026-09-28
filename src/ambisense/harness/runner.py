"""Checkpointed experiment loop. A 429 must not force a full re-run."""

from __future__ import annotations

import json
from pathlib import Path

from ambisense.classify.pipeline import classify_response
from ambisense.harness.client import GroqChatClient
from ambisense.harness.config import TPD_SOFT_LIMIT
from ambisense.io_util import append_jsonl, checkpoint_ids
from ambisense.schemas import Classification, RawResponse, Task


def _key(model_id: str, task: Task) -> str:
    return f"{model_id}|{task.task_id}|{task.surface.value}"


def _stamp_id(raw: RawResponse, key: str) -> RawResponse:
    payload = dict(raw.raw_json)
    payload["response_id"] = key
    return raw.model_copy(update={"raw_json": payload})


def run_one(
    client: GroqChatClient,
    model_id: str,
    task: Task,
    raw_path: Path,
    class_path: Path,
) -> Classification:
    key = _key(model_id, task)
    raw = client.complete_task(
        model_id=model_id,
        instruction=task.instruction,
        tools=task.tools,
        task_id=task.task_id,
        surface=task.surface,
    )
    raw = _stamp_id(raw, key)
    append_jsonl(raw_path, raw)
    labeled = classify_response(task, raw, chat=client.chat)
    append_jsonl(class_path, labeled)
    print(
        f"{key} outcome={labeled.outcome.value} src={labeled.classifier_source}",
        flush=True,
    )
    return labeled


def _append_error(path: Path, model_id: str, task: Task, exc: Exception) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "model_id": model_id,
        "task_id": task.task_id,
        "surface": task.surface.value,
        "error": str(exc),
    }
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record) + "\n")


def run_checkpointed(
    client: GroqChatClient,
    models: list[str],
    tasks: list[Task],
    raw_path: Path,
    class_path: Path,
) -> list[Classification]:
    done = checkpoint_ids(raw_path)
    skipped_path = raw_path.parent / "skipped.jsonl"
    error_path = raw_path.parent / "errors.jsonl"
    results: list[Classification] = []
    halted: set[str] = set()
    for model_id in models:
        for task in tasks:
            if model_id in halted:
                continue
            if _key(model_id, task) in done:
                continue
            used = client.tokens_used.get(model_id, 0)
            if used >= TPD_SOFT_LIMIT:
                _append_error(
                    skipped_path,
                    model_id,
                    task,
                    RuntimeError(f"soft TPD {TPD_SOFT_LIMIT} reached ({used})"),
                )
                halted.add(model_id)
                print(f"halt {model_id} tokens={used}", flush=True)
                continue
            try:
                results.append(run_one(client, model_id, task, raw_path, class_path))
            except Exception as exc:  # noqa: BLE001 — log and continue
                _append_error(error_path, model_id, task, exc)
                print(f"ERROR {_key(model_id, task)} {exc}", flush=True)
    return results


def classify_logged(
    tasks: list[Task],
    raw_rows: list[RawResponse],
    client: GroqChatClient | None,
) -> list[Classification]:
    by_id = {task.task_id: task for task in tasks}
    out: list[Classification] = []
    chat = client.chat if client else None
    for raw in raw_rows:
        task = by_id[raw.task_id]
        out.append(classify_response(task, raw, chat=chat))
    return out

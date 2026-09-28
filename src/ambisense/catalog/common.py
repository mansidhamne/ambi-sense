"""Helpers for building task objects without copying schema boilerplate."""

from __future__ import annotations

from typing import Any

from ambisense.schemas import (
    Ambiguity,
    Domain,
    GoldResolution,
    SurfaceForm,
    Task,
    ToolCall,
    ToolSpec,
)


def params(required: dict[str, str], optional: dict[str, str] | None = None) -> dict[str, Any]:
    properties = {key: {"type": "string", "description": desc} for key, desc in required.items()}
    if optional:
        properties.update(
            {key: {"type": "string", "description": desc} for key, desc in optional.items()}
        )
    return {
        "type": "object",
        "properties": properties,
        "required": list(required),
    }


def tool(name: str, description: str, required: dict[str, str], optional: dict[str, str] | None = None) -> ToolSpec:
    return ToolSpec(name=name, description=description, parameters=params(required, optional))


def gold(name: str, **arguments: Any) -> GoldResolution:
    return GoldResolution(tool_call=ToolCall(name=name, arguments=arguments))


def make_task(
    task_id: str,
    domain: Domain,
    ambiguity: Ambiguity,
    source: str,
    instruction: str,
    tools: list[ToolSpec],
    golds: list[GoldResolution],
    entities: list[str],
    notes: str = "",
) -> Task:
    return Task(
        task_id=task_id,
        domain=domain,
        ambiguity=ambiguity,
        surface=SurfaceForm.CANONICAL,
        source=source,
        instruction=instruction,
        tools=tools,
        gold_resolutions=golds,
        allowed_entities=entities,
        notes=notes,
    )

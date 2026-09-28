"""Apply template paraphrases to a task. Does not set verified=True."""

from __future__ import annotations

from copy import deepcopy

from ambisense.paraphrase.templates import (
    DOCSTRING_SUBS,
    INSTRUCTION_SUBS,
    apply_subs,
    reorder_two_clauses,
    wrap_instruction,
)
from ambisense.schemas import SurfaceForm, Task, ToolSpec


def paraphrase_tools(tools: list[ToolSpec]) -> list[ToolSpec]:
    rewritten: list[ToolSpec] = []
    for tool in tools:
        desc = apply_subs(tool.description, DOCSTRING_SUBS)
        rewritten.append(tool.model_copy(update={"description": desc}))
    return rewritten


def paraphrase_task(task: Task) -> Task:
    """Return a new task with surface=paraphrase. Human must still verify."""
    if task.surface is SurfaceForm.PARAPHRASE:
        raise ValueError(f"{task.task_id} is already a paraphrase")
    cloned = deepcopy(task)
    instruction = apply_subs(task.instruction, INSTRUCTION_SUBS)
    instruction = reorder_two_clauses(instruction)
    instruction = wrap_instruction(instruction)
    return cloned.model_copy(
        update={
            "task_id": f"{task.task_id}__p",
            "surface": SurfaceForm.PARAPHRASE,
            "instruction": instruction,
            "tools": paraphrase_tools(task.tools),
            "paraphrase_of": task.task_id,
            "paraphrase_verified": False,
        }
    )

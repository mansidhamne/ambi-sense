"""Shared Pydantic schemas for tasks, responses, and SDT labels."""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, model_validator


class Domain(str, Enum):
    GENERAL = "general"
    CLINICAL = "clinical"


class Ambiguity(str, Enum):
    AMBIGUOUS = "ambiguous"
    CLEAN = "clean"


class SurfaceForm(str, Enum):
    CANONICAL = "canonical"
    PARAPHRASE = "paraphrase"


class AgentOutcome(str, Enum):
    CLARIFY = "clarify"
    ACT = "act"


class SilentFailure(str, Enum):
    NONE = "none"
    INVENTED_ENTITY = "invented_entity"
    UNKNOWN = "unknown"


class SDTCell(str, Enum):
    HIT = "hit"
    MISS = "miss"
    FALSE_ALARM = "false_alarm"
    CORRECT_REJECTION = "correct_rejection"


class ToolSpec(BaseModel):
    name: str
    description: str
    parameters: dict[str, Any]


class ToolCall(BaseModel):
    name: str
    arguments: dict[str, Any] = Field(default_factory=dict)


class GoldResolution(BaseModel):
    """One schema-valid completion of the request."""

    tool_call: ToolCall
    note: str = ""


class Task(BaseModel):
    task_id: str
    domain: Domain
    ambiguity: Ambiguity
    surface: SurfaceForm = SurfaceForm.CANONICAL
    source: str
    instruction: str
    tools: list[ToolSpec]
    gold_resolutions: list[GoldResolution]
    allowed_entities: list[str] = Field(default_factory=list)
    paraphrase_of: str | None = None
    paraphrase_verified: bool | None = None
    notes: str = ""

    @model_validator(mode="after")
    def check_gold_count(self) -> Task:
        n = len(self.gold_resolutions)
        if self.ambiguity is Ambiguity.CLEAN and n != 1:
            raise ValueError(
                f"{self.task_id}: clean tasks must have exactly 1 gold, got {n}"
            )
        if self.ambiguity is Ambiguity.AMBIGUOUS and n < 2:
            raise ValueError(
                f"{self.task_id}: ambiguous tasks must have >=2 golds, got {n}"
            )
        return self


class RawResponse(BaseModel):
    task_id: str
    model_id: str
    surface: SurfaceForm
    text: str
    tool_calls: list[ToolCall] = Field(default_factory=list)
    raw_json: dict[str, Any] = Field(default_factory=dict)
    finish_reason: str | None = None


class Classification(BaseModel):
    task_id: str
    model_id: str
    surface: SurfaceForm
    outcome: AgentOutcome
    silent_failure: SilentFailure
    sdt_cell: SDTCell
    matched_gold_index: int | None = None
    classifier_source: str
    rationale: str = ""


class HandLabel(BaseModel):
    response_id: str
    task_id: str
    rater: str
    pass_id: int
    outcome: AgentOutcome
    silent_failure: SilentFailure
    notes: str = ""

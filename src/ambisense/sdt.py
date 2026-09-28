"""Map (ambiguity, outcome) to a signal-detection cell."""

from ambisense.schemas import AgentOutcome, Ambiguity, SDTCell

_MAP: dict[tuple[Ambiguity, AgentOutcome], SDTCell] = {
    (Ambiguity.AMBIGUOUS, AgentOutcome.CLARIFY): SDTCell.HIT,
    (Ambiguity.AMBIGUOUS, AgentOutcome.ACT): SDTCell.MISS,
    (Ambiguity.CLEAN, AgentOutcome.CLARIFY): SDTCell.FALSE_ALARM,
    (Ambiguity.CLEAN, AgentOutcome.ACT): SDTCell.CORRECT_REJECTION,
}


def sdt_cell(ambiguity: Ambiguity, outcome: AgentOutcome) -> SDTCell:
    """Return the SDT cell. Silent failure does not change the mapping."""
    return _MAP[(ambiguity, outcome)]

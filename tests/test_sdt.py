import unittest

from ambisense.schemas import AgentOutcome, Ambiguity, SDTCell
from ambisense.sdt import sdt_cell


class SDTTests(unittest.TestCase):
    def test_mapping(self) -> None:
        self.assertEqual(sdt_cell(Ambiguity.AMBIGUOUS, AgentOutcome.CLARIFY), SDTCell.HIT)
        self.assertEqual(sdt_cell(Ambiguity.AMBIGUOUS, AgentOutcome.ACT), SDTCell.MISS)
        self.assertEqual(sdt_cell(Ambiguity.CLEAN, AgentOutcome.CLARIFY), SDTCell.FALSE_ALARM)
        self.assertEqual(sdt_cell(Ambiguity.CLEAN, AgentOutcome.ACT), SDTCell.CORRECT_REJECTION)


if __name__ == "__main__":
    unittest.main()

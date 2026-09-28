import unittest

from ambisense.paraphrase.templates import (
    INSTRUCTION_SUBS,
    apply_subs,
    reorder_two_clauses,
)


class ParaphraseTests(unittest.TestCase):
    def test_no_chained_book_to_hold(self) -> None:
        out = apply_subs("Please book the itinerary.", INSTRUCTION_SUBS)
        self.assertIn("reserve", out)
        self.assertNotIn("hold", out)

    def test_compute_does_not_oscillate(self) -> None:
        out = apply_subs("compute the total", INSTRUCTION_SUBS)
        self.assertEqual(out, "calculate the total")

    def test_two_clause_swap(self) -> None:
        out = reorder_two_clauses("Context here. Do the action.")
        self.assertEqual(out, "Do the action. Context here.")

    def test_dots_in_handles_and_extensions(self) -> None:
        handle = "Send the standup recap to @jordan.lee."
        self.assertEqual(reorder_two_clauses(handle), handle)
        path = "Delete the file at /docs/q2_report.pdf."
        self.assertEqual(reorder_two_clauses(path), path)


if __name__ == "__main__":
    unittest.main()

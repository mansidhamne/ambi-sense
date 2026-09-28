import unittest

from ambisense.catalog.build import all_canonical_tasks
from ambisense.catalog.fixtures import fixture_bundle
from ambisense.labeling.packet import shuffled_rows


class PacketTests(unittest.TestCase):
    def test_no_gold_labels_in_packet(self) -> None:
        raws, _labels = fixture_bundle()
        rows = shuffled_rows(all_canonical_tasks(), raws, seed=7)
        self.assertEqual(len(rows), len(raws))
        for row in rows:
            self.assertEqual(row["outcome"], "")
            self.assertEqual(row["silent_failure"], "")
            self.assertNotIn("gold", row)

    def test_shuffle_is_deterministic(self) -> None:
        raws, _ = fixture_bundle()
        tasks = all_canonical_tasks()
        a = [row["response_id"] for row in shuffled_rows(tasks, raws, seed=7)]
        b = [row["response_id"] for row in shuffled_rows(tasks, raws, seed=7)]
        self.assertEqual(a, b)
        self.assertNotEqual(a, [str(r.raw_json["response_id"]) for r in raws])


if __name__ == "__main__":
    unittest.main()

import unittest
from collections import Counter

from ambisense.catalog.build import all_canonical_tasks
from ambisense.schemas import Ambiguity, Domain


class CatalogTests(unittest.TestCase):
    def test_balance_and_ids(self) -> None:
        tasks = all_canonical_tasks()
        counts = Counter((t.domain, t.ambiguity) for t in tasks)
        self.assertEqual(counts[(Domain.GENERAL, Ambiguity.AMBIGUOUS)], 20)
        self.assertEqual(counts[(Domain.GENERAL, Ambiguity.CLEAN)], 20)
        self.assertEqual(counts[(Domain.CLINICAL, Ambiguity.AMBIGUOUS)], 16)
        self.assertEqual(counts[(Domain.CLINICAL, Ambiguity.CLEAN)], 16)
        ids = [t.task_id for t in tasks]
        self.assertEqual(len(ids), len(set(ids)))


if __name__ == "__main__":
    unittest.main()

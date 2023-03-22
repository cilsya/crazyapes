# ------------------------------ Imports (Start) ------------------------------

# Native modules
import unittest

# ------------------------------ Imports (End) --------------------------------


class TypeTest(unittest.TestCase):

    def test_baseline(self):
        # 1 + 1 should equal 2

        a = 1 + 1
        self.assertEqual(a, 2)

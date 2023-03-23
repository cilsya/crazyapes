# ------------------------------ Imports (Start) ------------------------------

# Native modules
import unittest

# Custom modules
import CrazyApes

# ------------------------------ Imports (End) --------------------------------


class TypeTest(unittest.TestCase):

    def test_CrazyApes_has_OnInit(self):
        """
        Check if class have expected interface, OnInit method
        """

        # Check if class has method
        result = hasattr(CrazyApes.CrazyApesApp, 'OnInit')

        # Assert that it is true
        self.assertEqual(True, result)

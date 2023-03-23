# ------------------------------ Imports (Start) ------------------------------

# Native modules
import unittest

# Custom modules
import mage

# ------------------------------ Imports (End) --------------------------------


class TypeTest(unittest.TestCase):

    def test_mage_has_castSpell(self):
        """
        Check if class have expected interface, castSpell method
        """

        # Check if class has method
        result = hasattr(mage.Mage, 'castSpell')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_mage_has_keyPress(self):
        """
        Check if class have expected interface, keyPress method
        """

        # Check if class has method
        result = hasattr(mage.Mage, 'keyPress')

        # Assert that it is true
        self.assertEqual(True, result)

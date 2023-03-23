# ------------------------------ Imports (Start) ------------------------------

# Native modules
import unittest

# Custom modules
import fireball

# ------------------------------ Imports (End) --------------------------------


class TypeTest(unittest.TestCase):

    def test_fireball_has_idleUpdate(self):
        """
        Check if class have expected interface, idleUpdate method
        """

        # Check if class has method
        result = hasattr(fireball.Fireball, 'idleUpdate')

        # Assert that it is true
        self.assertEqual(True, result)

# ------------------------------ Imports (Start) ------------------------------

# Native modules
import unittest

# Custom modules
import enemy

# ------------------------------ Imports (End) --------------------------------


class TypeTest(unittest.TestCase):

    def test_Enemy_has_addGoal(self):
        """
        Check if class have expected interface, addGoal method
        """

        # Check if class has method
        result = hasattr(enemy.Enemy, 'addGoal')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_Enemy_has_idleUpdate(self):
        """
        Check if class have expected interface, idleUpdate method
        """

        # Check if class has method
        result = hasattr(enemy.Enemy, 'idleUpdate')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_Enemy_has_move(self):
        """
        Check if class have expected interface, move method
        """

        # Check if class has method
        result = hasattr(enemy.Enemy, 'move')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_Enemy_has_simulateAI(self):
        """
        Check if class have expected simulateAI, move method
        """

        # Check if class has method
        result = hasattr(enemy.Enemy, 'simulateAI')

        # Assert that it is true
        self.assertEqual(True, result)

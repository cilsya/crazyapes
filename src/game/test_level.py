# ------------------------------ Imports (Start) ------------------------------

# Native modules
import unittest

# Custom modules
import level

# ------------------------------ Imports (End) --------------------------------


class TypeTest(unittest.TestCase):

    def test_level_has_addEnemies(self):
        """
        Check if class have expected interface, addEnemies method
        """

        # Check if class has method
        result = hasattr(level.Level, 'addEnemies')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_level_has_addNPC(self):
        """
        Check if class have expected interface, addNPC method
        """

        # Check if class has method
        result = hasattr(level.Level, 'addNPC')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_level_has_addPlayer(self):
        """
        Check if class have expected interface, addPlayer method
        """

        # Check if class has method
        result = hasattr(level.Level, 'addPlayer')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_level_has_createLevel(self):
        """
        Check if class have expected interface, createLevel method
        """

        # Check if class has method
        result = hasattr(level.Level, 'createLevel')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_level_has_draw(self):
        """
        Check if class have expected interface, draw method
        """

        # Check if class has method
        result = hasattr(level.Level, 'draw')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_level_has_getHeight(self):
        """
        Check if class have expected interface, getHeight method
        """

        # Check if class has method
        result = hasattr(level.Level, 'getHeight')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_level_has_keyPress(self):
        """
        Check if class have expected interface, keyPress method
        """

        # Check if class has method
        result = hasattr(level.Level, 'keyPress')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_level_has_numEnemies(self):
        """
        Check if class have expected interface, numEnemies method
        """

        # Check if class has method
        result = hasattr(level.Level, 'numEnemies')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_level_has_setPlayerStart(self):
        """
        Check if class have expected interface, setPlayerStart method
        """

        # Check if class has method
        result = hasattr(level.Level, 'setPlayerStart')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_level_has_update(self):
        """
        Check if class have expected interface, update method
        """

        # Check if class has method
        result = hasattr(level.Level, 'update')

        # Assert that it is true
        self.assertEqual(True, result)

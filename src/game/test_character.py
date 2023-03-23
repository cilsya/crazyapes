# ------------------------------ Imports (Start) ------------------------------

# Native modules
import unittest

# Custom modules
# import ..game.character as clschk
import character

# ------------------------------ Imports (End) --------------------------------


class TypeTest(unittest.TestCase):

    def test_character_has_keyPress(self):
        """
        Check if class have expected interface, keyPress method
        """

        # Check if class has method
        result = hasattr(character.Character, 'keyPress')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_character_has_addLives(self):
        """
        Check if class have expected interface, addLives method
        """

        # Check if class has method
        result = hasattr(character.Character, 'addLives')

        # Assert that it is true
        self.assertEqual(True, result)

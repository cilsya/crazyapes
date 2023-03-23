# ------------------------------ Imports (Start) ------------------------------

# Native modules
import unittest

# Custom modules
import sprite

# ------------------------------ Imports (End) --------------------------------


class TypeTest(unittest.TestCase):

    def test_Sprite_has_addLives(self):
        """
        Check if class have expected interface, addLives method
        """

        # Check if class has method
        result = hasattr(sprite.Sprite, 'addLives')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_Sprite_has_draw(self):
        """
        Check if class have expected interface, draw method
        """

        # Check if class has method
        result = hasattr(sprite.Sprite, 'draw')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_Sprite_has_erase(self):
        """
        Check if class have expected interface, erase method
        """

        # Check if class has method
        result = hasattr(sprite.Sprite, 'erase')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_Sprite_has_getLives(self):
        """
        Check if class have expected interface, getLives method
        """

        # Check if class has method
        result = hasattr(sprite.Sprite, 'getLives')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_Sprite_has_getPosition(self):
        """
        Check if class have expected interface, getPosition method
        """

        # Check if class has method
        result = hasattr(sprite.Sprite, 'getPosition')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_Sprite_has_getX(self):
        """
        Check if class have expected interface, getX method
        """

        # Check if class has method
        result = hasattr(sprite.Sprite, 'getX')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_Sprite_has_getY(self):
        """
        Check if class have expected interface, getY method
        """

        # Check if class has method
        result = hasattr(sprite.Sprite, 'getY')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_Sprite_has_isAlive(self):
        """
        Check if class have expected interface, isAlive method
        """

        # Check if class has method
        result = hasattr(sprite.Sprite, 'isAlive')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_Sprite_has_isValidLevelMove(self):
        """
        Check if class have expected interface, isValidLevelMove method
        """

        # Check if class has method
        result = hasattr(sprite.Sprite, 'isValidLevelMove')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_Sprite_has_move(self):
        """
        Check if class have expected interface, move method
        """

        # Check if class has method
        result = hasattr(sprite.Sprite, 'move')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_Sprite_has_setCurrentTime(self):
        """
        Check if class have expected interface, setCurrentTime method
        """

        # Check if class has method
        result = hasattr(sprite.Sprite, 'setCurrentTime')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_Sprite_has_setLevel(self):
        """
        Check if class have expected interface, setLevel method
        """

        # Check if class has method
        result = hasattr(sprite.Sprite, 'setLevel')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_Sprite_has_setPosition(self):
        """
        Check if class have expected interface, setPosition method
        """

        # Check if class has method
        result = hasattr(sprite.Sprite, 'setPosition')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_Sprite_has_setSpeed(self):
        """
        Check if class have expected interface, setSpeed method
        """

        # Check if class has method
        result = hasattr(sprite.Sprite, 'setSpeed')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_Sprite_has_updateSprite(self):
        """
        Check if class have expected interface, updateSprite method
        """

        # Check if class has method
        result = hasattr(sprite.Sprite, 'updateSprite')

        # Assert that it is true
        self.assertEqual(True, result)

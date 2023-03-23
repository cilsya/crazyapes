# ------------------------------ Imports (Start) ------------------------------

# Native modules
import unittest

# Custom modules
import drawEngine

# ------------------------------ Imports (End) --------------------------------


class TypeTest(unittest.TestCase):

    def test_DrawEngine_has_createBackgroundTile(self):
        """
        Check if class have expected interface, createBackgroundTile method
        """

        # Check if class has method
        result = hasattr(drawEngine.DrawEngine, 'createBackgroundTile')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_DrawEngine_has_createSprite(self):
        """
        Check if class have expected interface, createSprite method
        """

        # Check if class has method
        result = hasattr(drawEngine.DrawEngine, 'createSprite')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_DrawEngine_has_deleteSprite(self):
        """
        Check if class have expected interface, deleteSprite method
        """

        # Check if class has method
        result = hasattr(drawEngine.DrawEngine, 'deleteSprite')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_DrawEngine_has_drawBackground(self):
        """
        Check if class have expected interface, drawBackground method
        """

        # Check if class has method
        result = hasattr(drawEngine.DrawEngine, 'drawBackground')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_DrawEngine_has_drawSprite(self):
        """
        Check if class have expected interface, drawSprite method
        """

        # Check if class has method
        result = hasattr(drawEngine.DrawEngine, 'drawSprite')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_DrawEngine_has_eraseSprite(self):
        """
        Check if class have expected interface, eraseSprite method
        """

        # Check if class has method
        result = hasattr(drawEngine.DrawEngine, 'eraseSprite')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_DrawEngine_has_setMap(self):
        """
        Check if class have expected interface, setMap method
        """

        # Check if class has method
        result = hasattr(drawEngine.DrawEngine, 'setMap')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_DrawEngine_has_setWindow(self):
        """
        Check if class have expected interface, setWindow method
        """

        # Check if class has method
        result = hasattr(drawEngine.DrawEngine, 'setWindow')

        # Assert that it is true
        self.assertEqual(True, result)

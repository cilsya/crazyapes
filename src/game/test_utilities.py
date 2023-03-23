# ------------------------------ Imports (Start) ------------------------------

# Native modules
import unittest

# Custom modules
import utilities

# ------------------------------ Imports (End) --------------------------------


class TypeTest(unittest.TestCase):

    def test_utilities_has_clear_row(self):
        """
        Check if module have expected interface, clear_row function
        """

        # Check if class has method
        result = hasattr(utilities, 'clear_row')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_utilities_has_clear_row_range(self):
        """
        Check if module have expected interface, clear_row_range function
        """

        # Check if class has method
        result = hasattr(utilities, 'clear_row_range')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_utilities_has_clear_screen(self):
        """
        Check if module have expected interface, clear_screen function
        """

        # Check if class has method
        result = hasattr(utilities, 'clear_screen')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_utilities_has_get_console_cursor_position(self):
        """
        Check if module have expected interface, get_console_cursor_position
        function
        """

        # Check if class has method
        result = hasattr(utilities, 'get_console_cursor_position')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_utilities_has_set_console_cursor_position(self):
        """
        Check if module have expected interface, set_console_cursor_position
        function
        """

        # Check if class has method
        result = hasattr(utilities, 'set_console_cursor_position')

        # Assert that it is true
        self.assertEqual(True, result)

    def test_utilities_has_set_console_cursor_visibility(self):
        """
        Check if module have expected interface, set_console_cursor_visibility
        function
        """

        # Check if class has method
        result = hasattr(utilities, 'set_console_cursor_visibility')

        # Assert that it is true
        self.assertEqual(True, result)

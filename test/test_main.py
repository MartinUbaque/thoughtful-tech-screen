import unittest
from main.sort import sort
class TestSort(unittest.TestCase):
    # Test case 1: Standard package
    # Nwither bulky nor heavy
    def test_sort_standard(self):
        self.assertEqual(sort(2, 3, 4, 5), "STANDARD")
    # Test case 2: Special package
    # Either bulky or heavy
    def test_sort_special(self):
        self.assertEqual(sort(150, 10, 10, 10), "SPECIAL")
    # Test case 3: Rejected package
    # Both bulky and heavy
    def test_sort_rejected(self):
        self.assertEqual(sort(150, 150, 150, 20), "REJECTED")

    # Test case 4: Invalid input
    # Invalid input, such as characters instead of numbers
    def test_sort_character_input(self):
        with self.assertRaisesRegex(ValueError, "Width must be a number"):
            sort("a", 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "Height must be a number"):
            sort(3, "a", 4, 5)
        with self.assertRaisesRegex(ValueError, "Length must be a number"):
            sort(3, 4, "a", 5)
        with self.assertRaisesRegex(ValueError, "Mass must be a number"):
            sort(3, 4, 5, "a")

    # Test case 5: Negative input
    # Another type of invalid input, negative numbers or numbers being 0
    def test_sort_negative_input(self):
        with self.assertRaisesRegex(ValueError, "Width must be greater than 0"):
            sort(-1, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "Height must be greater than 0"):
            sort(3, -1, 4, 5)
        with self.assertRaisesRegex(ValueError, "Length must be greater than 0"):
            sort(3, 4, 0, 5)
        with self.assertRaisesRegex(ValueError, "Mass must be greater than 0"):
            sort(3, 4, 5, 0)

    # Test case 6: String input
    # String input, just as it would be read from a console or a file
    def test_sort_string_numbers(self):
        self.assertEqual(sort("2", "3", "4", "5"), "STANDARD")
        self.assertEqual(sort("150", "10", "10", "10"), "SPECIAL")
        self.assertEqual(sort("150", "150", "150", "20"), "REJECTED")
            

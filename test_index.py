import unittest
from index import add_numbers

class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        result = add_numbers(-2, -3)
        self.assertEqual(result, -6)

    def test_add_mixed_numbers(self):
        result = add_numbers(5, -3)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
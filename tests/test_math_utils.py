# tests/test_math_utils.py

import unittest
from my_app.math_utils import add, divide

class TestMathUtils(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_divide_valid(self):
        self.assertEqual(divide(10, 2), 5.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_subtract(self):
        # Purposely failing test — subtract() not implemented
        from my_app.math_utils import subtract
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        # Purposely failing test — bad math
        result = 2 * 3  # even if you implement this later, it should fail intentionally
        self.assertEqual(result, 5)  # Wrong on purpose

if __name__ == '__main__':
    unittest.main()

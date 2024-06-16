# tests/test_multiply.py

import unittest
import sys
sys.path.append('/root/project/')
from calculator import multiply
print("----------------------------------------------------------------------")
print("Running muliplication test")
print("----------------------------------------------------------------------")
class TestMultiply(unittest.TestCase):

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(3, 5), 15)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-1, 1), -1)

    def test_multiply_mixed_numbers(self):
        self.assertEqual(multiply(-1, -1), 1)

if __name__ == "__main__":
    unittest.main()

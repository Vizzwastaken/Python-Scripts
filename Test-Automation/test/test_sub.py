# tests/test_subtract.py

import unittest
import sys
sys.path.append('/root/project/')
print("----------------------------------------------------------------------")
print("Running subtracttion test")
print("----------------------------------------------------------------------")
from calculator import subtract

class TestSubtract(unittest.TestCase):

    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_zero(self):
        self.assertEqual(subtract(5, 5), 0)

    def test_subtract_negative_result(self):
        self.assertEqual(subtract(-1, 1), -2)

if __name__ == "__main__":
    unittest.main()

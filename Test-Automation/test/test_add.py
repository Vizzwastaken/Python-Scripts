# tests/test_add.py

import unittest
import sys
sys.path.append('/root/project/')
from calculator import add
print("----------------------------------------------------------------------")
print("Running addition test")
print("----------------------------------------------------------------------")
class TestAdd(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, 1), 0)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, -1), -2)

if __name__ == "__main__":
    unittest.main()

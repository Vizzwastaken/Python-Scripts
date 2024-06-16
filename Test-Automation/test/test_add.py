# tests/test_add.py

import unittest
import sys
import os
current_directory = os.getcwd()
print(current_directory)
path = os.path.dirname(os.path.normpath(current_directory))
sys.path.append(path)
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

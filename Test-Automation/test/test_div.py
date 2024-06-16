# tests/test_divide.py

import unittest
import sys
import os

# Get the current working directory
current_directory = os.getcwd()
print("Current Directory:", current_directory)

# Determine the parent directory of the current directory
path = os.path.dirname(os.path.normpath(current_directory))

# Append the parent directory to sys.path to import modules from that directory
sys.path.append(path)

# Import the add function from the 'calculator' module located in the parent directory
from calculator import add

print("----------------------------------------------------------------------")
print("Running division test")
print("----------------------------------------------------------------------")
class TestDivide(unittest.TestCase):

    def test_divide_integer_result(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-1, 1), -1)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)

if __name__ == "__main__":
    unittest.main()

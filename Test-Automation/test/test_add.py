# tests/test_add.py

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

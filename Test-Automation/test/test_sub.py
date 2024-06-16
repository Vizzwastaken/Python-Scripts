# tests/test_subtract.py

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
from calculator import subtract

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

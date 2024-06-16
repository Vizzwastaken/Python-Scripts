# tests/test_multiply.py

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

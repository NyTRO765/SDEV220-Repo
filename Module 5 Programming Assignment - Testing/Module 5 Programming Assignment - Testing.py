"""
Module 5 Programming Assignment - Testing

Author: Tre'tin Alvarez
Description: This script is to complete a homework assignment based on the following URL: https://realpython.com/python-testing/#testing-your-code
Complete the following sections:
    Testing Your Code
    Writing Your First Test
    Executing Your First Test
"""

## Testing Your Code
import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == "__main_":
    unittest.main()

## Writing Your First Test
def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total

## Executing Your First Test
import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
    
    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == "__main_":
    unittest.main()

## End Comments
"""
When I ran the test suite, I got 5 tests executed. Four of them passed (indicated by .) and one failed (indicated by F).
The failing test was test_fraction, which expected the sum of [1/4, 1/4, 2/5] to equal 1, but the function actually returned Fraction(9, 10) (i.e. 0.9). That means my implementation of sum() is not handling fractional inputs (or rational arithmetic) correctly to match that expected behavior.
In practice, this failure is useful: it shows me a specific edge case that my function does not handle as intended. I can use that information to solve this.
Overall, the test results give me confidence in the parts that passed, and point out exactly what is broken or unexpected in the parts that failed.
"""
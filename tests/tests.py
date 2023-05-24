#!venv/bin/python
"""Unit tests for the calculator
"""
import unittest

from src.calculator import calculator


class AddTests(unittest.TestCase):
    """Test cases for calculator's Add function
    """
    def test_addition(self):
        # pylint: disable=missing-function-docstring
        self.assertEqual(2, calculator.add(1, 1))

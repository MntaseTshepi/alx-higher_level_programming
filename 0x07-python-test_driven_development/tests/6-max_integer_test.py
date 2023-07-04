#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered(self):
        """Test an ordered list of integers."""
        ordered = [5, 6, 7, 8]
        self.assertEqual(max_integer(ordered), 8)

    def test_unordered(self):
        """Test an unordered list of integers."""
        unordered = [5, 2, 7, 9]
        self.assertEqual(max_integer(unordered), 9)

    def test_max_at_beg(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [8, 4, 3, 2]
        self.assertEqual(max_integer(max_at_beginning), 8)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element(self):
        """Test a list with a single element."""
        one_element = [6]
        self.assertEqual(max_integer(one_element), 6)

    def test_floats(self):
        """Test a list of floats."""
        floats = [7.53, 6.33, -2.123, 5.2, 6.0]
        self.assertEqual(max_integer(floats), 7.53)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Test a string."""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':

    unittest.main()

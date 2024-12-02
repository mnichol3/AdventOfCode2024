"""
Tests for Day 1 solutions.

Usage
-----
> cd AdventOfCode2024
> python -m unittest tests.test_day1
"""
import unittest

from .__init__ import INPUT_DIR
from day1 import calc_distance, parse_input, quicksort


class TestDay1(unittest.TestCase):
    """Test cases for Day 1."""

    def setUp(self) -> None:
        """Set up before every test case."""
        self.input_path = INPUT_DIR.joinpath('day1_test.txt')
        self.list1, self.list2 = parse_input(self.input_path)

    def test_parse_input(self) -> None:
        """Test parse_input() function."""
        self.assertEqual(self.list1, [3, 4, 2, 1, 3, 3])
        self.assertEqual(self.list2, [4, 3, 5, 3, 9, 3])

    def test_quicksort(self) -> None:
        """Test custom quicksort()."""
        self.assertEqual(quicksort(self.list1), [1, 2, 3, 3, 3, 4])
        self.assertEqual(quicksort(self.list2), [3, 3, 3, 4, 5, 9])

    def test_sample_input(self) -> None:
        """Test calc_distance() with sample input."""
        self.assertEqual(calc_distance(self.list1, self.list2), 11)


if __name__ == '__main__':
    unittest.main()

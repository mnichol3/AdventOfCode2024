"""Tests for Day 1 solutions & helper functions.

Usage
-----
> cd AdventOfCode2024
> python -m unittest tests.test_day1
"""
import unittest

from .__init__ import INPUT_DIR
from day1 import part_1, part_2, parse_input, quicksort


def _get_input() -> tuple[list[int], list[int]]:
    """Parse and return the input lists."""
    return parse_input(INPUT_DIR.joinpath('day1.txt'))


class TestHelpers(unittest.TestCase):
    """Test helper functions."""

    def setUp(self) -> None:
        """Set up before every test case."""
        self.list1, self.list2 = _get_input()

    def test_parse_input(self) -> None:
        """Test parse_input() function."""
        self.assertEqual(self.list1, [3, 4, 2, 1, 3, 3])
        self.assertEqual(self.list2, [4, 3, 5, 3, 9, 3])

    def test_quicksort(self) -> None:
        """Test custom quicksort()."""
        self.assertEqual(quicksort(self.list1), [1, 2, 3, 3, 3, 4])
        self.assertEqual(quicksort(self.list2), [3, 3, 3, 4, 5, 9])


class TestSolutions(unittest.TestCase):
    """Test cases for Day 1 solutions."""

    def setUp(self) -> None:
        """Set up before every test case."""
        self.list1, self.list2 = _get_input()

    def test_part1(self) -> None:
        """Test part 1 solution with sample input."""
        self.assertEqual(part_1(self.list1, self.list2), 11)

    def test_part2(self) -> None:
        """Test part 2 solution with sample input."""
        self.assertEqual(part_2(self.list1, self.list2), 31)


if __name__ == '__main__':
    unittest.main()

"""Tests for Day 2 solutions & helper functions.

Usage
-----
> cd AdventOfCode2024
> python -m unittest tests.test_day2
"""
import unittest

from .__init__ import INPUT_DIR
from day2 import parse_input, part_1, part_2


class TestHelpers(unittest.TestCase):
    """Test helper functions."""

    def setUp(self) -> None:
        """Set up before every test case."""
        self.input = parse_input(INPUT_DIR.joinpath('day2_test.txt'))

    def test_parse_input(self) -> None:
        """Test parse_input() function."""
        self.assertEqual(self.input[0], [7, 6, 4, 2, 1])
        self.assertEqual(self.input[1], [1, 2, 7, 8, 9])
        self.assertEqual(self.input[2], [9, 7, 6, 2, 1])
        self.assertEqual(self.input[3], [1, 3, 2, 4, 5])
        self.assertEqual(self.input[4], [8, 6, 4, 4, 1])
        self.assertEqual(self.input[5], [1, 3, 6, 7, 9])


class TestSolutions(unittest.TestCase):
    """Test cases for Day 2 solutions."""

    def setUp(self) -> None:
        """Set up before every test case."""
        self.input = parse_input(INPUT_DIR.joinpath('day2_test.txt'))

    def test_part1(self) -> None:
        """Test part 1 solution with sample input."""
        self.assertEqual(part_1(self.input), 2)

    @unittest.skip('not implemented')
    def test_soln2(self) -> None:
        """Test part 2 solution with sample input."""
        self.assertEqual(part_2(self.input), 4)


if __name__ == '__main__':
    unittest.main()

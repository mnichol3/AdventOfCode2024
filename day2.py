"""Advent of Code 2024 - Day 2"""
from pathlib import Path


def part_1(report: list[list[int]]) -> int:
    """Part 1 Solution.

    Parameters
    ----------
    report: list of list of int

    Returns
    -------
    int
    """
    num_safe = 0

    for x in report:
        num_pos = 0
        num_in_range = 0

        diff = [x[i+1] - x[i] for i in range(len(x) - 1)]

        for z in diff:
            if z > 0:
                num_pos += 1

            if 1 <= abs(z) <= 3:
                num_in_range += 1

        if (
            num_in_range == len(diff) and
            (num_pos == 0 or num_pos == len(diff))
        ):
            num_safe += 1

    return num_safe


def part_2(report: list[list[int]]) -> int:
    """Part 2 Solution.

    Parameters
    ----------
    report: list of list of int

    Returns
    -------
    int
    """
    pass


def parse_input(f_path: Path) -> list[list[int]]:
    """Parse the input from a text file

    Parameters
    ----------
    f_path: pathlib.Path
        Path of input file.

    Returns
    -------
    list of list of int
    """
    inp = [
        [int(y) for y in x.split()]
        for x in f_path.read_text().split('\n') if x
    ]
    return inp


if __name__ == '__main__':
    input = parse_input(
        Path(__file__).parent.joinpath('input', 'day2.txt'))

    print(f'Part 1 solution: {part_1(input)}')
    print(f'Part 2 solution: {part_2(input)}')

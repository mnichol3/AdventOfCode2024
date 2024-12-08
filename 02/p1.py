"""Advent of Code 2024 - Day 2 Part 1"""
from pathlib import Path


INPUT_PATH = Path(__file__).parent.joinpath('input', 'day2.txt')


def valid_report(report: list[int]) -> bool:
    """Validate a report.

    Parameters
    ----------
    report: list of int

    Returns
    -------
    bool
        True if report is valid, else False.
    """
    valid_len = len(report) - 1
    num_pos = 0
    num_in_range = 0

    for i in range(valid_len):
        diff = report[i+1] - report[i]
        if diff > 0:
            num_pos += 1

        if 1 <= abs(diff) <= 3:
            num_in_range += 1

    if (
        num_in_range == valid_len and
        (num_pos == 0 or num_pos == valid_len)
    ):
        return True

    return False


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
    return [
        [int(y) for y in x.split()]
        for x in f_path.read_text().split('\n') if x
    ]


def get_solution(reports: list[list[int]]) -> int:
    """Get the number of valid reports."""
    return len([y for y in (valid_report(x) for x in reports) if y])


if __name__ == '__main__':
    print(f'Day 2 Part 1 solution: {get_solution(parse_input(INPUT_PATH))}')

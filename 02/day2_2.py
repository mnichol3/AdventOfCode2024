"""Advent of Code 2024 - Day 2 Part 2"""
from day2_1 import parse_input


def get_diffs(report: list[int]):
    diffs = []
    signs = []

    for i in range(len(report) - 1):
        diffs.append(report[i+1] - report[i])
        signs.append(get_sign(diffs[i]))

    return diffs, signs


def get_sign(x: int) -> int:
    """Get the sign of the given integer.

    Parameters
    ----------
    x: int

    Returns
    -------
    int
        0 if x == 0; 1 or -1.
    """
    if x == 0:
        return 0

    return -1 if abs(x) != x else 1


def valid_report(report: list[int]) -> int:
    """Validate a report.

    Parameters
    ----------
    report: list of int

    Returns
    -------
    int
        Index of first list element that violates a rule.
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


def get_solution(reports: list[list[int]]) -> int:
    """Get the number of valid reports."""
    return len([y for y in (valid_report(x) for x in reports) if y])


if __name__ == '__main__':

    tried = [
        247,
        259,
        262,
    ]
    reports = parse_input(INPUT_PATH)

    soln = get_solution(reports)

    assert soln not in tried, f'Already tried incorrect Part 2 Solution {soln_2}'
    assert soln > 255, f'Incorrect Part 2 Solution; {soln_2} < 255'
    print(f'Day 2 Part 2 solution: {soln}')
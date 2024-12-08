"""Advent of Code 2024 - Day 2 Part 2"""
from p1 import parse_input


def valid_report(report: list[int], valid_seq: list[int]) -> bool:
    """Validate a report.

    Parameters
    ----------
    report: list of int
    valid_seq: list of int

    Returns
    -------
    bool
        True if report is valid, else False.
    """
    violations = 0

    for i in range(len(report) - 1):
        if report[i+1] - report[i] not in valid_seq:
            violations += 1

        if violations > 1:
            return False

    return True


if __name__ == '__main__':
    num_valid = 0
    inc_seq = range(1, 4)
    dec_seq = range(-3, 0)

    for report in parse_input():
        if any([
            valid_report(report, inc_seq),
            valid_report(report, dec_seq),
            valid_report(report[:-1], inc_seq),
            valid_report(report[:-1], dec_seq),
            #valid_report(report[1:], inc_seq),
            #valid_report(report[1:], dec_seq),
        ]):
            num_valid += 1

    print(f'Day 02 Part 2 answer: {num_valid}')

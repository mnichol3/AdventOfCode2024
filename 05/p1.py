"""Advent of Code 2024 - Day 5 Part 1"""
from pathlib import Path


def parse_input(fname: str = None) -> tuple[list[str], list[str]]:
    """Parse the input from a text file.

    Parameters
    ----------
    None.

    Returns
    -------
    list of list of str
    """
    fname = 'day5.txt' if fname is None else fname
    raw_inp = (
        Path(__file__).parents[1].joinpath('input', fname)
        .read_text().split('\n')
    )

    delim = raw_inp.index('')

    return ([raw_inp[i] for i in range(delim+1) if raw_inp[i]],
            [raw_inp[j] for j in range(delim+1, len(raw_inp)) if raw_inp[j]])


def part1(rules: list[str], updates: list[str]) -> int:
    middle = []
    valid = True
    for row in updates:
        valid = True
        row_dict = {x: i for (i, x) in enumerate(row.split(','))}

        for row_k, row_i in row_dict.items():
            for rule in rules:
                if row_k in rule:
                    m, n = rule.split('|')
                    try:
                        if (
                            (m == row_k and row_dict[n] < row_i) or
                            (n == row_k and row_i < row_dict[m])
                        ):
                            valid = False
                            break
                    except KeyError:
                        pass

        if valid:
            n_vals = len(row_dict.keys())
            middle.append(int(list(row_dict.keys())[n_vals//2]))

    return sum(middle)


if __name__ == '__main__':
    print(f'Day 05 Part 1 answer: {part1(*parse_input())}')

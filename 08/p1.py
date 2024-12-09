"""Advent of Code 2024 - Day 8 Part 1"""
from collections import defaultdict
from itertools import combinations
from pathlib import Path


def parse_input(fname: str = None) -> list[list[str]]:
    """Parse the input from a text file.

    Parameters
    ----------
    None.

    Returns
    -------
    list of list of str
    """
    fname = 'input.txt' if fname is None else fname

    return [[y for y in x] for x in Path(fname).read_text().split('\n') if x]


def part1(grid: list[list[str]]) -> int:
    """Solution to Part 2.

    Parameters
    ----------
    grid: list of list of str

    Returns
    -------
    int

    Problem
    -------
    TODO

    Walkthrough
    TODO
    """
    locations = defaultdict(set)
    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        for j in range(n):
            if grid[i][j] != '.':
                locations[grid[i][j]].add((i, j))

    antinodes = set()
    for loc in locations.values():
        for (a, b), (c, d) in combinations(loc, 2):
            di = a - c
            dj = b - d
            for i, j in [(a+di, b+dj), (c-di, d-dj)]:
                if i in range(m) and j in range(n):
                    antinodes.add((i, j))

    return len(antinodes)


if __name__ == '__main__':
    print(f'Day 08 Part 1 answer: {part1(parse_input())}')

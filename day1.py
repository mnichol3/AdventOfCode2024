"""Advent of Code 2024 - Day 1"""

from pathlib import Path


StarList = list[list[int, int]]


def calc_distance(input: StarList) -> int:
    pass


def parse_input(f_path: Path) -> StarList:
    """Read the input from a file and return it as a nest list of ints.

    Parameters
    ----------
    f_path: pathlib.Path
        Path of input file.

    Returns
    -------
    list[list[int, int]]
    """
    if not isinstance(f_path, Path):
        f_path = Path(f_path)

    return list(zip(*[x.split() for x in f_path.read_text().split('\n') if x]))
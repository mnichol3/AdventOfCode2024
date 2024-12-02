"""Advent of Code 2024 - Day 1"""

from pathlib import Path


def calc_distance(list1: list[int], list2: list[int]) -> int:
    """Calculate the distances between sorted values in the input list.

    Parameters
    ----------
    list1: list of int
    list2: list of int

    Returns
    -------
    int
    """
    sum = 0
    list1 = quicksort(list1)
    list2 = quicksort(list2)

    if len(list1) != len(list2):
        len_str = f'{len(list1)}, {len(list2)}'
        raise ValueError(f'Input lists must have same length, got {len_str}')

    for idx, val1 in enumerate(list1):
        val2 = list2[idx]

        if val1 >= val2:
            minuend = val1
            subtrahend = val2
        else:
            minuend = val2
            subtrahend = val1

        sum += minuend - subtrahend

    return sum


def quicksort(arr: list[int]) -> list[int]:
    """Generic quicksort algorithm.

    Slower than built-in Python sorting algorithms but wheres the fun in using
    those?

    Parameters
    ----------
    arr: list of int
        List of integers to sort.

    Returns
    -------
    list of int
        Sorted list of integers.
    """
    lesser = []
    equal = []
    greater = []

    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    for x in arr:
        if x < pivot:
            lesser.append(x)
        elif x == pivot:
            equal.append(x)
        elif x > pivot:
            greater.append(x)

    return quicksort(lesser) + equal + quicksort(greater)


def parse_input(f_path: Path) -> list[list[int]]:
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

    a, b = list(zip(*[x.split() for x in f_path.read_text().split('\n') if x]))

    return [int(x) for x in a], [int(y) for y in b]


if __name__ == '__main__':
    input = parse_input(Path(__file__).parent.joinpath('input', 'day1.txt'))
    dist = calc_distance(*input)
    print(dist)

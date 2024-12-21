"""Advent of Code 2024 - Day 20 Part 2"""
import math
from collections import deque
from itertools import product

from p1 import parse_input, Maze, Point


def get_distance(a: Point, b: Point, max_diff: int = 20) -> int | None:
        """Return the manhattan distance if within the valid max value."""
        dist = abs(a[0]-b[0]) + abs(a[1]-b[1])

        if dist > max_diff:
             return None

        return dist


def find_shortcuts(
    maze: Maze,
    best_path: list[Point],
    length: int = 2,
) -> dict:
    """Find possible shortcuts in the best path.

    Parameters
    ----------
    maze: Maze
        Maze.
    best_path: list of tuple of (int, int)
        Coordinates of the computed best path.
    length: int, optional
        Maximum length of the cheat/shortcut. Default is 2.

    Returns
    -------
    dict of int, int
    """
    shortcuts = {}
    visited = set()

    for idx, point1 in enumerate(best_path):
        for point2 in best_path[idx+98:]:
            if point2 == maze.start:
                continue

            dist = get_distance(point1, point2, length)

            if dist and point2 not in visited:
                if dist in shortcuts:
                    shortcuts[dist] += 1
                else:
                    shortcuts[dist] = 1

        visited.add(point1)

    return shortcuts


if __name__ == '__main__':
    maze = Maze(parse_input())
    path = maze.bfs()
    print(f'Best path length = {len(path)-1}')

    shortcuts = find_shortcuts(maze, path, length=20)

    print(shortcuts)

    sum = 0
    for k, v in shortcuts.items():
        if k >= 100:
            sum += v

    print(f'Part 2 answer: {sum}')
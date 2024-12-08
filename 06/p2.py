"""Advent of Code 2024 - Day 6 Part 2"""
from itertools import cycle

from p1 import parse_input


def part2(guard_map: list[str]) -> int:
    """Solution to Part 2.

    Parameters
    ----------
    guard_map: list of str

    Returns
    -------
    int

    Problem Description
    -------------------
    * Same rules as Part 1:
        * If there is something directly in front of guard,
          turn right 90 degres.
        * Else, take one step forward.
    * Determine the number of positions an obstacle could be placed in order
      to form a closed loop of the guard's path.
        * Obstacle cannot be places on guard's starting position.

    Walkthrough
    -----------
    1. We no longer need to store visited positions.
    2. Move forward.
    3. If obstacle is encountered, turn 90 degrees right.
    4. Repeat 2 & 3 until 3 consecutive turns have been made.
    5. If
    """

    def get_starting_pos(guard_map: list[str]) -> tuple[int, int]:
        for i in range(len(guard_map)):
            for j in range(len(guard_map[0])):
                if guard_map[i][j] == '^':
                    return i, j

        return -1, -1

    movement = cycle([
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    ])

    ni = len(guard_map)
    nj = len(guard_map[0])

    curr_i, curr_j = get_starting_pos(guard_map)

    if (curr_i, curr_j) == (-1, -1):
        return 0

    vertices = set()
    obstacles = set()
    n_turns = 0
    prev_pos = None
    move = next(movement)
    while True:
        next_i = curr_i + move[0]
        next_j = curr_j + move[1]

        if not 0 <= next_i < ni or not 0 <= next_j < nj:
            print(obstacles)
            print(vertices)
            return len(obstacles)

        if guard_map[next_i][next_j] == '#':
            vertices.add((curr_i, curr_j))
            move = next(movement)
            n_turns += 1
            prev_pos = (curr_i, curr_j)
        else:
            if (curr_i, curr_j) != prev_pos:
                if move == (-1, 0):
                    for j in range(curr_j+1, nj):
                        if (curr_i, j) in vertices:
                            obstacles.add((next_i, next_j))
                            break
                elif move == (0, 1):
                    for i in range(curr_i+1, ni):
                        if (i, curr_j) in vertices:
                            obstacles.add((next_i, next_j))
                            break
                elif move == (1, 0):
                    for j in range(curr_j-1, -1, -1):
                        if (curr_i, j) in vertices:
                            obstacles.add((next_i, next_j))
                            break
                else:
                    for i in range(curr_i-1, -1, -1):
                        if (i, curr_j) in vertices:
                            obstacles.add((next_i, next_j))
                            break

            prev_pos = (curr_i, curr_j)
            curr_i = next_i
            curr_j = next_j


if __name__ == '__main__':
    #print(f'Day 06 Part 2 answer: {part2(parse_input("input_test.txt"))}')
    print(f'Day 06 Part 2 answer: {part2(parse_input())}')
    # 1576 too low
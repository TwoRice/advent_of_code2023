import numpy as np
import sys


def move_light(y, x, direction, grid, visited):
    visited.append((y, x, direction))
    y, x = np.array([y, x]) + np.array(direction)

    if y in [-1, len(grid)] or x in [-1, len(grid[0])] or (y, x, direction) in visited:
        return

    if grid[y, x] == "|":
        if abs(direction[0]) == 0:
            move_light(y, x, (1, 0), grid, visited)
            move_light(y, x, (-1, 0), grid, visited)
        else:
            move_light(y, x, direction, grid, visited)
    elif grid[y, x] == "-":
        if abs(direction[0]) == 1:
            move_light(y, x, (0, 1), grid, visited)
            move_light(y, x, (0, -1), grid, visited)
        else:
            move_light(y, x, direction, grid, visited)
    elif grid[y, x] == "/":
        if direction[0] == 1:
            move_light(y, x, (0, -1), grid, visited)
        elif direction[0] == -1:
            move_light(y, x, (0, 1), grid, visited)
        elif direction[1] == 1:
            move_light(y, x, (-1, 0), grid, visited)
        else:
            move_light(y, x, (1, 0), grid, visited)
    elif grid[y, x] == "\\":
        if direction[0] == 1:
            move_light(y, x, (0, 1), grid, visited)
        elif direction[0] == -1:
            move_light(y, x, (0, -1), grid, visited)
        elif direction[1] == 1:
            move_light(y, x, (1, 0), grid, visited)
        else:
            move_light(y, x, (-1, 0), grid, visited)
    else:
        move_light(y, x, direction, grid, visited)

if __name__ == "__main__":
    sys.setrecursionlimit(5000)
    with open("day16.txt", "r") as f:
        contraption = np.array([list(row) for row in f.read().split("\n")])

    visited = []
    move_light(0, -1, (0, 1), contraption, visited)
    print(f"Part 1: {len({(y, x) for y, x, d in visited}) - 1}")
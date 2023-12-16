import numpy as np
import sys
sys.setrecursionlimit(100000)

RIGHT = (0, 1)
LEFT = (0, -1)
DOWN = (1, 0)
UP = (-1, 0)
movements = {
    "|": {
        RIGHT: [UP, DOWN],
        LEFT: [UP, DOWN],
        DOWN: [DOWN],
        UP: [UP]
    },
    "-": {
        RIGHT: [RIGHT],
        LEFT: [LEFT],
        DOWN: [LEFT, RIGHT],
        UP: [LEFT, RIGHT]
    },
    "/": {
        RIGHT: [UP],
        LEFT: [DOWN],
        DOWN: [LEFT],
        UP: [RIGHT]
    },
    "\\": {
        RIGHT: [DOWN],
        LEFT: [UP],
        DOWN: [RIGHT],
        UP: [LEFT]
    },
    ".": {
        RIGHT: [RIGHT],
        LEFT: [LEFT],
        DOWN: [DOWN],
        UP: [UP]
    }
}

def move_light(y, x, direction, grid, visited):
    loop = (y, x, direction) in visited
    visited.add((y, x, direction))
    y, x = np.array([y, x]) + np.array(direction)

    if y in [-1, len(grid)] or x in [-1, len(grid[0])] or loop:
        return visited

    new_direction = movements[grid[y, x]][direction]
    for dir in new_direction:
        visited.update(move_light(y, x, dir, grid, visited))
    return visited

def calculate_energy(start_pos, direction, grid):
    visited = set()
    visited = move_light(*start_pos, direction, grid, visited)
    return len({(y, x) for y, x, d in visited})

if __name__ == "__main__":
    sys.setrecursionlimit(5000)
    with open("day16.txt", "r") as f:
        contraption = np.array([list(row) for row in f.read().split("\n")])

    print(f"Part 1: {calculate_energy((0, -1), (0, 1), contraption)}")
    
    num_energised = []
    for y in range(len(contraption)):
        num_energised.append(calculate_energy((y, 0), (0, 1), contraption))
        num_energised.append(calculate_energy((y, len(contraption[0])-1), (0, -1), contraption))
    for x in range(len(contraption[0])):
        num_energised.append(calculate_energy((0, x), (1, 0), contraption))
        num_energised.append(calculate_energy((len(contraption)-1, x), (-1, 0), contraption))
        
    print(f"Part 2: {max(num_energised)}")
import numpy as np

def check_symmetry(grid, i, j, diff_margin):    
    if j < len(grid) and i >= 0:
        diff = sum(grid[i] != grid[j])
        if diff <= diff_margin:
            return check_symmetry(grid, i-1, j+1, diff_margin-diff)
            
    smudge = not diff_margin
    return i+1, j-1, smudge

def find_symmetry(grid, diff_margin):
    for i in range(0, len(grid)-1, 1):
        diff = sum(grid[i] != grid[i+1])
        if diff <= diff_margin:
            start, end, smudge = check_symmetry(grid, i-1, i+2, diff_margin-diff)
            if (end == len(grid)-1 or start == 0) and smudge:
                return i+1

def inspect(grid, diff_margin=0):
    answer = find_symmetry(grid, diff_margin) 
    if answer: return answer * 100
    grid = grid.T
    return find_symmetry(grid, diff_margin) 

if __name__ == "__main__":
    with open("day13.txt", "r") as f:
        grids = [np.array([list(row) for row in map.split("\n")]) for map in f.read().split("\n\n")]
    
    print(f"Part 1: {sum([inspect(grid) for grid in grids])}")
    print(f"Part 2: {sum([inspect(grid, diff_margin=1) for grid in grids])}")
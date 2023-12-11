import numpy as np
from itertools import combinations, zip_longest

def shortest_path(a, b, empty_cols, empty_rows, scale=1):
    dist = abs(b[0] - a[0]) + abs(b[1] - a[1])
    
    for col, row in zip_longest(empty_cols, empty_rows, fillvalue=150):
        across_empty_col = col in range(a[1], b[1], 1 if a[1] < b[1] else -1)
        across_empty_row = row in range(a[0], b[0], 1 if a[0] < b[0] else -1)
        if across_empty_col and across_empty_row:
            dist += 2*scale
        elif across_empty_col or across_empty_row:
            dist += scale

    return dist

if __name__ == "__main__":
    with open("day11.txt", "r") as f:
        galaxy_map = np.array([list(row) for row in f.read().split("\n")])

    empty_cols = np.where(np.all(galaxy_map == ".", axis=0))[0]
    empty_rows = np.where(np.all(galaxy_map == ".", axis=1))[0]
    galaxy_locs = [(y, x) for y, x in zip(*np.where(galaxy_map == "#"))]
    galaxy_pairs = list(combinations(galaxy_locs, 2))

    sum_paths = 0
    for g1, g2 in galaxy_pairs:
        sum_paths += shortest_path(g1, g2, empty_cols, empty_rows)
    print(f"Part 1:{sum_paths}")

    sum_paths = 0
    for g1, g2 in galaxy_pairs:
        sum_paths += shortest_path(g1, g2, empty_cols, empty_rows, scale=999999)
    print(f"Part 2:{sum_paths}")
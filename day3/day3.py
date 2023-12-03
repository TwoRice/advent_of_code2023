import numpy as np
from collections import defaultdict

def check_neighbours(schematic, y, x):
    offsets = [-1, 0, 1]
    neighbours = [(y+dy, x+dx) for dx in offsets for dy in offsets]
    matches = [n for n in neighbours if schematic[n].isdigit()]     
    return matches

def get_part_number(schematic, y, x):
    part_num = schematic[y, x]
    check_right = x+1
    while check_right < 140 and schematic[y, check_right].isdigit():
        part_num += schematic[y, check_right]
        check_right += 1

    check_left = x-1
    while check_left >= 0 and schematic[y, check_left].isdigit():
        part_num = schematic[y, check_left] + part_num
        check_left -= 1

    return int(part_num)

def remove_sequences(part_idx):
    keep = []
    for i in range(len(part_idx) - 1):
        if part_idx[i][0] != part_idx[i+1][0]:
            keep.append(part_idx[i])
            continue
        if part_idx[i][1] + 1 != part_idx[i+1][1]:
            keep.append(part_idx[i])

    return keep

if __name__ == "__main__":
    with open("day3.txt", "r") as f:
        engine_schematic = np.array([list(line) for line in f.read().split("\n")])

    # Part 1
    symbols = np.where((engine_schematic != '.') & (~np.char.isdigit(engine_schematic)))
    symbols = list(zip(symbols[0], symbols[1]))
    
    part_idx = set()
    for symbol in symbols:
       part_idx.update(check_neighbours(engine_schematic, *symbol))
    part_idx = list(part_idx) + [(150, 150)]
    part_idx = remove_sequences(sorted(part_idx))
    part_num_sum = sum([get_part_number(engine_schematic, *idx) for idx in part_idx])

    print(f"Part 1: {part_num_sum}")

    # Part 2
    gears = np.where(engine_schematic == '*')
    gears = list(zip(gears[0], gears[1]))

    gear_ratio_sum = 0
    for gear in gears:
        part_idx = check_neighbours(engine_schematic, *gear) + [(150, 150)]
        part_idx = remove_sequences(sorted(part_idx))
        if len(part_idx) == 2:
            gear_ratio_sum += get_part_number(engine_schematic, *part_idx[0]) * get_part_number(engine_schematic, *part_idx[1])

    print(f"Part 2: {gear_ratio_sum}")    
import numpy as np

def find_pattern(values):
    n = len(values)
    longest_pattern = []
    for pattern_length in range(1, n//2 + 1):
        for i in range(n - 2*pattern_length + 1):
            pattern = values[i:i+pattern_length]
            if values[i:i+pattern_length] == values[i+pattern_length:i+2*pattern_length]:
                if len(pattern) > len(longest_pattern):
                    longest_pattern = pattern

    return longest_pattern

def find_sublist(lst, sublist):
    sub_len = len(sublist)
    for i in range(len(lst)):
        if lst[i:i+sub_len] == sublist:
            return i
    return -1

def tilt(platform, direction):
    if direction == "S":
        platform = platform[::-1]
    elif direction == "E":
        platform = platform.T[::-1]
    elif direction == "W":
        platform = platform.T
    
    for y, row in enumerate(platform):
        for x, loc in enumerate(row):
            new_y = y
            if loc == "O": 
                while new_y > 0 and platform[new_y-1, x] == ".":
                    new_y -= 1
                if new_y != y:
                    platform[new_y, x] = "O"
                    platform[y, x] = "."

    if direction == "S":
        return platform[::-1]
    elif direction == "E":
        return platform[::-1].T
    elif direction == "W":
        return platform.T
    return platform

def calculate_load(platform):
    return sum(np.sum(platform == "O", axis=1) * range(len(platform), 0, -1))

def read_input():
    with open("day14.txt", "r") as f:
        return np.array([list(row) for row in f.read().split("\n")])
    

if __name__ == "__main__":
    platform = read_input()
    platform = tilt(platform, "N")
    print(f"Part 1: {calculate_load(platform)}")

    platform = read_input()
    loads = []
    for _ in range(500):
        platform = tilt(platform, "N")
        platform = tilt(platform, "W")
        platform = tilt(platform, "S")
        platform = tilt(platform, "E")
        loads.append(calculate_load(platform))

    pattern = find_pattern(loads)
    offset = find_sublist(loads, pattern)
    load_idx = ((1000000000 - offset) % len(pattern)) - 1
    print(f"Part 2: {pattern[load_idx]}")
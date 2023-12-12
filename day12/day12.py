import re
import functools
from itertools import product

@functools.cache
def count_valid_permutations(map, group_counts, group_size):
    if not group_counts and "#" not in map:
        return 1
    elif not group_counts or len(map) == 0:
        return 0
        
    if map[0] == "?":
        return count_valid_permutations("#" + map[1:], group_counts, group_size) + \
            count_valid_permutations("." + map[1:], group_counts, group_size)
    elif map[0] == "#":
        return count_valid_permutations(map[1:], group_counts, group_size+1)
    elif map[0] == ".":
        if group_size == group_counts[0]:
            return count_valid_permutations(map[1:], group_counts[1:], 0)
        elif group_size > 0:
            return 0
        else:
            return count_valid_permutations(map[1:], group_counts, group_size)

def sum_valid_permutations(records):
    return sum([
        count_valid_permutations(condition_map + ".", group_counts, 0) 
        for condition_map, group_counts in records
    ])

if __name__ == "__main__":
    with open("day12.txt", "r") as f:
        records = []
        for record in f.read().split("\n"):
            condition_map, group_counts = record.split()
            group_counts = tuple(int(count) for count in group_counts.split(","))
            records.append((condition_map, group_counts))

        print(f"Part 1: {sum_valid_permutations(records)}")
        unfolded = [("?".join([condition_map]*5), group_counts*5) for condition_map, group_counts in records]
        print(f"Part 2: {sum_valid_permutations(unfolded)}")
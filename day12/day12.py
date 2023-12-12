import re
from itertools import product

def brute_force(records):
    unknown_search = re.compile(r"\?+")
    damaged_search = re.compile(r"\#+")
    valid_sum = 0
    for condition_map, group_counts in records:
        valid_combos = 0 
        group_combos = []
        spans = []
        for unknown in re.finditer(unknown_search, condition_map):
            unknown_len = len(unknown.group(0))
            group_combos.append(["".join(combo) for combo in product(".#", repeat=unknown_len)])
            spans.append(unknown.span())
    
        for combo in product(*group_combos):
            possible_combo = condition_map
            for group, span in zip(combo, spans):
                possible_combo = possible_combo[:span[0]] + group + possible_combo[span[1]:]
    
            valid = True
            damaged_groups = re.findall(damaged_search, possible_combo)
            if len(damaged_groups) != len(group_counts):
                valid = False
            else: 
                for group, counts in zip(damaged_groups, group_counts):
                    if len(group) != counts:
                        valid = False
                        break
                        
            if valid:
                valid_combos += 1
        valid_sum += valid_combos

    return valid_sum

if __name__ == "__main__":
    with open("day12.txt", "r") as f:
        records = []
        for record in f.read().split("\n"):
            condition_map, group_counts = record.split()
            group_counts = tuple(int(count) for count in group_counts.split(","))
            records.append((condition_map, group_counts))

        print(f"Part 1: {brute_force(records)}")
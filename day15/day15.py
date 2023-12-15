import re
from collections import defaultdict

def calc_hash(str):
    current_value = 0
    for char in str:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value

if __name__ == "__main__":
    with open("day15.txt", "r") as f:
        initialisation_strings = f.read().split(",")

    print(f"Part 1: {sum([calc_hash(str) for str in initialisation_strings])}")

    string_parts_search = re.compile(r"(.+)(-|=)(.*)")
    boxes = defaultdict(dict)
    for str in initialisation_strings:
        label, operation, power = re.findall(string_parts_search, str)[0]
        box_no = calc_hash(label)
    
        if operation == "=":
            boxes[box_no][label] = int(power)
        else:
            if label in boxes[box_no]: del boxes[box_no][label]
    
    total_focusing_power = 0
    for box_no, lenses in boxes.items():
        for i, (label, power) in enumerate(lenses.items()):
            total_focusing_power += (box_no+1) * (i+1) * power
    print(f"Part 2: {total_focusing_power}")
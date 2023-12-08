import math
from functools import reduce

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def find_end(network, start_node, ends_with_z=False):
    steps = 0
    found = False
    current_node = network[start_node]
    while not found:
        for direction in instructions:
            steps += 1
            go = 0 if direction == "L" else 1
            if ends_with_z and current_node[go].endswith("Z"):
                found = True
                break
            if current_node[go] == "ZZZ":
                found = True
                break
            current_node = network[current_node[go]]
    return steps     

if __name__ == "__main__":
    with open("day8.txt", "r") as f:
        navigation = f.read().split("\n")    

    instructions = navigation[0]
    network = {}
    for node in navigation[2:]:
        start_node, lr = node.split(" = ")
        left, right = lr.replace("(", "").replace(")", "").split(", ")
        network[start_node] = (left, right)

    print(f"Part 1: {find_end(network, 'AAA')}")

    start_nodes = [node for node in network.keys() if node.endswith("A")]
    steps = [find_end(network, node, ends_with_z=True) for node in start_nodes]
    print(f"Part 2: {reduce(lambda a, b: lcm(a, b), steps)}")
import math

def find_end(network, start_node, ends_with="ZZZ"):
    steps = 0
    found = False
    current_node = network[start_node]
    while not found:
        for direction in instructions:
            steps += 1
            go = 0 if direction == "L" else 1
            if current_node[go].endswith(ends_with):
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
    steps = [find_end(network, node, ends_with="Z") for node in start_nodes]
    print(f"Part 2: {math.lcm(*steps)}")
import numpy as np

def shoelace_formula(vertices):
    area = 0
    for i in range(len(vertices)-1):
        area += vertices[i][0] * vertices[i+1][1]
        area -= vertices[i][1] * vertices[i+1][0]
    return abs(area) / 2

def get_vertices(instructions):
    x, y = 0, 0
    vertices = [(x, y)]
    perimeter = 0
    for direction, distance in instructions:
        if direction == 0:
            x += distance
        elif direction == 1:
            y += distance
        elif direction == 2:
            x -= distance
        else:
            y -= distance
        vertices.append((x, y))
        perimeter += distance
        
    return vertices, perimeter

def calc_cubic_meters(instructions):
    vertices, perimeter = get_vertices(instructions)
    area = shoelace_formula(vertices)
    inside_points = area - perimeter/2 + 1

    return inside_points + perimeter
    
if __name__ == "__main__":
    with open("day18.txt", "r") as f:
        dig_plan = [instruction.split() for instruction in f.read().split("\n")]

    direction_map = {"R": 0, "D": 1, "L": 2, "U": 3}
    instructions = [(direction_map[direction], int(distance)) for direction, distance, _ in dig_plan]
    print(f"Part 1: {calc_cubic_meters(instructions)}")

    new_instructions = [(int(instruction[-2], 16), int(instruction[2:7], 16))for _, _, instruction in dig_plan]
    print(f"Part 2: {calc_cubic_meters(new_instructions)}")
    
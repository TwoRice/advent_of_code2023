import numpy as np

left_pipes = ["-", "L", "F"]
right_pipes = ["-", "J", "7"]
up_pipes = ["|", "F", "7"]
down_pipes = ["|", "J", "L"]

def find_connected_neighbours(pipe_map, y, x):
    searching = True
    count = 0
    while searching:
        count += 1
        current = pipe_map[y, x]
        pipe_map[y, x] = "0"
        # check left
        if x-1 >= 0 and current in right_pipes and pipe_map[y, x-1] in left_pipes:
            x = x-1
        # check right
        elif x+1 < len(pipe_map[0]) and current in left_pipes and pipe_map[y, x+1] in right_pipes:
            x = x+1
        # check up
        elif y-1 >= 0 and current in down_pipes and pipe_map[y-1, x] in up_pipes:
            y = y-1
        # check down
        elif y+1 < len(pipe_map) and current in up_pipes and pipe_map[y+1, x] in down_pipes:
            y = y+1
        else:
            searching = False           

    return count

if __name__ == "__main__":
    with open("day10.txt", "r") as f:
        pipe_map = np.array([list(row) for row in f.read().split("\n")])

    start_loc = np.where(pipe_map == "S")
    start_loc = start_loc[0][0], start_loc[1][0]
    pipe_map[start_loc] = "7"
    
    loop_length = find_connected_neighbours(pipe_map, *start_loc)
    print(f"Part 1 : {loop_length/2}")
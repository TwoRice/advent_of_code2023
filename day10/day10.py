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
    
    search_map = pipe_map.copy()
    loop_length = find_connected_neighbours(search_map, *start_loc)
    print(f"Part 1 : {loop_length/2}")

    loop_locs = np.where(search_map == "0")
    loop_locs = [(y, x) for y, x in zip(*loop_locs)]
    inside = 0
    for y in range(len(pipe_map)):
        for x in range(len(pipe_map[0])):
            if (y, x) not in loop_locs:
                search_left = x-1
                down_pipe_counts = 0
                while search_left >= 0:
                    if (y, search_left) in loop_locs and pipe_map[y, search_left] in down_pipes:
                        down_pipe_counts += 1
                    search_left -= 1
                if down_pipe_counts % 2 == 1:
                    inside += 1   
    print(f"Part 2: {inside}")     
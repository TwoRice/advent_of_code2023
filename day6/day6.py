def find_num_ways_to_win(time, best_distance):
    ways_to_win = 0
    for speed in range(1, time):
        distance = speed * (time - speed)
        if distance > best_distance: ways_to_win += 1
            
    return ways_to_win

if __name__ == "__main__":
    with open("day6.txt", "r") as f:
        race_data = [[int(x) for x in values.split(":")[1].split()] for values in f.readlines()]
        races = list(zip(*race_data))

    sum_ways_to_win = 1
    for time, best_distance in races:
        sum_ways_to_win *= find_num_ways_to_win(time, best_distance)
    print(f"Part 1: {sum_ways_to_win}")

    time, best_distance = [int("".join([str(v) for v in values])) for values in race_data]
    print(f"Part 2: {find_num_ways_to_win(time, best_distance)}")

import re
from collections import defaultdict

if __name__ == "__main__":
    with open("day2.txt", "r") as f:
        games = f.readlines()

    cubes_search = re.compile(r"(\d+) (green|red|blue)")
    game_id_search = re.compile(r"Game (\d+)")
    parsed_games = {}
    for game in games:
        game_id = int(re.search(game_id_search, game).group(1))
        cube_counts = defaultdict(list)
        for cluster in re.findall(cubes_search, game):
            cube_counts[cluster[1]].append(int(cluster[0]))
        parsed_games[game_id] = cube_counts


    game_id_sum = 0
    game_power_sum = 0
    for game_id, game in parsed_games.items():
        if max(game["red"]) <= 12 and max(game["green"]) <= 13 and max(game["blue"]) <= 14:
            game_id_sum += game_id
        game_power_sum += max(game["red"]) * max(game["green"]) * max(game["blue"])

    print(f"Part 1: {game_id_sum}")
    print(f"Part 2: {game_power_sum}")
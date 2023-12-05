map_names = [
    "seeds: ",
    "seed-to-soil map:\n",
    "soil-to-fertilizer map:\n",
    "fertilizer-to-water map:\n",
    "water-to-light map:\n",
    "light-to-temperature map:\n",
    "temperature-to-humidity map:\n",
    "humidity-to-location map:\n"
]

def parse_map(map):
    return [[int(x) for x in conversion.split()] for conversion in map]

def map_source_to_dest(source, dest):
    new_source = set()
    mapped = set()
    dest = parse_map(dest)
    for dest_start, source_start, length in dest:
        for num in source:
            if num >= source_start and num <= source_start + length:
                mapped.add(num)
                new_source.add(num + (dest_start - source_start))

    new_source.update(source - mapped)
    return new_source

def find_lowest_location(maps, seeds):
    max_location = max(parse_map(maps[-1]), key=lambda x: x[0])[0]
    found = False

    for num in range(max_location):
        if found: break
        lowest_location = num
        for i in range(-1, -len(maps), -1):
            for source_start, dest_start, length in parse_map(maps[i]):
                if num >= source_start and num <= source_start + length:
                    num += (dest_start - source_start)
                    break
        
        for seed_start, length in seeds:
            if num >= seed_start and num <= seed_start + length:
                found = True
                break

    return lowest_location - 1

if __name__ == "__main__":
    # Read data
    with open("day5.txt", "r") as f:
        alnamac = f.read()

    # Parse Data
    maps = []
    for i in range(len(map_names) - 1):
        start = alnamac.index(map_names[i]) + len(map_names[i])
        end = alnamac.index(map_names[i+1])
        maps.append(alnamac[start:end].split("\n")[:-2])
    maps.append(alnamac[end + len(map_names[-1]):].split("\n"))

    # Part 1
    source = {int(x) for x in maps[0][0].split()}
    for map in maps[1:]:
        source = map_source_to_dest(source, map)
    print(f"Part 1: {min(source)}")

    # Part 2
    seeds = iter([int(x) for x in maps[0][0].split()])
    seeds = list(zip(seeds, seeds))
    lowest_location = find_lowest_location(maps, seeds)
    print(f"Part 2: {lowest_location}")
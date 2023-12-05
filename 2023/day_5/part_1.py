from copy import deepcopy
from main import get_input

__info = [2023, 5, 1]

def main():
    data = get_input(*__info)
#     data = """seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4
# """.split("\n")
    
    title = "seeds"
    maps = {title: []}
    new_map = False
    
    for line in data[:-1]:
        if new_map:
            new_map = False
            title = line.split(" ")[0]
            maps[title] = []
            continue

        if line == "":
            new_map = True
            continue

        maps[title].append(line.split())

    seeds = [int(seed) for seed in maps["seeds"][0][1:]]
    del maps["seeds"]

    maps = {key: [[int(i) for i in val] for val in value] for key, value in maps.items()}


    for ranges in maps.values():
        range_seeds = deepcopy(seeds)

        for range_ in ranges:
            for index, seed in enumerate(range_seeds):

                if range_[1] <= seed < range_[1] + range_[2]:
                    seeds[index] = range_[0] + (seed - range_[1])

    print(seeds)
    print(min(seeds))

if __name__ == "2023.day_5.part_1":
    main()

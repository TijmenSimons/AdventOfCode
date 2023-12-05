from main import get_input

__info = [2023, 4, 2]

def main():
    data = get_input(*__info)
#     data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
# """.split("\n")

    instances = {}
    
    for line in data[:-1]:
        line = (line+" ").split(": ")
        cur_id = int(line[0][5:])

        multiplier = instances.setdefault(cur_id, 0)
        multiplier += 1

        winning_nrs = line[1].split("| ")[0].split()
        my_nrs      = line[1].split("| ")[1].split()

        count = 0

        for win_nr in winning_nrs:
            if win_nr in my_nrs:
                count += 1
        
        for i in range(count):
            instances.setdefault(cur_id+i+1, 0)
            instances[cur_id+i+1] += (1 * multiplier)

    print(sum([val + 1 for val in instances.values()]))


if __name__ == "2023.day_4.part_2":
    main()

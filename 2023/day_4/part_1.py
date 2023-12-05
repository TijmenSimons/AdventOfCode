from main import get_input

__info = [2023, 4, 1]

def main():
    data = get_input(*__info)
#     data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
# """.split("\n")

    # print(1 * (2**...))
    total = 0
    
    for line in data[:-1]:
        line = (line+" ").split(": ")

        winning_nrs = line[1].split("| ")[0].split()
        my_nrs      = line[1].split("| ")[1].split()

        count = 0

        for win_nr in winning_nrs:
            if win_nr in my_nrs:
                count += 1

        if count:
            total += 1 * (2**(count-1))

    print(total)


if __name__ == "2023.day_4.part_1":
    main()

from main import get_input, store_output

__info = [2022, 3, 1]

def main():
    data = get_input(*__info)
#     data = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw""".split("\n")
    
    def get_prio(char):
        return ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"].index(char) + 1

    total = 0
    for rucksack in data[:-1]:
        x = len(rucksack) // 2
        rs_1, rs_2 = rucksack[:x], rucksack[x:]

        for char in rs_1:
            if char in rs_2:
                duplicate = char

        total += get_prio(duplicate)

    store_output(total, *__info)


if __name__ == "2022.day_3.part_1":
    main()

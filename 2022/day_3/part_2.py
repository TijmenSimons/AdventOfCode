from main import get_input, store_output


__info = [2022, 3, 2]

def main():
    data = get_input(*__info)
#     data = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw""".split("\n")
    result = []
    for idx in range(len(data[:-1])//3):
        result.append([
            data[3*idx],
            data[3*idx+1],
            data[3*idx+2],
        ])
    
    def get_prio(char):
        return ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"].index(char) + 1

    total = 0
    for rucksack_group in result:
        rsg = rucksack_group
        
        for char in rsg[0]:
            if char in rsg[1] and char in rsg[2]:
                duplicate = char

        total += get_prio(duplicate)

    store_output(total, *__info)


if __name__ == "2022.day_3.part_2":
    main()
    

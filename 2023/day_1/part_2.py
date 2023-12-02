from main import get_input

__info = [2023, 1, 2]

def main():
    data = get_input(*__info)
    data = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""".split("\n")
    
    total = 0
    digits = {
        "one": 1, 
        "two": 2, 
        "three": 3, 
        "four": 4, 
        "five": 5, 
        "six": 6, 
        "seven": 7, 
        "eight": 8, 
        "nine": 9,
        "1": 1, 
        "2": 2, 
        "3": 3, 
        "4": 4, 
        "5": 5, 
        "6": 6, 
        "7": 7, 
        "8": 8, 
        "9": 9,
    }

    def clear(s):
        h = len(s)//2
        return s[:h] + "_" + s[h + 1:]

    def search_digit(line):
        for digit in digits.keys():
            if digit in line:
                return digit

    for line in data[:-1]:
        nrs = []
        # print(line)

        searching = True
        while searching:
            found = None
            found = search_digit(line)

            if found:
                idx = line.index(found)
                line = line[:idx] + clear(found) + line[idx+len(found):]

                nrs.append((idx, digits[found]))
                continue
            searching = False
        
        lowest = nrs[-1]
        highest = nrs[-1]

        for nr in nrs[:-1]:
            if nr[0] < lowest[0]:
                lowest = nr
            if nr[0] > highest[0]:
                highest = nr

        # print(line)
        # print(nrs)
        # print(int(str(lowest[1]) + str(highest[1])))
        # input()
        total += int(str(lowest[1]) + str(highest[1]))

    print(total)


if __name__ == "2023.day_1.part_2":
    main()

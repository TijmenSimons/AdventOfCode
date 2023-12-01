from main import get_input, store_output

__info = [2023, 1, 1]

def main():
    data = get_input(*__info)
    print("hello!")
#     data = """1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# """.split("\n")
    total = 0

    for line in data[:-1]:
        nr = ""
        for char in line:
            try:
                int(char)
                nr += char
            except:
                continue
        total += int(nr[0] + nr[-1])
    print(total)

    # store_output(data, *__info)


if __name__ == "2023.day_1.part_1":
    main()

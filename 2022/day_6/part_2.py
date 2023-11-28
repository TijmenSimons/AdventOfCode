from main import get_input, store_output

__info = [2022, 6, 2]

def main():
    data = get_input(*__info)
    data = """""".split("\n")
    store_output(data, *__info)


if __name__ == "2022.day_6.part_2":
    main()

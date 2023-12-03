from main import get_input

__info = [2023, 3, 2]

def main():
    data = get_input(*__info)
    data = """""".split("\n")
    
    for line in data[:-1]:
        print(line)


if __name__ == "2023.day_3.part_2":
    main()

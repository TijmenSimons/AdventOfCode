from main import get_input

__info = [2023, 2, 2]

def main():
    data = get_input(*__info)
#     data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# """.split("\n")

    total = 0
    
    for line in data[:-1]:
        split_1 = line.split(": ")

        pulls = split_1[1].split("; ")
        pulls = [{p.split(" ")[1]: int(p.split(" ")[0]) for p in pull.split(", ")} for pull in pulls]

        colors = {
            "red": 1,
            "green": 1,
            "blue": 1
        }

        for pull in pulls:
            for key, value in pull.items():
                if value > colors[key]:
                    colors[key] = value

        to_add = 1
        
        for value in colors.values():
            to_add *= value
        
        total += to_add

    print(total)


if __name__ == "2023.day_2.part_2":
    main()

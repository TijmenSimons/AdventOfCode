from main import get_input, store_output

__info = [2023, 3, 1]

def main():
    data = get_input(*__info)
#     data = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# """.split("\n")
    
    grid = [[char for char in line] for line in data[:-1]]

    def get(x, y):
        return grid[y][x]
    
    def get_besides(x, y, mod):
        result = []

        try:
            char = get(x + mod, y)
            int(char)
            result = get_besides(x+mod, y, mod)
            if mod > 0:
                result = [char] + result
            else:
                result += [char]
        except IndexError:
            ...
        except ValueError:
            ...

        return result


    def get_around(x, y):
        dx = -1
        dy = -1

        result = []

        for _ in range(8):
            try:
                char = get(x + dx, y + dy)
                result.append(char)
            except IndexError:
                ...

            dx += 1
            if dx > 1:
                dx = -1
                dy += 1
            
            if dy == 0:
                if dx == 0:
                    dx = 1

        return result
    
    # for line in grid:
    #     print("".join(line))

    total = 0
    output = []

    skip_amount = 0


    # for y, line in enumerate(grid):
    #     for x, char in enumerate(line):
    #         if skip_amount > 0:
    #             skip_amount -= 1
    #             continue

    #         if not char.isnumeric():
    #             continue

    #         around = get_around(x, y)

    #         if any(a_char != "." and not a_char.isnumeric() for a_char in around):
    #             left = get_besides(x, y, -1)
    #             right = get_besides(x, y, 1)

    #             num = int("".join(left) + char + "".join(right))
    #             skip_amount += len(right)

    #             output.append(f"{str(left)} {char} {str(right)} = {str(num)}")
    #             total += num

    # for y, line in enumerate(grid):
    #     for x, char in enumerate(line):
    #         if char == "." or char.isnumeric():
    #             continue

    #         around = get_around(x, y)
    #         layers = [around[0:3], around[3:5], around[5:8]]
    #         print()
    #         print(char, layers)

    #         dy = -1

    #         for my_y, layer in enumerate(layers):
    #             for idx, l_char in enumerate(layer):
    #                 dx = idx - 1
    #                 if dy == 0 and dx == 0:
    #                     dx = 1

    #                 if l_char.isnumeric():
    #                     left = get_besides(x+dx, y+dy, -1)
    #                     right = get_besides(x+dx, y+dy, 1)

    #                     num = int("".join(left) + l_char + "".join(right))

    #                     print(f"{l_char}: x{x} y{y} -> {dx}/{dy} x{x+dx} y{y+dy}")
    #                     print(f"{str(left)} {l_char} {str(right)} = {str(num)}")
    #                     total += num
                        
    #                     if my_y == 1:
    #                         continue

    #                     if idx == 0:
    #                         if layer[idx+1] != ".":
    #                             break
    #             dy += 1

    symbols = {}
    numbers = {}
    part1 = 0
    part2 = 0

    # Store coordinates of symbols and numbers
    with open('2023/day_3/input.txt', 'r') as file:
        # Store coordinates of symbols and numbers
        line_count = 0
        for line in file:
            current_num = ''
            current_idx = -1
            for char_idx, char in enumerate(line):
                if char.isdigit():
                    if current_num == '':
                        current_idx = char_idx
                    current_num += char
                else:
                    if char not in ['.', '\n']:
                        symbols[(line_count, char_idx)] = []
                    if current_num not in numbers:
                        numbers[current_num] = []
                    numbers[current_num].append((line_count, current_idx))
                    current_idx = -1
                    current_num = ''
            line_count += 1

        # Compute part 1 and add adjacent numbers to symbols dictionary
        for number in numbers:
            for coordinate in numbers[number]:
                i = coordinate[0] - 1
                while i < coordinate[0] + 2:
                    for j in range(coordinate[1] - 1, coordinate[1] + len(number) + 1):
                        if i >= 0 and j >= 0 and i < line_count and j < line_count and (i, j) in symbols:
                            part1 += int(number)
                            symbols[(i, j)].append(int(number))
                            i = coordinate[0] + 2
                            break
                    i += 1

    # print(symbols)
    # print(numbers)

    print(part1)
    # (too high) 1050932, 1048637, 1350338 
    # (just not right) 1033938 ?1122887 ?1128624
    store_output(output, *__info, True)


if __name__ == "2023.day_3.part_1":
    main()

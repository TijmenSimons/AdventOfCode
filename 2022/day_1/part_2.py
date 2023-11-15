from __main__ import get_input, store_output

__info = [2022, 1, 2]


def main():
    data = get_input(*__info)
#     data = """1000
# 2000
# 3000

# 4000

# 5000
# 6000

# 7000
# 8000
# 9000

# 10000""".split("\n")
    elf_loads = [0]
    for item in data:
        if not item:
            elf_loads.append(0)
        else:
            elf_loads[-1] += int(item)
    
    elf_loads.sort(reverse=True)
    top_three_calories = sum(elf_loads[:3])
    store_output(top_three_calories, *__info)


if __name__ == "2022.day_1.part_2":
    main()
    

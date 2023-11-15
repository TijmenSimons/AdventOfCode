from main import get_input, store_output

__info = [2022, 1, 1]

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

# 10000"""
    elf_loads = [0]
    for item in data:
        if not item:
            elf_loads.append(0)
        else:
            elf_loads[-1] += int(item)
    
    most_calories = max(elf_loads)
    store_output(most_calories, *__info)


if __name__ == "2022.day_1.part_1":
    main()
    

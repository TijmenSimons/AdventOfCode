from main import get_input, store_output

__info = [2022, 4, 1]

def main():
    data = get_input(*__info)
#     data = """2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8
# """.split("\n")
    total = 0
    for sections in data[:-1]:
        [start_1, end_1], [start_2, end_2] = [[int(y) for y in x.split("-")] for x in sections.split(",")]
        
        if start_1 <= start_2 <= end_1 and start_1 <= end_2 <= end_1 or \
            start_2 <= start_1 <= end_2 and start_2 <= end_1 <= end_2:
            # two within one
            total += 1

    store_output(total, *__info)


if __name__ == "2022.day_4.part_1":
    main()
    

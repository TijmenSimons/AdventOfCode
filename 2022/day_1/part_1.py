from main import get_input, store_output

__info = [2022, 1, 1]

def main():
    data = get_input(*__info)
    store_output(data, *__info)


if __name__ == "2022.day_1.part_1":
    main()
    

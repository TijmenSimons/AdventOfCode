from main import get_input, store_output

__info = [2022, 22, 1]

def main():
    string = "12R98L76R87R87L53L17L36R"

    result = []
    cache = ""
    for char in string:
        if char not in {"R", "L"}:
            cache += char
            continue

        if cache:
            result.append(cache)
        result.append(char)
        cache = ""

    if cache:
        result.append(char)

    print(result)
    
    data = get_input(*__info)
    store_output(data, *__info)


if __name__ == "2022.day_22.part_1":
    main()
    

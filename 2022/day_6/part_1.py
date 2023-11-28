from main import get_input, store_output

__info = [2022, 6, 1]

def main():
    data = get_input(*__info)
#     data = """bvwbjplbgvbhsrlpgdmjqwftvncz
# nppdvjthqldpwncqszvftbrmjlhg
# nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
# zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
# """.split("\n")
    
    def compare(idx, string):
        ltrs = string[idx:idx+4]
        
        new_ltrs = {ltr: ltr for ltr in ltrs}

        return len(new_ltrs) == 4

    for datastream in data[:-1]:
        max_ = len(datastream)
        idx = 0
        while not compare(idx, datastream):
            idx += 1
            if max_ < idx:
                print("broken")
                break
        print(idx+4)

    store_output(data, *__info)


if __name__ == "2022.day_6.part_1":
    main()

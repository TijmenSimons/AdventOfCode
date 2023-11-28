from main import get_input, store_output

__info = [2022, 5, 1]

def main():
    data = get_input(*__info)
#     data = """    [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
# """.split("\n")
    
    for idx, i in enumerate(data[:-1]):
        if i == "":
            stacks_data = data[:idx]
            move_data = data[idx+1:]
            break

    amount = int((len(stacks_data[0]) + 1) / 4)
    stacks = [[] for _ in range(amount)]

    stacks_data = stacks_data[:-1]
    stacks_data.reverse()

    for row in stacks_data:
        row += " "
        columns = [row[idx*4:idx*4+4] for idx in range(amount)]
        
        for stack_idx in range(amount):
            letter = columns[stack_idx][1:2]

            if letter != " ":
                stacks[stack_idx].append(letter)

    def move_item(times, from_, to):
        ltrs = stacks[from_][-1*times:]
        [stacks[from_].pop(-1) for _ in range(times)]
        stacks[to] += ltrs
            
    for move in move_data:
        instr = move.split(" ")
        try:
            move_item(int(instr[1]), int(instr[3])-1, int(instr[5])-1)
        except IndexError:
            ...

    [print(stack) for stack in stacks]
    output = "".join([stack[-1] for stack in stacks])

    store_output(output, *__info)


if __name__ == "2022.day_5.part_2":
    main()

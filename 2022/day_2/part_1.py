from main import get_input, store_output

__info = [2022, 2, 1]

def main():
    data = get_input(*__info)
#     data = """A Y
# B X
# C Z""".split("\n")
    total_score = 0
    for battle in data[:-1]:
        foe, me = battle.split(" ")

        foe = ["A", "B", "C"].index(foe)
        me = ["X", "Y", "Z"].index(me)

        # 1 > 0 
        # 2 > 1 
        # 0 > 2 

        score = me + 1
        if me == foe:
            score += 3

        if me == 0 and foe == 2 or \
            me == 1 and foe == 0 or \
            me == 2 and foe == 1:
            score += 6

        if me == 2 and foe == 0 or \
            me == 0 and foe == 1 or \
            me == 1 and foe == 2:
            score += 0

        total_score += score

    store_output(total_score, *__info)


if __name__ == "2022.day_2.part_1":
    main()
    

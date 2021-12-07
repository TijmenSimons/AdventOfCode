from input import input

depth_array = input.split("\n")

increase_amount = -1 # I could not be bothered. It's for Christmas!
last_depth_sum = 0
slot_1 = 0
slot_2 = 0

for depth in depth_array:
    depth = int(depth)
    # print('depth: '+str(depth)+' slot_1: '+str(slot_1)+' slot_2: '+str(slot_2)+'    =   ' + str(depth + slot_1 + slot_2))
    

    if slot_2 != 0:
        # print('active')

        depth_sum = depth + slot_1 + slot_2

        if depth_sum > last_depth_sum:
            
            increase_amount += 1

        #     print('higher :      '+ str(increase_amount))
        # else:
        #     print('not higher')
        
        last_depth_sum = depth_sum


    slot_2 = slot_1
    slot_1 = depth



print(increase_amount)
from input import input

depth_array = input.split("\n")

last_depth = int(depth_array[0])
increase_amount = 0

for depth in depth_array:
    depth = int(depth)
    
    if depth > last_depth:
        increase_amount+=1
    
    last_depth = depth

print(increase_amount)
from input import input


directions_array = input.split('\n')

x = 0 # horizontal
y = 0 # depth (vertical)

for direction in directions_array:
    raw_direction = direction.split(" ")
    match raw_direction[0]:
        case "forward":
            # print('forwards by '+str(raw_direction[1])+'!')
            x+=int(raw_direction[1])

        case "up":
            # print('upwards by '+str(raw_direction[1])+'!')
            y-=int(raw_direction[1])

        case "down":
            # print('downwards by '+str(raw_direction[1])+'!')
            y+=int(raw_direction[1])

print('\n\n\nMultiplying the final horizontal position ('+str(x)+') with the final depth ('+str(y)+') gives: '+str(x*y)+'\n\n')


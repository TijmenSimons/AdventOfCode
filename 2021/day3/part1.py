from input import input as input

def byte_to_int(byte):
    max = len(byte)
    pos = 0
    count = 0
    while max > pos:
        if byte[max - 1 - pos] == "1":
            count+=2**pos
        pos+=1
    return count


bit_array = input.split("\n")
gamma_rate = ""
epsilon_rate = ""

for column_pos in range(len(bit_array[0])):
    zero = 0
    one = 0
    for bit in bit_array:
        match bit[column_pos]:
            case "1":
                one+=1
            case "0":
                zero+=1
    if one > zero:
        gamma_rate+="1"
        epsilon_rate+="0"
    else:
        gamma_rate+="0"
        epsilon_rate+="1"

print('The gamma rate is: '+gamma_rate+' ('+str(byte_to_int(gamma_rate))+')\nAnd the epsilon rate is: '+epsilon_rate+' ('+str(byte_to_int(epsilon_rate))+')')
print('And these rates multiplied by each other result in: '+str(byte_to_int(gamma_rate)*byte_to_int(epsilon_rate)))
inputs = ""

with open("input.txt", "r") as f:
    inputs = f.read()

inputs = inputs.split("\n")

SNAFU = {
    "=": -2,
    "-": -1,
    "2": 2,
    "1": 1,
    "0": 0
}

def convertNumber(str):
    str = str[::-1]
    value = 0

    def getValue(num, idx): 
        return num * 5 ** idx

    def convertInt(num):
        if num == "-": return -1
        if num == "=": return -2
        else: return int(num)
        
    for (idx, num) in enumerate(str): 
        value += getValue(convertInt(num), idx)

    return value

from math import log
def convertSNAFU(number: int) -> str:
    snafu = ""
    number_of_SNAFU_digits = round(log(number)/log(5)) #Minimised the function (5^x-D)^2. The SNAFU will have as many numbers (x) that minimises the squared distance between 5^x and decimal number.
    num =0
    for _ in range(number_of_SNAFU_digits+1):
        d = {k: number - (v * 5 ** (number_of_SNAFU_digits) + num) for k, v in SNAFU.items()} #Calculate the distance to decimal input from the SNAFU^5
        snafu_key = min(d, key=lambda x: abs(d[x])) #The SNAFU digit would be the key that minimises the above distance.
        snafu += snafu_key    
        num += SNAFU[snafu_key]*5**number_of_SNAFU_digits
        number_of_SNAFU_digits -= 1    
    return snafu


# txt = "2=-1=0"

# r = convertNumber(txt)
# print(r)

# sn = convertSNAFU(r)
# print(sn)

total = 0

for row in inputs:
    num = convertNumber(row)
    total += num

total_snafu = convertSNAFU(total)
print(total_snafu)

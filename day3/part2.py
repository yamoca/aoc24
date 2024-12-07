import re

testinput = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

sum = 0 
do = True 
with open("input.txt") as f:
    data = f.readlines()

for line in data:
    matches = re.findall(r"(mul\(([0-9]{1,3}),([0-9]{1,3})\)|don't\(\)|do\(\))", line) # use r"___" for raw string so python doesnt get annoyed at backslashes
    for match in matches:
        print(sum)
        print(do)
        if match[0].find("mul") != -1 and do:
            sum += int(match[1]) * int(match[2])
        elif match[0].find("don't") != -1:
            do = False
        elif match[0].find("do") != -1:
            do = True


print(sum)
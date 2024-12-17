import copy

file = open("testinput.txt")
equations = { } 
for line in file.readlines():
    key = int(line.strip().split(":")[0])
    values = line.strip().split(":")[1].lstrip(" ").split(" ")
    values = [int(x) for x in values]  # convert to ints
    equations[key] = values 


def evaluateCalcs(desired, values, operators):
    sum = values[0] 
    values.pop(0) # start with first val and remove it
    for i in range(len(values)):
        if operators[i] == "*":
            print(sum, "*", values[i], "=", sum*values[i])
            sum = sum * values[i]
        elif operators[i] == "+":
            print(sum, "+", values[i], "=", sum+values[i])
            sum += values[i]
        else:
            print("unknown operator", operators[i], "in", operators)
        
    if sum == desired:
        return sum 
    else:
        return False



total_calibration_result = 0


for key in equations:
    desired = copy.deepcopy(key) 
    values = equations[key]
    operators = []
    for i in range(len(values)-1, 0, -1):
        if key % values[i] == 0:
            # print(key, "is divisble by", values[i])
            operators.insert(0, "*")
        else:
            operators.insert(0, "+")
            key -= values[i]

    if evaluateCalcs(desired, values, operators):
        total_calibration_result += desired 
    print(key)
    print(values)
    print(operators)
    print()


testdesired = 292 
testvals = [11, 6, 16, 20] 
testoperators = ['+', '*', '+']


print(total_calibration_result)
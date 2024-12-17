from itertools import product

file = open("input.txt")
equations = { } 
for line in file.readlines():
    key = int(line.strip().split(":")[0])
    values = line.strip().split(":")[1].lstrip(" ").split(" ")
    values = [int(x) for x in values]  # convert to ints
    equations[key] = values 


print(equations)

def evaluateCalcs(desired, values, operators):
    sum = values[0] 
    # sum = values.pop(0) # start with first val and remove it
    for i in range(1, len(values)):
        if operators[i-1] == "*":
            # print(sum, "*", values[i], "=", sum*values[i])
            sum = sum * values[i]
        elif operators[i-1] == "+":
            # print(sum, "+", values[i], "=", sum+values[i])
            sum += values[i]
        elif operators[i-1] == "|":
            sum = int(str(sum)+str(values[i]))
        else:
            print("unknown operator", operators[i], "in", operators)
        
    if sum == desired:
        return True 
    else:
        return False



total_calibration_result = 0
for key in equations:
    values = equations[key]
    operator_combinations = product("+*|", repeat=len(values)-1)
    for operators in operator_combinations:
        if evaluateCalcs(key, values, operators):
            total_calibration_result += key 
            break


print(total_calibration_result)
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
    # print(values, "pre pop len", len(values))
    sum = values.pop(0) # start with first val and remove it
    # print(values, "post pop", len(values))
    for i in range(len(values)):
        if operators[i-1] == "*":
            # print(sum, "*", values[i], "=", sum*values[i])
            sum = sum * values[i]
        elif operators[i-1] == "+":
            # print(sum, "+", values[i], "=", sum+values[i])
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
    # print(values)
    for i in range(len(values)-1, 0, -1):
        if key % values[i] == 0:
            print(key, "divided by", values[i], "equals", int(key/values[i]))
            operators.insert(0, "*")
            key = key / values[i]
            key = int(key)

        else:
            print(key, "minus", values[i], "equals", key-values[i])
            operators.insert(0, "+")
            key -= values[i]


    # print(operators)
    if evaluateCalcs(desired, values, operators):
        total_calibration_result += desired 
        # print(desired)
        # print(values)
        # print(operators)
        print()

    print(total_calibration_result)




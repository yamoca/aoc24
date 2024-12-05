reports = []
with open("input.txt") as f:
    for line in f:
        report = [int(x) for x in line.strip().split(" ")]
        reports.append(report)



def calcGradient(first, second):
    if first > second: 
        return "decreasing"
    elif first < second: 
        return "increasing"
    else:
        return "equal"





def isSafe(report):
    gradient = calcGradient(report[0], report[1])
    if gradient == "equal":
        return False
    else:
        for levelIndex in range(len(report)-1):
            if calcGradient(report[levelIndex], report[levelIndex+1]) != gradient:
                return False
            if gradient == "increasing":
                if report[levelIndex+1] - report[levelIndex] > 3:
                    return False
            if gradient == "decreasing":
                if report[levelIndex] - report[levelIndex+1] > 3:
                    return False

    return True 


safetotal = 0
for report in reports:
    if isSafe(report):
        safetotal += 1
    else:
        for levelIndex in range(len(report)):
            copy = report
            # print(copy)
            removedVal = copy.pop(levelIndex)
            if isSafe(copy):
                safetotal += 1
                break
            else:
                copy.insert(levelIndex, removedVal)






print(safetotal) 
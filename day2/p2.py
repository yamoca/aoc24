"""
game plan:
keep counter
if counter = 0 and unsafe, counter = 1 and remove current level, recheck by doing level-1 or smth
"""

"""
safes being categorizes as unsafes
2, 3, 4, 126, 127, 128, 256, 283, 306,  
"""


reports = []
with open("input.txt") as f:
    for line in f:
        report = [int(x) for x in line.strip().split(" ")]
        reports.append(report)


safe_count = 0
reportnum = 0
changedsafecoiunt = 0


def checkIsSafe(report):
    if int(report[0]) == int(report[1]):
        return False 
    elif int(report[0]) > int(report[1]): # e.g 10, 6
        gradient = "decreasing"
    else:
        gradient = "increasing"

    for level in range(len(report)-1):
        if gradient == "decreasing":
            if report[level] - report[level+1] > 3 or report[level] <= report[level+1]:
                return False
        if gradient == "increasing":
            if report[level] - report[level+1] < -3 or report[level] >= report[level+1]:
                return False


    return True


safes = []

for index in range(len(reports)):
    report = reports[index]
    if checkIsSafe(report):
        safe_count += 1
        safes.append(index)
        continue
    else:
        for i in range(len(report)-1):
            subreport = report[:]
            subreport.pop(i)
            if checkIsSafe(subreport):
                safe_count += 1
                safes.append(index)
                break
    



   
print(reports[safes[-1]])
# print(changedsafecoiunt) 
print(safe_count)
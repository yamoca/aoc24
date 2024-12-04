"""
game plan:
do report[i] - report[i+1] pos/neg = increasing/decreasing, value = increase value
check bounds 
increment safe counter
"""

reports = []
f = open("testinput.txt")
for line in f.readlines():
    report = line.strip().split(" ")
    reports.append(report)


safe_count = 0
for report in reports:
    unsafe = False
    if int(report[0]) == int(report[1]):
        unsafe = True
        break
    elif int(report[0]) > int(report[1]): # e.g 10, 6
        gradient = "decreasing"
    else:
        gradient = "increasing"

    for level in range(len(report)-1):
        if gradient == "decreasing":
            if int(report[level]) - int(report[level+1]) > 3:
                unsafe = True
        if gradient == "increasing":
            if int(report[level]) - int(report[level+1]) < 3:
                unsafe = True

    if not unsafe:
        print(report, " was safe")
        safe_count += 1


print(safe_count)
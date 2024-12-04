"""
game plan:
do report[i] - report[i+1] pos/neg = increasing/decreasing, value = increase value
check bounds 
increment safe counter
"""

reports = []
f = open("input.txt")
for line in f.readlines():
    report = line.strip().split(" ")
    reports.append(report)


safe_count = 0
for report in reports:
    unsafe = False
    if int(report[0]) == int(report[1]):
        print(report, " first numbers equal")
        unsafe = True
        break
    elif int(report[0]) > int(report[1]): # e.g 10, 6
        print(report, " decreasing")
        gradient = "decreasing"
    else:
        gradient = "increasing"
        print(report, " increasing")


    # problem where it allows decrease then increase or vice versa
    for level in range(len(report)-1):
        if report[level] == report[level+1]:
            unsafe = True
        if gradient == "decreasing":
            if int(report[level]) - int(report[level+1]) > 3 or report[level] < report[level+1]: # check if within bounds AND if gradient is same direction
                print(report, " unsafe at step 1" )
                unsafe = True
        if gradient == "increasing":
            if int(report[level]) - int(report[level+1]) < -3 or report[level] > report[level+1]:
                print(report, " unsafe at step 2")
                unsafe = True

    if not unsafe:
        print(report, " was safe")
        safe_count += 1


print(safe_count)
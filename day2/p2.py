"""
game plan:
keep counter
if counter = 0 and unsafe, counter = 1 and remove current level, recheck by doing level-1 or smth
"""



reports = []
f = open("testinput.txt")
for line in f.readlines():
    report = line.strip().split(" ")
    reports.append(report)


safe_count = 0
reportnum = 0
for report in reports:
    reportnum += 1
    unsafe = False
    if int(report[0]) == int(report[1]):
        # print(report, " first numbers equal")
        unsafe = True
    elif int(report[0]) > int(report[1]): # e.g 10, 6
        # print(report, " decreasing")
        gradient = "decreasing"
    else:
        gradient = "increasing"
        # print(report, " increasing")


    removedCounter = 0 
    copy = []
    for level in range(len(report)-1):
        # print("level: ", level)
        # print(report[level-removedCounter])
        # print(report[level+1-removedCounter])
        # print()
        if gradient == "decreasing":
            if int(report[level-removedCounter]) - int(report[level+1-removedCounter]) > 3 or int(report[level-removedCounter]) <= int(report[level+1-removedCounter]): # check if within bounds AND if gradient is same direction
                if removedCounter == 0: # ie dampener hasnt been activated
                    # report.remove(report[level])
                    report.pop(level+1)
                    print(report, "after removing")
                    print("value number: ", level, "value removed: ", report[level+1])
                    removedCounter += 1
                    copy = report
                else:
                    unsafe = True
                # break
        if gradient == "increasing":
            if int(report[level-removedCounter]) - int(report[level+1-removedCounter]) < -3 or int(report[level-removedCounter]) >= int(report[level+1-removedCounter]):
                if removedCounter == 0:
                    # report.remove(report[level])
                    report.pop(level+1)
                    print(report, "after removing")
                    print("value number: ", level, "value removed: ", report[level+1])
                    removedCounter += 1
                    copy = report
                else:
                    unsafe = True
                # break

    if not unsafe:
        print(report, " (report number: ", reportnum, ") was safe")
        print(copy)
        print()
        safe_count += 1


print(safe_count)
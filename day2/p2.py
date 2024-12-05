"""
game plan:
keep counter
if counter = 0 and unsafe, counter = 1 and remove current level, recheck by doing level-1 or smth
"""



# reports = []
# f = open("input.txt")
# for line in f.readlines():
#     report = line.strip().split(" ")
#     reports.append(report)

reports = []
with open("input.txt") as f:
    for line in f:
        report = [int(x) for x in line.strip().split(" ")]
        reports.append(report)


safe_count = 0
reportnum = 0

def checkIsSafe(report):
    # reportnum += 1
    if int(report[0]) == int(report[1]):
        # print(report, " first numbers equal")
        return False 
    elif int(report[0]) > int(report[1]): # e.g 10, 6
        # print(report, " decreasing")
        gradient = "decreasing"
    else:
        gradient = "increasing"
        # print(report, " increasing")


    ### PROBLEM: IN SOME SITUATIONS SHOULD REMOVE i, some others should remove i+1
    ### solution: must brute force (test sublists of removing each number from list aka consider 5234, error happens at 2 3 but answer is change 5 not 2 or 3)
    ### also incorrectly saying changed things are safe (not tracking back properly?)
    # removedCounter = 0 
    # copy = []


    levelnumber = 0 
    while levelnumber < len(report)-1:
        # print(report[levelnumber], report[levelnumber+1])
        # print()
        # print("checking with above values")
        if gradient == "decreasing":
            if int(report[levelnumber]) - int(report[levelnumber+1]) > 3 or int(report[levelnumber]) <= int(report[levelnumber+1]):
                # if removedCounter == 0:
                #     checkIsSafe(report.pop(levelnumber))
                    # removedval = report.pop(levelnumber)
                    # print(report, "after removing")
                    # print("value number: ", levelnumber, "value removed: ", removedval) 
                    # removedCounter += 1
                    # print(report[levelnumber], report[levelnumber+1])
                    # if levelnumber != 0:
                    #     levelnumber -=2 
                    # print(report[levelnumber], report[levelnumber+1])
                # else:
                return False
        if gradient == "increasing":
            if int(report[levelnumber]) - int(report[levelnumber+1]) < -3 or int(report[levelnumber]) >= int(report[levelnumber+1]):
                # if removedCounter == 0:
                #     checkIsSafe(report.pop(levelnumber))
                #     # removedval = report.pop(levelnumber)
                    # print(report, "after removing")
                    # print("value number: ", levelnumber, "value removed: ", removedval) 
                    # removedCounter += 1
                    # print(report[levelnumber], report[levelnumber+1])
                    # if levelnumber != 0:
                    #     levelnumber -=2 
                    # print(report[levelnumber], report[levelnumber+1])
                # else:
                return False

        levelnumber += 1



    # print(report, " (report number: ", reportnum, ") was safe")
    # print(copy)
    return True


for report in reports:
    if checkIsSafe(report):
        # print(report, "was safe")
        safe_count += 1
        continue
    for i in range(len(report)-1):
        # print("report, ", report)
        subreport = report[:]
        subreport.pop(i)
        # print("copy, ", subreport)
        if checkIsSafe(subreport):
            print(subreport, "is safe")
            safe_count += 1
            break



    # for level in range(len(report)-1):
    #     # print("level: ", level)
    #     # print(report[level-removedCounter])
    #     # print(report[level+1-removedCounter])
    #     # print()
    #     if gradient == "decreasing":
    #         if int(report[level-removedCounter]) - int(report[level+1-removedCounter]) > 3 or int(report[level-removedCounter]) <= int(report[level+1-removedCounter]): # check if within bounds AND if gradient is same direction
    #             if removedCounter == 0: # ie dampener hasnt been activated
    #                 # report.remove(report[level])
    #                 removedval = report.pop(level-removedCounter)
    #                 print(report, "after removing")
    #                 print("value number: ", level, "value removed: ", removedval) 
    #                 removedCounter += 1
    #                 copy = report
    #             else:
    #                 unsafe = True
    #             # break
    #     if gradient == "increasing":
    #         if int(report[level-removedCounter]) - int(report[level+1-removedCounter]) < -3 or int(report[level-removedCounter]) >= int(report[level+1-removedCounter]):
    #             if removedCounter == 0:
    #                 # report.remove(report[level])
    #                 removedval = report.pop(level-removedCounter)
    #                 print(report, "after removing")
    #                 print("increasing value number: ", level, "value removed: ", removedval) 
    #                 removedCounter += 1
    #                 copy = report
    #             else:
    #                 unsafe = True
    #             # break

    
print(safe_count)
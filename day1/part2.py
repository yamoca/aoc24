"""
initial idea:
remove duplicates from left list
count how many repeats by incrementing counter everytime difference = 0 

second
remove duplicates from left
count repeats by comparing if i+1 = i in right list

finalish (to working):
dont actually need to remove dupes from left
"""

list1 = []
list2 = []
f = open("input.txt", "r")
for line in f.readlines():
    parts = line.split("   ")
    list1.insert(0, int(parts[0]))
    list2.insert(0, int(parts[1].strip()))


list1.sort()

# def removeDuplicates(dupes):
#     totalRemoved = 0 # track count of items removed from list (as list will progressively get shorter) as items shift to the left
#     for i in range(len(dupes)-2):
#         if dupes[i-totalRemoved] == dupes[i-totalRemoved+1]:
#             dupes.pop(i-totalRemoved)
#             totalRemoved +=1

#     return dupes


# could make faster by removing the ones counted so not regoing over irrelevant numbers
# could also make faster cause if i sort it then i only need to look at a fraction of the whole list:
# search for first appearance of desired num, increment from there, as soon as dupes[i] > num, stop.
def countDupes(num, dupes):
    count = 0
    for i in range(len(dupes)):
        if dupes[i] == num: 
            count += 1

    return count



similarity_score = 0
for i in range(len(list1)):
    similarity_score += list1[i] * countDupes(list1[i], list2)

print(similarity_score)
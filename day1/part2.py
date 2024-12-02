"""
initial idea:
remove duplicates from left list
count how many repeats by incrementing counter everytime difference = 0 

second
remove duplicates from left
count repeats by comparing if i+1 = i in right list
"""

list1 = []
list2 = []
f = open("testinput.txt", "r")
for line in f.readlines():
    parts = line.split("   ")
    list1.insert(0, int(parts[0]))
    list2.insert(0, int(parts[1].strip()))


list1.sort()

def removeDuplicates(dupes):
    totalRemoved = 0 # track count of items removed from list (as list will progressively get shorter) as items shift to the left
    for i in range(len(dupes)-2):
        if dupes[i-totalRemoved] == dupes[i-totalRemoved+1]:
            dupes.pop(i-totalRemoved)
            totalRemoved +=1

    return dupes


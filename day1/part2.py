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


#remove duplicates 
list1.sort()

print(list1)
for i in range(len(list1)-2):
    print(i)
    print(list1[i])
    print(list1[i+1])
    print("")
    if list1[i] == list1[i+1]:
        list1.pop(i)
        i -= 1

print(list1)
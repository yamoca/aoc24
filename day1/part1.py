""" 
Thought process:
sort both lists small to large
compare into new list 
sum list 
"""

# def bubbleSort(list):
#     for i in range(len(list)-1):
#         for j in range(len(list)-1):
#             if list[i] > list[j+1]:
#                 # swap
#                 temp = list[i]
#                 list[i] = list[j+1]
#                 list[j+1] = temp
    
#     return list


list1 = []
list2 = []
f = open("input.txt", "r")
for line in f.readlines():
    parts = line.split("   ")
    list1.insert(0, int(parts[0]))
    list2.insert(0, int(parts[1].strip()))


# list1 = [3, 4, 2, 1, 3, 3]
# list2 = [4, 3, 5, 3, 9, 3]
list1.sort()
list2.sort()
sum = 0
for i in range(len(list1)):
    if list1[i] > list2[i]:
        print("difference: ", list1[i] - list2[i])
        sum += list1[i] - list2[i]
    else:
        print("difference: ", list2[i] - list1[i])
        sum += list2[i] - list1[i]
    print(sum)
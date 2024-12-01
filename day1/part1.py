""" 
Thought process:
sort both lists small to large
compare into new list 
sum list 
"""

def bubbleSort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1):
            if list[i] > list[j+1]:
                # swap
                temp = list[i]
                list[i] = list[j+1]
                list[j+1] = temp
    
    return list



list1 = [4, 2, 1, 3]
list2 = [3, 5, 3, 9]
list1 = bubbleSort(list1)
list2 = bubbleSort(list2)
print(list1)
print(list2)
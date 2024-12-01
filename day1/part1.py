""" 
Thought process:
sort both lists small to large
compare into new list 
sum list 
"""

def bubbleSort(list):
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            # swap
            temp = list[i]
            list[i] = list[i+1]
            list[i+1] = temp
    
    return list



testlist = [3, 1, 4, 5, 6]
print(bubbleSort(testlist))

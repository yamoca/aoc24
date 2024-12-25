file = open("input.txt")
testdiskmap = file.readline().strip()


def diskmap_to_diskblocks(diskmap):
    diskblocks = [] 
    id = 0
    for i in range(len(diskmap)):
        if i % 2 != 0: # odd index's are free space blocks 
            block = ["." for x in range(int(diskmap[i]))]
            if len(block) >= 1: #only append if block is not empty 
                diskblocks.append(block)
        else:
            block = [id for x in range(int(diskmap[i]))]
            id += 1
            diskblocks.append(block)

    return diskblocks


testdiskblock = diskmap_to_diskblocks(testdiskmap)
print(testdiskblock)
print()
print()
print()

def moveFreeSpace(diskblocks):
    i = len(diskblocks)-1
    while i >= 0:
        if len(diskblocks[i]) == 0:
            i -= 1
        elif diskblocks[i][0] != ".": # dont try and move free space 
            printthelist(diskblocks)
            free_space_index = findFreeSpaceToLeft(diskblocks, i, len(diskblocks[i]))
            if free_space_index != -1:
                size_of_space = len(diskblocks[free_space_index])
                diskblocks.insert(free_space_index, diskblocks[i])
                # print("inserted")
                # print(diskblocks)
                if size_of_space == len(diskblocks[i+1]):
                    print("fitted perfectly")
                    diskblocks.pop(i+1)
                    diskblocks.insert(i, diskblocks.pop(free_space_index+1))
                    printthelist(diskblocks)
                else:
                    consumed = diskblocks[free_space_index+1][len(diskblocks[i+1])-1:]
                    leftover = diskblocks[free_space_index+1][:len(diskblocks[i+1])-1]
                    # print("leftovers", leftover)
                    # print("consumed", consumed)
                    diskblocks.pop(i+1)
                    # print("popped")
                    # print(diskblocks)
                    diskblocks[free_space_index+1] = leftover
                    # print("leftovers modified")
                    # print(diskblocks)
                    diskblocks.insert(i+1, consumed)
                    # print("appended")
                    printthelist(diskblocks)
            else: # only decrement if nothing is inserted. if things are inserted into list and we decrement index will be pointing at wrong item
                i -= 1
        else: # if current block is free space, dont do anything and just decrement and go to next
            i -= 1
    return diskblocks


import itertools

def printthelist(diskblocks):
    deez = list(itertools.chain.from_iterable(diskblocks))
    string = ""
    for item in deez:
        string += str(item)
    print(string)


def findFreeSpaceToLeft(diskblocks, currentIndex, size):
    for i in range(currentIndex): # only look up to current index to avoid moving the wrong direction 
        if len(diskblocks[i]) >= size and diskblocks[i][0] == ".": # if its starts with "." it will be empty space
            return i
    else:
        return -1





print()
print()
print()
print()
print()
print()

diskblocks = moveFreeSpace(testdiskblock)
print(diskblocks)


oriented = list(itertools.chain.from_iterable(diskblocks)) 
print(oriented)

def calcChecksum(diskblocks):
    checkSum = 0
    for i in range(len(diskblocks)):
        if diskblocks[i] != ".":
            checkSum += i * diskblocks[i]

    return checkSum


print(calcChecksum(oriented))
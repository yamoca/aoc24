file = open("testinput.txt")
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

def moveFreeSpace(diskblocks):
    for i in range(len(diskblocks)-1, -1, -1): # loop backwards
        print()
        print()
        print()
        print(diskblocks[i])
        print("before changes this round")
        print(diskblocks)
        free_space_index = findFreeSpaceToLeft(diskblocks, i, len(diskblocks[i]))
        if free_space_index != -1:
            size_of_space = len(diskblocks[free_space_index])
            diskblocks.insert(free_space_index, diskblocks[i])
            print("inserted")
            print(diskblocks)
            if size_of_space == len(diskblocks[i]):
                diskblocks.pop(i+1)
                diskblocks.append(diskblocks.pop(free_space_index+1))
            else:
                consumed = diskblocks[free_space_index+1][len(diskblocks[i+1])-1:]
                leftover = diskblocks[free_space_index+1][:len(diskblocks[i+1])-1]
                print("leftovers", leftover)
                print("consumed", consumed)
                diskblocks.pop(i+1)
                print("popped")
                print(diskblocks)
                diskblocks[free_space_index+1] = leftover
                print("leftovers modified")
                print(diskblocks)
                diskblocks.append(consumed)
                print("appended")
                print(diskblocks)

    return diskblocks





def findFreeSpaceToLeft(diskblocks, currentIndex, size):
    for i in range(currentIndex): # only look up to current index to avoid moving the wrong direction 
        if len(diskblocks[i]) >= size and diskblocks[i][0] == ".": # if its starts with "." it will be empty space
            return i
    else:
        return -1


print(moveFreeSpace(testdiskblock))



def calcChecksum(diskblocks):
    checkSum = 0
    for i in range(len(diskblocks)):
        if diskblocks[i] == ".":
            break
        else:
            checkSum += i * diskblocks[i]

    return checkSum


# print(calcChecksum(oriented))
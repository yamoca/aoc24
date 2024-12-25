file = open("testinput.txt")
testdiskmap = file.readline().strip()


def diskmap_to_diskblocks(diskmap):
    diskblocks = [] 
    id = 0
    for i in range(len(diskmap)):
        if i % 2 != 0: # odd index's are free space blocks 
            block = ["." for x in range(int(diskmap[i]))]
            for num in block:
                diskblocks.append(num)
        else:
            block = [id for x in range(int(diskmap[i]))]
            id += 1
            for num in block:
                diskblocks.append(num)

    return diskblocks


testdiskblock = diskmap_to_diskblocks(testdiskmap)


def moveFreeSpace(diskblocks):
    currentChar = diskblocks[len(diskblocks)] 
    for i in range(len(diskblocks)-1, -1, -1): # loop backwards
        if diskblocks[i] == "john":
            pass



# oriented = moveFreeSpace(testdiskblock)
# print(oriented)

def findEmptySpace(diskblocks, size):
    first_free_space = diskblocks.index(".")
    currentChar = "."
    count = 0
    for i in range(first_free_space, len(diskblocks)):
        if count == size:
            return first_free_space, i-1
        elif diskblocks[i] == currentChar:
            count += 1
        else:
            break
    


print(testdiskblock)
print(findEmptySpace(testdiskblock, 3))


def calcChecksum(diskblocks):
    checkSum = 0
    for i in range(len(diskblocks)):
        if diskblocks[i] == ".":
            break
        else:
            checkSum += i * diskblocks[i]

    return checkSum


# print(calcChecksum(oriented))
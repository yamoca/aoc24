
file = open("input.txt")
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
print(testdiskblock)


def moveFreeSpace(diskblocks):
    for i in range(len(diskblocks)-1, -1, -1): # loop backwards
        diskblocks[diskblocks.index(".")] = diskblocks[i]
        diskblocks[i] = "."
    # ends up correct but with a "." in front so just remove it and put it at back
    # (because loops through whole list, doesnt stop as soon as there numbers and "." are seperated)
    diskblocks.pop(0)
    diskblocks.append(".")
    return diskblocks

oriented = moveFreeSpace(testdiskblock)
print(oriented)

def calcChecksum(diskblocks):
    checkSum = 0
    for i in range(len(diskblocks)):
        if diskblocks[i] == ".":
            break
        else:
            checkSum += i * diskblocks[i]

    return checkSum


print(calcChecksum(oriented))
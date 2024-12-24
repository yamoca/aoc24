# if 

testdiskmap = "2333133121414131402"


def diskmap_to_diskblocks(diskmap):
    diskblocks = "" 
    id = 0
    for i in range(len(diskmap)):
        if i % 2 != 0: # odd index's are free space blocks 
            block = ["." for x in range(int(diskmap[i]))]
            for num in block:
                diskblocks += num
        else:
            block = [id for x in range(int(diskmap[i]))]
            id += 1
            for num in block:
                diskblocks += str(num)

    return diskblocks


print(diskmap_to_diskblocks(testdiskmap))
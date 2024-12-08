import re

data = []
with open("testinput.txt") as f:
    for line in f.readlines():
        data.append(line.strip())


horizonantal = []
def count_matches(data):
    for line in data:
        matches = re.findall("(?=(XMAS|SAMX))", line) #(?=) is a lookahead to find overlapping e.g XMASAMX should find 2
        if len(matches) > 0:
            for match in matches:
                horizonantal.append(match)

    print(len(horizonantal))
    print(horizonantal)


count_matches(data)

rotatedtuple = tuple(zip(*data))
rotated = []
for line in rotatedtuple:
    line = ''.join(line)
    rotated.insert(0, line)

print("normal", data)
print("rotated", rotated)

count_matches(rotated)
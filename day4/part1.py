import re

data = []
with open("testinput.txt") as f:
    for line in f.readlines():
        data.append(line.strip())


horizonantal = []
for line in data:
    matches = re.findall("XMAS", line)
    if len(matches) > 0:
        for match in matches:
            horizonantal.append(match)

print(len(horizonantal))
print(horizonantal)
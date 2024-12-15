f = open("testinput.txt")
rules = []
updates = []
nextsegment = False
for line in f.readlines():
    if line == "\n":
        nextsegment = True
    else:
        if not nextsegment:
            rules.append(line.strip())
        else:
            updates.append(line.strip())


print(rules)
print()
print(updates)
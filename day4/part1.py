data = []
with open("testinput.txt") as f:
    for line in f.readlines():
        data.append(line.strip())



print(data)
file = open("testinput.txt")
equations = { } 
for line in file.readlines():
    value = int(line.strip().split(":")[0])
    parts = line.strip().split(":")[1].lstrip(" ").split(" ")
    parts = [int(x) for x in parts]  # convert to ints
    equations[value] = parts


print(equations)
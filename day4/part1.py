import re

data = []
with open("input.txt") as f:
    for line in f.readlines():
        data.append(line.strip())


# max diagonals = 2xwidth/height (should be a square) 
def get_diagonals(data, max_diagonals):
    diagonaldata = []
    combined = [] 
    # First set of diagonals (data[i][i+offset])
    for offset in range(max_diagonals//2):
        diagonal = [data[i][i+offset] for i in range(len(data)-offset)]
        diagonaldata.append(diagonal)
    
    # Second set of diagonals (data[i+1][i])
    for offset in range(max_diagonals//2):
        diagonal = [data[i+1+offset][i] for i in range(len(data)-1-offset)]
        diagonaldata.append(diagonal)

    for line in diagonaldata:
        line = ''.join(line)
        combined.insert(0, line)

    return combined 


horizonantal = []
def count_matches(data):
    for line in data:
        matches = re.findall("(?=(XMAS|SAMX))", line) #(?=) is a lookahead to find overlapping e.g XMASAMX should find 2
        if len(matches) > 0:
            for match in matches:
                horizonantal.append(match)

    print(len(horizonantal))
    # print(horizonantal)



# horizontal
count_matches(data)
# for test data should be 5

# diagonal
diagonaldata = get_diagonals(data, 2*len(data))

count_matches(diagonaldata)




# rotate
rotatedtuple = tuple(zip(*data))
rotated = []
for line in rotatedtuple:
    line = ''.join(line)
    rotated.insert(0, line)

# vertical
count_matches(rotated)
# for test data should be 3

rotateddiagonaldata = get_diagonals(data, 2*len(data))
count_matches(rotateddiagonaldata)



# counter = 0
# for i in range(len(data)):
#     for j in range(len(data)):
#         diagonaldata.append(data[i][j-counter])
#         counter += 1


# first diag = [0][0] data[1][1] data[2][2] [3][3] etc
# second diag = data[0][1] [1][2] [1][3]

# d1 = []
# d2 = []
# d3 = []
# d4 = []
# d5 = []
# d6 = []
# d7 = []
# d8 = []
# d9 = []
# d10 = []

# for i in range(len(data)):
#     d1.append(data[i][i])

# for i in range(len(data)-1):
#     d2.append(data[i][i+1])

# for i in range(len(data)-2):
#     d3.append(data[i][i+2])

# for i in range(len(data)-3):
#     d4.append(data[i][i+3])

# for i in range(len(data)-4):
#     d5.append(data[i][i+4])

# for i in range(len(data)-5):
#     d6.append(data[i][i+5])

# for i in range(len(data)-6):
#     d7.append(data[i][i+6])

# for i in range(len(data)-7):
#     d8.append(data[i][i+7])

# for i in range(len(data)-8):
#     d9.append(data[i][i+8])

# for i in range(len(data)-9):
#     d10.append(data[i][i+9])

# diagonaldata = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]
# print(diagonaldata)

# print(diagonaldata)
file = open("testinput.txt")
board = []
for line in file.readlines():
    row = list(line.strip())
    board.append(row)

print(board)
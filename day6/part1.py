file = open("input.txt")
board = []
for line in file.readlines():
    row = list(line.strip())
    board.append(row)





############################
# add bounding box of exclamation points for detecting out of bounds
for row in board:
    row.insert(0, "!")
    row.append("!")

topnbottom = []
for char in board[0]:
    topnbottom.append("!")

board.insert(0, topnbottom)
board.append(topnbottom)

#####################
print(board)



# one liner for below code
# starting_pos  = (row.index("^"), index) for index, row in enumerate(board) if "^" in row
for row_index, row in enumerate(board):
    if "^" in row:
        col_index = row.index("^")
        starting_pos = [row_index, col_index] ## slightly counterintuitive colindex is x (think about it) BUT THATS HOW IT WORKS IN FLIPPING board[y][x]



## 2d arrays do not play nice with coordinates, dont think about it in that way
inside = True 

position_coords = starting_pos
while inside:
    char_at_position = board[position_coords[0]][position_coords[1]]
    print(position_coords)
    print(char_at_position)

    north_char = board[position_coords[0]-1][position_coords[1]]
    east_char = board[position_coords[0]][position_coords[1]+1]
    south_char = board[position_coords[0]+1][position_coords[1]]
    west_char = board[position_coords[0]][position_coords[1]-1]

    if char_at_position == "^": ## moving north 
        if north_char == "!": ## trying to move out of bounds 
            inside = False
            board[position_coords[0]][position_coords[1]] = "X" # mark path 
        elif north_char == "#": ## obstruction
            board[position_coords[0]][position_coords[1]] = ">" # turn right (east)
        else:
            board[position_coords[0]-1][position_coords[1]] = "^" ## move forwards (north)
            board[position_coords[0]][position_coords[1]] = "X" # mark path 
            position_coords[0] -= 1 # update position
    elif char_at_position == ">": ## moving east
        if east_char == "!":
            inside = False
            board[position_coords[0]][position_coords[1]] = "X" # mark path 
        elif east_char == "#":
            board[position_coords[0]][position_coords[1]] = "v"
        else:
            board[position_coords[0]][position_coords[1]+1] = ">"
            board[position_coords[0]][position_coords[1]] = "X"
            position_coords[1] += 1 
    elif char_at_position == "v":
        if south_char == "!":
            inside = False
            board[position_coords[0]][position_coords[1]] = "X" # mark path 
        elif south_char == "#":
            board[position_coords[0]][position_coords[1]] = "<"
        else:
            board[position_coords[0]+1][position_coords[1]] = "v"
            board[position_coords[0]][position_coords[1]] = "X"
            position_coords[0] += 1 
    elif char_at_position == "<":
        if west_char == "!":
            inside = False
            board[position_coords[0]][position_coords[1]] = "X" # mark path 
        elif west_char == "#":
            board[position_coords[0]][position_coords[1]] = "^"
        else:
            board[position_coords[0]][position_coords[1]-1] = "<"
            board[position_coords[0]][position_coords[1]] = "X"
            position_coords[1] -= 1 
    else:
        print("error, current position did not have a direction indicator")
        print(board)
        print(position_coords)
        inside = False
    


print(board)


## now count x's 

counter = 0
for row_index, row in enumerate(board):
    for col_index, cell in enumerate(row):
        if cell == "X":
            counter += 1

print(counter)
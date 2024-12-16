import copy

filetoopen = "input.txt"

file = open(filetoopen)
board = []
for line in file.readlines():
    row = list(line.strip())
    board.append(row)
file.close()

###########################
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
# make copy
originalboard = copy.deepcopy(board)
# now we can modify board without modifying originalboard


# one liner for below code
# starting_pos  = (row.index("^"), index) for index, row in enumerate(board) if "^" in row
for row_index, row in enumerate(board):
    if "^" in row:
        col_index = row.index("^")
        starting_pos = [row_index, col_index] ## slightly counterintuitive colindex is x (think about it) BUT THATS HOW IT WORKS IN FLIPPING board[y][x]


print(starting_pos)

## 2d arrays do not play nice with coordinates, dont think about it in that way
def containsLoop(board):
    visited_cells = []
    inside = True 

    counter = 0 
    # position_coords = starting_pos
    # position_coords = [7, 5]
    position_coords = [91, 92]
    revisitedcount = 0
    while inside:
        counter += 1
        if counter >= 10000:
            print("loop found")
            print(board)
            return True # loop found
        char_at_position = board[position_coords[0]][position_coords[1]]
        # print(position_coords)
        # print(char_at_position)

        north_char = board[position_coords[0]-1][position_coords[1]]
        east_char = board[position_coords[0]][position_coords[1]+1]
        south_char = board[position_coords[0]+1][position_coords[1]]
        west_char = board[position_coords[0]][position_coords[1]-1]

        if char_at_position == "^": ## moving north 
            # if north_char == "#": ## visited

            #     return True
            #     inside = False
            if north_char == "!": ## trying to move out of bounds 
                inside = False
                print("boarder reached at ", position_coords[0], position_coords[1])
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
                print("boarder reached")
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
                print("boarder reached")
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
                print("boarder reached")
                board[position_coords[0]][position_coords[1]] = "X" # mark path 
            elif west_char == "#":
                board[position_coords[0]][position_coords[1]] = "^"
            else:
                board[position_coords[0]][position_coords[1]-1] = "<"
                board[position_coords[0]][position_coords[1]] = "X"
                position_coords[1] -= 1 
        else:
            print("error, current position did not have a direction indicator")
            for row in board:
                print("".join(row))
            print(position_coords)
            inside = False
    
    return False 


print("initial run to get visited_cells")
containsLoop(board) ## need to run to once to get visited cells
for row in board:
    print("".join(row))
print()
visited_cells = []
for row_index, row in enumerate(board):
    for col_index, cell in enumerate(row):
        if cell == "X" or cell == "|":
            coord = [row_index, col_index]
            visited_cells.append(coord)



positionsthatmakeloop = 0 

# test = visited_cells[0]
# print(test)
# print(board[test[0]][test[1]])
# print(originalboard)
# tempboard[test[0]][test[1]] = "#"
# print("inserted block")
# print(tempboard)
# print("og")
# print(originalboard)
print(visited_cells)
print(visited_cells.index([1, 9]))
for coord in visited_cells:
    tempboard = copy.deepcopy(originalboard)
    if tempboard[coord[0]][coord[1]] != "^":
        tempboard[coord[0]][coord[1]] = "#"
        if containsLoop(tempboard):
            positionsthatmakeloop += 1



print(positionsthatmakeloop)

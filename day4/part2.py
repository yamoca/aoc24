# need a completely different approach 
# find all a's, look in a grid around them

data = []
with open("testinput.txt") as f:
    for line in f.readlines():
        data.append(line.strip())
    

sum = 0
"""
wont be any crosses on the outside e.g 
####
#  #
####
so can just start search in second row 2nd column
"""
for i in range(1, len(data)-1):
    for j in range(1, len(data[i])-1):
        if data[i][j] == "A":
            # could be center of a cross
            if data[i-1][j-1] == "M" and data[i+1][j+1] == "S":
                if data[i-1][j+1] == "M" and data[i+1][j-1] == "S":
                    # cross
                    sum += 1 
                elif data[i-1][j+1] == "S" and data[i+1][j-1] == "M":
                    # cross
                    sum += 1 
            elif data[i-1][j-1] == "S" and data[i+1][j+1] == "M":
                if data[i-1][j+1] == "M" and data[i+1][j-1] == "S":
                    # cross
                    sum += 1 
                elif data[i-1][j+1] == "S" and data[i+1][j-1] == "M":
                    # cross
                    sum += 1 


print(sum)
data = "70949 6183 4 3825336 613971 0 15 182"
data = [int(x) for x in data.split()]

def blink(data):
    nextline = []
    for i in range(len(data)):
        if data[i] == 0:
            nextline.append(1)
        elif len(str(data[i])) % 2 == 0:
            first_half = str(data[i])[:len(str(data[i]))//2] # floor division to remain as int e.g 4/2=2.0 
            second_half = str(data[i])[len(str(data[i]))//2:]
            nextline.append(int(first_half))
            nextline.append(int(second_half))
        else:
            nextline.append(data[i]*2024)
    
    return nextline
    

print("initial")
print(data)
desired_blinks = 25

for i in range(1, desired_blinks+1):# +1 because range is exclusive
    print(i, "blinks")
    data = blink(data) 
    # print(data)


print("# stones after", desired_blinks, "blinks")
print(len(data))
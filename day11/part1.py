data = "0 1 10 99 999"
data = [int(x) for x in data.split()]

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
    


print(nextline)
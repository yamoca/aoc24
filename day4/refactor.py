f = open("input.txt", "r")
a = []
w = ['']*8
total = 0

for i in f:
    a.append(i.strip())

s = 'Z' * (len(a[0])+6)
for i in range(len(a)):
    a[i] = 'ZZZ' + a[i] + 'ZZZ'
    
for i in range(3):
    a.insert(0, s)
    a.append(s)

for y in range(len(a)):
    for x in range(len(a[y])):
        if a[y][x] == 'X':
            w[0] = a[y][x:x+4]
            w[1] = a[y][x]+a[y+1][x+1]+a[y+2][x+2]+a[y+3][x+3]
            w[2] = a[y][x]+a[y+1][x]+a[y+2][x]+a[y+3][x]
            w[3] = a[y][x]+a[y+1][x-1]+a[y+2][x-2]+a[y+3][x-3]
            w[4] = a[y][x]+a[y][x-1]+a[y][x-2]+a[y][x-3]
            w[5] = a[y][x]+a[y-1][x-1]+a[y-2][x-2]+a[y-3][x-3]
            w[6] = a[y][x]+a[y-1][x]+a[y-2][x]+a[y-3][x]
            w[7] = a[y][x]+a[y-1][x+1]+a[y-2][x+2]+a[y-3][x+3]
            total += w.count('XMAS')    
            
print(total)


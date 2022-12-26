l = open("8.txt").read().split("\n")

def score(i, j):
    height = l[i][j]
    total = 1
    for d in [[1,0], [-1,0], [0,1], [0,-1]]:
        count = 1
        
        x, y = [d[0] * count + i, d[1] * count + j]
        while 0 <= x < len(l[0]) and 0 <= y < len(l):
            #print(x, y)
            if l[x][y] >= l[i][j] and (x != i or y != j):
                count += 1
                break
            
            count += 1
            x, y = [d[0] * count + i, d[1] * count + j]
        #print(count)
        total *= count - 1
    return total
ma = 0
for i in range(len(l)):
    for j in range(len(l[0])):
        if score(i, j) > ma:
            ma = score(i, j)
print(ma)

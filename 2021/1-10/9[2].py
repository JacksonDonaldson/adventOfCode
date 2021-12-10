f = open("9.txt").read().split("\n")
l = []
for r in f:
    l.append([int(i) for i in r])

def exists(r,c,l):
    return r >= 0 and r < len(l) and c >=0 and c < len(l[r])

difs = [[1,0],[-1,0],[0,1],[0,-1]]
total = 0

def fill(x,y,l):
    total = 0
    if exists(x,y,l) and l[x][y] != "X" and l[x][y] != 9:
        total += 1
        l[x][y] = "X"
        for d in difs:
            total += fill(x+d[0],y+d[1],l)
    return total

lens = []
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j] != "X" and l[i][j] != 9:
            lens.append(fill(i,j,l))
    
lens.sort()
lens.reverse()
print(lens[0]*lens[1]*lens[2])
#ans < 1568

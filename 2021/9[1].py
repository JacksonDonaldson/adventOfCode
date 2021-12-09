f = open("9.txt").read().split("\n")
l = []
for r in f:
    l.append([int(i) for i in r])

def exists(r,c,l):
    return r >= 0 and r < len(l) and c >=0 and c < len(l[r])

difs = [[1,0],[-1,0],[0,1],[0,-1]]
total = 0
for i in range(len(l)):
    for j in range(len(l[i])):
        for d in difs:
            x = i+d[0]
            y = j+d[1]
            if exists(x,y,l) and l[x][y] <= l[i][j]:
                break
        else:
            print(l[i][j])
            print(i)
            print(j)
            total += 1 + l[i][j]
print(total)
#ans < 1568

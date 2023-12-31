f = open("11.txt")


def exists(r,c,l):
    return r >= 0 and r < len(l) and c >=0 and c < len(l[r])

l = f.read().split("\n")
for i in range(len(l)):
    l[i] = [int(j) for j in l[i]]
    
def step(l):
    for i in range(len(l)):
        for j in range(len(l[i])):
            l[i][j] +=1

    directions = [[0,1],[0,-1],[1,1],[1,-1],[1,0],[-1,0],[-1,1],[-1,-1]]
    total = 0
    flashes = True
    while flashes:
        flashes = False
        for i in range(len(l)):
            for j in range(len(l[i])):
                if l[i][j] > 9:
                    flashes = True
                    total += 1
                    l[i][j] = 0
                    for d in directions:
                        x = i + d[0]
                        y = j + d[1]
                        if exists(x,y,l):
                            if l[x][y]!= 0:
                                l[x][y] += 1
    return total
def nogood(l):
    for i in l:
        for j in i:
            if j != 0:
                return True
    return False
i = 0
while nogood(l):
    step(l)
    i+=1
print(i)
#not 485

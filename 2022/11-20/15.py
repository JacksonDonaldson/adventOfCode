import jcksn as j
l = open("15.txt").read().split("\n")
total = 0

f = []
ypos = 2000000
remove =set()
for line in l:
    g = line.split(" ")
    sx = int(g[2][2:-1])
    sy = int(g[3][2:-1])

    bx = int(g[8][2:-1])
    by = int(g[9][2:])
    if by == ypos:
        remove.add(bx)
    
    distance = abs(sx-bx) + abs(sy-by)

    if ypos in range(sy-distance, sy+distance+1):
        i = ypos
        
        startX = sx - (distance - abs(i - sy))
        endX = sx+(distance - abs(i - sy))
        print(startX, endX)
        f.append((startX, endX))
print("done")
res = set()

for pair in f:
    for i in range(pair[0], pair[1] + 1):
        if i not in remove:
            res.add(i)
print(len(res))
    
#5878678

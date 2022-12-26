import jcksn as j
l = open("15.txt").read().split("\n")
total = 0

v = 4000000
f = dict()
for i in range(v + 1):
    f[i] = []


remove =set()
for line in l:
    print(line)
    g = line.split(" ")
    sx = int(g[2][2:-1])
    sy = int(g[3][2:-1])

    bx = int(g[8][2:-1])
    by = int(g[9][2:])
    
    distance = abs(sx-bx) + abs(sy-by)

    for i in range(max(0, sy-distance), min(v + 1, sy+distance+1)):
        
        
        startX = sx - (distance - abs(i - sy))
        endX = sx+(distance - abs(i - sy))

        
        f[i].append((min(v, max(0, startX)), max(0, min(v, endX))))
print("done")
res = set()

for y in range(v+ 1):
    if(y % 50000 == 0):
        print(y)
    l = f[y]
    l.sort(key = lambda x: x[1])
    
    for j in range(len(l)-1):
        for other in l[j+1:]:
            if other[0] <= l[j][1] + 1:
                break
        else:
            print(l[j][1] + 1, y)
            
    
    
#5878678

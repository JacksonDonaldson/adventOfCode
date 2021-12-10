from collections import Counter
f = open("5.txt")
r = f.read().split("\n")
b = []
for l in r:
    p0 = l[:l.index(" ")].split(",")
    p1 = l[l.index(">")+2:].split(",")
    b.append([p0,p1])

for l in range(len(b)):
    for j in range(len(b[l])):
        b[l][j] = [int(i) for i in b[l][j]]
def getPoints(line):
    p1 = line[0]
    p2 = line[1]
    if p1[0] - p2[0] == 0:
        return [[p1[0],i] for i in range(min(p1[1],p2[1]),max(p1[1],p2[1])+1)]
    elif p1[1] - p2[1] == 0:
        return [[i,p1[1]] for i in range(min(p1[0],p2[0]),max(p1[0],p2[0])+1)]
    l = []
    xSign = int(p2[0] > p1[0]) * 2 - 1
    ySign = int(p2[1] > p1[1]) * 2 - 1
    i=0
    x = p1[0]
    y=p1[1]
    while x != p2[0]:
        l.append([x,y])
        x+=xSign
        y+=ySign
    l.append([x,y])
        
    return l
points = []
for line in b:
    points.extend(getPoints(line))

c = Counter([str(p) for p in points])

total = 0
for v in c.most_common():
    if v[1] > 1:
        total +=1
print(total)

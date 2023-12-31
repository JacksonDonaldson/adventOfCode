import jScripts
f = open("22.txt")
l = f.read().split("\n")

l = jScripts.isplit(l, " x=,y.z")

active = []

def pointOverlap(rect, minPoint,maxPoint):
    minV = rect[0]
    maxV = rect[1]
    for p in [0,1,2]:
        #iffy
        if minV[p] > maxPoint[p] or maxV[p] < minPoint[p]:
            break
    else:
        return True
    return False

def overlap(minPoint, maxPoint):
    #a list of all active rects that overlap with given rect
    overlapPoint = []
    for a in active:
        if pointOverlap(a, minPoint, maxPoint):
            overlapPoint.append(a)
            
    return overlapPoint


def remove(removed, stay):
    final = []

    #deal with everything above & below the cube to be removed
    
    if stay[1][2] > removed[1][2]:
        
        topMaxZ = stay[1][2]
        topMinZ = removed[1][2]+1
        final.append([[stay[0][0],stay[0][1],topMinZ],[stay[1][0],stay[1][1],topMaxZ]])
        newMaxZ = topMinZ - 1
        #print(f"top: {final[-1]}")
    else:
        newMaxZ = stay[1][2]
        
    if stay[0][2] < removed[0][2]:
        topMaxZ = removed[0][2]-1
        topMinZ = stay[0][2]
        final.append([[stay[0][0],stay[0][1],topMinZ],[stay[1][0],stay[1][1],topMaxZ]])
        newMinZ = topMaxZ + 1
        #print(f"bot: {final[-1]}")
    else:
        newMinZ = stay[0][2]


    #left & right

    if stay[1][0] > removed[1][0]:
        #right
        rightMinX = removed[1][0]+1
        rightMaxX = stay[1][0]
        final.append([[rightMinX, stay[0][1], newMinZ],[rightMaxX,stay[1][1],newMaxZ]])
        #print(f"right: {final[-1]}")
        newMaxX = rightMinX - 1
    else:
        newMaxX = stay[1][0]
        
    if stay[0][0] < removed[0][0]:

        leftMaxX = removed[0][0]-1
        leftMinX = stay[0][0]
        final.append([[leftMinX, stay[0][1], newMinZ],[leftMaxX,stay[1][1],newMaxZ]])
        #print(f"left: {final[-1]}")
        newMinX = leftMaxX + 1
    else:
        newMinX = stay[0][0]


    #front & back

    if stay[1][1] > removed[1][1]:
        
        frontMaxY = stay[1][1]
        frontMinY = removed[1][1]+1
        final.append([[newMinX,frontMinY,newMinZ],[newMaxX,frontMaxY,newMaxZ]])
        #print(f"front: {final[-1]}")
    if stay[0][1] < removed[0][1]:
        frontMaxY = removed[0][1]-1
        frontMinY = stay[0][1]
        final.append([[newMinX,frontMinY,newMinZ],[newMaxX,frontMaxY,newMaxZ]])
        #print(f"back: {final[-1]}")
    return final

for line in l:
    mode = line[0]
    x = [int(line[1]),int(line[2])]
    y = [int(line[3]),int(line[4])]
    z = [int(line[5]),int(line[6])]

    minPoint = [min(x),min(y),min(z)]
    maxPoint = [max(x),max(y),max(z)]

    if overlap(minPoint,maxPoint):
        #print(overlap(minPoint,maxPoint))
        #reshape the rectangles
        rects = overlap(minPoint,maxPoint)
        #make a hole in all other points to open one for this point
        for rect in rects:
            #print(active)
            active.remove(rect)
            #print([minPoint,maxPoint])
            active.extend(remove([minPoint,maxPoint], rect))
            #print(active)
        if mode == "on":
            #keep this rect, and for each other point that this overlaps,
            #if it's not totally encompassed, reduce it so it doesn't double count
            active.append([minPoint,maxPoint])
            
            
    else:
        if mode == "on":
            active.append([minPoint,maxPoint])

def area(a):
    ma = a[1]
    mi = a[0]
    return (ma[0] - mi[0]+1) * ( ma[1] - mi[1]+1) * (ma[2]-mi[2]+1)

total = 0
for a in active:
    total += area(a)
print(total)


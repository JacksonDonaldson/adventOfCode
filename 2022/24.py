import jcksn as j
total = 0
l = open("24.txt").read().split("\n")

blizards = dict()
possiblePositions = set()
for r in range(1, len(l) - 1):
    for c in range(1, len(l[0]) - 1):
        if l[r][c] != ".":
            blizards[(r-1,c-1)] = l[r][c]
        


cSize = len(l[0]) - 2
rSize = len(l) - 2

m = 0

possiblePositions.add((-1,0))
trip = 1

while True:
    nextPos = set()
    for pos in possiblePositions:
        if trip == 1 and pos == (len(l)-3, len(l[0]) - 3):
            print("Win!")
            print(m)
            nextPos.clear()
            nextPos.add((len(l)-2, len(l[0]) - 3))
            
            trip = 2
            break
        if trip == 2 and pos == (0,0):
            print("win2")
            print(m)
            nextPos.clear()
            nextPos.add((-1,0))
            trip = 3
            break
        if trip == 3 and pos == (len(l)-3, len(l[0]) - 3):
            print("Win!")
            print(m)
            quit()
        for v in j.orthag(pos):
            #print(v)
            if v not in blizards and v[0] >= 0 and v[0] < rSize and v[1] >= 0 and v[1] < cSize:
                nextPos.add(v)
        if pos not in blizards:
            nextPos.add(pos)
    #print(blizards)
    newBliz = dict()
    for b in blizards:
        for h in blizards[b]:
            r, c = b
            if h == ">":
                d = [0,1]
            if h == "v":
                d = [1,0]
            if h == "<":
                d = [0,-1]
            if h == "^":
                d = [-1,0]
            if ((r + d[0]) %rSize, (c + d[1]) % cSize) not in newBliz:
                newBliz[((r + d[0]) %rSize, (c + d[1]) % cSize)] = []
            newBliz[((r + d[0]) %rSize, (c + d[1]) % cSize)].append(h)
    blizards = newBliz
    possiblePositions = nextPos
    m+=1
                
                
                
            
#not 251

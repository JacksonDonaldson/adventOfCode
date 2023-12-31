import numpy
#finally...

def getIn():
    t = input()
    ins = []
    while t != "done":
        ins.append(t)
        t = input()

    d = {}
    while len(ins) > 0:
        id = ins[0][5:9]
        board = []
        for i in range(1,11):
            board.append(list(ins[i]))
        ins = ins[12:]
        d[id] = board
        #print(board)
        
    return d    



def getEdges(board):
    #takes a 10x10 board and returns a list of outermost rows and collumns
    edges = [board[0].copy(), board[9].copy()]
    edges[0].reverse()
    foo = []
    foob = []
    for i in range(9, -1, -1):
        foo.append(board[i][0])
        foob.append(board[i][9])
    edges.append(foo.copy())
    edges.append(foob.copy())
    edges[2].reverse()
    #edges is in format [top, bottom, left, right]
    return edges
def findSimilar(d, row):
    #searches for items in d that have an outer row matching row
    matches = []
    for key in d.keys():
        thing = d[key]
        edges = getEdges(d[key])
        if row in edges:
            matches.append(key)
            continue
        r = row.copy()
        r.reverse()
        if r in edges:
            matches.append(key)
            continue
    return matches

def rotate(ar, count):
    test = numpy.array(ar)
    test = numpy.rot90(test, count)
    ar = test.tolist()
    return ar
    
            
def reorient(original, mover, direction):
##    print("matching " + mover + " to " + original)
    if direction == "R":
        oEdge = getEdges(d[original])[3].copy()
    elif direction == "D":
        oEdge = getEdges(d[original])[1].copy()
    oEdge.reverse()
    
##    print("edge of original: ")
##    print(oEdge)
##    
    try:
        flip = False
##        print(getEdges(d[mover]))
        mIndex = getEdges(d[mover]).index(oEdge)
    except:
        flip = True
        oEdge.reverse()
        mIndex = getEdges(d[mover]).index(oEdge)
##    print("Flipping at end: " + str(flip))
    if direction == "R":
        if mIndex == 0:
            rotation = 1
        elif mIndex == 1:
            rotation = 3
        elif mIndex == 2:
            rotation = 0
        elif mIndex == 3:
            rotation = 2
        d[mover] = rotate(d[mover], rotation)
        if flip:
            d[mover].reverse()
            
    if direction == "D":
        if mIndex == 0:
            rotation = 0
        elif mIndex == 1:
            rotation = 2
        elif mIndex == 2:
            rotation = 3
        elif mIndex == 3:
            rotation = 1
        d[mover] = rotate(d[mover], rotation)
        if flip:
            for r in range(0, len(d[mover])):
                d[mover][r].reverse()

    
        

d = getIn()


for key in d.keys():
    total = 0
    for edge in getEdges(d[key]):
        
        #print(findSimilar(d, edge))
        if len(findSimilar(d, edge)) == 1:
            total += 1
    if total == 2:
        #corner found
        corner = key
        break
p = [0] * 12
pic = []
for i in range(0,12):
    pic.append(p.copy())

pic[0][0] = corner
d[corner] = rotate(d[corner], 3)



for i in range(0,12):
    if i != 0:
        #set up next row
        bEdge = getEdges(d[pic[i-1][0]])[1]
##        print(i)
        
        nextPart = findSimilar(d, bEdge)
##        print(nextPart)
        nextPart.remove(pic[i-1][0])
        nextPart = nextPart[0]
        pic[i][0] = nextPart
        reorient(pic[i-1][0], nextPart, "D")
        
    for j in range(0,11):
##        print("j: " + str(j))
        
        rEdge = getEdges(d[pic[i][j]])[3]

##        print("matching edge: " + str(rEdge))
        nextPart = findSimilar(d, rEdge)
        print(nextPart)
        nextPart.remove(pic[i][j])
        nextPart = nextPart[0]
##        print("Edge found in " + str(nextPart))
        
        pic[i][j+1] = nextPart

##        print("which looks like: ")
##        for r in d[nextPart]:
##            print(r)
##        print()

##        print("running reorient")
        #edge found - now we have to reorient to match
        reorient(pic[i][j], nextPart, "R")
##        print('reorient ran. result: ')
##        for r in d[nextPart]:
##            print(r)
##        print()
##        print()
##        print()

#now, pic contains the ordered picture
#so convert it to the actual picture

final = []
for row in pic:
    if True:
        rows = [[],[],[],[],[],[],[],[],[],[]]
        for part in row:
            if part != 0:
                for i in range(1, 9):
                    rows[i].extend(d[part][i][1:-1])
        final.extend(rows[1:-1])

def checkFinal(final):
    for rot in [0,1,1,1]:
        
        final = rotate(final, rot)
        
##        for r in final:
##            for t in r:
##                print(t, end = "")
##            print()
        
        total = 0
        for r in range(0, len(final) - 3):
            for c in range(0, len(final) - 20):
                good = True
                for pair in [[0, 18],[1,0],[2,1],[2,4],[1,5],[1,6],[2,7],[2,10],[1,11],[1,12],[2,13],[2,16],[1,17],[1,18],[1,19]]:
                    if final[r + pair[0]][c + pair[1]] == ".":
                        good = False
                        break
                if good:
                    for pair in [[0, 18],[1,0],[2,1],[2,4],[1,5],[1,6],[2,7],[2,10],[1,11],[1,12],[2,13],[2,16],[1,17],[1,18],[1,19]]:
                        final[r + pair[0]][c + pair[1]] = "c"
                    total += 1
        print(total)
        if total > 0:
            roughness = 0
            for r in final:
                for c in r:
                    if c == "#":
                        roughness +=1
            print(roughness)

checkFinal(final)
final.reverse()          

checkFinal(final)

for r in range(0,len(final)):
    final[r].reverse()

checkFinal(final)

final.reverse()

checkFinal(final)

        
    
    



l = [[[['#', '#', '#', '#', '.', '#', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '#'], ['#', '.', '.', '#', '#', '#', '#', '#'], ['.', '.', '.', '.', '.', '#', '#', '.'], ['#', '#', '.', '.', '.', '#', '#', '#'], ['#', '.', '.', '#', '.', '#', '.', '#'], ['.', '#', '#', '.', '.', '.', '#', '.'], ['#', '.', '.', '.', '#', '#', '.', '.']]]]
#l= [[[[".","#","."],[".",".","#"],["#","#","#"]]]]
#hypercubes?
import copy
def exists(l, position):
    
    for p in position:
        if p < 0:
            return False
    w = position[0]
    z = position[1]
    y = position[2]
    x = position[3]
    if w >= len(l):
        return False
    if z >= len(l[0]):
        return False
    if y >= len(l[0][0]):
        return False
    if x >= len(l[0][0][0]):
        return False
    return True

def activeCount(l, position):
    #returns the number of active squares around the position
    total = 0
    w = position[0]
    z = position[1]
    y = position[2]
    x = position[3]
    for wAdj in [-1,0,1]:
        for zAdj in [-1,0,1]:
            for yAdj in [-1,0,1]:
                for xAdj in [-1,0,1]:
                    
                    if exists(l,[w+wAdj,z+zAdj,y+yAdj,x+xAdj]) and l[w+wAdj][z+zAdj][y+yAdj][x+xAdj] == "#":
                        total+=1
    if l[w][z][y][x] == "#":
        total -= 1
    return total
        
def applyRules(l):
    lCopy = copy.deepcopy(l)
    #print(l)
    #print(lCopy)

    #applies rules to a 3 dimensional list
    #precondition: list has space around it (edges are already filled in)
    for w in range(0,len(l)):
        for z in range(0,len(l[w])):
            for y in range(0,len(l[w][z])):
                for x in range(0,len(l[w][z][y])):
                    active = activeCount(l, [w,z,y,x])
                    if active == 3 or (l[w][z][y][x] == "#" and active == 2):
                        lCopy[w][z][y][x] = "#"
                    else:
                        lCopy[w][z][y][x] = "."
    return lCopy
                
def applySpacing(l):
    #given a 4 dimensional matrix, creates inactive squares surrounding it
    for cube in l:
        for sector in cube:
            for row in sector:
                row.insert(0,".")
                row.append(".")
            sector.insert(0,["."]*len(sector[0]))
            sector.append(["."]*len(sector[0]))
        blank = []
        bRow = ["."] * len(l[0][0][0])
        for i in range(0,len(l[0][0])):
            blank.append(bRow.copy())
        cube.append(copy.deepcopy(blank))
        cube.insert(0,copy.deepcopy(blank))
    #make a blank cube and insert at 0 and append
    #todo
    bRow = ["."] * len(l[0][0][0])
    bSector = []
    for i in range(0,len(l[0][0])):
        bSector.append(copy.deepcopy(bRow))
    bCube = []
    for i in range(0,len(l[0])):
        bCube.append(copy.deepcopy(bSector))
    l.append(copy.deepcopy(bCube))
    l.insert(0,copy.deepcopy(bCube))
    return l
for i in range(0,6):
    #print('spacing')
    #for i in l:
        #print(i)
    l = applySpacing(l)
    #for i in l:
    #    print(i)
    #print("spaced")
    l = applyRules(l)
total = 0
for cube in l:
    for sector in cube:
        for row in sector:
            for letter in row:
                if letter == "#":
                    total += 1
print(total)

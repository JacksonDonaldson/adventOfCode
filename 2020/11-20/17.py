l = [[['#', '#', '#', '#', '.', '#', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '#'], ['#', '.', '.', '#', '#', '#', '#', '#'], ['.', '.', '.', '.', '.', '#', '#', '.'], ['#', '#', '.', '.', '.', '#', '#', '#'], ['#', '.', '.', '#', '.', '#', '.', '#'], ['.', '#', '#', '.', '.', '.', '#', '.'], ['#', '.', '.', '.', '#', '#', '.', '.']]]
#l= [[[".","#","."],[".",".","#"],["#","#","#"]]]
import copy
def exists(l, position):
    
    for p in position:
        if p < 0:
            return False
    z = position[0]
    y = position[1]
    x = position[2]
    if z >= len(l):
        return False
    if y >= len(l[0]):
        return False
    if x >= len(l[0][0]):
        return False
    return True

def activeCount(l, position):
    #returns the number of active squares around the position
    total = 0
    z = position[0]
    y = position[1]
    x = position[2]
    for zAdj in [-1,0,1]:
        for yAdj in [-1,0,1]:
            for xAdj in [-1,0,1]:
                
                if exists(l,[z+zAdj,y+yAdj,x+xAdj]) and l[z+zAdj][y+yAdj][x+xAdj] == "#":
                    total+=1
    if l[z][y][x] == "#":
        total -= 1
    return total
        
def applyRules(l):
    lCopy = copy.deepcopy(l)
    #print(l)
    #print(lCopy)

    #applies rules to a 3 dimensional list
    #precondition: list has space around it (edges are already filled in)
    for z in range(0,len(l)):
        for y in range(0,len(l[z])):
            for x in range(0,len(l[z][y])):
                active = activeCount(l, [z,y,x])
                if active == 3 or (l[z][y][x] == "#" and active == 2):
                    lCopy[z][y][x] = "#"
                else:
                    lCopy[z][y][x] = "."
    return lCopy
                
def applySpacing(l):
    #given a 3 dimensional matrix, creates inactive squares surrounding it
    for sector in l:
        for row in sector:
            row.insert(0,".")
            row.append(".")
        sector.insert(0,["."]*len(sector[0]))
        sector.append(["."]*len(sector[0]))
    blank = []
    bRow = ["."] * len(l[0][0])
    for i in range(0,len(l[0])):
        blank.append(bRow.copy())
    l.append(copy.deepcopy(blank))
    l.insert(0,copy.deepcopy(blank))
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
for sector in l:
    for row in sector:
        for letter in row:
            if letter == "#":
                total += 1
print(total)

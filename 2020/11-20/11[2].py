ins = []
import copy
while True:
    j = input()
    if j == "-1":
        break
    ins.append(list(j))
def cast(pos, direction, l):
    pos[0] += direction[0]
    pos[1] += direction[1]
    while 0<=pos[0]<len(l) and 0<=pos[1] <len(l[1]) and l[pos[0]][pos[1]] == ".":
        pos[0] += direction[0]
        pos[1] += direction[1]
    
    if pos[0] <0 or pos[0] >= len(l) or pos[1]<0 or pos[1] >= len(l[1]):
        return False
    return l[pos[0]][pos[1]] == "#"

def applyRules(l):
    applied = copy.deepcopy(l)
    for row in range(0,len(l)):
        for seat in range(0,len(l[row])):
            adjOc = 0
            if seat != ".":
                pos = [row,seat]
                #print(pos)
                for i in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]:
                    if cast(pos.copy(),i,l):
                        #print(i)
                        adjOc+=1
                #print(adjOc)
##            print(str(row) + "," + str(seat))
##            print(adjOc)
            if l[row][seat] == "L" and adjOc == 0:
                applied[row][seat] = "#"
            elif l[row][seat] == "#" and adjOc >=5:
                applied[row][seat] = "L"

    return applied
ins = applyRules(ins)
for i in ins:
    print(i)

while True:
    ins = applyRules(ins);
occs = 0
for i in ins:
    for j in i:
        if j == "#":
            occs +=1
print(occs)

import copy
import j
f = open("15.txt")
l = f.read().split("\n")
for i in range(len(l)):
    l[i] = [int(j) for j in l[i]]

og = copy.deepcopy(l)

l = og
lists = []
for i in range(5):
    lists.append([0]*5)
    
for i in range(5):
    for j in range(5):
        newL = copy.deepcopy(og)
        for k in range(len(newL)):
            newL[k] = [(l+i+j) for l in newL[k]]
            for v in range(len(newL[k])):
                while newL[k][v] > 9:
                    newL[k][v] -=9
            
        lists[i][j] = copy.deepcopy(newL)
l=[]
for i in lists:
    toAdd = []
    for k in range(len(og)):
        toAdd.append([])
        
    for j in i:
        for r in j:
            toAdd[j.index(r)].extend(r)
    for add in toAdd:
        l.append(add)


li = [9999999] * len(l[0])

import j
storedMins = []
for i in range(len(l)):
    storedMins.append(li.copy())
storedMins[0][0] = 0
for i in range(100):
    sCopy = copy.deepcopy(storedMins)
    for r in range(len(l)):
        for c in range(len(l[r])):
            value = []
            for d in [[0,1],[1,0],[-1,0],[0,-1]]:
                x = r+d[0]
                y = c+d[1]
                if j.exists(x,y,l) and storedMins[x][y] + l[r][c] < storedMins[r][c]:
                    storedMins[r][c] = storedMins[x][y] +l[r][c]
    if sCopy == storedMins:
        break
    else:
        print(i)
#ans > 1760

print(storedMins[-1][-1])
#<404

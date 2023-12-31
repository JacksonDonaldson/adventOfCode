ins = []
import copy
while True:
    j = input()
    if j == "-1":
        break
    ins.append(list(j))

def applyRules(l):
    applied = copy.deepcopy(l)
    for row in range(0,len(l)):
        for seat in range(0,len(l[row])):
            adjOc = 0
            if seat != ".":
                for i in range(-1,2):
                    try:
                        if row-1>=0 and seat+i>=0 and l[row-1][seat + i] == "#":
                            adjOc+=1
                    except:
                        continue
                for i in [-1,1]:
                    try:
                        if seat+i>=0 and l[row][seat+i] == "#":
                            adjOc+=1
                    except:
                        continue
                for i in range(-1,2):
                    try:
                        if seat+i>=0 and l[row+1][seat+i] == "#":
                            adjOc += 1
                    except:
                        continue
                    
##            print(str(row) + "," + str(seat))
##            print(adjOc)
            if l[row][seat] == "L" and adjOc == 0:
                applied[row][seat] = "#"
            elif l[row][seat] == "#" and adjOc >=4:
                applied[row][seat] = "L"

    return applied
ins = applyRules(ins)
for i in ins:
    print(i)
while True:
    prev = copy.deepcopy(ins)
    ins = applyRules(ins);
    if ins == copy:
        break
occs = 0
for i in ins:
    for j in i:
        if j == "#":
            occs +=1
print(occs)

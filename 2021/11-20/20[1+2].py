import jScripts
import copy
f = open("20.txt")
l = f.read().split("\n")

en = l[0]
l = l[2:]

lenL = len(l[0])

for v in range(len(l)):
    l[v] = list(l[v])

##for v in l:
##    print(v)
##
##print("")

k=100
for i in range(k):
    l.insert(0,["."] * lenL)
    l.append(["."] * lenL)

##for v in l:
##    print(v)
##print("")

for i in range(len(l)):
    for j in range(k):
        l[i].insert(0,".")
        l[i].append(".")

def enhancePix(x,y,l, default):
    dirs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,0],[0,1],[1,-1],[1,0],[1,1]]
    s = ""
    for d in dirs:
        x1 = x + d[0]
        y1 = y + d[1]
       # print(f"{x1=}{y1=}")
        if not jScripts.exists(x1,y1,l):
            s += default
        elif l[x1][y1] == ".":
            s += "0"
        else:
            s+= "1"
    #print(s)
    return int(s,2)

def enhance(l,default):
    ret = copy.deepcopy(l)
    for i in range(len(ret)):
        for j in range(len(ret[i])):
            ret[i][j] = en[enhancePix(i,j,l,default)]
    return ret

##for v in l:
##    print(v)
##
##print("")
for i in range(25):
    l = enhance(l,"0")
    l = enhance(l,"1")
    print(i)

##for v in l:
##    print(v)

total = 0
for i in l:
    for j in i:
        if j == "#":
            total += 1
print(total)

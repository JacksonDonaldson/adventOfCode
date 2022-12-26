import jScripts
import copy
f = open("25.txt")
l = f.read().split("\n")
l = [list(i) for i in l]

def step(l):
    newL = []
    for i in range(len(l)):
        newL.append(["."] * len(l[0]))
    #print(newL)
    
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] == ">":
                if l[i][(j+1)%len(l[i])] == ".":
                    newL[i][(j+1)%len(l[i])] = ">"
                    #print("setting")
                    #print(i)
                    #print((j+1)%len(l[i]))
                else:
                    newL[i][j] = ">"
            elif l[i][j] == "v":
                newL[i][j] = "v"
            
    #print(newL)
    l = copy.deepcopy(newL)
    
    newL = []
    for i in range(len(l)):
        newL.append(["."] * len(l[0]))

    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] == "v":
                if l[(i+1)%len(l)][j] == ".":
                    newL[(i+1)%len(l)][j] = "v"
                    #print("assigned")
                else:
                    newL[i][j] = "v"
            elif l[i][j] == ">":
                newL[i][j] = l[i][j]
    return copy.deepcopy(newL)

i=0

while True:
    i+=1
    lastL = copy.deepcopy(l)
    l = step(l)
    if l == lastL:
        break
    if i % 100 == 0:
        print(i)

print("done:")
print(i)
                        
    

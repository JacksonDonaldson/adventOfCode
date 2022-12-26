l = open("7.txt").read()

l = l.split("\n")
total = 0
for s in l:
    if s[0] != "d" and s[0] != "$":
        total += int(s.split(" ")[0])
print(total)
root = ["", dict()]

currentDir = root

i = 0
while i < len(l):
    
    
    s = l[i]
    #print(s)
    #print(currentDir)
    if l[i][0] == "$":
        if l[i][2:4] == "cd":
            path = s[5:]
            if path == "..":
                currentDir = currentDir[0]
            elif path == "/":
                currentDir = root
            else:
                if path not in currentDir[1]:
                    currentDir[1][path] = dict()
                
                currentDir = [currentDir, currentDir[1][path]]
                
        elif s[2:4] == "ls":
            i+=1
            t = l[i]
            while t[0] != "$":
                if t[0] == "d":
                    pass
                else:
                    t = t.split(" ")
                    currentDir[1][t[1]] = int(t[0])
                i+=1
                if i == len(l):
                    break
                t = l[i]
            i-=1
    i+=1
def size(d):
    if type(d) == type(dict()):
        return sum([size(d[k]) for k in d.keys()])
    return int(d)

total = 0
minner = ""
minVal = 700000000

searched = 999999999999

def search(n):
    global minVal, minner
    total = 0
    #print(n)
    for key in n.keys():
        if type(n[key]) == type(dict()):
            if size(n[key]) > searched:
                if size(n[key]) < minVal:
                    minner = key
                    minVal = size(n[key])
                    print(minner)
                    print(size(n[key]))
                total += size(n[key])
                #print(n[key])
                
                #print("found!")
            total += search(n[key])
    return total

searched = 30000000 - (70000000 - size(root[1]))

print(search(root[1]))
                
                

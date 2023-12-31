l = open("12.txt").read().split("\n")
l = [list(f) for f in l]
startX = 0
startY = 0
x = 0
eX = 0
eY = 0

starts = []

for f in l:

    if "S" in f:
        startX = x
        startY = f.index("S")
    if "E" in f:
        eX = x
        eY = f.index("E")
    x+=1

for x in range(len(l)):
    for y in range(len(l[0])):
        if l[x][y] == "a":
            starts.append([x,y])

l[startX][startY] = "a"
starts.append([startX, startY])

l[eX][eY] = "z"

def search(x, y, depth):
    if depth > 485:
        yield 1
    #print(x, y)
    if l[x][y] == "´" or (l[x][y] == "a" and depth > 0):
        yield -2
    if x == eX and y == eY:
        yield 1

    
    news = []
    for d in [[1,0],[-1,0],[0,1],[0,-1]]:
        newX = x + d[0]
        newY = y + d[1]
        if newX >= 0 and newY >= 0 and newX < len(l) and newY <len(l[0]):
            if ord(l[newX][newY]) <= ord(l[x][y]) + 1:
                news.append([newX,newY])
    #print(x, y, news)
    l[x][y] = "´"
    yield -1
    #print("cont")
    calls = []
    for p in news:
        calls.append(search(p[0], p[1], depth + 1))
    #print(calls)
    while True:
        ind = 0
        for i in range(len(calls)):
            res = calls[i - ind].__next__()
            if res == -2:
                #print(calls#print(i)
                calls = calls[0:i - ind] + calls[i-ind + 1:]
                ind += 1
                #print(calls)
            elif res != -1:
                #print(x, y)
                yield res + 1
        if len(calls) == 0:
            #print(x, y)
            yield -2
        yield -1

import copy
minP= 9999
for s in starts:
    f = search(s[0], s[1], 0)
    p = 0
    storeL = copy.deepcopy(l)
    #print(l[0])
    while True:
        p = f.__next__()
        if p!= -1:
            #print(s[0], s[1])
            #print(p)
            break
    if p != -2 and p < minP:
        minP = p
        print(p)
    l = storeL
print(minP)
    
        

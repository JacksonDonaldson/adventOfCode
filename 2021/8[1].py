f = open("8.txt")
l = f.read().split("\n")
l = [i.split(" | ") for i in l]
for i in range(len(l)):
    l[i] = [k.split() for k in l[i]]

def findPossible(signal, digits):
    possible = []
    for value in digits:
        if signal in value:
            if len(value) == 2:
                possible.append([0,1])
            elif len(value) == 3:
                possible.append([0,1,5])
            elif len(value) == 4:
                possible.append([0,1,4,6])
            else:
                possible.append([0,1,2,3,4,5,6])


    appear = possible[0]
    for p in possible:
        toRemove = []
        for a in appear:
            if a not in p:
                toRemove.append(a)
        for r in toRemove:
            appear.remove(r)
    return appear

def findPairs(l):
    toRemove = []
    for v in l:
        if len(v) == 2 and v in l[l.index(v)+1:]:
            toRemove.append(v)
            
    for v in toRemove:
        for i in range(len(l)):
            if len(l[i]) > 2:
                if v[0] in l[i]:
                    l[i].remove(v[0])
                if v[1] in l[i]:
                    l[i].remove(v[1])
    return l

def findSingles(l):
    known = []
    for i in range(len(l)):
        if len(l[i]) == 1:
            known.append(l[i][0])
            #print(l[i])
    for k in known:
        #print(k)
        for i in range(len(l)):
            if len(l[i]) != 1:
                #print(l[i])
                if k in l[i]:
                    l[i].remove(k)
    return l

def decode(r):
    starts = r[0]
    ends = r[1]
    l = []
    for signal in "abcdefg":
        l.append(findPossible(signal, starts + ends))
        l=findPairs(l)
        l = findSingles(l)
        l = findPairs(l)
    return l    
total = 0
for r in l:
    decode(r)
print(total)

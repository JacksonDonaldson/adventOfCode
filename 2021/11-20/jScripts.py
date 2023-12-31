def exists(x,y,l):
    return x >= 0 and x < len(l) and y >=0 and y < len(l[x])

difs = [[0,1],[0,-1],[1,1],[1,-1],[1,0],[-1,0],[-1,1],[-1,-1]]
def adjacent(x,y,l):
    returns = []
    for d in difs:
        i = x + d[0]
        j = y + d[1]
        if exists(i,j,l):
            returns.append([i,j])
    return returns

def isplit(ins, delimiters):


    toReturn = []
    for line in ins:
        l = []
        value = ""
        for c in line:
            if c not in delimiters:
                value += c
            else:
                if value != "":
                    l.append(value)
                value = ""
        l.append(value)
        toReturn.append(l)
    return toReturn
            

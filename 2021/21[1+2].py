import jScripts
from functools import cache

p1 = 8
p2 = 6

n=0
n1 = 0
def getNum():
    global n, n1
    n1+=1
    n+=1
    if n == 101:
        n = 1
    
    return n


difs = []
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            difs.append(i+j+k)
@cache     
def getCount(p1Score,p1Loc, p2Score,p2Loc, move):
    p1total = 0
    p2total = 0
    for d in difs:
        if move == 1:
            pS = p1Loc + d
        else:
            pS = p2Loc + d
            
        while pS > 10:
            pS -= 10
        
        if move == 1:
            if p1Score + pS > 20:
                p1total += 1
            else:
                v = getCount(p1Score+pS,pS, p2Score,p2Loc, 2)
                p1total += v[0]
                p2total += v[1]
        else:
            #print("p2")
            if p2Score + pS > 20:
                p2total += 1
            else:
                v = getCount(p1Score,p1Loc, p2Score+pS,pS, 1)
                p1total += v[0]
                p2total += v[1]
                
    return [p1total, p2total]

print(getCount(0,p1, 0, p2, 1))

import j
from functools import cache
target = [32,65,-255,-177]

maxY = -99999
x = 0
y = -999

def collides(x,y):
    p = [0,0]
    while p[0] < 66 and p[1] > -300:
        #print(p)
        p[0] += x
        p[1] += y
        y-=1
        if x != 0:
            x = x/abs(x) * abs(x) - 1
        if p[0] >= 32 and p[0] <= 65 and p[1] >= -225 and p[1] <= -177:
        #if p[0] >= 20 and p[0] <= 30 and p[1] >= -10 and p[1] <= -5:

            return True
    return False

@cache
def maxVal(y):
    t = 0
    while y > 0:
        t += y
        y -=1
        
    return t
total = 0
while True:
    y+=1
    x = 0
    #print(f"{x=} {y=}")
    while x < 66:
        if collides(x,y):
            total += 1
            print(f"{x=} {y=}")
        x+=1

    if y > 900:
        break
print(total)





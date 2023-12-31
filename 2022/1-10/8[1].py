l = open("8.txt").read().split("\n")
l = [list(s) for s in l]
total = 0

def do(l):
    global total
    for s in l:
        if s[0][0] == "a":
            curMax = int(s[0][1]) - 1
        else:
            curMax = int(s[0]) - 1
        i = 0
        while i < len(s):
            c = s[i]
            if c[0] == "a":
                i+=1
                curMax = max(curMax, int(c[1]))
                continue
            if int(c) > curMax:
                curMax = int(c)
                s[i] = "a" + s[i]
                total += 1
            i+=1
    return l

do(l)
print(l)
l = [s[::-1] for s in l]
do(l)
print(l)
import numpy as np
l = np.array(l).T.tolist()

do(l)
print(l)
l = [s[::-1] for s in l]
do(l)
print(l)

total = 0
for s in l:
    for c in s:
        if c[0] == "a":
            total += 1
        



    

print(total)

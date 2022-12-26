import jcksn as j
import cProfile
l = open("18.txt").read().split("\n")

f = set()
from collections import Counter
for line in l:
    f.add(tuple([int(j) for j in line.split(",")]))




    


    #maxVal = max([b[0] + b[1] + b[2] for b in f])
def orthag(x):
    return ((x[0] + 1, x[1], x[2]),(x[0]- 1, x[1], x[2]),(x[0], x[1]+ 1, x[2]),(x[0], x[1]- 1, x[2]),(x[0], x[1], x[2]+ 1),(x[0], x[1], x[2]- 1))

def main(c):
    extern = set()
    add = [(0,0,0)]
    print(len(add))
    for i in range(c):
        #print(i, len(add))
        #print(extern)
        #print(add)

        for a in add:
            extern.add(a)
        oldAdd = add
        add = set()
        for x in oldAdd:
            #print("starting test of ", e)
            good = False
            for a in ((x[0] + 1, x[1], x[2]),(x[0]- 1, x[1], x[2]),(x[0], x[1]+ 1, x[2]),(x[0], x[1]- 1, x[2]),(x[0], x[1], x[2]+ 1),(x[0], x[1], x[2]- 1)):
                if a not in f:
                    if a not in extern and a[0] >= -1 and a[1] >=-1 and a[2] >= -1:
                        add.add(a)


    i = 0         
    total = 0
    for p in f:
        i += 1
        if i % 100 == 0:
            print(i)
        for a in orthag(p):
            if a not in f and a in extern:
                total +=1

    print("ANSWER: ", total)
# 2019 < ans < 3322
# not 2058

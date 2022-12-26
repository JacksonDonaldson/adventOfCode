import jcksn as j
l = open("18.txt").read().split("\n")

f = set()
for line in l:
    f.add(tuple([int(j) for j in line.split(",")]))
total = len(l) * 6
for p in f:
    for a in j.orthag(p):
        if a in f:
            total -=1
print(total)

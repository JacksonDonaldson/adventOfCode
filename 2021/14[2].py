import j
from collections import Counter
f = open("14.txt")
l = f.read().split("\n")
start = l[0]
rules = l[2:]
rules = j.isplit(rules, " -> ")

d = {}
for r in rules:
    d[r[0]] = r[1]

def step(d, c):
    end = ""
    c2 = Counter()
    for key in c:
        v1 = key[0] + d[key]
        v2 = d[key] + key[1]
        c2[v1] += c[key]
        c2[v2] += c[key]
    return c2


    end += string[-1]
    return end

c = Counter()
for i in range(len(start)-1):
    value = start[i:i+2]
    c[value]+=1
    
for i in range(40):
    c = step(d,c)
    print(len(start))
    print(i)

#ans > 1476985801107
count = Counter()
for key in c:
    count[key[0]] += c[key]
    #count[key[1]] += c[key]
c = count
print(c.most_common()[0][1] - c.most_common()[-1][1] + 1)

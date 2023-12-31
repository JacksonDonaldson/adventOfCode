import j

f = open("14.txt")
l = f.read().split("\n")
start = l[0]
rules = l[2:]
rules = j.isplit(rules, " -> ")

d = {}
for r in rules:
    d[r[0]] = r[1]

def step(d, string):
    end = ""
    for i in range(len(string)-1):
        key = string[i:i+2]
        if key in d.keys():
            end += string[i] + d[key]
        else:
            end += string[i]


    end += string[-1]
    return end

for i in range(10):
    start = step(d,start)
    print(i)
from collections import Counter

c = Counter(start)
print(c.most_common()[0][1] - c.most_common()[-1][1])

import j
l = j.isplit(open("12.txt").read().split("\n"),"-")
d = {}
for v in l:
    value = d.get(v[0],[])
    value.append(v[1])
    d[v[0]] = value
    value = d.get(v[1],[])
    value.append(v[0])
    d[v[1]] = value

def findWays(value,taken):
    toGo = d[value]
    total = 0

    for go in toGo:
        if go == "end":
            total += 1
        elif go not in taken:

            if value.islower():
                
                cont = taken.copy()
                cont.append(value)
                total += findWays(go, cont)
            else:

                total += findWays(go,taken)
    return total

print(findWays("start",[]))
#< 9390

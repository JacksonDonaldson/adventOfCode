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

def findWays(value,taken, takeTwice):
    toGo = d[value]
    total = 0

    for go in toGo:
        if go == "end":
            total += 1
        elif go not in taken or (go == takeTwice and go not in taken[taken.index(go)+1:]):

            if value.islower():
                
                cont = taken.copy()
                cont.append(value)
                total += findWays(go, cont,takeTwice)
            else:

                total += findWays(go,taken,takeTwice)
    return total


general = findWays("start",[],"")
total = general
for key in d:
    if key.islower() and key != "start" and key != "end":
        total += findWays("start",[],key) - general
        
print(total)
#< 9390

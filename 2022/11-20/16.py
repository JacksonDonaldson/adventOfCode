import jcksn as j
l = open("16.txt").read().split("\n")
total = 0

valves = dict()

for line in l:
    f = line.split(" ")
    name = f[1]
    rate = f[4][5:-1]
    lead = f[9:]
    for i in range(len(lead) - 1):
        lead[i] = lead[i][:-1]

    valves[name] = [rate, lead]
import copy
nonzero = []
for v in valves:
    if valves[v][0] != "0":
        nonzero.append(v)
print(nonzero)

def distance(location,time, end):
    if location == end:
        return 0
    if time == 0:
        return -1
    minDist = -1
    for connection in valves[location][1]:
        o = distance(connection, time-1, end)
        if minDist == -1 or (o!= -1 and o < minDist):
            minDist = o
    if minDist == -1:
        return -1
    return minDist + 1

links = []
for location in nonzero:
    dists = []
    for other in nonzero:
        if other == location:
            continue
        time = 5
        o = distance(location, time, other)
        while o == -1:
            time += 2
            o = distance(location, time, other)
        dists.append((other, o))
    links.append(dists)
print(links)
starts = []
for loc in nonzero:
    time=5
    o = distance("AA", time, loc)
    while o == -1:
        time += 2
        o = distance("AA", time, loc)
    starts.append((loc, o))
print(starts)
vals = dict()
vals["AA"] = starts
for i in range(len(links)):
    vals[nonzero[i]] = links[i]

from functools import cache

@cache
def search(time1, v1, time2, v2, replaced):
    ##print(dt)

    connec1 = vals[v1]
    rate1 = int(valves[v1][0])

    connec2 = vals[v2]
    rate2 = int(valves[v2][0])

    if v1 == v2:
        rate2 = 0
    
    maxT = 0

    if time1 > 0:
        if rate1 != 0:
            valves[v1][0] = 0
            r = set(replaced)
            r.add(v1)
            r = frozenset(r)
            for con in connec1:

                location, t = con
                o = rate1 * max(time1-1, (time1 - 1 - t))
                o += search(time1 - 1 - t, location, time2, v2, r)
                if o > maxT:
                    maxT = o
            valves[v1][0] = rate1
            
    if time2 > 0:
        if rate2 != 0:
            valves[v2][0] = 0
            r = set(replaced)
            r.add(v1)
            r = frozenset(r)
            for con in connec2:
                location, t = con
                o = rate2 * max(time2 - 1, time2 - 1 - t)
                o += search(time1, v1, time2 -1 - t, location, r)
                if o > maxT:
                    maxT = o
            valves[v2][0] = rate2
    return maxT
                
    #close 1
    
ma = 0
for i in range(9, len(starts)):
    for j in range(i+1, len(starts)):
        location1, time1 = starts[i]
        location2, time2 = starts[j]
        print(location1, location2)
        print(search(26 - time1, location1, 26 - time2, location2, frozenset()))
        


# 2709 < x < 2911
#2752

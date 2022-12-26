l = open("19.txt").read().split("\n")

blues = []
for line in l:
    line = line.split(" ")
    blue = [line[6], line[12], line[18], line[21], line[27], line[30]]
    blues.append([int(b) for b in blue])

from functools import cache
@cache
def getBestGeodes(time, oreps, clayps, obsidps, gps, ore, clay, obsid, geodes):
    if oreps > maxOps:
        return 0
    if clayps > maxCps:
        return 0
    if obsidps > maxObps:
        return 0
    if time == 1:
        #if geodes > 6:
            
            #print(geodes, gps)
        return geodes + gps
    #print(time, oreps, clayps, obsidps, gps, ore, clay, obsid, geodes)
    if time > 26:
        #quit()
        print(time)
    ore += oreps
    clay += clayps
    obsid += obsidps
    geodes += gps

    t = time - 1
    oreCost, clayCost, obsidOreCost, obsidClayCost, geodeOreCost, geodeObsCost = costs
    maxGeodes = 0
    if ore - oreps >= geodeOreCost and obsid - obsidps >= geodeObsCost:
        return getBestGeodes(t, oreps, clayps, obsidps, gps + 1, ore - geodeOreCost, clay, obsid - geodeObsCost, geodes)
            
           
    if ore - oreps >= oreCost:
        o = getBestGeodes(t, oreps + 1, clayps, obsidps, gps, ore - oreCost, clay, obsid, geodes)
        if o > maxGeodes:
            maxGeodes = o

    if ore - oreps >= clayCost:
        o = getBestGeodes(t, oreps, clayps + 1, obsidps, gps, ore - clayCost, clay, obsid, geodes)
        if o > maxGeodes:
            maxGeodes = o

    if ore - oreps >= obsidOreCost and clay - clayps >= obsidClayCost:
        #print(time, ore, oreps, clay, clayps)
        o = getBestGeodes(t, oreps, clayps, obsidps + 1, gps, ore - obsidOreCost, clay - obsidClayCost, obsid, geodes)
        if o > maxGeodes:
            maxGeodes = o

    o= getBestGeodes(t, oreps, clayps, obsidps, gps, ore, clay, obsid, geodes)
    if o > maxGeodes:
        maxGeodes = o
    return maxGeodes


total =0
i = 1
for blue in blues:
    costs = blue
    maxOps = max([blue[0], blue[1], blue[2], blue[4]])
    maxCps = blue[3] // 2 + 1
    maxObps = blue[-1]
    
    res = getBestGeodes(32, 1, 0, 0, 0, 0, 0, 0, 0)
    getBestGeodes.cache_clear()
    total += res * i
    print(i, res)
    i+=1
print(total)
#ans > 6080

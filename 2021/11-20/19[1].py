import jScripts
f = open("19.txt")
l = f.read().split("\n")
scanners = []
scanner = []
for line in l:
    if line == "":
        continue
    if line[1] == "-":
        scanners.append(scanner)
        scanner = []
    else:
        scanner.append([int(j) for j in line.split(",")])
scanners.append(scanner)
scanners = scanners[1:]


forwardPol = [-1,1]

final = []
forwards = [1,2,3]


for pol in forwardPol:
    for forward in forwards:
        other = forwards.copy()
        other.remove(forward)
        if pol > 0:
            possibles = [[other[0],other[1]],[-other[0],other[1]],[-other[1],other[0]],[other[1],-other[0]]]
        else:
            possibles = [[-other[0],other[1]],[other[0],-other[1]],[other[1],other[0]],[-other[1],-other[0]]]
            
        final.extend([[p[0],forward * pol, p[1]] for p in possibles])
def sign(n):
    if n == 0:
        return 0
    return int(n / abs(n))
import copy
final = [[1,2,3],[-1,2,-3],[-3,2,1],[3,2,-1],[-1,-2,3],[1,-2,-3],[-3,-2,-1],[3,-2,1]]
zFinal = copy.deepcopy(final)
yFinal= copy.deepcopy(final)
for z in zFinal:
    if z[0] == 3 or z[0] == -3:
        swap = z[0]
        z[0] = abs(z[1]) * sign(z[0])
        z[1] = abs(swap) * sign(z[1])
    else:
        swap = z[2]
        z[2] = abs(z[1]) * sign(z[2])
        z[1] = abs(swap) * sign(z[1])
    if -2 in z:
        z[z.index(-2)] = 2
    else:
        z[z.index(2)] = -2
    final.append(z)


for y in yFinal:
    if y[0] == 1 or y[0] == -1:
        swap = y[0]
        y[0] = abs(y[1]) * sign(y[0])
        y[1] = abs(swap) * sign(y[1])
    else:
        swap = y[2]
        y[2] = abs(y[1]) * sign(y[2])
        y[1] = abs(swap) * sign(y[1])
    if -2 in y:
        y[y.index(-2)] = 2
    else:
        y[y.index(2)] = -2
    final.append(y)

print(final)

def findSimilar(scanner1P, scanner2P, scanner1, scanner2):
    #determine scanner 2's offset based on ps, then return other # of similar
    #could be in any of the 24 directions (final)
    
##    for v in [0,1,2]:
##        if abs(scanner1P[v] - scanner2P[v]) > 2000:
##            #print("skipping")
##            return False
    maxTotal = 0
    find = False
    for offset in final:
        x = abs(offset[0])-1
        y = abs(offset[1])-1
        z = abs(offset[2])-1
        xS = sign(offset[0])
        yS = sign(offset[1])
        zS = sign(offset[2])

        #print(f"{x=}{y=}{z=}")
        scanner2Pos = [scanner1P[0] - xS * scanner2P[x], scanner1P[1] - yS * scanner2P[y], scanner1P[2] - zS * scanner2P[z]]
        
        total = 0

        adjustedLocs = []
        for value in scanner2:
            
            adjustedPos = [scanner2Pos[0] + value[x] * xS, scanner2Pos[1] + value[y] * yS, scanner2Pos[2]+ value[z] * zS]
            adjustedLocs.append(adjustedPos)
            if adjustedPos in scanner1:
                #print(adjustedPos)
                #print(adjustedPos)
                
                total += 1
        if total >= 12:
##            if find:
##                print("found!")
##            find = True
##            continue
            print(f"{adjustedLocs=}")
            print(f"{x=}{xS=}{y=}{yS=}{z=}{zS=}")
            print(f"{scanner2Pos=}")
            print()
            return [scanner2Pos,adjustedLocs]
    return False

def checkOverlap(scanner1, scanner2):
    maxT = 0
    for v in scanner1:
        for v2 in scanner2:
            t = findSimilar(v,v2,scanner1,scanner2)
            if t:
                print(v)
                print(v2)
                return t
    return False

beaconLocations = set([tuple(s) for s in scanners[0]])


#for every overlap,
realPositions = ["?"] * len(scanners)
realPositions[0] = [0,0,0]

tryLater = []
#quit()
#print(f"{scanners[1]=}")
while "?" in realPositions:
    for scanner1 in range(0,len(scanners)):
        for scanner2 in range(0, len(scanners)):
            if scanner1 == scanner2 or realPositions[scanner2] != "?" or realPositions[scanner1] == "?":
                continue
            else:
                print(scanner1)
                print(scanner2)
            c = checkOverlap(scanners[scanner1],scanners[scanner2])
            if c:
                print(f"{scanner1=} {scanner2=}")
                s1Pos = realPositions[scanner1]
                try:
                    
                    realPositions[scanner2] = c[0]#[s1Pos[0] + c[0][0], s1Pos[1] + c[0][1], s1Pos[2] + c[0][2]]
                    print(f"{realPositions=}")
                    scanner2Pos = realPositions[scanner2]

                    scanners[scanner2] = c[1]
                    for v in c[1]:
                        beaconLocations.add(tuple(v))
                    #adjust values
    ##                newValues = []
    ##                for value in c[1]:
    ##                    print(f"{value=}")
    ##                    #print(f"{s1Pos=}")
    ##                    #print(f"{[s1Pos[0] + value[0], s1Pos[1] + value[1], s1Pos[2] + value[2]]=}")
    ##                    v = [s1Pos[0] + value[0], s1Pos[1] + value[1], s1Pos[2] + value[2]]
    ##                    newValues.append(v)
    ##                    print(f"{newValues[-1]=}")
    ##                    beaconLocations.add(tuple(newValues[-1]))
    ##                scanners[scanner2] = newValues.copy()

                except:
                    print("error")
                    tryLater.append([scanner1,scanner2])
print(len(beaconLocations))

#ans < 438





                

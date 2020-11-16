import math

field = []

while True:
    x = input()
    if x == "-1":
        break
    field.append(list(x))


def div(x,y):
    if x == 0:
        if y == 0:
            return 999
        return 1000000
    else:
        return y/x

maxVis = 0
visLoc = []
belt = 13
ast = 11
if field[belt][ast] == "#":
    #found an asteroid. now find number of asteroids visable from it
    aboveTans = []
    belowTans = []
    visible = 0
    posHorizontal = True
    negHorizontal = True
    for relativeBelt in range(0, len(field)):
        for relativeAst in range(0, len(field[belt])):
            if field[relativeBelt][relativeAst] == "#":
                #an asteroid. if it's above, check aboveList
                #if below, check belowlist
                #if tan is in there, it's hidden, if it's not, it's visible
                #(add to list)
                x = relativeAst - ast
                y = relativeBelt - belt
                if y > 0:
                    if div(x,y) not in aboveTans:
                        aboveTans.append(div(x,y))
                        visible +=1
                elif y < 0:
                    if div(x,y) not in belowTans:
                        belowTans.append(div(x,y))
                        visible +=1
                else:
                    #y == 0, so we're doing horizontals, handled seperately
                    if x>0 and posHorizontal:
                        #print("positive horizontal")
                        posHorizontal = False
                        visible +=1
                    elif x<0 and negHorizontal:
                        #print("negative horizontal")
                        negHorizontal = False
                        visible +=1
aboveTans.sort()
belowTans.sort()
belowTans.reverse()
dest = 0
for i in range(0,len(aboveTans)):
    if aboveTans[i]> 0:
        dest +=1
        aboveTans[i] = -999999999
print(dest)
dest += len(belowTans)
dest +=2 #account for horizontals
aboveTans.sort()
aboveTans.reverse()
i = 200 - dest -1
print(aboveTans[i])

    

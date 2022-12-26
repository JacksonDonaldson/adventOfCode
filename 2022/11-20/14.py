import jcksn as j
l = open("14.txt").read().split("\n")


taken = dict()
maxY = 0
for line in l:
    lines = line.split(" -> ")
    #print(lines)
    for i in range(1, len(lines)):
        path = [lines[i-1].split(","), lines[i].split(",")]

        start = path[0]
        end = path[1]

        stX = min(int(path[0][0]), int(path[1][0]))
        eX = max(int(path[0][0]), int(path[1][0]))
        stY = min(int(path[0][1]), int(path[1][1]))
        eY = max(int(path[0][1]), int(path[1][1]))

        for x in range(stX, eX + 1):
            for y in range(stY, eY + 1):
                if y > maxY:
                    maxY = y
                taken[(x,y)] = "X"

for i in range(-9999, 9999):
    taken[(i, maxY+2)] = "X"

def runSand():
    s = [500, 0]
    while True:
        
        if (s[0], s[1] + 1) not in taken:
            s = [s[0], s[1] + 1]
        elif (s[0] -1, s[1] + 1) not in taken:
            s = [s[0] -1, s[1] + 1]
        elif (s[0] +1, s[1] + 1) not in taken:
            s = [s[0] +1, s[1] + 1]
        else:
            taken[tuple(s)] = "S"
            #print(s)
            return s != [500, 0]
        

i = 0
while runSand():
    i+=1
print(i)

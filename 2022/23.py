import jcksn as j
l = open("23.txt").read().split("\n")
elves = set()
for r in range(len(l)):
    for c in range(len(l[r])):
        if l[r][c] == "#":
            elves.add((r,c))

proposals = [
    [lambda x: (x[0] -1, x[1]) not in elves and (x[0] -1, x[1] + 1) not in elves and (x[0] - 1, x[1] - 1) not in elves,
     lambda x: (x[0] -1, x[1])],
    [lambda x: (x[0] +1, x[1]) not in elves and (x[0] +1, x[1] + 1) not in elves and (x[0] + 1, x[1] - 1) not in elves,
     lambda x: (x[0] + 1, x[1])],
    [lambda x: (x[0] +1, x[1]-1) not in elves and (x[0], x[1] - 1) not in elves and (x[0] - 1, x[1] - 1) not in elves,
     lambda x: (x[0], x[1] - 1)],
    [lambda x: (x[0] +1, x[1]+1) not in elves and (x[0], x[1] + 1) not in elves and (x[0] - 1, x[1] + 1) not in elves,
     lambda x: (x[0], x[1] + 1)]]

def p(e):
    for i in range(14):
        for j in range(14):
            if (i,j) in e:
                print("#", end = "")
            else:
                print(".", end = "")
        print()
print(len(elves))
r = 0
cont = True

while cont:
    cont = False
    r += 1
    proposed = dict()
    nextElves = set()
    #p(elves)
    #print()
    for elf in elves:
        for loc in j.adjacent(elf):
            if loc in elves:
                break
        else:
            nextElves.add(elf)
            continue

        for prop in proposals:
            #print(elf)
            if prop[0](elf):
                newLocation = prop[1](elf)
                if newLocation not in proposed:
                    proposed[newLocation] = []
                proposed[newLocation].append(elf)
                break
        else:
            nextElves.add(elf)
            continue

    for k in proposed.keys():
        elves = proposed[k]
        if len(elves) == 1:
            cont = True
            nextElves.add(k)
        else:
            for e in elves:
                nextElves.add(e)
    proposals = proposals[1:] + proposals[:1]
    elves = nextElves
print(r)

rows = [l[0] for l in elves]
cols = [l[1] for l in elves]

        
    

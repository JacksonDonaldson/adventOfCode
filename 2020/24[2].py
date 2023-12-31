def getIn():
    i = input()
    ins = []
    while i != "done":
        ins.append(delim(i))
        i = input()
    return ins

def delim(moves):
    deliminated = []
    while len(moves) > 0:
        if moves[0] == "e" or moves[0] == "w":
            deliminated.append(moves[0])
            moves = moves[1:]
            continue
        deliminated.append(moves[0:2])
        moves = moves[2:]
    return deliminated

def makeMove(move):
    global locations
    row = 0
    col = 0
    for m in move:
        if m == "w":
            col -=2
        elif m == "e":
            col +=2
        elif m == "nw":
            col -=1
            row +=1
        elif m == "ne":
            col +=1
            row +=1
        elif m == "sw":
            col -=1
            row -=1
        elif m == "se":
            col +=1
            row -=1
        else:
            print("m not found: " + str(m))
    #print(move)
    
    key = (row, col)
    #print(key)
    if key not in locations.keys():
        locations[key] = True
    else:
        locations[key] = not locations[key]
        
moves = getIn()
locations = {}
for move in moves:
    makeMove(move)

total = 0
for key in locations.keys():
    if locations[key]:
        total +=1
print(total)

def adjacents(key):
    r = key[0]
    c = key[1]
    return [(r,c-2),(r,c+2),(r+1,c+1),(r+1,c-1),(r-1,c+1),(r-1,c-1)]

def adjacentCount(key):
    close = 0
    #print(locations)
    #print(key)
    #print(adjacents(key))
    
    for adj in adjacents(key):
        try:
            if locations[adj]:
                close += 1
        except:
            pass
    #print(close)
    return close

def test(key):
    if key in locations.keys() and locations[key]:
        if 1 <= adjacentCount(key) <=2:
            return True
    return adjacentCount(key) == 2


def life(locations):
    adjusted = {}
    for key in locations.keys():
        if test(key):
            adjusted[key] = True
        for adjacent in adjacents(key):
            if test(adjacent):
                adjusted[adjacent] = True
    return adjusted

for i in range(0, 100):
    locations = life(locations)
    total = 0
    for key in locations.keys():
        if locations[key]:
            total +=1
    print(total)
    
#ans>408
#ans == 434

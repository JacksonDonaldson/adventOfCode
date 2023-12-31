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
    
    key = str(row) + " " + str(col)
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
#ans>408
#ans == 434

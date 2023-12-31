ins = []
while True:
    j = input()
    if j == "-1":
        break
    ins.append(j)
facing = 1;
loc = [0,0]
wayLoc = [10,1]
for move in ins:
    direction = move[0]
    amount = int(move[1:])
    if direction == "N":
        wayLoc[1]+=amount
    elif direction == "E":
        wayLoc[0] += amount
    elif direction == "S":
        wayLoc[1] -= amount
    elif direction == "W":
        wayLoc[0] -= amount
    elif direction == "R":
        for i in range(0,int(amount/90)):
            wayLoc = [wayLoc[1], -wayLoc[0]];
    elif direction == "L":
        for i in range(0, int(amount/90)):
            wayLoc = [-wayLoc[1], wayLoc[0]]
    elif direction == "F":
        for i in range(0,amount):
            loc[0]+=wayLoc[0]
            loc[1] += wayLoc[1]
            
    else:
        print("direction error")
print(str(abs(loc[0]) + abs(loc[1])))
    

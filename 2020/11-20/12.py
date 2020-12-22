ins = []
while True:
    j = input()
    if j == "-1":
        break
    ins.append(j)
facing = 1;
loc = [0,0]
for move in ins:
    direction = move[0]
    amount = int(move[1:])
    if direction == "N":
        loc[1]+=amount
    elif direction == "E":
        loc[0] += amount
    elif direction == "S":
        loc[1] -= amount
    elif direction == "W":
        loc[0] -= amount
    elif direction == "R":
        facing = (facing + amount/90)%4;
    elif direction == "L":
        facing = (facing-amount/90)%4
    elif direction == "F":
        if facing == 0:
            loc[1] += amount
        elif facing == 1:
            loc[0] += amount
        elif facing == 2:
            loc[1] -= amount;
        elif facing == 3:
            loc[0] -= amount;
        else:
            print("facing error")
    else:
        print("direction error")
print(str(abs(loc[0]) + abs(loc[1])))
    

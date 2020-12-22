field = []
while True:
    i = input();
    if i == "-1":
        break
    field.append(i)
x = 0
total = 1;
for down in [1,3,5,7]:
    x = 0
    trees = 0
    for i in range(0,len(field)):
        if field[i][x] == "#":
            trees+=1
        x = (x+down) % len(field[0])
    print(trees)
    total *= trees
down = 1
x = 0
trees = 0
i=0
while True:
    try:
        
        if field[i][x] == "#":
            trees+=1
    except:
        break
    x = (x+down) % len(field[0])
    i+=2
total *= trees
print(total)
#141864800
#828326400

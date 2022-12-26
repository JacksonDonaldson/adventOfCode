l = open("9.txt").read().split("\n")

locations = []
for i in range(10):
    locations.append([0,0])
res = set()
for move in l:
    if move[0] == "R":
        direc = [0,1]
    elif move[0] == "L":
        direc = [0,-1]
    elif move[0] == "U":
        direc = [1,0]
    else:
        direc = [-1,0]
    count = int(move.split(" ")[1])
    #print(count)
    for i in range(count):
        #print(head)
        locations[0] = [locations[0][0] + direc[0], locations[0][1] + direc[1]]

        print("start", locations)
        for i in range(1, len(locations)):
            print(locations)
            print(i, locations[i])
            print("at start of loop prev val is ", locations[i-1])
            print("at start of loop current val is", locations[i])

            if locations[i-i][0] - locations[i][0] > 1:
                print("1")
                locations[i] = [locations[i-i][0] - 1, locations[i-i][1]]
            if locations[i-i][0] - locations[i][0] < -1:
                print("2")
                locations[i] = [locations[i-i][0] + 1, locations[i-i][1]]
            if locations[i-i][1] - locations[i][1] > 1:
                print("at start of 3 prev val is", locations[i-1])
                print("so index 1 is", locations[i-1][1])
                v = locations[i-1][1]
                s = locations[i][1]
                print("locations[i-1][1]", locations[i-1][1])
                print("locations[i][1]", locations[i][1])
                print("idk anymore", (locations[i-i][1]) - (locations[i][1]))
                print("v-s", v-s)
                print(type(v))
                locations[i] = [locations[i-i][0], locations[i-i][1] - 1]
                print("so i is now", locations[i]) 
            if locations[i-i][1] - locations[i][1] < -1:
                print("4")
                locations[i] = [locations[i-i][0], locations[i-i][1] + 1]
            print("done", locations[i])
        print(locations)
        res.add(tuple(locations[-1]))

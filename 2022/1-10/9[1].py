l = open("9.txt").read().split("\n")

locations = []
for i in range(10):
    locations.append([0,0])
locations[0] = [0, 0]
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

        #print("start", locations)
        for i in range(1, len(locations)):
            head = locations[i-1]
            tail = locations[i]
            #print(locations)
            #print(i, locations[i])
            #print("at start of loop prev val is ", locations[i-1])
            #print("at start of loop current val is", locations[i])
            if head[0] - tail[0] > 1 and head[1] - tail[1] > 1:
                tail = [head[0] - 1, head[1] - 1]
            elif head[0] - tail[0] < -1 and head[1] - tail[1] < -1:
                tail = [head[0] + 1, head[1] + 1]
            elif head[0] - tail[0] > 1 and head[1] - tail[1] < -1:
                tail = [head[0] - 1, head[1] + 1]
            elif head[0] - tail[0] < -1 and head[1] - tail[1] > 1:
                tail = [head[0] + 1, head[1] - 1]
            elif head[0] - tail[0] > 1:
                tail = [head[0] - 1, head[1]]
                
            elif head[0] - tail[0] < -1:
                tail = [head[0] + 1, head[1]]
                
            elif head[1] - tail[1] > 1:
                tail = [head[0], head[1] - 1]

            elif head[1] - tail[1] < -1:
                #print("4")
                tail = [head[0], head[1] + 1]
            locations[i] = tail
            #print("done", locations[i])
        #print(locations)
        res.add(tuple(locations[-1]))
        #print(locations)
    ##print(locations)

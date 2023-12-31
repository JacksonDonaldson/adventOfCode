import math
seats = []
while True:
    j = input()
    if j == "-1":
        break
    seats.append(j)
largestNum = 0
plane = []
for i in range(0,128):
    plane.append([0]*8)
    
for seat in seats:
    mi = 0
    ma = 127
    for letter in seat[0:7]:
        if letter == "F":
            ma -= math.floor((ma-mi)/2)
        elif letter == "B":
            mi += math.ceil((ma-mi)/2)
        else:
            print("AAh")

    row = mi
    mi = 0
    ma = 7
    for letter in seat[7:]:
        if letter == "L":
            ma -= math.floor((ma-mi)/2)
        elif letter == "R":
            mi += math.ceil((ma-mi)/2)
        else:
            print("AAh")
    column = mi
    plane[row][column] = 1
for row in plane:
	for j in row:
		if j == 0:
			print(plane.index(row))
			
print(largestNum)

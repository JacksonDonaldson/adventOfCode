l = open("3.txt").read().split("\n")
c = [0,0]
counts = []
for i in range(len(l[0])):
    counts.append(c.copy())

for i in range(len(l)):
    for j in range(len(l[i])):
        counts[j][int(l[i][j])] += 1

maxes = ""
mins = ""
for col in counts:
    if col[0] > col[1]:
        maxes+="0"
        mins+="1"
    else:
        maxes+="1"
        mins+="0"
print(int(maxes,2) * int(mins,2))

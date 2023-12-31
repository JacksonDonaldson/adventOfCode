l = open("1.txt").read().split("\n")

ma = 0

vals = []
total = 0
for i in l:
    if i == "":
        vals.append(total)
        total = 0
    else:
        total += int(i)
vals.append(total)
vals.sort()
vals = vals[::-1]
print(vals[0] + vals[1] + vals[2])

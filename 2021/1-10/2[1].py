l = []
i = input()
while i != "done":
    l.append(i.split(" "))
    i = input()
print(l[0])

depth = 0
horiz = 0

for dir in l:
    if dir[0] == "forward":
        horiz += int(dir[1])
    elif dir[0] == "down":
        depth += int(dir[1])
    else:
        depth -= int(dir[1])
print(depth * horiz)

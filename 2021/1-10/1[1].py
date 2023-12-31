l = []
i = input()
while i != "done":
    l.append(i)
    i = input()

total = 0
last = int(l[0])
for i in range(1,len(l)):
    if int(l[i]) > last:
        total += 1
    last = int(l[i])

print(total)

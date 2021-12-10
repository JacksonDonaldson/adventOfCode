l = []
i = input()
while i != "done":
    l.append(int(i))
    i = input()

total = 0
last = l[0] + l[1] + l[2]
for i in range(1,len(l)-2):
    if l[i]+l[i+1]+l[i+2] > last:
        total += 1
    last = l[i]+l[i+1]+l[i+2]

print(total)

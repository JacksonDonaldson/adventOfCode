
f = open("6.txt").read().split(",")
f = [int(i) for i in f]
l = [0,0,0,0,0,0,0,0,0]
for i in range(9):
    l[i] = f.count(i)


for i in range(256):
    zero =l[0]
    for j in range(8):
        l[j] = l[j+1]
    l[8] = zero
    l[6] += zero
print(sum(l))

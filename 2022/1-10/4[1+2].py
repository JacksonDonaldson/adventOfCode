l = open("4.txt").read().split("\n")

total = 0

for s in l:
    v = s.split(",")
    n1, n2 = v[0].split("-")
    m1, m2 = v[1].split("-")
    n1 = int(n1)
    n2 = int(n2)
    m1 = int(m1)
    m2 = int(m2)
    if n1 >= m1:
        if m2 >= n1:
            total += 1
    else:
        if n2 >= m1:
            total +=1
print(total)

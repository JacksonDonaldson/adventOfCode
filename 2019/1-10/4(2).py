total = 0
for i in range(178416,676461):
    double = False
    i = str(i)
    for j in range(0,len(i) - 1):
        if i[j+1] == i[j]:
            left = False
            right = False
            if j - 1 <0 or i[j-1] != i[j]:
                left = True
            if j + 2 >= len(i) or i[j+2] != i[j]:
                right = True
            if left and right:
                double = True
        if i[j+1] < i[j]:
            double = False
            break
    if double:
        total += 1
print(total)

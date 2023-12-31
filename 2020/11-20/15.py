lastAppearance = [0] * 30000000
print("hey")
l = [1,5,0,9,11,18]
lastAppearance[18] = 0
lastAppearance[11] = 1
lastAppearance[9] = 2
lastAppearance[0] = 3
lastAppearance[5] = 4
k = 4
lastNum = 1
while k < 29999998:
    k+=1
    if k% 100000 == 0:
        print(k)
    #print(k)
    j = k - lastAppearance[lastNum]
    if j == k and lastNum != 18:
        j = 0
    lastAppearance[lastNum] = k
    lastNum = j
print(lastNum)

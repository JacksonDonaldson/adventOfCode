ins = []
while True:
    j = input()
    if j == "-1":
        break
    ins.append(int(j))

for i in range(0,len(ins)):
    #for each number, check each bit after that number
    for j in range(i,len(ins)):
        total = 0;
        l = []
        for k in range(i,j):
            total += ins[k]
            l.append(ins[k])
        if total == 10884537:
            print(max(l) + min(l))
            quit()
    print(i)
    

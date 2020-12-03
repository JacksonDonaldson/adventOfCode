ins = []
while True:
    i = input();
    if i == "-1":
        break
    ins.append(int(i))
for i in range(0,len(ins)):
    for j in range(i+1,len(ins)):
        total = 2020 - ins[i] - ins[j]
        if total == 0:
            continue
        for k in range(j+1,len(ins)):
            if ins[k] == total:
                print(ins[i]*ins[j]*ins[k])

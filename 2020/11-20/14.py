ins = []
while True:
    j = input()
    if j == "-1":
        break
    ins.append(j)

def doMask(mask, n):
    n = str(bin(n))[2:]
    
    while len(n)<36:
        n = "0" + n
    print(n)
    for i in range(1,len(n)+1):
        if mask[-i] != "X":
            n = n[0:len(n)-i] + mask[-i] + n[len(n)-i+1:]
    print(n)
    return int(n,2)
memory = {}
for i in ins:
    if "mask" in i:
        mask = i[7:]
    else:
        address = i[i.index("[") + 1:i.index("]")]
        value = int(i[i.index("=")+2:])
        print(mask)
        print(value)
        memory[address] = doMask(mask,value)
        
total = 0
for m in memory:
    total += memory[m]
print(total)
#ans < 10992011820304464859

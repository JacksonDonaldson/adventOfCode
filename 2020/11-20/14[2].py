ins = []
while True:
    j = input()
    if j == "-1":
        break
    ins.append(j)
def bits(length):
    #returns a sequence of possible bit sequences
    if length == 1:
        return["1","0"]
    b = bits(length-1)
    toReturn = []
    for i in b:
        toReturn.append("1" + i)
        toReturn.append("0" + i)
    return toReturn
def possible(n):
    values = []
    x = 0
    for i in range(0,len(n)):
        if n[i] == "X":
             x+= 1
    bit = bits(x)
    for b in bit:
        testN = n
        for num in b:
            testN = testN[0:testN.index("X")] + num + testN[testN.index("X")+1:]
        values.append(testN)
    if len(values) == 0:
        values = [n]
    for v in range(0,len(values)):
        values[v] = int(values[v],2)
    return values
def doMask(mask, n):
    n = str(bin(n))[2:]
    
    while len(n)<36:
        n = "0" + n
    
    for i in range(1,len(n)+1):
        if mask[-i] != "0":
            n = n[0:len(n)-i] + mask[-i] + n[len(n)-i+1:]
    n = possible(n)
    
    return n
memory = {}
for i in ins:
    if "mask" in i:
        mask = i[7:]
    else:
        address = int(i[i.index("[") + 1:i.index("]")])
        value = int(i[i.index("=")+2:])
        print(mask)
        print(value)
        address = doMask(mask,address)
        for a in address:
            memory[str(a)] = value
        
total = 0
for m in memory:
    total += memory[m]
print(total)
#ans < 10992011820304464859

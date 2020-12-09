ins = []
while True:
    j = input()
    if j == "-1":
        break
    ins.append(int(j))
prev = []
for i in range(0,25):
    prev.append(ins[i])

def canSum(l, n):
    for i in l:
        if n-i in l:
            return True
    return False
for i in range(25,len(ins)):
    if (not canSum(prev, ins[i])):
        print(ins[i])
        break
    prev.append(ins[i])
    prev.pop(0)
    

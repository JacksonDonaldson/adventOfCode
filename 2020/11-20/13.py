x = 0
ins = [[41,3],[569,13],[29,15],[19,13],[23,13],[937,44],[37,13],[17,10]]
#ins = [13,x,x,41,x,x,x,x,x,x,x,x,x,569,x,29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,23,x,x,x,x,x,x,x,937,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,17]
#try to find cycles
#ins = [[7,1],[59,2],[61,3]]
cycle = []

for i in ins:
    offsets = []
    t = 0
    n = i[0]
    desiredOffset = i[1]
    while True:
        t+=13
        offset = n - (t % n)
        offsets.append(offset)
        if offsets[0:int(len(offsets)/2)] == offsets[int(len(offsets)/2):]:
            print(offsets)
            break
    
    print(offsets)
    print(n)
    d = [len(offsets)/2]
    for o in range(0,int(len(offsets)/2)):
        if offsets[o] == desiredOffset:
            print("point found")
            print(o)
            print(offsets[o])
            print(desiredOffset)
            d.append(o + 1)
            print("end point")
    cycle.append(d)
#ans > 2174772600
print(cycle)
def foo(set1, set2):
    i = 0
    n1 = set1[1]
    m1 = set1[0]
    n2 = set2[1]
    m2 = set2[0]
    oh = []
    while True:
        test = m2 * i + n2
        test -= n1
        oh.append(test % m1)
        if oh[0:int(len(oh)/2)] == oh[int(len(oh)/2):]:
            break
        i+=1
    cycleLength = int(len(oh)/2)
    offset = oh.index(0)
    m = cycleLength * m2
    n = n2 + offset * m2
    return [m,n]
while len(cycle) != 1:
    print(cycle)
    cycle.insert(0,foo(cycle.pop(1),cycle.pop(0)))
print(cycle[0][1]*13)

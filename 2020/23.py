cups = list("586439172")
#cups = list("389125467")
for c in range(0,len(cups)):
    cups[c] = int(cups[c])
for i in range(10,1000001):
    cups.append(i)
cups = [0,cups]
def doMove(cups):
    active = cups[0]
##    print("active:")
##    print(active)
##    print(cups)
    remove = []
    cups = cups[1]
    ogValue = cups[active]
    for i in range(1,4):
        j = (active+1)
        if j >= len(cups):
            active-=1
            j = 0
        remove.append(cups.pop(j))
##    print(remove)
##    print(cups)
    i = 1
    dest = (ogValue - i)
    if dest == 0:
        dest = 10000000
    while dest in remove:
        i+=1
        dest = (ogValue - i) % 10000000
        if dest == 0:
            dest = 10000000
##    print("destination:")
##    print(dest)
    dest = cups.index(dest)
##    print(dest)
    for i in range(0,3):
        cups.insert(dest,remove.pop())
    #cups[dest+1:dest+1] = remove
    if(dest+1<=active):
        active +=3
    active = (active+1)%10000000
    #active = (cups.index(ogValue) + 1) % 10000000
    return [active,cups]
for i in range(0,10000000):
    cups = doMove(cups)
##    print(cups)
##    print()
    if(i % 1000) == 0:
        print(i)


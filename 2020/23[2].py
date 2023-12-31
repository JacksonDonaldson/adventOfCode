#linked lists, dictionaries, same idea
ll = {}
ll[5] = 8
ll[8] = 6
ll[6] = 4
ll[4] = 3
ll[3] = 9
ll[9] = 1
ll[1] = 7
ll[7] = 2
ll[2] = 10
for i in range(10,1000000):
    ll[i] = i + 1
ll[1000000] = 5

active = 5


def doMove(ll, active):
    movers = [ll[active], ll[ll[active]], ll[ll[ll[active]]]]
    #print(movers)
    ll[active] = ll[movers[2]]
    dest = active - 1
    if dest == 0:
        dest = 1000000
    while dest in movers:
        dest -= 1
        if dest == 0:
            dest = 1000000
    temp = ll[dest]
    ll[dest] = movers[0]
    ll[movers[2]] = temp
    return ll[active]
    


for i in range(0,10000000):
    active = doMove(ll, active)

print(ll[1] * ll[ll[1]])

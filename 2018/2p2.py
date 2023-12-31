def getIn():
    t = input()
    ins = []
    while t!= "done":
        ins.append(t)
        t = input()
    return ins

ids = getIn()

def dif(s1, s2):
    difs = 0
    for i in range(0,len(s1)):
        if s1[i] != s2[i]:
            difs += 1
        if difs > 1:
            return False
    return difs == 1
for i in range(0, len(ids)):
    for j in range(i+1, len(ids)):
        if dif(ids[i],ids[j]) == 1:
            print(i)
            print(j)

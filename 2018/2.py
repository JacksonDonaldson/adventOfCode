def getIn():
    t = input()
    ins = []
    while t!= "done":
        ins.append(t)
        t = input()
    return ins

def count(letter, s):
    c = 0
    while letter in s:
        s = s[s.index(letter) + 1:]
        c +=1
    return c
ids = getIn()
twoCount = 0
threeCount = 0
for id in ids:
    for letter in id:
        if count(letter, id) == 2:
            twoCount +=1
            break
    for letter in id:
        if count(letter, id) == 3:
            threeCount +=1
            break
print(twoCount * threeCount)

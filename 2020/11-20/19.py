ins = []
while True:
    j = input()
    if j == "-1":
        break
    ins.append(j)
keys = {}
for i in ins:
    key = i[0:i.index(":")]
    i = i[i.index(":")+2:]
    rules = i.split(" ")
    keys[key] = rules

    
def possibles(rules):
    if "|" in rules:
        n1 = possibles(rules[0:rules.index("|")])
        n2 = possibles(rules[rules.index("|") + 1:])
        for n in n2:
            n1.append(n)
        return n1

    possible = [""]
    for rule in rules:
        if keys[rule] == ['"a"']:
            for p in range(0,len(possible)):
                possible[p]+="a"
        elif keys[rule] == ['"b"']:
            for p in range(0,len(possible)):
                possible[p]+="b"
        else:
            j = possibles(keys[rule])
            #print(j)
            dummy = []
            for item in j:
                for p in possible:
                    dummy.append(p + item)
            possible = dummy.copy()
    #print(possible)
    return possible
j = possibles(keys["0"])
length = len(j[0])
f = possibles(keys["42"])
flength = len(f[0])
t = possibles(keys["31"])
tlength = len(t[0])
print(flength)
print(tlength)
print(length)
def interpretMessage(m):
    if len(m) % flength != 0:
        print("not matching mod")
        return False
    if m in j:
        print("already in")
        return True
    if len(m)<length:
        print("lower length")
        return False
    divided = []
    for i in range(0,int(len(m)/flength)):
        divided.append(m[i*flength:i*flength+flength])
    for d in range(0,len(divided)):
        if divided[d] in f:
            divided[d] = "f"
        elif divided[d] in t:
            divided[d] = "t"
        else:
            print("not in f or t")
            return False
    fcount = 0
    tcount = 0
    for d in divided:
        if d == "f":
            if tcount>0:
                print("f after t")
                return False
            fcount+=1
        if d == "t":
            tcount+=1
    print(divided)
    return fcount >tcount and tcount > 0
    print(divided)
print("possibled")
total= 0
while True:
    k = input()
    if k == "-1":
        break
    if interpretMessage(k):
        total+=1
        print(total)
        print(k)
    else:
        print("no")
print(total)
#ans>256
                
                

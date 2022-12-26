f = open("6.txt").read()

def unique(s):
    for i in range(14):
        if s[i] in s[i+1:]:
            return False
    return True

i = 14
s = f[:14]
for c in f[14:]:
    if unique(s):
        print(i)
    i+=1
    s+= c
    s = s[1:]

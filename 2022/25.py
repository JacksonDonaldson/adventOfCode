import jcksn as j
l = open("25.txt").read().split("\n")
total = 0

def conv(n):
    v = 0
    for s in range(len(n)):
        h = 0
        if n[s] == "-":
            h = -1
        elif n[s] == "=":
            h = -2
        else:
            h = int(n[s])
        v += h * 5  ** (len(n) - s - 1)
    return v
        
for n in l:
    total += conv(n)

def back(n, power):
    #print(n)
    if n == 1:
        return "1"
    if n == 2:
        return "2"
    if n == 0:
        return "0"
    if n == -1:
        return "-"
    if n == -2:
        return "="
    
    if n > (1.5 * 5**power):
        return "2" + back(n - 2*5**power, power-1)
    if n > (.5 * 5**power):
        return "1" + back(n- 5**power, power-1)
    if n > (-.5 * 5**power):
        return "0" + back(n, power-1)
    if n >(-1.5 * 5**power):
        return "-" + back(n+ 5**power, power-1)
    return "=" + back(n+ 2 * 5**power, power-1)
    

i = 0
while 3 * (5 ** i) < total:
    i+=1
print(back(total, i))
    

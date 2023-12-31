q = ["Z", "J", "N", "W", "P", "S"]
w = ["G", "S", "T"]
e = ["V", "Q", "R", "L", "H"]
r = ["V", "S", "T", "D"]
t = ["Q", "Z", "T", "D", "B", "M", "J"]
y = ["M", "W", "T", "J", "D", "C", "Z", "L"]
u = ["L", "P", "M", "W", "G", "T", "J"]
i = ["N", "G", "M", "T", "B", "F", "Q", "H"]
o = ["R", "D", "G", "C", "P", "B", "Q", "W"]
l = [q,w,e,r,t,y,u,i,o]

ins = open("5.txt").read().split('\n')

for move in ins:
    foo, count, fro, n1, to, n2 = move.split(" ")

    
    l[int(n2)-1].extend(l[int(n1)-1][-int(count):])
    l[int(n1)-1] = l[int(n1)-1][:-int(count)]

for f in l:
    print(f[-1], end = "")

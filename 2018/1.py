t = input()
t = t.split(",")
total = 0
i = 0
l = []
while total not in l:
    l.append(total)
    total += eval(t[i%len(t)])
    
    i+=1
print(total)

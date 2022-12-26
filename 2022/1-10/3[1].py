l = open("3.txt").read().split("\n")

total = 0
for i in range(0, len(l), 3):
    
    for s in l[i]:
        if s in l[i+1]:
            if s in l[i+2]:
                h = ord(s) - 64
                if h <= 26:
                    total += h + 26
                else:
                    total += h - 26 - 6
                break
print(total)

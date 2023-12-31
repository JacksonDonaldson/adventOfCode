l = open("10.txt").read().split("\n")
res = "." * 40

t = []
for i in range(6):
    t.append(list(res))
    

def checkCyc():
    
    c = i % 40
    r = i // 40
    #print(r, c, i, x)
    if c == x or c + 1 == x or c - 1 == x:
        #print(c, x, "val")
        t[r][c] = "#"
        

x = 1
i = 0
for s in l:
    
    
    if s[0] == "a":
        d, n = s.split(' ')
        i += 1
        checkCyc()
        x += int(n)
    i+=1
    checkCyc()


    

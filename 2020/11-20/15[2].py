
l = [1,5,0,9,11,18]
l = {"18":5,"11":4,"9":3,"0":2,"5":1}
lastNum = 1
k = 6
while k < 30000000:
    k+=1
    #print(lastNum)
    try:
        j = l[str(lastNum)]
    except:
        j = 0
    l[str(lastNum)] = 0
    for i in l:
        l[i] +=1
    lastNum = j
    
print(lastNum)

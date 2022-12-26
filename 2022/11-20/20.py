

import jcksn as j
l = open("20.txt").read().split("\n")
total = 0
operate = []
for i in range(len(l)):
    operate.append([i, (int(l[i]) * 811589153)])

for i in range(len(operate)):
    operate[i].append(operate[i][1])
    operate[i][1] = operate[i][1] % (len(operate) - 1)

for i in range(10):
    print(i)
    #print(operate)
    current = 0
    while current < len(operate):
        i = 0
        while operate[i][0] != current:
            i+=1
        #print(i, operate[i][1])
        newLocation = i

        for _ in range(operate[i][1]):
            newLocation += 1
            if newLocation == len(operate):
                newLocation = 0
        
##        else:
##            n = operate[i][1]
##            newLocation -=1
##            if newLocation == -1:
##                newLocation = len(operate)-1
##
##            #print("starting backtracking")
##            for j in range(((abs(n))% (len(operate) - 1) )):
##                
##                #print(newLocation)
##                if newLocation == 0:
##                    newLocation = len(operate)
##                newLocation -= 1
##            #print("ended at", newLocation)
                
        

        store = operate[i]
        #print("newLocation: ", newLocation, "i", i, "operate: ", operate[i])
        if(newLocation < 0):
            print(newLocation)
            print(operate.index(store))
            #newLocation = newLocation % 4999
        operate.insert(newLocation + 1, operate[i])
        
        
        if newLocation < i:
            i+=1
        #print(i)
        #print(operate[:10])
        operate.pop(i)
        

        if(newLocation < 0):
            print("new index", operate.index(store))
            quit()
        #print(" ".join([str(o[2]) for o in operate]))
        current+=1


#not 1700
#not -4400
# > 2323
f = [o[2] for o in operate]
#print(f)
ind = f.index(0)
print(f[(ind + 1000) % len(f)], f[(ind + 2000) % len(f)], f[(ind + 3000) % len(f)])
print(f[(ind + 1000) % len(f)]+ f[(ind + 2000) % len(f)]+ f[(ind + 3000) % len(f)])

# < 5660022753022
# < 4991273290950
# = 548634267428

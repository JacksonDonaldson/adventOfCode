import jcksn as j

l = open("13.txt").read().split("\n\n")

def ordered(left, right):
    if type(left) == type(right) == int:
        if left < right:
            return -1
        if right < left:
            return 1
        return 0
    if type(left) == type(right) == list:
        k = 0
        for f in range(len(left)):
            k+=1
            if f == len(right):
                return 1
            o = ordered(left[f], right[f])
            if o != 0:
                return o
            
        if k == len(right):
            return 0
        return -1

    if type(left) == int:
        return ordered([left], right)
    
    return ordered(left, [right])
i = 0
total = 0

allP = []
for pair in l:
    i+=1
    
    left, right = pair.split("\n")
    
    
    left = eval(left)
    right = eval(right)

    allP.append(left)
    allP.append(right)

done = False
while not done:
    i = 0
    done = True
    while i < len(allP) - 1:
        o = ordered(allP[i], allP[i+1])
        if o == 1:
            allP[i], allP[i+1] = [allP[i+1], allP[i]]
            done = False
            i+=1
        if o == 0:
            print(allP[i], allP[i+1])
        i += 1

for i in range(len(allP) - 1):
    if ordered(allP[i], allP[i+1]) != -1:
        print(i)
print((allP.index([[2]])+1) * (1+allP.index([[6]])))


import j
import math
f = open("18.txt")
l = f.read().split("\n")

def explode(v,i):

    nums = j.isplit([v], "[],")[0][0:-1]
    #nums = [i for i in nums if i != [""]]
    #print(nums)
    index = 0
    search = 0
    wasNum = False
    while search < i:
        if v[search] in "[],":
            if wasNum:
                wasNum = False
        else:
            
            if not wasNum:
                index += 1
            wasNum = True
        search += 1
    #print(index)
    #print(nums)
    if index != 0:
        nums[index-1] = str(int(nums[index]) + int(nums[index-1]))
    if index < len(nums) - 2:
        nums[index+2] = str(int(nums[index+1]) + int(nums[index+2]))
    #print(nums)
    newV = ""
    newi = 0
    ind = 0
    while newi < len(v):
        #print(newV)
        if newi == i - 1:
            newi += 1
            continue
        if newi == i:
            newV += "0"
            ind += 2
            newi += len(nums[index]) + 2 + len(nums[index+1])
##            if index == 0:
##                print("active")
##                newi += 1
            if i == len(nums) - 1:
                print(v)
            continue
        if v[newi] in "[],":
            newV += v[newi]
            newi += 1
            prevNum = False                
            continue                            
        if v[newi] not in "[],":
            
            if not prevNum:
                newV += nums[ind]
                ind += 1
            prevNum = True
            newi += 1
    return newV

def split(v,i):
    nums = j.isplit([v], "[],")[0][0:-1]
    index = nums.index(str(i))
    #print(nums)
    nums[index] = "[" + str(int(int(nums[index]) /2)) + "," + str(math.ceil(int(nums[index])/2)) + "]"
    #print(nums)
    newV = ""
    newi = 0
    ind = 0
    while newi < len(v):
        #print(newV)
        #print(newV)
        if v[newi] in "[],":
            newV += v[newi]
            newi += 1
            prevNum = False                
            continue                            
        if v[newi] not in "[],":
            
            if not prevNum:
                newV += nums[ind]
                #print("adding " + nums[ind])
                #print(f"{ind=}")
                ind += 1
            if ind != index:
                prevNum = True
            newi += 1
    return newV
def step(v):
    count = 0
    i = 0
    for c in v:
        i+=1
        
        if c == "[":
            count += 1
        elif c == "]":
            count -=1

        if count > 4:
            #continue until good pair found
            while v[i] in "[],":
                i += 1
            storI = i
            while True:
                while v[i] not in "[],":
                    i += 1
                #number
                i += 1#comma
                if v[i] not in "[],":
                    break
                else:
                    while v[i] in "[],":
                        i += 1
                    storI = i
                    #continue until next hope
            
            v = explode(v,storI)
            return v
        
    for n in j.isplit([v], "[],")[0][0:-1]:
        if int(n) >= 10:
            #print(n)
            
            v = split(v,n)
            return v
    return False
total = l[0]
prevTotal = total
for v in l[1:]:
    total = "[" + total + "," + v + "]"
    prevTotal = total
    while True:
        #print(total)
        total = step(total)
        #print(total)
        #print("step done")
        if not total:
            total = prevTotal
            break
        prevTotal = total
    #print("1")
    #print(total)

def magnitude(n):
    try:
        return int(n)
    except:
        return 3 * magnitude(n[0]) + 2 * magnitude(n[1])

print(magnitude(eval(total)))
    
    

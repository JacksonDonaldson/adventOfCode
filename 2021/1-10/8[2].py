f = open("8.txt")
l = f.read().split("\n")
l = [i.split(" | ") for i in l]
for i in range(len(l)):
    l[i] = [k.split() for k in l[i]]


#given a signal (a,b,c, ect), and a set of digits returns the positions that digit could possibly occupy
def findPossible(signal, digits):
    possible = []

    #for each digit in the row, look at its length
    #the numbers correspond to segments going around the display counterclockwise starting from the top right, with the middle segment being 6
    
    for value in digits:
        #if signal appears, then it must correspond to one of the segments that can light up with that length of value
        if signal in value:
            if len(value) == 2:
                possible.append([0,1])
            elif len(value) == 3:
                possible.append([0,1,5])
            elif len(value) == 4:
                possible.append([0,1,4,6])
            else:
                possible.append([0,1,2,3,4,5,6])

        #if it doesn't appear, then it must be one of the segments that can not light up, given that length
        else:
            if len(value) == 2:
                possible.append([2,3,4,5,6])
            elif len(value) == 3:
                possible.append([2,3,4,6])
            elif len(value) == 4:
                possible.append([2,3,5])
            elif len(value) == 5:
                possible.append([0,1,3,4])
            elif len(value) == 6:
                possible.append([0,3,6])
            else:
                print("bad")
            

    #knock down possible places because a value has to be in every list in possible to be valid
    appear = possible[0]
    for p in possible:
        toRemove = []
        for a in appear:
            if a not in p:
                toRemove.append(a)
        for r in toRemove:
            appear.remove(r)

    
    return appear

#if a pair of values (like 2 signals that can just be 0 & 1) appears, remove those values from all other places
def findPairs(l):
    toRemove = []
    for v in l:
        if len(v) == 2 and v in l[l.index(v)+1:]:
            toRemove.append(v)
            
    for v in toRemove:
        for i in range(len(l)):
            if len(l[i]) > 2:
                if v[0] in l[i]:
                    l[i].remove(v[0])
                if v[1] in l[i]:
                    l[i].remove(v[1])
    return l

#remove known segments from all other locations
def findSingles(l):
    known = []
    for i in range(len(l)):
        if len(l[i]) == 1:
            known.append(l[i][0])
            #print(l[i])
    for k in known:
        #print(k)
        for i in range(len(l)):
            if len(l[i]) != 1:
                #print(l[i])
                if k in l[i]:
                    l[i].remove(k)
    return l

#translate back to decimal, given the map l generated earlier
def decimify(n,l):
    ans = []
    for letter in n:
        ans.append(l["abcdefg".index(letter)])
    ans.sort()
    #print(ans)
    ans = [i[0] for i in ans]
    if ans == [0,1]:
        return "1"
    if ans == [0,1,5]:
        return "7"
    if ans == [0,1,2,3,4,5]:
        return "0"
    if ans == [0,1,4,6]:
        return "4"
    if ans == [0,2,3,5,6]:
        return "2"
    if ans == [0,1,2,5,6]:
        return "3"
    if ans == [1,2,4,5,6]:
        return "5"
    if ans == [1,2,3,4,5,6]:
        return "6"
    if ans == [0,1,2,3,4,5,6]:
        return "8"
    if ans == [0,1,2,4,5,6]:
        return "9"
    print("BAD")

#translate each number in the output
def translate(l, nums):
    #print(l)
    res = ""
    for n in nums:
        res += decimify(n,l)
    return int(res)


#takes in a row, and decodes it
def decode(r):
    
    starts = r[0]
    ends = r[1]
    
    l = []
    total = 0

    #for each signal, find out where it can be then add the constraints of pairs & singles
    for signal in "abcdefg":
        #print(signal)
        #print(starts + ends)

        
        l.append(findPossible(signal, starts + ends))
        l=findPairs(l)
        l = findSingles(l)
        l = findPairs(l)

   #this leaves a list where the first position is a number that represents "a"'s location, the second represents "b"'s location, and so on
        
    total += translate(l, ends)
    return total
    #return l    
total = 0
for r in l:
    total += int(decode(r))
print(total)

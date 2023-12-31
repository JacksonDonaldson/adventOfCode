import j
import math

f = open("16.txt")
l = f.read()
l = [bin(int(s,16)) for s in l]
s = "".join([(4-len(str(s)[2:]))* "0" +str(s)[2:] for s in l])

ind = 0
total = 0

def convert(t, values):
    print(t)
    print(values)
    if t == "000":
        return sum(values)
    if t == "001":
        t = 1
        for v in values:
            t*= v
        return t
    if t == "010":
        return min(values)

    if t == "011":
        return max(values)

    if t == "101":
        return int(values[0] > values[1])
    if t == "110":
        return int(values[1] > values[0])
    if t == "111":
        return int(values[0] == values[1])
    print("bad")
    
def parsePacket(s, limit=-1):
    print(f"{s=}")
    ind = 0
    total = 0

    toReturn = []
    
    while ind < len(s):
        limit -= 1
        
        if "1" not in s[ind+1:]:
            break
        version = s[ind:ind+3]
        #print(version)
        total += int(version,2)
        t = s[ind+3:ind+6]
        #print(t)
        ind += 6
        if t == "100":
            #print(s[ind])
            num = ""
            while s[ind] == "1":
                num += s[ind+1:ind+5]
                ind += 5
            num += s[ind+1:ind+5]
            ind += 5
            toReturn.append(int(num,2))
            
            #print(f"literal found {ind}")
        else:
            
            if s[ind] == "0":
                #print(f"version 0 found {ind=}")
                ind+=1
                totalLen = int(s[ind:ind+15],2)
                #print(s[ind:ind+15])
                
                ind += 15

                values = parsePacket(s[ind:ind+totalLen])
                toReturn.append(convert(t,values))
                ind += totalLen

            elif s[ind] == "1":
                ind+=1
                #print(f"version 1 found {ind=}")
                subLen= int(s[ind:ind+11],2)
                #print(s[ind:ind+11])
                foo = parsePacket(s[ind+11:], subLen)
                
                ind += 11 + foo[1]
                values = foo[0]

                toReturn.append(convert(t,values))
                
        if limit == 0:
            break


    if limit >= 0:
        return [toReturn, ind]
    return toReturn

print(parsePacket(s))
    

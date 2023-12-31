f = open("7in.txt").read()
d = {}
while len(f)>0:
    try:
        line = f[0:f.index("\n")]
        f = f[f.index("\n")+1:]
    except:
        line = f[0:]
        f = ""
    #print(line)
    color = line[0:line.index("contain")-6]
    #print(color)
    line = line[line.index("contain")+8:]
    #print(line)
    holds = []
    while(len(line)>0):
        bag = line[0:line.index("bag")-1]
        num = bag[0:bag.index(" ")]
        bag = bag[bag.index(" ") + 1:]
        #add num here
        holds.append([num,bag])
        #print(num)
        #print(bag)
        try:
            line = line[line.index(",")+2:]
        except:
            line = ""
        #print(line)
    d[color] = holds

def count(n):
    total = 0
    #print(n)
    #print
    for i in d[n]:
        if i == ["no", "other"]:
            return 1
        else:
            try:
                print(i[1] + ":" )
                k = count(i[1])
                print(k)
                total += int(i[0]) * k
            except:
                print("error:")
                print(i)
    
    return total + 1
print(count("shiny gold") - 1)
#11300<ans

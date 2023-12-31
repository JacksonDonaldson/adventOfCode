import jScripts
f = open("24.txt")
l = f.read().split("\n")
l = jScripts.isplit(l," ")

p = str(int("9" * 14) + 1)
def getPossible():
    global p
    p = int(p) - 1
    while "0" in str(p):
        p -=1
    #if (int(p) % 1001 == 0):
        #print(p)
    return p

def hasI(string, i):
    openCount = 0
    j=0
    for char in string[i:]:
        j+=1
        if "v" in char or "x" in char or "y" in char or "z" in char or "w" in char:
            return False

        if char == "(":
            
            openCount +=1
        if char == ")":
            #print(char)
            openCount -= 1
        if openCount == 0:
            return j+i

def evaluate(values,c,index):
    replace = eval(values[c:index])
    
    if type(replace) == type(True):
        return replace
##                    print("bool did")
##                    print(values)
    else:
        return str(eval(values[c:index]))

def replacet0(values):
    depth = 0
    if "*0" in values:
        i = values.index("*0")
        startI = i
        depth = 1
        while depth != 0:
            if values[startI] == "(":
                depth -=1
            elif values[startI] == ")":
                depth += 1
            startI -=1
        #print(startI)
        values = values[:startI+2] + "0" + values[i+2:]
    if "0*" in values:
        i = values.index("0*")
        endI = i
        depth = 1
        while depth != 0:
            if values[endI] == "(":
                depth +=1
            elif values[endI] == ")":
                depth -= 1
            endI +=1
        values = values[:i-1] + "0" + values[endI:]
    return values
def simplify(values):
    while replacet0(values) != values:
        values = replacet0(values)
    c=0
    while c < len(values):
        if values[c] == "(":
            index = hasI(values,c)
            
            if index:
                #print(values)
##                print(c)
##                print(index)
##                print("simplifying")
##                print(values[c:index])
                newValues = values[c:index]
                mode = "normal"
                if "o" in newValues:
                    new = newValues.replace("o","1")
                    lastValue = evaluate(new, 0,len(newValues))
                    #print(f"{lastValue=}")
                    new2 = newValues.replace("o","2")
                    if evaluate(new2,0,len(newValues)) == str(int(lastValue) + 1):
                        mode = "additive"
                    else:
                        mode = "normal"
                    good = True
                    for m in range(2,10):
                        new = newValues.replace("o",str(m))
                        print(new)
                        if mode == "additive":
                            if evaluate(new,0,len(newValues)) != str(int(lastValue) -1+m):
                                print("failed")
                                newValue = evaluate(new,0,len(newValues))
                                print(f"{newValue=}")
                                good = False
                                c+=1
                                break
                        elif evaluate(new,0,len(newValues)) != lastValue:
                            print("failed")
                            newValue = evaluate(new,0,len(newValues))
                            print(f"{newValue=}")
                            good = False
                            c+=1
                            break
                    if not good:
                        continue
                    if mode == "additive":
                        newValues = "(o + " + str(int(lastValue)-1) + ")"
                    else:
                        newValues = new
                if mode == "normal":
                    newValues = evaluate(newValues,0,len(newValues))
                if type(newValues) == type(True):
                    values = values[:c-3] + str(int(newValues)) + values[index:]
                else:
                    values = values[:c] + str(newValues) + values[index:]
                #print("final values of values: ")
                #print(values)
                
        c+=1
    return values
    
def stepify(l):
    steps = [l[0]]
    step = ["o","0","0","0"]
    i=0
    for d in l[1:]:
        #print(d)
        com = d[0]
        s = f"{d[1]}"
        start = "wxyz".index(s)
        if len(d) > 2:
            #print(f"{inst[2]}")
            val = f"{d[2]}"
            if val == "w":
                end = step[0]
            elif val == "x":
                end = step[1]
            elif val == "y":
                end = step[2]
            elif val == "z":
                end = step[3]
            else:
                end = val
                
        if com == "inp":
            steps.append(step)
            steps.append(d)
            step = ["w","x","y","z"]
            step[start] = "o"
            for v in range(4):
                if step[v] != "o":
                    try:
                        int(steps[-2][v])
                        step[v] = steps[-2][v]
                    except:
                        pass
            
        elif com == "add":
            
            step[start] += "+"
            step[start] = "(" + step[start] + end + ")"
        elif com == "mul":
            step[start] += "*"
            step[start] = "(" + step[start] + end + ")"
            #exec(f"{start} = {start} * {inst[2]}")
        elif com == "div":
            step[start] += "//"
            step[start] = "(" + step[start] + end + ")"
        elif com == "mod":
            step[start] += "%"
            step[start] = "(" + step[start] + end + ")"
        else:
            step[start] = "int(" + step[start] +"=="+ end + ")"

        while simplify(step[start]) != step[start]:
            step[start] = simplify(step[start])
        #print(step[start])
    steps.append(step)
    return steps
            
l = stepify(l)        
            #exec(f"{start} = int({start} == {inst[2]})")
#[w,x,y,z]
def getValue(p,param, steps):
    ind = 0
    if len(steps) < 10:
        print(steps)
    for step in l[p:]:

        
        ind += 1

        if step[0] == "inp":
            start = "wxyz".index(step[1])
            
            for i in range(9,0,-1):
                param[4]=i
                
                getValue(p+ind,param.copy(), steps + str(i))
            continue  
        i = 0
        p2 = []
        for v in step:
            v = v.replace("w",str(param[0]))
            v = v.replace("x",str(param[1]))
            v = v.replace("y",str(param[2]))
            v = v.replace("z",str(param[3]))
            v = v.replace("o",str(param[4]))
            p2.append(v)
            i+=1

        for i in range(4):
            param[i] = eval(p2[i])
        
    

                
        


    if param[3] == 0:
        print(steps)
        print(param)
        print("!!!!!!!")
        
    

            
        

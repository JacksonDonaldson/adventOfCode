def parseFunction(func):
    initial = [];
    i=0;
    constants = ['0','1','2','3','4','5','6','7','8','9'];
    while i<len(func):
        #adds to parts each section of the function
        initial.append(func[i]);
        #deal with special cases (mplied multiplication)
        try:
            if func[i] == ")" or func[i] in constants:
                #print("check");
                if func[i+1] == "(":
                    initial.append("*");
                    #print(initial);
        except:
            break
        
        
        i+=1;
    #print(initial);
    #deal with special cases (multi-digit numbers)
    temp =[];
    i=0;
    while i<len(initial):
        if i==0:
            temp.append(initial[i]);
            i+=1;
            continue
        if initial[i] in constants and initial[i-1] in constants:
            dummy = temp[-1];
            del temp[-1]
            temp.append(dummy + initial[i]);
            i+=1;
            continue
        temp.append(initial[i]);
        i+=1;
            #check for multi digit and condense
            #check for variable next to constant
            #check for para next to eachother
            #if go through all without incident, done
    initial = temp;
    return initial.copy()
def doOpperation(n1,n2,op):
    #print(n1)
    #print(n2)
    #print(op)
    if op == "+":
        return int(n1) + int(n2)
    if op == "*":
        return int(n1)*int(n2)
    
def evaluate(func):
    i= 0
    constants = ['1','2','3','4','5','6','7','8','9','0']
    n1 = "none"
    n2 = "none"
    while i<len(func):
        value = func[i]
        if value == "(":
            #evaluate the parenthesis
            start = i+1
            neededLefts = 1
            while neededLefts > 0:
                i+=1
                if func[i] == ")":
                    neededLefts -= 1
                if func[i] == "(":
                    neededLefts +=1
            #print(func)
            #print(start)
            #print(i)
            if n1 == "none":
                n1 = evaluate(func[start:i])
            else:
                n2 = evaluate(func[start:i])
                n1 = doOpperation(n1,n2,op)
        elif value in constants:
            if n1 == "none":
                n1 = value
            else:
                n2 = value
                n1 = doOpperation(n1,n2,op)
        elif value in ["+","*"]:
            op = value
        i+=1
    return n1
total = 0   
while True:
    j = input()
    if j == "-1":
        break
    j = parseFunction(j.replace(" ",""))
    total += evaluate(j)
print(total)

class Intcode:
    def __init__(self, code, inputs):
        self.inputs = inputs
        self.code = code
        self.i = 0
        self.inputLocation = 0
        self.outs = []

    def resetAndRun(self, inputs):
        self.inputs = inputs
        self.inputLocation = 0
        return self.runCode()
    
    def runCode(self):
        #runs through the program, until we reach a 99.
        #pointer incrementation is handled by individiual methods
        
        while self.code[self.i] != 99:
            opcode = int(str(self.code[self.i])[-2:])
            modes = str(self.code[self.i])[:-2]
            if opcode == 1:
                self.add(modes, self.code[self.i+1], self.code[self.i+2], self.code[self.i+3])
            elif opcode == 2:
                self.multiply(modes, self.code[self.i+1], self.code[self.i+2], self.code[self.i+3])
            elif opcode ==3:
                self.set(self.code[self.i+1])
            elif opcode == 4:
                return self.output(modes, self.code[self.i+ 1])
            elif opcode == 5:
                self.jIfTrue(modes, self.code[self.i+1], self.code[self.i+2])
            elif opcode == 6:
                self.jIfFalse(modes, self.code[self.i+1], self.code[self.i+2])
            elif opcode == 7:
                self.lessThan(modes, self.code[self.i+1], self.code[self.i+2], self.code[self.i+3])
            elif opcode == 8:
                self.equals(modes, self.code[self.i+1], self.code[self.i+2], self.code[self.i+3])
            elif opcode == 99:
                break
            else:
                print("opcode error")
                
        return "done"
                
    def paramatize(self, mode, value):
        #takes in a parameter and a value, and returns the appropriate value for that parameter and value (don't use for location codes)
        if mode == "0":
            return self.code[value]
        elif mode == "1":
            return value
        else:
            print("invalid mode found")
            
    def padModes(self, modeList, length):
        #pads modes to length, for use in paramatization
        while len(modeList) < length:
            modeList = "0" + modeList
        return modeList

    def add(self, modes, add1, add2, location):
        modes = self.padModes(modes, 3);
        add1 = self.paramatize(modes[-1], add1)
        add2 = self.paramatize(modes[-2], add2)
        self.code[location] = add1 + add2
        self.i += 4
    
    def multiply(self, modes, mult1, mult2, location):
        modes = self.padModes(modes, 3);
        mult1 = self.paramatize(modes[-1], mult1)
        mult2 = self.paramatize(modes[-2], mult2)
        self.code[location] = mult1 * mult2
        self.i += 4
        
    def set(self, location):
        #print(self.inputs)
        self.code[location] = int(self.inputs[self.inputLocation])
        self.inputLocation +=1
        self.i +=2

    def output(self, modes, out):
        modes = self.padModes(modes,1)
        out = self.paramatize(modes[-1], out)
        #print(out)
        #print("i equals " + str(self.i))
        self.i+=2
        return out
    
    def jIfTrue(self, modes, test, jumpLocation):
        modes = self.padModes(modes,2)
        test = self.paramatize(modes[-1], test)
        jumpLocation = self.paramatize(modes[-2], jumpLocation)
        if test != 0:
            self.i = jumpLocation
        else:
            self.i += 3
            
    def jIfFalse(self, modes, test, jumpLocation):
        modes = self.padModes(modes,2)
        test = self.paramatize(modes[-1], test)
        jumpLocation = self.paramatize(modes[-2], jumpLocation)
        if test == 0:
            self.i = jumpLocation
        else:
            self.i += 3

    def lessThan(self, modes, p1, p2, location):
        modes = self.padModes(modes, 3)
        p1 = self.paramatize(modes[-1], p1)
        p2 = self.paramatize(modes[-2], p2)
        if p1 < p2:
            self.code[location] = 1
        else:
            self.code[location] = 0
        self.i += 4
        
    def equals(self, modes, p1, p2, location):
        modes = self.padModes(modes, 3)
        p1 = self.paramatize(modes[-1], p1)
        p2 = self.paramatize(modes[-2], p2)
        if p1 == p2:
            self.code[location] = 1
        else:
            self.code[location] = 0
        self.i += 4
        
def posible(current, phases):
    #returns all not repeating possible ocmbinations given a list, not repeating
    pos = []
    if phases == []:
        return current
    for phase in phases:
        foo = posible(current + phase,
                phases[0:phases.index(phase)] + phases[phases.index(phase)+1:])
        if foo == str(foo):
            pos.append(foo)
        else:
            for f in foo:
                pos.append(f)
    return pos

def test(settings):
    #print("running program with input " + str(settings[0])+ ", " + str(0))
    #print("running a")
    #print(settings[0])
    a = Intcode(code.copy(), [settings[0], 0])
    b = Intcode(code.copy(), [settings[1], a.runCode()])
    c = Intcode(code.copy(), [settings[2], b.runCode()])
    d = Intcode(code.copy(), [settings[3], c.runCode()])
    e = Intcode(code.copy(), [settings[4], d.runCode()])
    out = e.runCode();
    loop = 0
    while out != "done":
        loop+=1
        foo = a.resetAndRun([out].copy())
        fooa = b.resetAndRun([foo].copy())
        foob = c.resetAndRun([fooa].copy())
        fooc = d.resetAndRun([foob].copy())
        lastOut = out
        print(lastOut)
        #fuck this line in particular
        out=e.resetAndRun([fooc].copy())
    print(loop)
    return lastOut

posPhases = posible("", ["5","6","7","8","9"])
code = [3,8,1001,8,10,8,105,1,0,0,21,34,51,76,101,114,195,276,357,438,99999,3,9,1001,9,3,9,1002,9,3,9,4,9,99,3,9,101,4,9,9,102,4,9,9,1001,9,5,9,4,9,99,3,9,1002,9,4,9,101,3,9,9,102,5,9,9,1001,9,2,9,1002,9,2,9,4,9,99,3,9,1001,9,3,9,102,2,9,9,101,4,9,9,102,3,9,9,101,2,9,9,4,9,99,3,9,102,2,9,9,101,4,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99]
#code = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
#27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
large = -9999999999
largePos = []
for pos in posPhases:
    print("running pos " + str(pos))
    j = test(list(pos))
    print("result of pos: " + str(j));
    try:
        if j> large:
            largePos = pos
            large = j
    except:
        print("AAh")
print(largePos)
print(large)

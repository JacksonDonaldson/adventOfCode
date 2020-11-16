class Intcode:
    def __init__(self, code, inputs):
        self.inputs = inputs
        self.code = code
        self.i = 0
        self.inputLocation = 0
        self.outs = []
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
                self.output(modes, self.code[self.i+ 1])
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

        return self.outs
                
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
        self.code[location] = int(self.inputs[self.inputLocation])
        self.inputLocation +=1
        self.i +=2

    def output(self, modes, out):
        modes = self.padModes(modes,1)
        out = self.paramatize(modes[-1], out)
        #print(out)
        #print("i equals " + str(self.i))
        self.outs.append(out)
        self.i+=2

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
    out = Intcode(code, [settings[0], 0]).runCode()[0]
    for i in range(1,5):
        if out == None:
            #print("none found")
            break
        #print("running program with input " + str(settings[i])+ ", " + str(out))
        out = Intcode(code, [settings[i], out]).runCode()[0]
        
    return out

posPhases = posible("", ["0","1","2","3","4"])
code = [3,8,1001,8,10,8,105,1,0,0,21,34,51,76,101,114,195,276,357,438,99999,3,9,1001,9,3,9,1002,9,3,9,4,9,99,3,9,101,4,9,9,102,4,9,9,1001,9,5,9,4,9,99,3,9,1002,9,4,9,101,3,9,9,102,5,9,9,1001,9,2,9,1002,9,2,9,4,9,99,3,9,1001,9,3,9,102,2,9,9,101,4,9,9,102,3,9,9,101,2,9,9,4,9,99,3,9,102,2,9,9,101,4,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99]
#code = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
#1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
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

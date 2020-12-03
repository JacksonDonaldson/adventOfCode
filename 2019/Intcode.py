class Intcode:
    def __init__(self, code, inputs = [], returnMode = False):
        self.inputs = inputs
        self.code = code
        for i in range(0,10000):
            code.append(0)
        self.i = 0
        self.inputLocation = 0
        self.outs = []
        self.relativeBase = 0
        self.returnMode = returnMode

    def resetAndRun(self, inputs):
        self.inputs = inputs
        self.inputLocation = 0
        return self.runCode()
    
    def runCode(self):
        #runs through the program, until we reach a 99.
        #pointer incrementation is handled by individiual methods
        
        while True:
            opcode = int(str(self.code[self.i])[-2:])
            modes = str(self.code[self.i])[:-2]
            if opcode == 1:
                self.add(modes, self.code[self.i+1], self.code[self.i+2], self.code[self.i+3])
            elif opcode == 2:
                self.multiply(modes, self.code[self.i+1], self.code[self.i+2], self.code[self.i+3])
            elif opcode ==3:
                self.set(modes, self.code[self.i+1])
            elif opcode == 4:
                out = self.output(modes, self.code[self.i+ 1])
                if self.returnMode:
                    break
            elif opcode == 5:
                self.jIfTrue(modes, self.code[self.i+1], self.code[self.i+2])
            elif opcode == 6:
                self.jIfFalse(modes, self.code[self.i+1], self.code[self.i+2])
            elif opcode == 7:
                self.lessThan(modes, self.code[self.i+1], self.code[self.i+2], self.code[self.i+3])
            elif opcode == 8:
                self.equals(modes, self.code[self.i+1], self.code[self.i+2], self.code[self.i+3])
            elif opcode == 9:
                self.relative(modes, self.code[self.i+1])
            elif opcode == 99:
                out = "done"
                break
            else:
                print("opcode error")
        
        if(self.returnMode):
            return out
        return self.outs
                
    def paramatize(self, mode, value):
        #takes in a parameter and a value, and returns the appropriate value for that parameter and value (don't use for location codes)
        if mode == "0":
            return self.code[value]
        elif mode == "1":
            return value
        elif mode == "2":
            return self.code[self.relativeBase + value]
        else:
            print("invalid mode found")

    def paramatizeLocation(self, mode, value):
        if mode == "0":
            return value
        elif mode == 1:
            print("error, 1 found in location")
        elif mode == "2":
            return value + self.relativeBase
        else:
            print('error, invalid mode in location')
        
    def padModes(self, modeList, length):
        #pads modes to length, for use in paramatization
        while len(modeList) < length:
            modeList = "0" + modeList
        return modeList

    def add(self, modes, add1, add2, location):
        modes = self.padModes(modes, 3);
        add1 = self.paramatize(modes[-1], add1)
        add2 = self.paramatize(modes[-2], add2)
        location = self.paramatizeLocation(modes[-3], location)
        self.code[location] = add1 + add2
        self.i += 4
    
    def multiply(self, modes, mult1, mult2, location):
        modes = self.padModes(modes, 3);
        mult1 = self.paramatize(modes[-1], mult1)
        mult2 = self.paramatize(modes[-2], mult2)
        location = self.paramatizeLocation(modes[-3], location)
        self.code[location] = mult1 * mult2
        self.i += 4
        
    def set(self, modes, location):
        modes = self.padModes(modes, 1);
        location = self.paramatizeLocation(modes[-1], location)
        self.code[location] = self.inputs[self.inputLocation]
        self.inputLocation +=1
        self.i +=2

    def output(self, modes, out):
        modes = self.padModes(modes,1)
        out = self.paramatize(modes[-1], out)
        #print(out)
        #print("i equals " + str(self.i))
        self.outs.append(out)
        self.i+=2
        if(self.returnMode):
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
        location = self.paramatizeLocation(modes[-3], location)
        if p1 < p2:
            self.code[location] = 1
        else:
            self.code[location] = 0
        self.i += 4
        
    def equals(self, modes, p1, p2, location):
        modes = self.padModes(modes, 3)
        p1 = self.paramatize(modes[-1], p1)
        p2 = self.paramatize(modes[-2], p2)
        location = self.paramatizeLocation(modes[-3], location)
        if p1 == p2:
            self.code[location] = 1
        else:
            self.code[location] = 0
        self.i += 4

    def relative(self, modes, add):
        modes = self.padModes(modes, 1);
        add = self.paramatize(modes[-1], add)
        self.relativeBase+= add
        self.i +=2
        

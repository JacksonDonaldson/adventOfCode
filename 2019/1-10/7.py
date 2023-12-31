ogprogram = [3,8,1001,8,10,8,105,1,0,0,21,34,51,76,101,114,195,276,357,438,99999,3,9,1001,9,3,9,1002,9,3,9,4,9,99,3,9,101,4,9,9,102,4,9,9,1001,9,5,9,4,9,99,3,9,1002,9,4,9,101,3,9,9,102,5,9,9,1001,9,2,9,1002,9,2,9,4,9,99,3,9,1001,9,3,9,102,2,9,9,101,4,9,9,102,3,9,9,101,2,9,9,4,9,99,3,9,102,2,9,9,101,4,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99]
ogprogram = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
program = ogprogram.copy();

def valueWithMode(mode, value):
    global program
    if mode == 0:
        return int(program[value])
    if mode == 1:
        return int(value)
    else:
        print("mode out of range")

def getModes(length, instruction):
    modes = str(instruction)[:-2]
    while len(modes) < length:
        modes = "0" + modes
    m = []
    for mode in modes:
        m.append(int(mode))
    return m.copy()

def runProgram(inputs):
    #runs program, returns output
    i = 0;
    ival = 0;
    program = ogprogram.copy()
    while True:
        opcode = int(str(program[i])[-2:])
        if opcode == 1:
            print("adding")
            modes = getModes(3,program[i])
##            print("program[" + str(valueWithMode(modes[2],i+3)) +  "] now equals " + str(program[valueWithMode(modes[2], i+1)] + program[valueWithMode(modes[1], i+2)]))
##            print("program[" + str(valueWithMode(modes[1], i+1)))
##            print("+")
##            print("program{" + str(valueWithMode(modes[0], i+2)))
##            print("modes: " + str(modes))
##            print("opcode: " + str(opcode))
##            print("original instructions: " + str(program[i:i+4]))
##            print("setting program[" + str(program[i+3]))
##            print("add 1: " + str(program[valueWithMode(modes[2], i+1)]))
##            print("add 2: " + str(program[valueWithMode(modes[1], i+2)]))
            program[program[i+3]] = program[valueWithMode(modes[2], i+1)] + program[valueWithMode(modes[1], i+2)]
            i+=4
        elif opcode == 2:
            print("multiplying")
            modes = getModes(3,program[i])
##            print("modes: " + str(modes))
##            print("opcode: " + str(opcode))
##            print("original instructions: " + str(program[i:i+4]))
##            print("setting program[" + str(program[i+3]))
##            print("multiple 1: " + str(program[valueWithMode(modes[2], i+1)]))
##            print("multiple 2: " + str(program[valueWithMode(modes[1], i+2)]))
            #print("program[" + str(program[i+3]) +  "] now equals " + str(valueWithMode(modes[1], i+1) * valueWithMode(modes[0], i+2)))
            
            program[program[i+3]] = program[valueWithMode(modes[2], i+1)] * program[valueWithMode(modes[1], i+2)]
            i+=4
        elif opcode == 3:
            print("setting program[" + str(program[i+3]))
            print("it's now " + str(inputs[ival]))
            program[program[i+1]] = int(inputs[ival])
            ival+=1
            i+=2
        elif opcode == 4:
            print("printing program[" + str(valueWithMode(modes[0], i+1)))
            modes = getModes(1,program[i])
            #print(program[valueWithMode(modes[0], i+1)])
            return program[valueWithMode(modes[0], i+1)]
            i+=2
        elif opcode == 5:
            modes = getModes(2, program[i])
            print("jump if true ing: checking if 0== program[ " + str(valueWithMode(modes[1], i+1)))
            if program[valueWithMode(modes[0], i+1)] != 0:
                print("mode: " + str(modes))
                print("jumping to what ever's at program[" + str(valueWithMode(modes[0], i+2)))
                i = program[valueWithMode(modes[1], i+2)]
                print('jumping to (not 0)' + str(i))
            else:
                print("it was 0")
                i+= 3
        elif opcode == 6:
            modes = getModes(2, program[i])
            if program[valueWithMode(modes[1], i+1)] == 0:
                i = program[valueWithMode(modes[0], i+2)]
                print("jumpirn to (equal to 0)" + str(i))
            else:
                i+= 3
        elif opcode == 7:
            modes = getModes(3, program[i])
            if program[valueWithMode(modes[2], i+1)] < program[valueWithMode(modes[1], i+2)]:
                program[program[i+3]] = 1
                print("smaller")
            else:
                program[program[i+3]] = 0
                print("not smaller")
            i+=4
        elif opcode == 8:
            modes = getModes(3, program[i])
            
            if program[valueWithMode(modes[2], i+1)] == program[valueWithMode(modes[1], i+2)]:
                print("equal")
                program[program[i+3]] = 1
            else:
                program[program[i+3]] = 0
                print("not equal")
            i+=4
        elif opcode == 99:
            #print(program)
            break
        else:
            print("error, opcode not found")
            print("i = " + str(i))
            print(opcode)
            break
#to do: test at each possible point

phases = ["0", "1", "2", "3", "4"]
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
#runProgram([5])
#quit()
def test(settings):
    print("running program with input " + str(settings[0])+ ", " + str(0))
    out = Intcode(code, [int(settings[0]), 0])
    for i in range(1,5):
        if out == None:
            print("none found")
            break
        print("running program with input " + str(settings[i])+ ", " + str(out))
        out = runProgram([int(settings[i]), out])
        
    return out
quit()
posPhases = posible("", phases)
large = -99999999990
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
        continue
print(largePos)

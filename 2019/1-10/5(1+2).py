program = [3,225,1,225,6,6,1100,1,238,225,104,0,1002,148,28,224,1001,224,-672,224,4,224,1002,223,8,223,101,3,224,224,1,224,223,223,1102,8,21,225,1102,13,10,225,1102,21,10,225,1102,6,14,225,1102,94,17,225,1,40,173,224,1001,224,-90,224,4,224,102,8,223,223,1001,224,4,224,1,224,223,223,2,35,44,224,101,-80,224,224,4,224,102,8,223,223,101,6,224,224,1,223,224,223,1101,26,94,224,101,-120,224,224,4,224,102,8,223,223,1001,224,7,224,1,224,223,223,1001,52,70,224,101,-87,224,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,1101,16,92,225,1101,59,24,225,102,83,48,224,101,-1162,224,224,4,224,102,8,223,223,101,4,224,224,1,223,224,223,1101,80,10,225,101,5,143,224,1001,224,-21,224,4,224,1002,223,8,223,1001,224,6,224,1,223,224,223,1102,94,67,224,101,-6298,224,224,4,224,102,8,223,223,1001,224,3,224,1,224,223,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,677,677,224,102,2,223,223,1005,224,329,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,344,101,1,223,223,1107,226,226,224,102,2,223,223,1006,224,359,101,1,223,223,1108,677,677,224,102,2,223,223,1005,224,374,101,1,223,223,8,677,226,224,1002,223,2,223,1005,224,389,101,1,223,223,108,226,677,224,1002,223,2,223,1006,224,404,1001,223,1,223,107,677,677,224,102,2,223,223,1006,224,419,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,434,101,1,223,223,1007,677,677,224,102,2,223,223,1005,224,449,1001,223,1,223,8,677,677,224,1002,223,2,223,1006,224,464,101,1,223,223,1108,677,226,224,1002,223,2,223,1005,224,479,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,494,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,509,1001,223,1,223,1007,226,677,224,1002,223,2,223,1006,224,524,1001,223,1,223,107,226,226,224,1002,223,2,223,1006,224,539,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,554,101,1,223,223,1108,226,677,224,102,2,223,223,1006,224,569,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,584,1001,223,1,223,7,226,226,224,1002,223,2,223,1006,224,599,101,1,223,223,8,226,677,224,102,2,223,223,1005,224,614,101,1,223,223,7,226,677,224,1002,223,2,223,1005,224,629,101,1,223,223,1008,226,677,224,1002,223,2,223,1006,224,644,101,1,223,223,107,226,677,224,1002,223,2,223,1005,224,659,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226]
i = 0;

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
while True:
    opcode = int(str(program[i])[-2:])
    if opcode == 1:
        #print("adding")
        modes = getModes(3,program[i])
        #print("program[" + str(valueWithMode(modes[2],i+3)) +  "] now equals " + str(program[valueWithMode(modes[1], i+1)] + program[valueWithMode(modes[0], i+2)]))
        #print("program[" + str(valueWithMode(modes[1], i+1)))
        #print("+")
        #print("program{" + str(valueWithMode(modes[0], i+2)))
        print("modes: " + str(modes))
        print("opcode: " + str(opcode))
        print("original instructions: " + str(program[i:i+4]))
        print("setting program[" + str(program[i+3]))
        print("add 1: " + str(program[valueWithMode(modes[2], i+1)]))
        print("add 2: " + str(program[valueWithMode(modes[1], i+2)]))
        program[program[i+3]] = program[valueWithMode(modes[2], i+1)] + program[valueWithMode(modes[1], i+2)]
        i+=4
    elif opcode == 2:
        #print("multiplying")
        modes = getModes(3,program[i])
        print("modes: " + str(modes))
        print("opcode: " + str(opcode))
        print("original instructions: " + str(program[i:i+4]))
        print("setting program[" + str(program[i+3]))
        print("multiple 1: " + str(program[valueWithMode(modes[2], i+1)]))
        print("multiple 2: " + str(program[valueWithMode(modes[1], i+2)]))
        #print("program[" + str(program[i+3]) +  "] now equals " + str(valueWithMode(modes[1], i+1) * valueWithMode(modes[0], i+2)))
        
        program[program[i+3]] = program[valueWithMode(modes[2], i+1)] * program[valueWithMode(modes[1], i+2)]
        i+=4
    elif opcode == 3:
        print("setting program[" + str(program[i+3]))
        program[program[i+1]] = int(input())
        i+=2
    elif opcode == 4:
        print("printing program[" + str(valueWithMode(modes[0], i+1)))
        modes = getModes(1,program[i])
        print(program[valueWithMode(modes[0], i+1)])
        i+=2
    elif opcode == 5:
        modes = getModes(2, program[i])
        if program[valueWithMode(modes[1], i+1)] != 0:
            i = program[valueWithMode(modes[0], i+2)]
            print('jumping to (not 0)' + str(i))
        else:
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
        break

        

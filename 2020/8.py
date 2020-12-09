code = []
while True:
    j = input()
    if j == "-1":
        break
    j = j.split(" ")
    code.append(j)

def runProgram(c):
    i = 0;
    accumulator = 0
    run = []
    while i not in run and i <len(c):
        run.append(i)
        instruction = c[i][0]
        argument = int(c[i][1])
        if instruction == "nop":
            i+=1
        elif instruction == "acc":
            accumulator += argument
            i+=1
        elif instruction == "jmp":
            i += argument
        else:
            print("instruction error")
            print(instruction)
    return [i not in run, accumulator]
##
import copy
for i in range(0, len(code)):
    inst = code[i][0]
    c = copy.deepcopy(code)
    if inst == "jmp":
        c[i][0] = "nop"
        j = runProgram(c)
    elif inst== "nop":
        c[i][0] = "jmp"
        j = runProgram(c)
    if j[0]:
        print(i)
        print(j[1])
        print(c)
#ans>847

code = []
while True:
    j = input()
    if j == "-1":
        break
    j = j.split(" ")
    code.append(j)
i = 0;
accumulator = 0
run = []
while i not in run:
    run.append(i)
    instruction = code[i][0]
    argument = int(code[i][1])
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
print(accumulator)

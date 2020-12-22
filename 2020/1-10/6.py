f = open("6in.txt")
f = f.read()
group = []
person = []
totalYes = 0
for letter in f:
    if letter == "\n":
        group.append(person.copy())
        person = []
        if newLine:
            #print(group)
            group.pop(-1)
            print(group)
            #there's an extra for some reason, I couldn't tell you why
            test = group[0]
            
            remove = []
            for person in group:
                #print(person)
                #print(test)
                for answer in test:
                    if answer not in person:
                        remove.append(answer)
            remove = list(set(remove))
            for r in remove:
                test.remove(r)
            print("adding " + str(len(test)))
            totalYes+=len(test)
            group = []
            person = []
        newLine = True
    else:
        newLine = False
        person.append(letter)
group.append(person)
test = group[0]
for person in group:
    print(person)
    print(test)
    remove = []
    for answer in test:
        if answer not in person:
            print("removing " + answer)
            remove.append(answer)
            
        print(test)
    print(remove)
    for r in remove:
        test.remove(r)
totalYes += len(test)

print(totalYes)
#ans<3191

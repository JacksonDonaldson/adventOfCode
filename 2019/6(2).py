links = {}
orbits = []
while True:
    i = input()
    if i == "-1":
        break
    foo = i.split(")");
    links[foo[1]] = foo[0]
    orbits.append(foo)
total = 0

def orbitLinks(orbit):
    if links[orbit] == "COM":
        return ["COM"]
    else:
        pastOrbits = orbitLinks(links[orbit])
        pastOrbits.append(orbit)
        return pastOrbits.copy()
youOrbits = orbitLinks("YOU")
sanOrbits = orbitLinks("SAN")
youOrbits.reverse()
sanOrbits.reverse()
for yourbit in youOrbits:
    for sanbit in sanOrbits:
        if yourbit == sanbit:
            
            print(youOrbits.index(yourbit) + sanOrbits.index(sanbit) - 2)
print(total)


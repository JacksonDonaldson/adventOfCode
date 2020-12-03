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
def orbitCount(orbit):
    if links[orbit] == "COM":
        return 1
    else:
        return orbitCount(links[orbit]) + 1
for orbit in orbits:
    total += orbitCount(orbit[1])
print(total)


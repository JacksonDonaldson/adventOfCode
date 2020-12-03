io = {"x" : 1, "y" : 4, "z" : 4}
iov = {"x" : 0, "y" : 0, "z" : 0}
europa= {"x" : -4, "y" : -1, "z" : 19}
europav = {"x" : 0, "y" : 0, "z" : 0}
ganymede = {"x" : -15, "y" : -14, "z" : 12}
ganymedev = {"x" : 0, "y" : 0, "z" : 0}
callisto = {"x" : -17, "y" : 1, "z" : 10}
callistov = {"x" : 0, "y" : 0, "z" : 0}
#test input
##io = {"x" : -8, "y" : -10, "z" : 0}
##iov = {"x" : 0, "y" : 0, "z" : 0}
##europa= {"x" : 5, "y" : 5, "z" : 10}
##europav = {"x" : 0, "y" : 0, "z" : 0}
##ganymede = {"x" : 2, "y" : -7, "z" : 3}
##ganymedev = {"x" : 0, "y" : 0, "z" : 0}
##callisto = {"x" : 9, "y" : -8, "z" : -3}
##callistov = {"x" : 0, "y" : 0, "z" : 0}
planets = {"io":io, "europa":europa,"ganymede":ganymede,"callisto":callisto}
velocities = {"io":iov, "europa":europav,"ganymede":ganymedev,"callisto":callistov}
def compare(i1, i2):
    if i2>i1:
        return 1
    elif i2<i1:
        return -1
    return 0
for i in range(0,1000):
    #update velocites
    for planet in planets:
        for planet2 in planets:
            for direction in ["x","y","z"]:
                velocities[planet][direction] += compare(planets[planet][direction],planets[planet2][direction])
    for planet in planets:
        for direction in ["x","y","z"]:
            planets[planet][direction] += velocities[planet][direction]
nrg = 0                                                                                                
#calculate energy
for planet in planets:
    posnrg = 0
    kinnrg = 0
    for direction in ["x","y","z"]:
        posnrg+=abs(planets[planet][direction])
        kinnrg+= abs(velocities[planet][direction])

    nrg+= posnrg*kinnrg
print(nrg)
        

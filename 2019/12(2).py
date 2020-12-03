io = {"x" : 1, "y" : 4, "z" : 4}
iov = {"x" : 0, "y" : 0, "z" : 0}
europa= {"x" : -4, "y" : -1, "z" : 19}
europav = {"x" : 0, "y" : 0, "z" : 0}
ganymede = {"x" : -15, "y" : -14, "z" : 12}
ganymedev = {"x" : 0, "y" : 0, "z" : 0}
callisto = {"x" : -17, "y" : 1, "z" : 10}
callistov = {"x" : 0, "y" : 0, "z" : 0}
#test input
##io = {"x" : -1, "y" : 0, "z" : 2}
##iov = {"x" : 0, "y" : 0, "z" : 0}
##europa= {"x" : 2, "y" : -10, "z" : -7}
##europav = {"x" : 0, "y" : 0, "z" : 0}
##ganymede = {"x" : 4, "y" : -8, "z" : 8}
##ganymedev = {"x" : 0, "y" : 0, "z" : 0}
##callisto = {"x" : 3, "y" : 5, "z" : -1}
##callistov = {"x" : 0, "y" : 0, "z" : 0}
planets = {"io":io, "europa":europa,"ganymede":ganymede,"callisto":callisto}
velocities = {"io":iov, "europa":europav,"ganymede":ganymedev,"callisto":callistov}
def compare(i1, i2):
    if i2>i1:
        return 1
    elif i2<i1:
        return -1
    return 0
i=0
import copy
p = copy.deepcopy(planets)
v = copy.deepcopy(velocities)
x = 0
y = 0
z = 0
while True:
    i+=1
    #update velocites
    for planet in planets:
        for planet2 in planets:
            for direction in ["x"]:
                velocities[planet][direction] += compare(planets[planet][direction],planets[planet2][direction])
    for planet in planets:
        for direction in ["x"]:
            planets[planet][direction] += velocities[planet][direction]
    if planets == p and velocities == v:
        print(i)
        x = i
        break
i=0
while True:
    i+=1
    #update velocites
    for planet in planets:
        for planet2 in planets:
            for direction in ["y"]:
                velocities[planet][direction] += compare(planets[planet][direction],planets[planet2][direction])
    for planet in planets:
        for direction in ["y"]:
            planets[planet][direction] += velocities[planet][direction]
    if planets == p and velocities == v:
        print(i)
        y = i
        break
i=0
while True:
    i+=1
    #update velocites
    for planet in planets:
        for planet2 in planets:
            for direction in ["z"]:
                velocities[planet][direction] += compare(planets[planet][direction],planets[planet2][direction])
    for planet in planets:
        for direction in ["z"]:
            planets[planet][direction] += velocities[planet][direction]
    if planets == p and velocities == v:
        print(i)
        z = i
        break

#use wolfram alpha to calculate lcm of x,y,z


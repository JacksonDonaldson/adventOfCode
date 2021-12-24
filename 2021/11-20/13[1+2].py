f = open("13.txt")
l = f.read().split("\n")
p = l[:l.index("")]
m = l[l.index("")+1:]

for i in range(len(p)):
    p[i] = [int(j) for j in p[i].split(",")]

def flipX(line, p):
    final = set()
    for point in p:
        if point[0] > line:
            final.add((line - (point[0]-line), point[1]))
        else:
            final.add(tuple(point))

    return list(final)

def flipY(line, p):
    final = set()
    for point in p:
        if point[1] > line:
            final.add((point[0], line - (point[1]-line)))
        else:
            final.add(tuple(point))
    return list(final)

for move in m:
    if move[11]=="x":
        p = flipX(int(move[13:]), p)
    elif move[11] == "y":
        p = flipY(int(move[13:]),p)
    else:
        print('badd')
#p = flipX(0,p)
p = flipY(0,p)
import matplotlib.pyplot as plt

x = [i[0] for i in p]
y = [i[1] for i in p]

plt.scatter(x,y)
plt.show()

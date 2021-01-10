p1 = []
p2 = []
print("Player 1:")
while True:
    j = input()
    if j == "-1":
        break
    p1.append(int(j))
print("Player 2:")
while True:
    j = input()
    if j == "-1":
        break
    p2.append(int(j))

while len(p1) > 0 and len(p2)>0:
    print()
    print(p1)
    print(p2)
    c1 = p1.pop(0)
    c2 = p2.pop(0)
    print(c1)
    print(c2)
    if c1>c2:
        print("p1 wins")
        p1.append(c1)
        p1.append(c2)
    else:
        print("p2 wins")
        p2.append(c2)
        p2.append(c1)
if len(p1)>0:
    winner = p1
else:
    winner = p2
score = 0
for i in range(1,len(winner) + 1):
    score += winner[-i] * i
print(score)

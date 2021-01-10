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
def recursiveCombat(p1,p2):
    alreadyPlayed = []
    while len(p1) > 0 and len(p2)>0:
        sitch = p1.copy() +["sep"] + p2.copy()
        if sitch in alreadyPlayed:
            #print("already played!")
            return ["p1",p1]
        else:
            alreadyPlayed.append(sitch)
        
        #print()
        #print(p1)
        #print(p2)
        
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        
        #print(c1)
        #print(c2)
        roundWinner = "none"
        if len(p1) >= c1 and len(p2) >= c2:
            #print("recurse!")
            roundWinner = recursiveCombat(p1.copy()[0:c1],p2.copy()[0:c2])[0]
        if roundWinner == "p1":
            #print("p1 wins the recursion")
            p1.append(c1)
            p1.append(c2)
        elif roundWinner == "p2":
            #print("p2 wins the recursion")
            p2.append(c2)
            p2.append(c1)
        elif c1>c2:
            #print("p1 wins")
            p1.append(c1)
            p1.append(c2)
        else:
            #print("p2 wins")
            p2.append(c2)
            p2.append(c1)
    if len(p1) > 0:
        return ["p1",p1]
    else:
        return ["p2",p2]
winner = recursiveCombat(p1.copy(),p2.copy())
print(winner[0])
print(winner[1])
winner = winner[1]
score = 0
for i in range(1,len(winner) + 1):
    score += winner[-i] * i
print(score)
#ans > 31332

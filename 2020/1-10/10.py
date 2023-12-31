ins = []
while True:
    j = input()
    if j == "-1":
        break
    ins.append(int(j))

oneDif = 0
twoDif = 0
threeDif = 0
def nextJolts(n):
    global oneDif
    global twoDif
    global threeDif
    global ins
    if n+1 in ins:
        oneDif+=1
        nextJolts(n+1)
    elif n+2 in ins:
        twoDif +=1
        nextJolts(n+2)
    elif n+3 in ins:
        threeDif += 1
        nextJolts(n+3)
nextJolts(0)
threeDif +=1
print(oneDif * threeDif)

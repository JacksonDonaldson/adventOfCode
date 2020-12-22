ins = []
while True:
    j = input()
    if j == "-1":
        break
    ins.append(int(j))
insRes = {}


def nextJolts(n):
    global ins
    if str(n) in insRes:
        return insRes[str(n)]
    total = 0;
    if n+1 in ins:
        total += nextJolts(n+1)
    if n+2 in ins:
        total += nextJolts(n+2)
    if n+3 in ins:
        total += nextJolts(n+3)
    if total == 0:
        total = 1;
    insRes[str(n)] = total
    return total

print(nextJolts(0))

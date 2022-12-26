l = open("2.txt").read().split("\n")

score = 0
for n in l:
    s = n.split(" ")
    #print(s)
    if s[1] == "X":
        score += 1
        if s[0] == "A":
            score += 3
        if s[0] == "C":
            score += 6
    if s[1] == "Y":
        score += 2
        if s[0] == "A":
            score += 6
        if s[0] == "B":
            score += 3
    if s[1] == "Z":
        score += 3
        if s[0] == "C":
            score += 3
        if s[0] == "B":
            score += 6
print(score)
        

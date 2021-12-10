f = open("10.txt")
l = f.read().split("\n")
starts = "([{<"
ends = ")]}>"

scores = [3,57,1197,25137]
total = 0
good = []
for line in l:
    saved = ""
    #print(line)
    for char in line:
        if char in starts:
            i = starts.index(char)
            saved += ends[i]
            
        elif char in ends:
            i = ends.index(char)
            if saved[-1] != ends[i]:
                total += scores[i]
                #print(ends[i])
                break
            else:
                saved = saved[:-1]
        else:
            print("bad")
    else:
        good.append(saved)

values = ["",")","]","}",">"]
scores = []
for end in good:
    score = 0
    for char in end[::-1]:
        score *= 5
        score += values.index(char)
    scores.append(score)

import statistics
print(statistics.median(scores))

print(total)

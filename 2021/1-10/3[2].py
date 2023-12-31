l = open("3.txt").read().split("\n")

def firstCount(l,index):
    c = [0,0]

    for j in range(len(l)):
        c[int(l[j][index])] += 1
    return c

most = l.copy()
least = l.copy()

index = 0
while len(most) > 1:
    print(most)
    print(index)
    counts = firstCount(most,index)
    if counts[0] > counts[1]:
        most = [i for i in most if i[index] == "0" ]
    else:
        most = [i for i in most if i[index] == "1"]
    index+=1

index = 0
while len(least) > 1:
    print(least)
    print(index)
    counts = firstCount(least,index)
    print(counts)
    if counts[1] < counts[0]:
        least = [i for i in least if i[index] == "1"]
        print("1")
    else:
        least = [i for i in least if i[index] == "0"]
    index += 1

print(most)
print(least)
print(int(least[0],2) * int(most[0],2))

#ans>3407535

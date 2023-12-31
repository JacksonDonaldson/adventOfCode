ins = []
while True:
    i = input()
    if i == "-1":
        break
    i.split(" ")
    ins.append(i);

valid = 0
for i in ins:
    mi = i[0:i.index("-")]
    ma= i[i.index("-")+1:i.index(" ")]
    mi = int(mi)
    ma = int(ma)
    letter = i[i.index(" ") + 1: i.index(" ") + 2]
    total = 0
    for j in range(i.index(" ") + 3, len(i)):
        if i[j] == letter:
            total +=1
    if mi<=total<=ma:
        valid +=1
print(valid)

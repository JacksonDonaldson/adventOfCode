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
    pw = i[i.index(" ") + 4:]
    #print(pw)
    #print(mi)
    #print(ma)
    #print(pw[mi-1])
    #print(pw[ma-1])
    if pw[mi-1] == letter and pw[ma-1] != letter:

        #print("valid")
        valid +=1
    if pw[mi-1] != letter and pw[ma-1] == letter:
        valid+=1
    
print(valid)

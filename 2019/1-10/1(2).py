ints = []
while True:
    i = int(input())
    if i == -1:
        break
    ints.append(i);
total = 0
for i in ints:
    while(i>8):
        total += int(i/3)-2
        i = int(i/3)-2
    
print(total)

subject = 7
big = 20201227
def findSize(n):
    test = 1
    i = 0
    while test != n:
        i+=1
        test *= subject
        test = test % big
    return i

n1 = 14205034
n2 = 18047856

n1 = findSize(n1)

subject = n2
final = 1
for i in range(0, n1):
    final *= subject
    final = final%big

print(final)


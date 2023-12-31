f = open("1.txt").read()

i = f.split("\n")
total = 0

for line in i:
    #print(line)

    for i in range(len(line)):
        if line[i] in "1234567890":
            first = line[i]
            break
        for b, a in enumerate(["092348qwureoaisfhdkjzn", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
            if line[i:].startswith(a):
                first = str(b)
                break
        else:
            continue
        break

    for i in range(len(line))[::-1]:
        if line[i] in "1234567890":
            last = line[i]
            break
        for b, a in enumerate(["092348qwureoaisfhdkjzn", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
            if line[i:].startswith(a):
                last = str(b)
                break
        else:
            continue
        break
    #print(first, last)
    total += int(first + last)

print(total)
#54550 > ans > 54462

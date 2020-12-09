x = open("4in.txt")
x = x.read()
current = ""
passports = []
passport = {}
i=0
thing = ""
while i < len(x):
    if x[i] == "\n" and x[i+1] == "\n":
        passport[thing] = current
        current = ""
        passports.append(passport.copy())
        passport = {}
        i+=2
        continue
    if x[i] == "\n":
        passport[thing] = current
        current = ""
        i+=1
        continue
    if x[i] == ":":
        thing = current
        i+=1
        current = ""
        continue
    if x[i] == " ":
        passport[thing] = current
        i+=1
        current = ""
        continue
    current += x[i]
    i+=1
passports.pop(-1)
valids = 0
def c(pp, key):
    if key not in pp:
        return False
    d = pp[key]
    if key == "byr":
        return 1920<= int(d) <=2002
    if key == "iyr":
        return 2010 <= int(d) <=2020
    if key == "eyr":
        return 2020<= int(d) <= 2030
    if key == "hgt":
        print("a")
        if d[-2:] == "cm":
            return 150<=int(d[:-2])<=193
        elif d[-2:] == "in":
            return 59<=int(d[:-2])<=76

    if key == "hcl":
        if len(d) != 7:
            return False
        for i in range(1,7):
            if d[i] not in "abcdef0123456789":
                return False
        return d[0] == "#"
    if key == "ecl":
        return d == "amb" or d=="blu" or d=="brn" or d=="gry" or d=="grn" or d== "hzl" or d== "oth"
    if key == "pid":
        try:
            int(d)
            return len(d) == 9
        except:
            return False
    print(key)

for pp in passports:
    if c(pp,"ecl") and c(pp,"pid") and c(pp,"eyr") and c(pp,"hcl") and c(pp,"byr") and c(pp,"iyr") and c(pp,"hgt"):
        valids+=1

print(valids)

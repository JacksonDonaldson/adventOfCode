d=h=a=0
l = [i.split(" ") for i in open("2.txt").read().split("\n")]
for z in l:
    h,d,a = [h + int(z[0] == "forward") * int(z[1]), d +int(z[0] == "forward") * a * int(z[1]),  a + (int(z[0] != "forward")) * (2*int(z[0] == "down")-1) * int(z[1])]
print(d*h)

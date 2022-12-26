import jcksn as j
l = open("21.txt").read().split("\n")

monks = dict()

for line in l:
    v = line.split(" ")
    res = []
    if len(v) == 2:
        res = int(v[1])
    else:
        res = [v[1], v[2], v[3]]
        
    monks[v[0][:-1]] = res

monks["root"] = ['ztbt', '==', 'jzqh']
def ev(name):
    m = monks[name]
    if type(m) == int:
        return m
    n1 = str(ev(m[0]))
    n2 = str(ev(m[2]))
    if(name == "root"):
        return n1
    return eval(n1 + m[1] + n2)

i = 1
monks["humn"] = i

desired = 32310041242752

while float(ev("root")) > desired:
    i*=2
    monks["humn"] = i

start = i / 2
end = i

while(ev("root") != desired):
    
    val = (start + end) // 2
    monks["humn"] = int(val)
    e= float(ev("root"))
    if e > desired:
        start = val + 1
    elif e < desired:
        end = val - 1
    else:
        print("done!")
        print(val)
print(i)




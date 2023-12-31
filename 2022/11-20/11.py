class Monkey():
    def __init__(self, items, func, test, m1, m2):
        self.items = items
        self.func = func
        self.test = test
        self.m1 = m1
        self.m2 = m2
        self.total = 0
        self.other = 0
    def set(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    def turn(self):
        self.other += len(self.items)
        for i in range(len(self.items)):
            #print(self.items)
            
            self.total += 1
            j = self.items[0]
            self.items = self.items[1:]

            j = self.func(j)
            j = j % 9699690
            #print(j)
            if self.test(j):
                self.m1.add(j)
            else:
                self.m2.add(j)
    def add(self, e):
        #print("adding")
        self.items.append(e)
        #print(self.items)

m0 = Monkey([54,89,94], lambda x: x * 7, lambda x: x % 17 == 0, 0, 0)
m1 = Monkey([66,71], lambda x: x + 4, lambda x: x % 3 == 0, 0, 0)
m2 = Monkey([76, 55, 80, 55, 55, 96, 78], lambda x: x + 2, lambda x: x % 5 == 0, 0, 0)
m3 = Monkey([93, 69, 76, 66, 89, 54, 59, 94], lambda x: x + 7, lambda x: x % 7 == 0, 0, 0)
m4 = Monkey([80, 54, 58, 75, 99], lambda x: x * 17, lambda x: x % 11 == 0, 0, 0)
m5 = Monkey([69, 70, 85, 83], lambda x: x + 8, lambda x: x % 19 == 0, 0, 0)
m6 = Monkey([89], lambda x: x + 6, lambda x: x % 2 == 0, 0, 0)
m7 = Monkey([62, 80, 58, 57, 93, 56], lambda x: x * x, lambda x: x % 13 == 0, 0, 0)


m0.set(m5,m3)
m1.set(m0,m3)
m2.set(m7,m4)
m3.set(m5,m2)
m4.set(m1,m6)
m5.set(m2,m7)
m6.set(m0,m1)
m7.set(m6,m4)


#m0 = Monkey([79,98], lambda x: x * 19, lambda x: x % 23 == 0, 0, 0)
#m1 = Monkey([54, 65, 75, 74], lambda x: x + 6, lambda x: x % 19 == 0, 0, 0)
#m2 = Monkey([79, 60, 97], lambda x: x * x, lambda x: x % 13 == 0, 0, 0)
#m3 = Monkey([74], lambda x: x + 3, lambda x: x % 17 == 0, 0, 0)

for i in range(10000):
    m0.turn()
    m1.turn()
    m2.turn()
    m3.turn()
    m4.turn()
    m5.turn()
    m6.turn()
    m7.turn()

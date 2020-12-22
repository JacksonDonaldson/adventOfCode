name = {
'departure location': '29-917 or 943-952',
'departure station': '50-875 or 884-954',
'departure platform': '41-493 or 503-949',
'departure track': '50-867 or 875-966',
'departure date': '30-655 or 679-956',
'departure time': '46-147 or 153-958',
'arrival location': '50-329 or 344-968',
'arrival station': '42-614 or 623-949',
'arrival platform': '35-849 or 860-973',
'arrival track': '42-202 or 214-959',
'class': '38-317 or 329-968',
'duration': '44-530 or 539-953',
'price': '28-713 or 727-957',
'route': '30-157 or 179-966',
'row': '38-114 or 136-969',
'seat': '45-441 or 465-956',
'train': '44-799 or 824-951',
'type': '41-411 or 437-953',
'wagon': '39-79 or 86-969',
'zone':"48-306 or 317-974"}
for n in name:
    o = name[n]
    n1 = int(o[:o.index("-")])
    n2 = int(o[o.index("-") + 1:o.index(" ")])
    o = o[o.index("r"):]
    n3 = int(o[o.index("r") + 2: o[o.index("r"):].index("-")])
    n4 = int(o[o[o.index("r"):].index("-")+1:])
    print([n1,n2,n3,n4])
    name[n] = [[n1,n2],[n3,n4]]

    
nearby = open("16in.txt").read()
tickets = []
num = ''
ticket = []
for n in nearby:
    if n == "\n":
        ticket.append(int(num))
        tickets.append(ticket.copy())
        ticket = []
        num = ""
        continue
    elif n == ",":
        ticket.append(int(num))
        num = ""
        continue
    else:
        num +=n
ticket.append(int(num))
tickets.append(ticket)
def between(l,n):
    return n>= l[0] and n<=l[1]
def valid(n):
    for field in name:
        for options in name[field]:
            if between(options, n):
                return True
    return False
invalidTotal= 0
isValid = []
for ticket in tickets:
    validTicket = True
    for value in ticket:
        if not valid(value):
            validTicket = False
    isValid.append(validTicket)
checkedTickets = []
for i in range(0,len(isValid)):
    if(isValid[i]):
        checkedTickets.append(tickets[i])

possible = []
j = []
for n in name:
    j.append(n)
for i in range(0,len(tickets[0])):
    possible.append(j.copy())
print(possible)
def fieldValid(field,n):
    for options in name[field]:
        if between(options,n):
            return True
    return False
                        
#for each ticket, go through each value
#At that i value, check the list of possible remaining fields it could be
#if it would not be valid for that field,
#remove that field from the list of possible fields for that i value
for ticket in checkedTickets:
    for i in range(0,len(ticket)):
        toRemove = []
        for p in possible[i]:
            if not fieldValid(p,ticket[i]):
                #that is no longer a possible field for this part of the ticket
                toRemove.append(p)
        #print(toRemove)
        #print(ticket[i])
        for r in toRemove:
            
            possible[i].remove(r)
        
#now, look for ones with only 1 possibility left, and remove that from evert;hing else
#if that leaves 1 left, add that toRemove and restart
i = 0
done = [0] * len(possible)
toRemove = []

while i < len(possible):
    for r in toRemove:
        try:
            possible[i].remove(r)
        except:
            pass
    if len(possible[i]) == 1:
        done[i] = possible[i].copy()
        toRemove.append(possible[i][0])
        possible[i] = []
        i = 0
        continue
    i+=1

myTicket = [191,89,73,139,71,103,109,53,97,179,59,67,79,101,113,157,61,107,181,137]
m = myTicket
print(m[1]*m[2]*m[5]*m[11]*m[15]*m[19])













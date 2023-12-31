##lines = []
##while True:
##    x = input()
##    if x == "-1":
##        break
##    lines.append(x)
##formula = {}
##for line in lines:
##    line = line.split(" ")
##    x = [line[-2]]
##    for i in range(0,len(line)-3):
##        if i % 2 == 1:
##            continue
##        if line[i+1][-1] == ",":
##            line[i+1] = line[i+1][:-1]
##        x.append([line[i],line[i+1]])
##    print(x)
##    print(str(line[-1]))
##    formula[str(line[-1])] = x
##    #above used to get this
formula = {'NMDF': ['2', ['1', 'BNZK']], 'GSRWZ': ['4', ['3', 'KPQPD']], 'SRGL': ['7', ['2', 'ZRSFC']], 'HMTC': ['7', ['5', 'XNPDM'], ['1', 'FGCV']], 'CDKF': ['9', ['18', 'LHTNC'], ['1', 'WGXGV']], 'FKHRJ': ['5', ['24', 'BMQM']], 'XNSVC': ['6', ['2', 'LFPNB']], 'TXDQK': ['7', ['9', 'ZKFRH'], ['4', 'XGPLN'], ['17', 'SPQP'], ['2', 'GVNTZ'], ['1', 'JMSCN'], ['9', 'SHQN'], ['1', 'DZLWC'], ['18', 'MSKQ']], 'JPZT': ['9', ['2', 'QFTW']], 'GQRB': ['7', ['1', 'KJCK'], ['1', 'TFKZ'], ['2', 'XNSVC']], 'KJCK': ['7', ['16', 'JPZT'], ['3', 'DCPW']], 'RNXJ': ['7', ['24', 'LGKPJ'], ['11', 'CDKF'], ['2', 'HVZQM']], 'ZKFRH': ['7', ['1', 'NMDF'], ['16', 'DBLGK'], ['1', 'HVZQM']], 'FUEL': ['1', ['4', 'TXDQK'], ['55', 'TNZT'], ['39', 'KDTG'], ['6', 'NVBH'], ['15', 'SDVMB'], ['53', 'XVKHV'], ['28', 'FKHRJ']], 'NVBH': ['1', ['3', 'CDKV'], ['11', 'FGCV']], 'XMCNV': ['9', ['3', 'SPNRW'], ['7', 'JMSCN']], 'PQVBV': ['6', ['14', 'FGCV'], ['3', 'CQLRM'], ['1', 'TFKZ']], 'DSKH': ['7', ['5', 'KJCK'], ['10', 'DCPW']], 'DZLWC': ['5', ['5', 'NMDF'], ['1', 'TFKZ']], 'RTSBT': ['6', ['1', 'TNZT']], 'XVLBX': ['6', ['178', 'ORE']], 'CWKH': ['5', ['1', 'SPNRW']], 'SPNRW': ['3', ['15', 'ZRSFC'], ['2', 'PQVBV'], ['2', 'SRGL']], 'QWMZQ': ['4', ['1', 'SHQN'], ['7', 'XNSVC']], 'BNZK': ['4', ['5', 'NVBH'], ['41', 'SHQN']], 'TNZT': ['4', ['1', 'CDKV'], ['6', 'KJCK']], 'KDTG': ['9', ['5', 'ZTBG'], ['1', 'HVZQM'], ['27', 'CDKV'], ['1', 'LHTNC'], ['2', 'RTSBT'], ['2', 'SHQN'], ['26', 'DZLWC']], 'SHQN': ['7', ['11', 'CDKV']], 'GVNTZ': ['7', ['13', 'QWMZQ'], ['19', 'FCFG']], 'ZRSFC': ['9', ['1', 'SHQN'], ['4', 'XNSVC']], 'SDVMB': ['8', ['2', 'ZKFRH'], ['9', 'HVZQM'], ['1', 'KJCK'], ['3', 'GQRB'], ['11', 'DBLGK'], ['8', 'DZLWC'], ['2', 'SPQP'], ['5', 'RNXJ']], 'JMSCN': ['7', ['5', 'SPNRW']], 'XNPDM': ['7', ['2', 'XVLBX'], ['19', 'KPQPD']], 'CDKV': ['8', ['2', 'JPZT']], 'MSKQ': ['7', ['1', 'GQRB']], 'MHQVS': ['3', ['1', 'SHQN'], ['13', 'DSKH']], 'LFPNB': ['8', ['9', 'JPZT']], 'SPQP': ['9', ['15', 'SPNRW'], ['4', 'GQRB']], 'TFKZ': ['3', ['1', 'JPZT']], 'FGCV': ['6', ['1', 'BMQM']], 'DCPW': ['9', ['24', 'FKHRJ']], 'XGPLN': ['8', ['2', 'GSRWZ']], 'BMQM': ['6', ['5', 'QPSDR'], ['1', 'XVLBX']], 'QPSDR': ['7', ['128', 'ORE']], 'ZTBG': ['7', ['2', 'LHTNC'], ['6', 'FCFG'], ['5', 'GVNTZ']], 'KRDGK': ['6', ['9', 'KJCK'], ['6', 'MHQVS'], ['5', 'NVBH']], 'FCFG': ['2', ['3', 'HMTC'], ['4', 'QWMZQ']], 'LGKPJ': ['1', ['4', 'WGXGV'], ['5', 'PQVBV']], 'CQLRM': ['5', ['42', 'XVLBX']], 'DBLGK': ['9', ['1', 'CWKH']], 'LHTNC': ['5', ['1', 'KRDGK'], ['2', 'GQRB'], ['12', 'TFKZ']], 'WGXGV': ['8', ['1', 'CQLRM'], ['1', 'HMTC']], 'QFTW': ['1', ['116', 'ORE']], 'XVKHV': ['5', ['13', 'XMCNV']], 'HVZQM': ['9', ['12', 'LGKPJ'], ['8', 'FKHRJ']], 'KPQPD': ['6', ['5', 'QPSDR']]}
    
extra = {}
oreCount = 0
def getOre(chemical):
    global oreCount
    needed = formula[chemical].copy()
    amount = int(needed.pop(0))
    #print(needed)
    for reactant in needed:
        reactantChemical = reactant[1]
        amountRequired = int(reactant[0])
        if reactantChemical == "ORE":
            oreCount += amountRequired
        else:
            try:
                recieved = extra[reactantChemical]
            except:
                recieved = 0
            while recieved < amountRequired:
                recieved += getOre(reactantChemical)
            extra[reactantChemical] = recieved - amountRequired
    return amount

def findCycle(cycle):
    for i in range(1,int(len(cycle)/2)+1):
        #check if cycle[0:i] repeats throughout the entire cycle
        prospective = cycle[0:i]
        isMatch = True
        for j in range(0,int(len(cycle)/i)):
            point = j * i;
            #print("checking from " + str(point) + " to " + str(point + i))
            if prospective != cycle[point:point+i]:
                #It's not a match
                isMatch = False
                break
        if isMatch:
            return i

run = 0
extracycle = {}

#detect cyles of each thing
for extr in extra:
    extracycle[extr] = [0]
for extr in extra:
    extracycle[extr].append(extra[extr])
print(extracycle)
i = 0
while oreCount < 1000000000000:
    getOre("FUEL")
    i+=1
    if(i%10000 == 0):
        print(i)
print("answer: " , end = "")
print(i - 1)
#found raw cycle data- now we have to find cyclic length


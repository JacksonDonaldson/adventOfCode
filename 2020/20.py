def getIn():
    t = input()
    ins = []
    while t != "done":
        ins.append(t)
        t = input()

    d = {}
    while len(ins) > 0:
        id = ins[0][5:9]
        board = []
        for i in range(1,11):
            board.append(list(ins[i]))
        ins = ins[12:]
        d[id] = board
        #print(board)
        
    return d    



def getEdges(board):
    #takes a 10x10 board and returns a list of outermost rows and collumns
    edges = [board[0], board[9]]
    foo = []
    foob = []
    for i in range(0,10):
        foo.append(board[i][0])
        foob.append(board[i][9])
    edges.append(foo.copy())
    edges.append(foob.copy())
    return edges
def findSimilar(d, row):
    #searches for items in d that have an outer row matching row
    matches = []
    for key in d.keys():
        thing = d[key]
        edges = getEdges(d[key])
        if row in edges:
            matches.append(key)
            continue
        r = row.copy()
        r.reverse()
        if r in edges:
            matches.append(key)
            continue
    return matches


d = getIn()


for key in d.keys():
    total = 0
    for edge in getEdges(d[key]):
        
        #print(findSimilar(d, edge))
        if len(findSimilar(d, edge)) == 1:
            total += 1
    if total > 1:   
        print(total)
        print(key)
        

#now we have the key of one of the boards. Expand from there
up = findSimilar(d, d[key][0])

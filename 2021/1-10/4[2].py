f=open("4.txt")
moves = f.readline().split(",")
moves[-1] = "28"
#moves = [int(i) for i in moves]
f.readline()
x = f.read()
x= x.replace("  ", " ")
boards = x.split("\n\n")

boards = [f.split("\n") for f in boards]
for i in range(len(boards)):
    boards[i] = [f.split(" ") for f in boards[i]]

for i in range(len(boards)):
    for j in range(len(boards[i])):
        boards[i][j] = [k for k in boards[i][j] if k != ""]
print(boards)

def doSum(board):
    total = 0
    for r in board:
        for c in r:
            if c != "X":
                total += int(c)
    print(total)
    
def checkWin():
    mode = False
    if sum([1 for b in boards if b[0][0] == "d"]) == len(boards) - 1:
        mode = True
    for board in boards:
        if board[0][0] == "d":
            continue
        for row in board:
            for l in row:
                if l != "X":
                    break
            else:
                #win found
                if(mode):
                    doSum(board)
                    return True
                board[0][0] = "d"
        for i in range(5):
            for j in range(5):
                if board[j][i] != "X":
                    break
            else:
                if(mode):
                    doSum(board)
                    return True
                board[0][0] = "d"
for move in moves:
    print(move)
    for i in range(len(boards)):
        #print(boards[i])
        for j in range(len(boards[i])):
            for k in range(len(boards[i][j])):
                if boards[i][j][k] == move:
                    boards[i][j][k] = "X"
                    
        #print(boards[i])

    if checkWin():
        print(move)
        break

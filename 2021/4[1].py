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
    for board in boards:
        for row in board:
            for l in row:
                if l != "X":
                    break
            else:
                #win found
                doSum(board)
                return True
        for i in range(5):
            for j in range(5):
                if board[j][i] != "X":
                    break
            else:
                doSum(board)
                return True
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

board = [' ' for x in range(10)]

def insertletter(letter,pos):
    board[pos]=letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printboard(board):
    print("   |   |   ")
    print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
    print("   |   |   ")

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def winner(board,letter):
    return ((board[1] == letter and board[2] == letter and board[3] == letter) or (board[4] == letter and board[5] == letter and board[6] == letter) or (board[7] == letter and board[8] == letter and board[9] == letter) or (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter) or (board[3] == letter and board[6] == letter and board[9] == letter) or (board[1] == letter and board[5] == letter and board[9] == letter) or (board[3] == letter and board[5] == letter and board[7] == letter))

def playerMove():
    run =True
    while run:
        move = input("Enter Position(1-9) : ")
        try:
            move = int(move)
            if move > 0 and move<10:
                if spaceIsFree(move):
                    run = False
                    insertletter('X',move)
                else:
                    print("Already Occupied")
            else:
                print("Invalid !!!")
        except:
            print("Number Only !!!")

def selectRandom(list):
    import random 
    ln = len(list)
    r = random.randrange(0,ln)
    return list[r]


def aiMove():
    possiblMoves = [x for x,letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0;
    for let in ['O','X']:
        for i in possiblMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if winner(boardcopy,let):
                move = i
                return move

    cornerOpen = []
    for i in possiblMoves:
        if i in [1,3,7,9]:
            cornerOpen.append(i)

    if len(cornerOpen) > 0:
        move = selectRandom(cornerOpen)
        return move
    
    if 5 in possiblMoves:
        move = 5
        return move

    edgeOpen = []
    for i in possiblMoves:
        if i in [2,4,6,8]:
            edgeOpen.append(i)
    
    if len(edgeOpen) > 0:
        move = selectRandom(edgeOpen)
        return move
    
    
def main():
    print("Welcome !!!")
    printboard(board)
    while not(isBoardFull(board)):
        if not(winner(board,'O')):
            playerMove()
            printboard(board)
        else:
            print("You Lost !!!")
            break
        if not(winner(board,'X')):
            move = aiMove()
            if move == 0:
                print(" ")
            else:
                insertletter('O',move)
                print("Computer places on position : ",move)
                printboard(board)
        else: 
            print("You Win !!!")
            break
            


    if(isBoardFull(board)):
        print("Tie Game")

while True:
    x = input("Do you want play ?(y/n) : ")
    if x.lower() == "y":
       board = [' ' for x in range(10)]
       print("------------------------------------")
       main()
    else:
        break
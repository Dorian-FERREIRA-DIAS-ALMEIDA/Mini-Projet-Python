import copy

def NewBoard(n,m):
    board = [[0] * m for a in range(n)]
    return board

def displayBoard(board, n, m):
    for i in range(n):
        if 0<=i<9:
            print(i + 1, ' |', end='')
        else:
            print(i + 1, '|', end='')
        for j in range(m):
            if board[i][j]==0:
                print('.',end='')
            elif board[i][j]==1:
                print('X',end='')
            else:
                print('O',end='')
        print('')
    print('   ','━'*m)
    print('    ',end='')
    for i in range(m):
        print(chr(i+65),end='')

#displayBoard(NewBoard(13,15),13,15)

def possibleSquare(board,n,m, i, j):
    if i>n or j>m:
        return False
    elif board[i-1][j-1]==0:
        return True
    return False

#print(possibleSquare(NewBoard(13,15),13,15,1,1))


def selectSquare(board,n,m):
    i=int(input('\n Veuillez entrer la première coordonnées:'))
    j=int(input('\n Veuillez entrer la seconde coordonnées:'))
    while not possibleSquare(board,n,m,i,j):
        i = int(input("\nVeuillez entrer la première coordonnées:"))
        j = int(input("\n Veuillez entrer la seconde coordonnées:"))
    return i,j

#print(selectSquare(NewBoard(13,15),13,15))

def updateBoard(board,n,m,player,i,j):
    if player==1:
        other=2
    else:
        other=1
    boardCopy = copy.deepcopy(board)
    for a in range(n):
        for b in range(m):
            if board[a][b]==player:
                if a>0 and board[a-1][b]==0:
                    boardCopy[a-1][b]=player
                if a<n-1 and board[a+1][b]==0:
                    boardCopy[a+1][b]=player
                if b>0 and board[a][b-1]==0:
                    boardCopy[a][b-1]=player
                if b<m-1 and board[a][b+1]==0:
                    boardCopy[a][b+1]=player
            elif board[a][b]==other:
                if a>0 and boardCopy[a-1][b]==0:
                    boardCopy[a-1][b]=other
                if a<n-1 and boardCopy[a+1][b]==0:
                    boardCopy[a+1][b]=other
                if b>0 and boardCopy[a][b-1]==0:
                    boardCopy[a][b-1]=other
                if b<m - 1 and boardCopy[a][b+1]==0:
                    boardCopy[a][b+1] = other
    for a in range(n):
        for b in range(m):
            board[a][b]=boardCopy[a][b]
    board[i-1][j-1]=player
    displayBoard(board,n,m)

#updateBoard(NewBoard(13,15),13,15,1,13,15)

def again(board, n, m):
    for i in range(n):
        for j in range(m):
            if possibleSquare(board,n,m,i,j) == True:
                return True
    return False

#print(again(NewBoard(13,15),13,15))

def jackRabbits(n, m):
    board=NewBoard(n,m)
    turn=0
    displayBoard(board,n,m)
    while again(board,n,m)==True:
        turn+=1
        if turn%2==1:
            i,j=selectSquare(board,n,m)
            updateBoard(board,n,m,1,i,j)
        else:
            i,j=selectSquare(board,n,m)
            updateBoard(board,n,m,2,i,j)
    if turn%2==1:
        print("\n Le joueur 1 a perdu")
    else:
        print("\n Le joueur 2 a perdu")

jackRabbits(4,5)
def NewBoard(n):
    while n%2!=0:
        n=int(input("Veuillez choisir une taille conforme (un nombre pair):"))
    board = [[0] * n for a in range(n)]
    return board
#print(NewBoard(5))

def displayBoard(board):
    n=len(board)
    for i in range(n):
        if 0<=i<9:
            print(i + 1, ' |', end='')
        else:
            print(i + 1, '|', end='')
        for j in range(n):
            if board[i][j]==0:
                print('.',end='')
            elif board[i][j]==1:
                print('X',end='')
            else:
                print('O',end='')
        print('')
    print('   ','━'*n)
    print('    ',end='')
    for i in range(n):
        print(i+1,end='')

#displayBoard(NewBoard(12))

def possible(board, i, j):
    n = len(board)
    if i>n or j>n or i<1 or j<1:
        return False
    elif board[i-1][j-1]==0:
        return True
    return False
#print(possible(NewBoard(12),2,3))

def selectSquare(board):
    i=int(input('\n Veuillez entrer la première coordonnées:'))
    j=int(input('\n Veuillez entrer la seconde coordonnées:'))
    while not possible(board,i,j):
        i = int(input("\nVeuillez entrer la première coordonnées:"))
        j = int(input("\n Veuillez entrer la seconde coordonnées:"))
    return i,j

def attract_pions(board,i,j):
    n = len(board)
    for a in range(j-1,-1,-1):
        if board[i][a]!=0 and board[i][a+1]==0:
            board[i][a],board[i][a+1]=0,board[i][a]
    for a in range(j+1,n):
        if board[i][a]!=0 and board[i][a-1]==0:
            board[i][a],board[i][a-1]=0,board[i][a]
    for a in range(i-1,-1,-1):
        if board[a][j]!=0 and board[a+1][j]==0:
            board[a][j],board[a+1][j]=0,board[a][j]
    for a in range(i+1,n):
        if board[a][j]!=0 and board[a-1][j]==0:
            board[a][j],board[a-1][j]=0,board[a][j]
    return board

def updateBoard(board,player,i,j):
    n = len(board)
    board[i-1][j-1]=player
    attract_pions(board,i-1,j-1)
    displayBoard(board)

def again(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j]==0:
                return True
    return False

def Attract(n):
    board=NewBoard(n)
    displayBoard(board)
    turn=0
    player1,player2,still_possible=0,0,0
    while again(board,n)==True:
        turn+=1
        if turn%2==1:
            i,j=selectSquare(board)
            updateBoard(board,1,i,j)
        else:
            i,j=selectSquare(board)
            updateBoard(board,2,i,j)
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if board[i][j] == 2 and board[i + 1][j + 1] == 1 and board[i + 1][j - 1] == 1 and board[i - 1][
                j + 1] == 1 and board[i - 1][j - 1] == 1:
                player1 += 1
            elif board[i][j] == 1 and board[i + 1][j + 1] == 2 and board[i + 1][j - 1] == 2 and board[i - 1][
                j + 1] == 2 and board[i - 1][j - 1] == 2:
                player1 += 1
    if player1 > player2:
        print("\n Le Joueur 2 a gagné!")
    elif player1 < player2:
        print("\n Le Joueur 1 a gagné!")
    else:
        print("\n Match nul!")

Attract(4)

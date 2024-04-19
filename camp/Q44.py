import numpy as np

def is_board_full(board):
    return not any(' ' in row for row in board)
def check_winner(board,player):
    for row in board:
        if all(cell==player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col]==player for row in range (3)):
            return True
    if all(board[i][i]==player for i in range(3)) and all(board[i][2-i]==player for i in range(3)):
        return True
    return False
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('----------')
def evaluate_board(board):
    if check_winner(board,'X'):
        return 1
    elif check_winner(board,'O'):
        return -1
    else:
        return 0
def minimax(board,depth,is_maximising):
    if check_winner(board,'X'):
        return 1
    elif check_winner(board,'O'):
        return -1
    elif is_board_full(board):
        return 0
    
    if is_maximising:
        max_eval=float('-inf')
        for i in range(3):
            for j in range (3):
                if board[i][j]==' ':
                    board[i][j]='O'
                    eval=minimax(board,depth+1,False)
                    board[i][j]=' '
                    max_eval=max(max_eval,eval)
        return max_eval
    else:
        min_eval=float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j]==' ':
                    board[i][j]='X'
                    eval=minimax(board,depth+1,True)
                    board[i][j]=' '
                    min_eval=min(min_eval,eval)
        return min_eval

def find_best_move(board):
    best_eval=float('-inf')
    best_move=None
    for i in range(3):
            for j in range (3):
                if board[i][j]==' ':
                    board[i][j]='O'
                    eval=minimax(board,0,False)
                    board[i][j]=' '
                    if eval>best_eval:
                        best_eval=eval
                        best_move=(i,j)
    return best_move

def play_ttt():
    board=[[' ' for _ in range(3)] for _ in range (3)]
    print('Welcome!')
    print_board(board)
    while not is_board_full(board) and not check_winner(board,'X') and not check_winner(board,'O'):
        #players turn
        row,col=map(int,input("enter with space:").split())
        if board[row][col]==' ':
            board[row][col]='O'
            print_board(board)
        else:
            print('invalid')
            continue
        if check_winner(board,'O'):
            print("u win!")
            return
        elif is_board_full(board):
            print("Draw!")
            return
        
        #comp turn
        print('computer turn')
        bm=find_best_move(board)
        board[bm[0]][bm[1]]='X'
        print_board(board)
        if check_winner(board,'X'):
            print("comp wins!")
            return
        elif is_board_full(board):
            print("Draw!")
            return
play_ttt()
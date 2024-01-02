import random

borad = [[1,2,3,],[4,5,6],[7,8,9]]

def print_all(board):

    for i in range(3):
        print('|',end='')
        for j in range(3):
            print(board[i][j],'|',sep='',end='')
        print('')

occupied = []
def enter_way(board,place):
    global occupied
    for i in range(3):
        for j in range(3):
            if board[i][j] == place:
                occupied.append(board[i][j] )
                board[i][j] = 'O'

    random_number = random.randint(1,9)
    while random_number in occupied:
        random_number = random.randint(1, 9)
    for i in range(3):
        for j in range(3):
            if board[i][j] == random_number:
                occupied.append(board[i][j])
                board[i][j] = 'X'


pl_win = False
comp_win = False

def chek_who_win(borad):
    global pl_win
    global comp_win
    for j in range(3):
        if borad[0][j] == borad[1][j] and borad[1][j] == borad[2][j]:
            if borad[1][j] == 'X':
                 comp_win = True
            else:
                pl_win = True

    for i in range(3):
        if borad[i][0] == borad[i][1] and borad[i][1] == borad[i][2]:
            if borad[i][1] == 'X':
                comp_win = True
            else:
                pl_win = True

    if borad[0][0] == borad[1][1] and borad[1][1] ==  borad[2][2]:
        if borad[0][0] == 'X':
            comp_win = True
        else:
            pl_win = True

    if borad[0][2] == borad[1][1] and borad[1][1] == borad[2][0]:
        if borad[0][2] == 'X':
            comp_win = True
        else:
            pl_win = True


print_all(borad)

while not pl_win or not comp_win:
    place = int(input('enter way: '))
    if len(occupied) == 8:
        print('GAME DRAW')
        break
    enter_way(borad,place)
    chek_who_win(borad)
    print_all(borad)

    if pl_win:
        print('PLAYER WIN')
        break
    elif comp_win:
        print('COMPUTER WIN')
        break
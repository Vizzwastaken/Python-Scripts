import random

board = {'top-R': ' ','top-M': ' ','top-L': ' ','mid-R': ' ','mid-M': ' ','mid-L': ' ','low-R': ' ','low-M': ' ','low-L': ' '}

player = input("select your symbol : ")

if player == 'x':
    comp = 'o'
else:
    comp = 'x'

def printboard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print("------")
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print("------")
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def check_win(board):
    if   board['low-L'] == board['low-M'] == board['low-R'] != ' ' :
        return True
    elif board['top-L'] == board['top-M'] == board['top-R'] != ' ' :
        return True
    elif board['mid-L'] == board['mid-M'] == board['mid-R'] != ' ' :
        return True
    elif board['low-L'] == board['mid-M'] == board['top-R'] != ' ' :
        return True
    elif board['top-L'] == board['mid-M'] == board['low-R'] != ' ' :
        return True
    elif board['top-R'] == board['mid-R'] == board['low-R'] != ' ' :
        return True
    elif board['top-M'] == board['mid-M'] == board['low-M'] != ' ' :
        return True
    elif board['top-L'] == board['mid-L'] == board['low-L'] != ' ' :
        return True
    else:    
        return False
    
def player_move(symbol):
    val = input("enter your postion : ")
    board[val] = symbol
    printboard(board)
    res = check_win(board)
    if res == True:
        print("player wins")
        exit()
    
def computer_move(comp):
    empty_positions = [key for key, value in board.items() if value == ' ']
    computer_val = random.choice(empty_positions)
    board[computer_val] = comp
    print("Computer's move:")
    printboard(board)
    cres = check_win(board)
    if cres == True:
        print("computer wins")
        exit()

while True:
    if player_move(player):
        exit()
    if computer_move(comp):
        exit()

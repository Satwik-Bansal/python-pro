board=["-","-","-","-","-","-","-","-","-"]

game_active = True
winner = None
current = "X"
player1=""
player2=""


def display_board():
    print(" | ", board[0], " | ", board[1], " | ", board[2], " | ")
    print(" | ", board[3], " | ", board[4], " | ", board[5], " | ")
    print(" | ", board[6], " | ", board[7], " | ", board[8], " | ")

def play_game():

    print("Welcome to Tic Tac Toe...")
    print("Please enter your names : ")
    get_players()

    display_board()

    while game_active:

        handle_turn(current)

        check_game_over()

        change_player()


    if (winner=="X"):
        print("Winner : ", player1)
    elif(winner=="O"):
        print("Winner : ", player2)
    elif winner==None:
        print("Tie")



def handle_turn(current):
    valid=False

    position = input("Enter position from 1-9 : ")

    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9",]:
                position = input("Invalid inuput. Enter valid position from 1-9 : ")

        position = int(position)-1

        if board[position]=="-":
                valid=True


        else:
                print("Position already taken enter an empty space ")

    board[position] = current
    display_board()

def check_game_over():
    
    check_win()

    check_tie()



def check_win():

    global winner

    row_winner=check_rows()

    column_winner=check_columns()

    diagonal_winner=check_diagonals()

    if row_winner:
            winner=row_winner

    elif column_winner:
            winner=column_winner

    elif diagonal_winner:
            winner=diagonal_winner

    else:
            winner=None

    return

def check_rows():

    global game_active

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_active=False

    if row_1:
        return board[0]

    elif row_2:
        return board[3]

    elif row_3:
        return  board[6]

    return

def check_columns():
    global game_active

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_active = False

    if column_1:
        return board[0]

    elif column_2:
        return board[1]

    elif column_3:
        return board[2]

    return

def check_diagonals():
    global game_active

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2 :
        game_active = False

    if diagonal_1:
        return board[0]

    elif diagonal_2:
        return board[2]

    return


def check_tie():
    global game_active

    if "-" not in board:
        game_active=False
    
    return


def change_player():
    global current

    if current=="X":
        current="O"

    elif current=="O":
        current="X"
    return

def get_players():
    global player1,player2
    player1=input("Enter name of player 1 : ")
    player2=input("Enter name of player 2 : ")
    print(player1," is X")
    print(player2," is O")


play_game()
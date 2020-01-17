#board

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

#display board

game_still_going = True 
winner = None
current_player = "X"


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#play game
display_board()

def play_game():

         
    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()
      

#The game has ended
             
#handle turn

def handle_turn(player):
    print(player +  " 's turn! \n")
    position = input("Choose a position from 1 to 9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1 to 9: ")

        position = int(position) - 1
        
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there! Go again. \n")
   
    board[position] = player
    display_board()

#flip player

def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


#check if game is over

def check_if_game_over():
    check_if_win()
    check_if_tie()

    global game_still_going
    if  game_still_going == False:

        if winner == "X" or winner == "O":
            print(winner + " won!")
            print('''
                               
 \ \        / (_)                      
  \ \  /\  / / _ _ __  _ __   ___ _ __ 
   \ \/  \/ / | | '_ \| '_ \ / _ \ '__|
    \  /\  /  | | | | | | | |  __/ |   
     \/  \/   |_|_| |_|_| |_|\___|_|   
                                      
       ''' )

        elif winner == None:
            print(" \n It's a tie!")

        print('Do you want to play again?')
        answer = input("yes/no: \n")
        if answer == "yes":
            game_still_going = True
            for i in range(len(board)):
                board[i] = '-'
            display_board()
            play_game()

#check win

def check_if_win():
    
    global winner
  #check rows
    row_winner = check_rows()

  #check columns
    column_winner = check_columns()

  #check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner

    elif column_winner:
        winner = column_winner

    elif  diagonal_winner:
        winner = diagonal_winner

    else:
        winner = None       
  
def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None
    
def check_columns():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

    else:
        return None
    

def check_diagonals():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    else:
        return None

#check if tie

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
        return True
    else:
        return False

play_game()




















  


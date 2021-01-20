#Open Source
#Decode By Virgo Gans
#Subscribe Virgo Gans

from time import sleep
from os import system

# Reset
Color_Off="\033[0m"       # Text Reset

# Regular Colors
Black="\033[0;30m"        # Black
Red="\033[0;31m"          # Red
Green="\033[0;32m"        # Green
Yellow="\033[0;33m"       # Yellow
Blue="\033[0;34m"         # Blue
Purple="\033[0;35m"       # Purple
Cyan="\033[0;36m"         # Cyan
White="\033[0;37m"        # White

# Background
On_Black="\033[40m"       # Black
On_Red="\033[41m"         # Red
On_Green="\033[42m"       # Green
On_Yellow="\033[43m"      # Yellow
On_Blue="\033[44m"        # Blue
On_Purple="\033[45m"      # Purple
On_Cyan="\033[46m"        # Cyan
On_White="\033[47m"       # White

# Bold
BBlack="\033[1;30m"       # Black
BRed="\033[1;31m"         # Red
BGreen="\033[1;32m"       # Green
BYellow="\033[1;33m"      # Yellow
BBlue="\033[1;34m"        # Blue
BPurple="\033[1;35m"      # Purple
BCyan="\033[1;36m"        # Cyan
BWhite="\033[1;37m"       # White

# Underline
UBlack="\033[4;30m"       # Black
URed="\033[4;31m"         # Red
UGreen="\033[4;32m"       # Green
UYellow="\033[4;33m"      # Yellow
UBlue="\033[4;34m"        # Blue
UPurple="\033[4;35m"      # Purple
UCyan="\033[4;36m"        # Cyan
UWhite="\033[4;37m"       # White



system('clear')

print(Red+"─╔╗───────")
print("╔╝╚╗──────")
print("╚╗╔╝╔╗╔══╗")
print("─║║─║║║╔═╝")
print("─║╚╗║║║╚═╗")
print("─╚═╝╚╝╚══╝\n")
sleep(1)
print(Green+"─╔╗─────────")
print("╔╝╚╗────────")
print("╚╗╔╝╔══╗╔══╗")
print("─║║─║╔╗║║╔═╝")
print("─║╚╗║╔╗║║╚═╗")
print("─╚═╝╚╝╚╝╚══╝\n")
sleep(1)
print(Cyan+"─╔╗─────────")
print("╔╝╚╗────────")
print("╚╗╔╝╔══╗╔══╗")
print("─║║─║╔╗║║║═╣")
print("─║╚╗║╚╝║║║═╣")
print("─╚═╝╚══╝╚══╝")
print(Black+"p")
sleep(2)
system('clear')

rounds = 0
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

system('clear')
def game_board():
    print(BRed+"           Decode By Virgo Gans ")
    print(BWhite+"           Youtube : Virgo Gans ")
    print()
    print(Blue+" -  |  -  | -  " + "           1 |  2  |  3")
    print("---------------" + "           ------------")
    print(" -  |  -  | -  " + "           4 |  5  |  6")
    print("---------------" + "           ------------")
    print(" -  |  -  | -  " + "           7 |  8  |  9")
    print()


def display_board():
    print(Cyan+"\n")
    print(board[0] + "  |  " + board[1] + "  |  " + board[2] + "           1 |  2  |  3")
    print("--------------" + "         --------------")
    print(board[3] + "  |  " + board[4] + "  |  " + board[5] + "           4 |  5  |  6")
    print("--------------" + "         --------------")
    print(board[6] + "  |  " + board[7] + "  |  " + board[8] + "           7 |  8  |  9")
    print("\n")


def player_var():
    global p1
    global p2
    p1 = input(Cyan+"Hey! player 1 you want to be x or o - ").upper()
    while p1 not in ["X", "O"]:
        print()
        p1 = input(Red+"Hey! player 1 you want to be x or o - ").upper()
        print()
    p2 = ""
    if p1 == "X":
        p2 = "O"
        print()
        print(Purple+"Player 1 X will go first")
        print()
    elif p1 == "O":
        p2 = "X"
        print()
        print(Purple+"Player 2 X will go first")
    


def player_turn():
    while (p1 == "X" and p2 == "O") or (p1 == "O" and p2 == "X"):
        global rounds
        rounds = rounds + 1
        pix = int(input(Purple+"Hey player x where you wanna enter - ")) - 1
        while pix not in [0, 1, 2, 3, 4, 5, 6, 7, 8] or board[pix] == "X" or board[pix] == "O":
            print()
            print()
            pix = int(input(Purple+"Hey player x where you wanna enter - ")) - 1
            print()
        if board[pix] == "-":
            board[pix] = "X"
            display_board()
        else:
            print()
            print("something is wrong")
        if board[0] == "X" and board[1] == "X" and board[2] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[3] == "X" and board[4] == "X" and board[5] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[6] == "X" and board[7] == "X" and board[8] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "O" and board[1] == "O" and board[2] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[3] == "O" and board[4] == "O" and board[5] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[6] == "O" and board[7] == "O" and board[8] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "X" and board[3] == "X" and board[6] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[1] == "X" and board[4] == "X" and board[7] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[2] == "X" and board[5] == "X" and board[8] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "O" and board[3] == "O" and board[6] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[1] == "O" and board[4] == "O" and board[7] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[2] == "O" and board[5] == "O" and board[8] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "X" and board[4] == "X" and board[8] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[2] == "X" and board[4] == "X" and board[6] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[2] == "O" and board[4] == "O" and board[6] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "O" and board[4] == "O" and board[8] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif rounds == 5 and (board[0] == "X" or "O" and board[1] == "X" or "O" and board[2] == "X" or "O" and board[
            3] == "X" or "O" and board[4] == "X" or "O" and board[5] == "X" or "O" and board[6] == "X" or "O" and board[
                                  7] == "X" or "O" and board[8] == "X" or "O"):
            print()
            print("THIS IS TIE")
            print()
            break

        pio = int(input(Yellow+"Hey player O where you wanna enter - ")) - 1
        while pio not in [0, 1, 2, 3, 4, 5, 6, 7, 8] or board[pio] == "X" or board[pio] == "O":
            print()
            print()
            pio = int(input(Yellow+"Hey player O where you wanna enter - ")) - 1
            print()
        if board[pio] == "-":
            board[pio] = "O"
            display_board()
        else:
            print()
            print("something is wrong")
        if board[0] == "X" and board[1] == "X" and board[2] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[3] == "X" and board[4] == "X" and board[5] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[6] == "X" and board[7] == "X" and board[8] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "O" and board[1] == "O" and board[2] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[3] == "O" and board[4] == "O" and board[5] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[6] == "O" and board[7] == "O" and board[8] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "X" and board[3] == "X" and board[6] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[1] == "X" and board[4] == "X" and board[7] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[2] == "X" and board[5] == "X" and board[8] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "O" and board[3] == "O" and board[6] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[1] == "O" and board[4] == "O" and board[7] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[2] == "O" and board[5] == "O" and board[8] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "X" and board[4] == "X" and board[8] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[2] == "X" and board[4] == "X" and board[6] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[2] == "O" and board[4] == "O" and board[6] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "O" and board[4] == "O" and board[8] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif rounds == 5 and (board[0] == "X" or "O" and board[1] == "X" or "O" and board[2] == "X" or "O" and board[
            3] == "X" or "O" and board[4] == "X" or "O" and board[5] == "X" or "O" and board[6] == "X" or "O" and board[
                                  7] == "X" or "O" and board[8] == "X" or "O"):
            print()
            print("THIS IS TIE")
            print()
            break


def game_play():
    game_board()
    player_var()
    player_turn()


game_play()


def replay():
    print()
    r = input("Do you want to play again (y/n) -  ").upper()
    print()
    while r not in ["Y", "N"]:
        print()
        r = input("Do you want to play again (y/n) -  ").upper()
        print()
    if r == "Y":
        global rounds
        global board
        rounds = 0
        board = ["-", "-", "-",
                 "-", "-", "-",
                 "-", "-", "-"]
        print()
        game_play()
        print()
        replay()
    elif r == "N":
        print()
        print("THANK YOU FOR PLAYING TIC TAC TOE!!!")
        print("\nSubscribe Virgo Gans")


replay()



















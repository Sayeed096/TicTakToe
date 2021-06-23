#!/usr/bin/python

import os

# Global declaration


# Clear the screen or terminal
def clear():
    os.system("cls")


# Get players input for Board location
def player_choice( px=0 ):
    ''' Get choice of player on Board location. '''

    while True:
        p_input = input(f"[Player_{px+1}] Enter the Board Location (1-9): ") #; print("1st", type(p_input) )
        if p_input.isdigit() == True:
            p_in = int(p_input)                                      #; print("2nd", type(p_in) )
            if p_in in range(1, 10):
                return p_in
            else:
                print("The inpute is out of range. Please try again...")
                continue
        else:
            print("The inpute is not a valid positive number. Please try again...")
            continue

    return -1


# Board map conver to index number
def board_map(location=0):
    ''' Convert Board location into index number of board tuple '''

    if   location == 0: return ([1, 2, 3], [4, 5, 6], [7, 8, 9])
    elif location == 1: i = 0; j = 0
    elif location == 2: i = 0; j = 1
    elif location == 3: i = 0; j = 2
    elif location == 4: i = 1; j = 0
    elif location == 5: i = 1; j = 1
    elif location == 6: i = 1; j = 2
    elif location == 7: i = 2; j = 0
    elif location == 8: i = 2; j = 1
    elif location == 9: i = 2; j = 2
    else:               i = 0; j = 0

    return (i, j)


# update the board 
def update_board(b, l=0, symbol=''):
    ''' Update the board location with symbol'''

    i, j = board_map(l)
    b[i][j] = symbol

    return b


# Show the board
def show_board(b):
    ''' To show the board on terminal. '''
    # To clear the terminal

    # To show the board
    row_dt =  '--- --- ---'
    print(f" {b[2][0]} | {b[2][1]} | {b[2][2]} ")
    print(row_dt)
    print(f" {b[1][0]} | {b[1][1]} | {b[1][2]} ")
    print(row_dt)
    print(f" {b[0][0]} | {b[0][1]} | {b[0][2]} ")


# Check the board status and result
def check_board(b):
    ''' Check the board status and return result. '''

    # Column
    c1 = [i[0] for i in b]
    c2 = [i[1] for i in b]
    c3 = [i[2] for i in b]
    # Diagonal
    d1 = [b[0][0], b[1][1], b[2][2]]
    d2 = [b[0][2], b[1][1], b[2][0]]

    def _win(px=''):
        # Check in row by count {px}
        if   b[0].count(px) == 3 or b[1].count(px) == 3 or b[2].count(px) == 3: res = True
        elif c1.count(px) == 3 or c2.count(px) == 3 or c3.count(px) == 3: res = True
        elif d1.count(px) ==3 or d2.count(px) == 3: res = True
        else: res = False

        return res


    if   _win('x'): print("Congratulaton! Player x win the game"); return True
    elif _win('o'): print("Congratulaton! Player o win the game"); return True
    else: print("Continue the game..."); return False


# Exit from the game
def exit_game():
    print("Bye Bye!!!")
    exit()


# Main game loop
def game_loop(board, symbols=('x', 'O')):
    """ Main game loop for playing the game and check the result. """
    turn = 0

    def _show(b, syms):

        clear()
        print("Board map: ")
        show_board(board_map(0))
        print (f"Player 1 = {syms[0]}, Player 2 = {syms[1]}"); print()
        show_board(b)

    def _play(player=0, board=board):

        # Ask Player1's choice of Board
        p_iloc = player_choice(player)

        # Update Board and clear screen and then show updated Board
        board = update_board(board, p_iloc, symbols[player])

    while(turn < 10):
        
        _show(board, symbols)
        
        # Get player input and update board
        _play(turn%2, board)
        _show(board, symbols)

        # Check Board status and show result or next play
        if check_board(board):
            break
        else: turn += 1

    return 0


# main function declaration
def main(*args, **kwargs):
    """ Main function for enter the game (program). """

    game_en = True
    # Show Initial Information
    
    while(game_en):
        """ Start and restart game loop. """
        # Initialize the board and clear screen
        brd = ([' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '])  #; print("Init:",  brd )
        clear()

        # User input for set Player1 symbol "x|O"
        p1_sym = input("Enter player1 symbol (x|o): ")
        p2_sym = 'o' if p1_sym == 'x' else 'x'

        # Show players' symbol and location of choice
        # show_board(board_map(0))
        # print(f"Player1 = {p1_sym} and Player2 = {p2_sym}")

        # User input for start game
        start_game = input("Star the game (Y|N):").lower()

        # Enter Game loop for play and check result
        if start_game == 'y':
            # Show Initial blank board
            # show_board(brd)
            game_loop(brd,(p1_sym, p2_sym))
        else: exit_game()

        # User input for restart the game or exit
        re_st = input("Enter 'r' to restart the game: ").lower()
        game_en = True if re_st == 'r' else False

    # Show exit information
    exit_game()


# Call the main function
if __name__ == '__main__':
    main()


# Comment section 
    # print( player_choice(1) )
    # brd = ([' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '])  ; print("Init:",  brd )
    # update_board(brd, 3, 'x')                         ; print( brd )
    # update_board(brd, 7, 'O')                         ; print( brd )
    # brd[1][0] = 'X';  show_board(brd)
    # brd[1][0] = 'o'; brd[1][1] = 'o'; brd[1][2] = 'o'; print( brd)
    # check_board(brd)

'''
    # Count 'x|o' in rows
    if   b[0].count('x') == 3 and b[1].count('x') == 3 or b[3].count('x') == 3: print("Congratulaton Player 1!")
    elif b[0].count('o') == 3 and b[1].count('o') == 3 or b[3].count('o') == 3: print("Congratulaton Player 2!")
    else: pass
    # Count 'x|o' in colums
    c1 = [i[0] for i in b]
    c2 = [i[1] for i in b]
    c3 = [i[2] for i in b]
    if   c1.count('x') == 3 or c2.count('x') == 3 or c3.count('x') == 3: print("Congratulaton Player 1!")
    elif c1.count('o') == 3 or c2.count('o') == 3 or c3.count('o') == 3: print("Congratulaton Player 2!")
    else: pass

    # Diagonal check 'x|o' 
    d1 = [b[0][0], b[1][1], b[2][2]]
    d2 = [b[0][2], b[1][1], b[2][0]]
    if  d1.count('x') ==3 or d2.count('x') == 3: print("Congratulaton Player 1!")
    elif  d1.count('o') ==3 or d2.count('o') == 3: print("Congratulaton Player 2!")
    else: pass
'''
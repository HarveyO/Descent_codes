# Battleship Game credit to codecademy
'''
The Battleship game is created for a single player to play on a classic board.
The player is engaged in the game with an endpoint to sink the ship if only the
player guesses the number correctly. To make it quite interesting, the player is
limited to a number of guesses to sink the ship (in this case, 3 guesses).
'''

# import random library
from random import randint

# create an empty list
board = []

# the loop sets elements as a 5X5 grid on the board
for x in range(0, 5):
    board.append(["O"] * 5)


def print_board(board):
    '''
    This function simply displays the setting of the board
    '''

    # a loop to form the grid with spaces
    for row in board:
        print(" ".join(row))


# displays the board
print_board(board)


def random_row(board):
    '''
    This function returns a random number that represents the rows
    on the board
    '''
    return randint(0, len(board) - 1)


def random_col(board):
    '''
    This function returns a random number that represents the columns
    on the board
    '''
    return randint(0, len(board[0]) - 1)


# assign the chosen row position to an object
ship_row = random_row(board)

# assign the chosen column position to an object
ship_col = random_col(board)

# empty list to keep the positions guessed
positions = []

# a loop for the number of guesses the player has.
for turn in range(3):

    print(f"Turn {turn + 1}")

    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    keep = (guess_row, guess_col)

    if (guess_row < 0) and (guess_col < 0):
        print("You have to enter only positive integers!")
    else:

        # first condition that the player guesses the number right
        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sank my battleship!")
            print(ship_row)
            print(ship_col)
            break

        else:
            # second condition that the player guesses out of range
            if guess_row not in range(5) or guess_col not in range(5):
                print("Oops, that's not even in the ocean.")

            # third condition that the player has guessed that number (position) before.
            elif board[guess_row][guess_col] == "X":
                print("You guessed that one already.")

            else:
                # fourth condition that the player's guess is incorrect, thereby replacing the position with an X
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X"

            # store positions of guesses by the player
            positions.append(keep)

            # this condition checks that the player has reached the maximum number of guess
            if (turn == 2):
                print("Game Over! The correct guess should be: ")
                print(ship_row)
                print(ship_col)

    # display the board with all the trials
    print_board(board)

    # display the positions the player has guessed
    print(positions)

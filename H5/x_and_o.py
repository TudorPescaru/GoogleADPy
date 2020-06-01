#!/usr/bin/env python3

def display_board():
    """
    Print the board at the current state
    Args: None
    Return: None
    """

    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])


def check_win(b, m):
    """
    Check to see if win condition is met for given mark
    Args: m = type of mark to be checked (X or O) - str
    Return: bool
    """

    return ((b[0] == m and b[1] == m and b[2] == m) or
            (b[3] == m and b[4] == m and b[5] == m) or
            (b[6] == m and b[7] == m and b[8] == m) or
            (b[0] == m and b[3] == m and b[6] == m) or
            (b[1] == m and b[4] == m and b[7] == m) or
            (b[2] == m and b[5] == m and b[8] == m) or
            (b[0] == m and b[4] == m and b[8] == m) or
            (b[2] == m and b[4] == m and b[6] == m))


def check_draw():
    """
    Check to see if draw condition is met
    Args: None
    Return bool
    """

    return ' ' not in board


def test_move(m, i):
    """
    Test if a move results in a win
    Args: m = type of mark (X or O) - str
          i = position on the boar - int
    Return: bool
    """

    test_board = board.copy()
    test_board[i] = m
    return check_win(test_board, m)


def computer_move(player, computer):
    """
    Guidelines to determine computer movement
    Args: player = mark used by the player - str
          computer = mark used by the computer - str
    """

    # Check to see if move for win exists
    # First check if you can win then check is you can counter player win
    for mark in [computer, player]:
        for i in range(9):
            if board[i] == ' ' and test_move(mark, i):
                board[i] = computer
                return

    # Prioritize center position
    if board[4] == ' ':
        board[4] = computer
        return

    # Find first available corner if middle is marked
    for i in [0, 2, 6, 8]:
        if board[i] == ' ':
            board[i] = computer
            return

    # Find first available edge if middle and corners are marked
    for i in [1, 3, 5, 7]:
        if board[i] == ' ':
            board[i] = computer
            return


def play_game():
    """
    Function that runs the game itself
    Args: None
    Returns: None
    """

    # Initialise board
    global board
    board = [' '] * 9
    winner = False

    # Get first person to play (X goes first)
    start = input("Go first or second?(1/2): ")
    if start == '2':
        player = 'O'
        computer = 'X'
    else:
        player = 'X'
        computer = 'O'

    # Display initial state
    print("You are " + player)
    display_board()
    if player == 'X':
        turn = player
    else:
        turn = computer
    print("X goes first")

    # Run game
    while winner is False:
        print(turn + "'s turn")

        # Get player input
        if turn == player:
            valid = False
            # Ask for input until valid postion is given
            while valid is False:
                try:
                    move = int(input("Input a position to mark (1-9): "))
                    if board[move - 1] != ' ':
                        print("Invalid position")
                    else:
                        valid = True
                        board[move - 1] = turn
                except:
                    print("Invalid position")
        else: # Computer makes move
            computer_move(player, computer)

        # Check if move led to a win
        if check_win(board, turn):
            winner = True
            display_board()
            print(turn + " won! Congratulations!")
            continue

        # Check if move led to a draw
        if check_draw():
            winner = True
            display_board()
            print("It's a draw!")
            continue

        display_board()

        # Switch player for next turn
        if turn == player:
            turn = computer
        else:
            turn = player


def main():
    """
    Main function for the program. Runs game and checks for replay request.
    Args: None
    Returns: None
    """

    play = True
    while play:
        play_game()
        # Check if player wants to play again
        again = input("Play again?(y/n): ")
        if again == 'n':
            play = False


if __name__ == "__main__":
    main()

# Tic Tac Toe

import random


class Board:
    def __init__(self, board):
        self.board = board

    def drawBoard(self):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('     |     |     ')
        print('  ' + self.board[7] + '  |  ' + self.board[8] + '  |  ' + self.board[9] + '  ')
        print('_____|_____|_____')
        print('     |     |     ')
        print('  ' + self.board[4] + '  |  ' + self.board[5] + '  |  ' + self.board[6] + '  ')
        print('_____|_____|_____')
        print('     |     |     ')
        print('  ' + self.board[1] + '  |  ' + self.board[2] + '  |  ' + self.board[3] + '  ')
        print('     |     |     ')

    def makeMove(self, letter, move):
        self.board[move] = letter

    def isBoardFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if isSpaceFree(self.board, i):
                return False
        return True

    def isWinner(self, le):
        bo = self.board
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
                (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
                (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
                (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
                (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
                (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
                (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
                (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with player 1's letter as the first item, and player 2's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        answer = input()
        if answer.lower() == 'x':
            letter = 'X'
        elif answer.lower() == 'o':
            letter = 'O'
        else:
            print('Please pick X or O.')

    # the first element in the tuple is player 1's letter, the second is player 2's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'O'
    else:
        return 'X'


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '


def getXMove(board):
    # Let player X type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is X\'s next move? (1-9)')
        move = input()
    return int(move)


def getOMove(board):
    # Let player O type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What O\'s next move? (1-9)')
        move = input()
    return int(move)


print('Welcome to Tic Tac Toe!')
print('''
     |     |     
  7  |  8  |  9  
_____|_____|_____
     |     |     
  4  |  5  |  6  
_____|_____|_____
     |     |     
  1  |  2  |  3  
     |     |     
''')
print('This is how the Tic-Tac-Toe board will look.')
print('When it is your turn, type the corresponding number of the square you want to place your letter in.\n')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1Letter, player2Letter = inputPlayerLetter()
    turn = whoGoesFirst()
    print(turn + ' will go first.')
    gameIsPlaying = True
    board = Board(theBoard)

    while gameIsPlaying:
        if turn == 'X':
            # Player X's turn.
            board.drawBoard()
            move = getXMove(theBoard)
            board.makeMove(player1Letter, move)

            if board.isWinner(player1Letter):
                board.drawBoard()
                print('Hooray! Player 1 has won the game!')
                gameIsPlaying = False
            else:
                if board.isBoardFull():
                    board.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'O'

        else:
            # Player O's turn.
            board.drawBoard()
            move = getOMove(theBoard)
            board.makeMove(player2Letter, move)

            if board.isWinner(player2Letter):
                board.drawBoard()
                print('Hooray! Player 2 has won the game!')
                gameIsPlaying = False
            else:
                if board.isBoardFull():
                    board.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'X'

    if not playAgain():
        break

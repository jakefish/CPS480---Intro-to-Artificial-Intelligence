import random

"""

A game class designed for a tic-tac-toe


Attributes:

    board:             An array with a size of 10, used to store player and computer moves
                       and display the board to the player

    difficulty_level:  Takes an integer and changes the AI difficulty_level
                       based on the number the game is instantiated with (0, 1, or 2)

    player_letter:     Stores the player's letter (X or O)

    computer_letter:     Stores the computer's letter (X or O)

Functions:
    - create_board(): prints out the current state of the game board
    - choose_player_letter(): Takes input from the user to determine which letter
                              the computer and user will play as
    - determine_who_plays_first(): Determines if the computer or player will start first
    - make_a_move(): utility function used to make a move on the board
    - check_for_winner(): Returns true if a letter, X or O has 3 in a row
    - check_empty_board_space(): Utility function used to check for empty board positions
    - get_player_move(): Takes user input and marks their input on the board
    - get_computer_move(): The computer AI, makes a move based on the difficulty_level
    - make_a_random_move(): Function for AI to make a random move
    - check_if_board_is_full(): Checks for empty positions and returns true if there are none


"""


class Game:

    def __init__(self, difficulty_level):
        self.board = ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?']
        self.difficulty_level = difficulty_level
        self.player_letter = ''
        self.computer_letter = ''

    def create_board(self):
        print '\n'
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print '\n'

    def choose_player_letter(self):
        self.player_letter = raw_input('Which you like to play as X or O?')
        self.player_letter = self.player_letter.upper()
        if self.player_letter == 'X':
            self.computer_letter = 'O'
        else:
            self.computer_letter = 'X'

    def determine_who_plays_first(self):
        random_player = ['Computer', 'Player']
        return random_player[random.randint(0, 1)]

    def make_a_move(self, letter, move):
        self.board[move] = letter

    def check_for_winner(self, letter):
        if self.board[7] == letter and self.board[8] == letter and self.board[9] == letter:
            winner = True
        elif self.board[4] == letter and self.board[5] == letter and self.board[6] == letter:
            winner = True
        elif self.board[1] == letter and self.board[2] == letter and self.board[3] == letter:
            winner = True
        elif self.board[7] == letter and self.board[4] == letter and self.board[1] == letter:
            winner = True
        elif self.board[8] == letter and self.board[5] == letter and self.board[2] == letter:
            winner = True
        elif self.board[9] == letter and self.board[6] == letter and self.board[3] == letter:
            winner = True
        elif self.board[7] == letter and self.board[5] == letter and self.board[3] == letter:
            winner = True
        elif self.board[3] == letter and self.board[6] == letter and self.board[9] == letter:
            winner = True
        elif self.board[1] == letter and self.board[5] == letter and self.board[9] == letter:
            winner = True
        else:
            winner = False
        return winner

    def check_empty_board_space(self, move):
        if self.board[move] == '?':
            return True

    def get_player_move(self):
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.check_empty_board_space(int(move)):
            print('What is your next move? (1-9)')
            move = raw_input()
        return int(move)

    def get_computer_move(self, computer_letter):

        #-AI-Level-0
        if self.difficulty_level is 0:
            finding_valid_move = True
            while finding_valid_move:
                computer_move = random.randint(1,9)
                print computer_move
                if self.check_empty_board_space(computer_move):
                    return computer_move
            return computer_move

        #-AI-Level-1
        elif self.difficulty_level is 1:
            for position in range(1, 10):
                if self.check_empty_board_space(position):
                    self.make_a_move(computer_letter, position)
                    if self.check_for_winner(computer_letter):
                        return position
                    self.make_a_move('?', position)
            return self.level_zero(computer_letter)

        #-AI-Level-2
        else:

            for position in range(1, 10):
                if self.check_empty_board_space(position):
                    self.make_a_move(computer_letter, position)
                    if self.check_for_winner(computer_letter):
                        return position
                    self.make_a_move('?', position)

            for position in range(1, 10):
                if self.check_empty_board_space(position):
                    self.make_a_move(self.player_letter, position)
                    if self.check_for_winner(self.player_letter):
                        return position
                    self.make_a_move('?', position)

            for position in range(1, 10):
                if self.check_empty_board_space(position):
                    self.make_a_move(computer_letter, position)
                    if self.check_for_winner(computer_letter):
                        for position in range(1, 10):
                            if self.check_empty_board_space(position):
                                self.make_a_move(computer_letter, position)
                                if self.check_for_winner(computer_letter):
                                    return position
                                self.make_a_move('?', position)
                        return position
                    self.make_a_move('?', position)

            return self.make_a_random_move(computer_letter)


    def make_a_random_move(self, computer_level):
        finding_valid_move = True
        while finding_valid_move:
            computer_move = random.randint(1,10)
            if self.check_empty_board_space(computer_move):
                finding_valid_move = False
        return computer_move

    def check_if_board_is_full(self):
        for position in range(1, 10):
            if self.check_empty_board_space(position):
                return False
        return True

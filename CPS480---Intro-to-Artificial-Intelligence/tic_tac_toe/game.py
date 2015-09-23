import random



class Game:

    def __init__(self, difficulty_level):
        self.board = [' '] * 10
        self.fake_board = [' '] * 10
        self.difficulty_level = difficulty_level
        self.player_letter = ''

    def draw_board(self):
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')

    def choose_player_letter(self):
        player_letter = raw_input('Which you like to play as X or O?')
        player_letter = player_letter.upper()
        if player_letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

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
        if self.board[move] == ' ':
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
                print 'Position'
                print position
                if self.check_empty_board_space(position):
                    self.make_a_move(computer_letter, position)
                    if self.check_for_winner(computer_letter):
                        return position
                    self.make_a_move(' ', position)
            return self.level_zero(computer_letter)

        #-AI-Level-2
        else:

            for position in range(1, 10):
                if self.check_empty_board_space(position):
                    self.make_a_move(computer_letter, position)
                    if self.check_for_winner(computer_letter):
                        return position
                    self.make_a_move(' ', position)

            for position in range(1, 10):
                if self.check_empty_board_space(position):
                    self.make_a_move(self.player_letter, position)
                    if self.check_for_winner(self.player_letter):
                        return position
                    self.make_a_move(' ', position)


            return self.level_zero(computer_letter)


    def level_zero(self, computer_level):
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

class Game:

    def __init__(self):
        self.board = [' '] * 10

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
        print player_letter

        if player_letter is 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def determine_who_plays_first(self):
        import random
        random_player = ['computer', 'player']
        return random_player[random.randint(0, 1)]

    def make_a_move(board, letter, move):
        self.board[move] = letter

    def check_for_winner(self, letter):
        if self.board[7] == letter and self.board[8] == letter and self.board[9] == letter
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
        elif self.board[9] == letter and self.board[5] == letter and self.board[3] == letter:
            winner = True
        else:
            winner = False
        return winner







board = [' '] * 10

game = Game()

game.draw_board()
game.choose_player_letter()
print game.determine_who_plays_first()

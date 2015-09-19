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
        if player_letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def determine_who_plays_first(self):
        import random
        random_player = ['Player', 'Player']
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
        elif self.board[9] == letter and self.board[5] == letter and self.board[3] == letter:
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





game = Game()
player_letters = game.choose_player_letter()
print player_letters
player_letter = player_letters[0]
print player_letter
computer_letter = player_letters[1]
first_player = game.determine_who_plays_first()
print "{0} will make the first move".format(first_player)


game_playing = True
while game_playing:
    if first_player is 'Player':

        player_move = game.get_player_move()
        game.make_a_move(player_letter, player_move)
        game.draw_board()

        if game.check_for_winner(player_letter):
            print "Congratulations you won!"
            game_playing = False



    else:
        break

from game import Game



game = Game(2)
player_letters = game.choose_player_letter()
game.player_letter = player_letters[0]
player_letter = player_letters[0]
computer_letter = player_letters[1]
player_turn = game.determine_who_plays_first()
print "{0} will make the first move".format(player_turn)
game_playing = True
count = 2

while game_playing:

    if count % 2 == 0:

        player_move = game.get_player_move()
        game.make_a_move(player_letter, player_move)
        print " "
        game.draw_board()
        if game.check_for_winner(player_letter):
            game.draw_board()
            print "Congratulations you won!"
            game_playing = False
        else:
            if game.check_if_board_is_full():
                print "You have tied the game."
                game_playing = False
            else:
                count = count + 1

    else:
        computer_move = game.get_computer_move(computer_letter)
        game.make_a_move(computer_letter, computer_move)
        game.draw_board()
        if game.check_for_winner(computer_letter):
            game.draw_board()
            print('You just lost to a computer...')
            game_playing = False

        else:
            if game.check_if_board_is_full():
                game.draw_board()
                print "You have tied the game."
                game_playing = False
            else:
                count = count + 1

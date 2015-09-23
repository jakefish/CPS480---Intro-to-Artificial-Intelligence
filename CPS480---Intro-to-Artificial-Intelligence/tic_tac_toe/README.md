
Github:
https://github.com/jakefish/CPS480---Intro-to-Artificial-Intelligence.git

To build/run:

 In the terminal under the tic_tac_toe directory execute the following:
  ``` python start_game.py ```

AI implementation:

   Each level of AI is based of the difficulty_level that is instantiated with
   the game (0, 1, or >2).  


   AI-Level-0
   For level zero the AI keeps making random moves, while checking if the random
   move is valid, and plays the first valid random move it finds.  Since level zero
   is used in the other levels of AI this has it's own function called make_a_random_move().

   AI-Level-1
   In this level, the AI looks at all of the possible valid positions it can play
   and actually plays these moves, while checking if each move is a winner.  If the
   AI comes across a winning move it returns that position and then makes the move,
   otherwise it will replace the "moves" it made with a "?" to match the rest of the
   board and call make_a_random_move().

   AI-Level-2
   This level is similar to the last one, except after looking for a winning move,
   it blocks the player or sets itself up for a win.  If there is no winning move the
   AI will play the player's letter instead of it's own in all of the valid moves
   and check if that move wins for the player, and if it does it returns that position
   and places its piece there.  If there is no block or winning move available, the
   computer looks two moves ahead(by literally playing two moves), and finds a winning
   path and then plays the last position in that path to set itself up for a win.
   And of course like the rest, if none of this is possible it plays a random move.

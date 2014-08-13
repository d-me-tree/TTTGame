"""
This module implements the Machine Player logic based on Monte Carlo simulation
and runs the Tic-Tac-Toe game.
"""

import TTTBoard as ttt
import random
import os

# Constants for Monte Carlo simulator
# Change as desired
NTRIALS = 50   # Number of trials to run
MCMATCH = 1.0  # Score for squares played by the machine player
MCOTHER = 1.0  # Score for squares played by the other player
    
# Functions that implement the Machine Player based on Monte Carlo simulation
def mc_trial(board, player):
    """
    (TTTBoard, const) -> None
    
    Monte Carlo trial
    The function modifies the board by playing a game, starting
    with the given player, by making random moves, alternating
    between players.
    """
    available_moves = board.get_empty_squares()
    random.shuffle(available_moves)
    while not board.check_win():
        next_move = available_moves.pop(0)
        board.move(next_move[0], next_move[1], player)
        player = ttt.switch_player(player)
    return

def mc_update_scores(scores, board, player):
    """
    (list of lists, TTTBoard, const) -> None
    
    The function scores the completed board and updates the
    scores grid.
    If game is drawn, then all squares receive a score of 0.
    If player wins, each square that matches the player gets +MCMATCH
    and each square that matches the other player gets -MCOTHER.
    Conversely, if player loses, each square that matches the player
    gets -MCMATCH and each square that matches the other player gets
    +MCOTHER.
    All empty squares get a score of 0.
    """
    winner = board.check_win()
    if winner == ttt.DRAW:
        return
    const = 1
    if winner != player:
        const = -1
    score_values = {ttt.EMPTY: 0, player: MCMATCH * const,
         ttt.switch_player(player): -MCOTHER * const}
    scores_dim = len(scores)
    for col in range(scores_dim):
        for row in range(scores_dim):
            scores[row][col] += score_values.get(board.square(row, col))
    return

def get_best_move(board, scores):
    """
    (TTTBoard, list of lists) -> (int, int)
    
    Given a current board and a grid of scores, out of all
    of the empty squares with the maximum score randomly return
    one of them as a (row, column) tuple.
    """
    available_moves = board.get_empty_squares()
    max_score = -10000
    candidate_squares = []
    for square in available_moves:
        square_score = scores[square[0]][square[1]]
        if square_score > max_score:
            max_score = square_score
            candidate_squares = [square]
        elif square_score == max_score:
            candidate_squares.append(square)
    random.shuffle(candidate_squares)
    if not candidate_squares:
        print "Error: no possible next move"
        return ()
    else:
        return candidate_squares.pop(0)
            
def mc_move(board, player, trials):
    """
    (TTTBoard, const, int) -> (int, int)
    
    Using Monte Carlo simulation return a move for the player
    in the form of a (row, column) tuple. 
    """
    scores = [[0 for dummy_col in range(board.get_dim())]
              for dummy_row in range(board.get_dim())]
    for dummy_trial in range(trials):
        temp_board = board.clone()
        mc_trial(temp_board, player)
        mc_update_scores(scores,
                         temp_board, player)
    return get_best_move(board, scores)


# Game helper function
def game_settings(reverse = False, dim = 3, user = ttt.PLAYERO):
	"""
	(bool, int, player) -> (bool, int, player_user, player_computer)
	
	Prints current game settings.
	Allows the user to update the settings and returns a tuple:
	reverse tic-tac-toe: True/False
	dimension of the game board: int
	what user chooses to play: O or X
	what computer will play based on what user chose: X or O.
	"""
	if reverse:
		game_type = "r"
	else:
		game_type = "t"
	if user == ttt.PLAYERO:
		computer = ttt.PLAYERX
		user_plays = "O"
	else:
		user_plays = "X"
	print "Tic-Tac-Toe Game Settings\n" + "-" * 25
	print "In reverse game you lose if you get three-in-a-row.\n"
	print "[r]everse or [t]raditional:", game_type
	print "grid size:", dim
	print "X (starts the game) or O:", user_plays
	change_settings = raw_input("\nDo you want to change these settings? [y/n] ")
	if change_settings == "y":
		game_type = raw_input("\n[r]everse or [t]raditional: ")
		if game_type == "r":
			reverse = True
		dim = raw_input("grid size: ")
		user_plays = raw_input("You want to play X or O: ")
		if user_plays.capitalize() == "X":
			user = ttt.PLAYERX
			computer = ttt.PLAYERO
	return reverse, int(dim), user, computer

# Game logic
def play():
	players = {ttt.PLAYERX: "You play X\n", ttt.PLAYERO: "You play O\n"}
	
	reverse, dim, user, computer = game_settings()
	
	board = ttt.TTTBoard(dim, reverse)
	board.clear()
	
	while True:
		# first move
		os.system("clear")
		if user == ttt.PLAYERX:
			print players.get(user)
			print str(board)
			user_move = raw_input("\n\nWhat is your move?\nType in RowCol: ")
			board.move(int(user_move[0]), int(user_move[1]), user)
			os.system("clear")
			print players.get(user)
			print str(board)
			player_to_move = ttt.switch_player(user)
		else:
			computer_move = mc_move(board, computer, NTRIALS)
			board.move(computer_move[0], computer_move[1], computer)
			os.system("clear")
			print players.get(user)
			print str(board)
			player_to_move = ttt.switch_player(computer)
	
		game_end = None			
		while not game_end:
			if player_to_move == user:
				user_move = raw_input("\nYour move: ")
				# make sure that user makes a valid move
				while board.square(int(user_move[0]), int(user_move[1])) != ttt.EMPTY:
					user_move = raw_input("Wrong move! Try again: ")
				board.move(int(user_move[0]), int(user_move[1]), user)
			else:
				computer_move = mc_move(board, computer, NTRIALS)
				board.move(computer_move[0], computer_move[1], computer)
			os.system("clear")
			print players.get(user)
			print str(board)
			game_end = board.check_win()
			player_to_move = ttt.switch_player(player_to_move)
		
		messages = {ttt.PLAYERX: "X wins!", ttt.PLAYERO: "O wins!", ttt.DRAW: "It's a tie!"}
		print "\n%s" % messages.get(game_end)
		
		next_step = raw_input("\nHit Enter to play again\nCtrl + C to quit\ntype s to change settings: ")
		if next_step.lower() == "s":
			os.system("clear")
			reverse, dim, user, computer = game_settings()
			board = ttt.TTTBoard(dim, reverse)
		board.clear()
	

if __name__ == "__main__":
	print play()
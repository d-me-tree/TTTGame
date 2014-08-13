"""
TTTBoard class keeps track of the current state of the game board.
This module also contains switch_player helper function and some useful
constants.
"""

import copy

# Constants for Tic-Tac-Toe game
EMPTY = 1
PLAYERX = 2
PLAYERO = 3
DRAW = 4

# helper function
def switch_player(player):
	"""
	Return PLAYERX on input PLAYERO and
	PLAYERO on input PLAYERX.
	"""
	player_map = {PLAYERX: PLAYERO, PLAYERO: PLAYERX}
	return player_map.get(player)

class TTTBoard(object):
    """
    Class to represent a Tic-Tac-Toe board.
    """

    def __init__(self, dim = 3, reverse = False, board = None):
        """
        Initialize the TTTBoard object with the given dimension and 
        whether or not the game should be reversed.
        """
        self._dim = dim
        self._reverse = reverse
        self._board = board
            
    def __str__(self):
        """
        Human readable representation of the board.
        """
        const_2_str_map = {EMPTY: " ", PLAYERX: "X", PLAYERO: "O"}
        
        board_string = "   " + "   ".join(str(i) for i in range(self._dim)) + "\n\n"
        for row in range(self._dim):
        	board_string += "%d  %s |" % (row, const_2_str_map.get(self._board[row][0]))
        	for col in range(1, self._dim - 1):
        		board_string += " %s |" % const_2_str_map.get(self._board[row][col])
        	board_string += " %s" % const_2_str_map.get(self._board[row][-1])
        	if row != (self._dim - 1):
        		board_string += "\n   " + "-" * (4 * self._dim - 3) + "\n"
        return board_string
        

    def get_dim(self):
        """
        Return the dimension of the board.
        """
        return self._dim
    
    def square(self, row, col):
        """
        Returns one of the three constants EMPTY, PLAYERX, or PLAYERO 
        that correspond to the contents of the board at position (row, col).
        """
        return self._board[row][col]

    def get_empty_squares(self):
        """
        Return a list of (row, col) tuples for all empty squares.
        """
        list_of_empty_squares = []
        for row in range(self._dim):
        	for col in range(self._dim):
        		if self._board[row][col] == EMPTY:
        			list_of_empty_squares.append((row, col))
        return list_of_empty_squares

    def move(self, row, col, player):
        """
        Place player on the board at position (row, col).
        player should be either the constant PLAYERX or PLAYERO.
        Does nothing if board square is not empty.
        """
        if self._board[row][col] == EMPTY:
        	self._board[row][col] = player

    def check_win(self):
        """
        Returns a constant associated with the state of the game
            If PLAYERX wins, returns PLAYERX.
            If PLAYERO wins, returns PLAYERO.
            If game is drawn, returns DRAW.
            If game is in progress, returns None.
        """
        players = {PLAYERX:PLAYERX, PLAYERO:PLAYERO}
        if self._reverse:
        	players = {PLAYERX:PLAYERO, PLAYERO:PLAYERX}
        
        # check if there are any winning rows
        row_wins = 0
        for row in self._board:
        	if EMPTY not in row and len(set(row)) == 1:
        		row_wins += 1
        		if row_wins == 2:
        			return DRAW
        		else:
        			return players.get(row[0])
        
        # check if there are any winning columns
        col_wins = 0
        for num in range(self._dim):
        	col = [row[num] for row in self._board]
        	if EMPTY not in col and len(set(col)) == 1:
        		col_wins += 1
        		if col_wins == 2:
        			return DRAW
        		else:
        			return players.get(col[0])
        
        # winning diag?
        diag = [self._board[num][num] for num in range(self._dim)]
        if EMPTY not in diag and len(set(diag)) == 1:
        	return players.get(diag[0])
        
        # winning antidiag?
        antidiag = [self._board[num][self._dim - 1 - num] for num in range(self._dim)]
        if EMPTY not in antidiag and len(set(antidiag)) == 1:
        	return players.get(antidiag[0])
        
        if not self.get_empty_squares():
        	return DRAW
        return
            
    def clone(self):
        """
        Return a copy of the board.
        """
        return copy.deepcopy(self)
        
    def clear(self):
    	"""
    	Clears the board.
    	Returns None.
    	"""
    	self._board =[[EMPTY for dummy_col in range(self._dim)] for dummy_row in range(self._dim)]
    	return
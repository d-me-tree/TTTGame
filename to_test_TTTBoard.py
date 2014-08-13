"""
These are some of the tests that I used to check TTTBoard.py
This is a starting point to develop unit tests.
"""

board = TTTBoard(3, False, [[EMPTY, PLAYERX, EMPTY],
                            [PLAYERO, PLAYERX, EMPTY],
                            [PLAYERO, EMPTY, EMPTY]])
print board.get_dim()
print str(board)
print board.square(0, 1)
print board.get_empty_squares()
board.move(2, 1, PLAYERX)
print str(board)
print board.check_win()
board1 = TTTBoard(3, True, [[PLAYERX, PLAYERO, PLAYERO],
                            [PLAYERO, PLAYERX, PLAYERX],
                            [PLAYERO, PLAYERX, PLAYERX]])
print str(board1)
print board1.check_win()
board2 = TTTBoard(3, True, [[PLAYERX, PLAYERO, PLAYERX],
                            [PLAYERO, PLAYERX, PLAYERX],
                            [PLAYERO, PLAYERX, PLAYERO]])
print str(board2)
print board2.check_win()
board3 = TTTBoard(3, True, [[PLAYERO, PLAYERX, EMPTY],
                            [PLAYERO, PLAYERX, EMPTY],
                            [PLAYERO, EMPTY, EMPTY]])
print str(board3)
print board3.check_win()

print board._board is board.clone()
board.clear()
print str(board)
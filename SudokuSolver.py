from SudokuGame import *
from SudokuBoard import *
from SudokuUI import *

class SudokuSolver(object):
	'''
	For solving a valid sudoku board
	'''
	def __init__(self, UI):
		self.UI = UI
		self.game = UI.game



	def solve_sudoku(self):
		board = self.game.running_puzzle.board
		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j] == self.game.running_puzzle.SPACE_CHAR:
					for c in '123456789':
						if self.is_valid_move(i, j, c):
							self.game.user_move(i, j, c)
							if self.solve_sudoku():
								self.UI.draw_puzzle()
								return True
							else:
								self.game.user_move(i, j, self.game.running_puzzle.SPACE_CHAR)
								self.UI.draw_puzzle()
					return False
		return True 

	def is_valid_move(self, x, y, c):
		'''
		Checks if a specific move of solver is valid 
		according to rules of Sudoku (no same number in column, row, or block)
		'''
		board = self.game.running_puzzle.board 
		for i in range(9):
			if board[i][y] == c or board [x][i] == c:
				return False
			for i in range(3):
				for j in range(3):
					if board[(x//3) * 3 + i][y//3 * 3 + j] == c:
						return False
		return True 

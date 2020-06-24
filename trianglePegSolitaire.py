'''
Triangle Peg Solitaire
Not specifically a programming challenge, but I chose to use a program to try to find solutions.
https://redd.it/gawouk
'''

import random
from math import ceil, sqrt

ROUNDS = 10 ** 3
BOARD_DIMENSION = 4
CELL_COUNT = BOARD_DIMENSION * (BOARD_DIMENSION + 1) // 2

def main():
	scores = []
	for _ in range(ROUNDS):
		game = Game()
		while game.makeRandomMove():
			pass
		pieces = game.pieces()
		if pieces <= 1:
			scores.append(game.moves)
	# Combine double, triple, etc. moves into single tuples.
	for moves in scores:
		i = 0
		while i < len(moves) - 1:
			if moves[i][-1] == moves[i + 1][0]:
				moves[i] = (*moves[i], moves[i + 1][1], moves[i + 1][2])
				moves.pop(i + 1)
			else:
				i += 1
	scores.sort(key=len)
	cutoff = 3
	print(f'Best {cutoff} scores:')
	for moves in scores[:cutoff]:
		print(f'{len(moves)}: {moves}')

class Game():
	def __init__(self):
		self.board = [True] * CELL_COUNT
		# self.board[random.randrange(CELL_COUNT)] = False
		self.board[1] = False
		self.moves = []

	def makeRandomMove(self):
		moveOptions = []
		for from_ in range(CELL_COUNT):
			if self.board[from_]:
				for over, to in self.validMoves(from_):
					moveOptions.append((from_, over, to))
		if moveOptions:
			chosen = random.choice(moveOptions)
			self._move(*chosen)
			return chosen
		else:
			return False

	def _move(self, from_, over, to):
		self.board[from_] = False
		self.board[to] = True
		self.board[over] = False
		self.moves.append((from_, over, to))
	
	def validMoves(self, from_):
		# Quadratic formula for n^2 + n - 2x - 2, with floor() to zero-index it.
		rowIndex = ceil((-1 + sqrt(9 + 8 * from_)) / 2) - 1
		columnIndex = from_ - rowIndex * (rowIndex + 1) // 2
		# The values that are added to a cell's index to get the indexes of the cell jumped over and the cell moved to.
		possibleMoves = []
		if rowIndex - columnIndex > 1:
			# Up + right.
			possibleMoves.append((-rowIndex, -(rowIndex * 2 - 1)))
			# Right.
			possibleMoves.append((1, 2))
		# Down + right.
		possibleMoves.append((rowIndex + 2, rowIndex * 2 + 5))
		# Down + left.
		possibleMoves.append((rowIndex + 1, rowIndex * 2 + 3))
		if columnIndex > 1:
			# Left.
			possibleMoves.append((-1, -2))
			# Up + left.
			possibleMoves.append((-(rowIndex + 1), -(rowIndex * 2 + 1)))

		# Check that `over` and `to` are not out of the bounds of `board`, `over` is occupied, and `to` is not.
		validMoves = []
		for overOffset, toOffset in possibleMoves:
			over = from_ + overOffset
			to = from_ + toOffset
			try:
				if over >= 0 and self.board[over] and to >= 0 and not self.board[to]:
					validMoves.append((over, to))
			except IndexError:
				pass
		return validMoves

	def pieces(self):
		'''Return the number of pieces remaining in self.board.'''
		return sum(self.board)

if __name__ == '__main__':
	main()

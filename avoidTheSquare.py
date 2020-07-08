'''
My solution to the Avoid the Square problem by Matt Parker.
https://www.think-maths.co.uk/avoidthesquare
https://www.youtube.com/watch?v=FMQQFbZaQTk
'''

from random import randrange

ATTEMPTS = 10 ** 3
N = 5

def main():
	'''Create random boards and print those that happen to be solutions.'''
	solutions = set()
	for _ in range(ATTEMPTS):
		# Construct board.
		board = [[False for _ in range(N)] for _ in range(N)]
		for _ in range(N ** 2 // 2):
			row = randrange(N)
			column = randrange(N)
			while board[row][column]:
				row = randrange(N)
				column = randrange(N)
			board[row][column] = True

		# Find any squares.
		try:
			for i, row in enumerate(board):
				for j, column in enumerate(row):
					if board[i][j]:
						for sideLen in range(1, min(N - i, N - j)):
							if board[i + sideLen][j] and board[i][j + sideLen] and board[i + sideLen][j + sideLen]:
								raise SquareFound()
		except SquareFound:
			continue

		frozenBoard = tuple(tuple(row) for row in board)
		if frozenBoard not in solutions:
			# Print the board on one line.
			print('|'.join(''.join('X' if board[row][column] else '.' for column in range(N)) for row in range(N)))
			solutions.add(frozenBoard)

class SquareFound(Exception):
	pass

if __name__ == '__main__':
	main()

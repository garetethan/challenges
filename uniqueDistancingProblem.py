'''
My attempt to solve the Unique Distancing Problem by Matt Parker.
https://www.youtube.com/watch?v=M_YOCQaI5QI

I do not attempt to eliminate reflections or rotations from the list of solutions.
'''

from math import sqrt
from random import randrange

N = 6
ROUNDS = 10 ** 6

def main():
	solutions = set()
	for _ in range(ROUNDS):
		tokenPositions = set()
		# Place tokens randomly.
		for _ in range(N):
			row = randrange(N)
			column = randrange(N)
			while (row, column) in tokenPositions:
				row = randrange(N)
				column = randrange(N)
			tokenPositions.add((row, column))
		
		# Find the distances between all of the tokens.
		distances = set()
		try:
			for position in tokenPositions:
				for other in tokenPositions:
					if position < other:
						distance = sqrt((position[0] - other[0]) ** 2 + (position[1] - other[1]) ** 2)
						if distance in distances:
							raise DistancesEqual()
						else:
							distances.add(distance)
		except DistancesEqual:
			continue

		# Print if new solution.
		if tokenPositions not in solutions:
			print('|'.join(''.join('X' if (row, column) in tokenPositions else '.' for column in range(N)) for row in range(N)))
			solutions.add(frozenset(tokenPositions))
	
	print(f'{len(solutions)} solutions found.')

class DistancesEqual(Exception):
	pass

if __name__ == '__main__':
	main()

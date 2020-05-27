# https://open.kattis.com/problems/trik

def main():
	moves = input()
	position = 1
	for move in moves:
		if move == 'A':
			if position == 1:
				position = 2
			elif position == 2:
				position = 1
		elif move == 'B':
			if position == 2:
				position = 3
			elif position == 3:
				position = 2
		# move is C
		else:
			if position == 1:
				position = 3
			elif position == 3:
				position = 1

	print(position)

if __name__ == '__main__':
	main()

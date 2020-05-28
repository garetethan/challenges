# https://redd.it/cn6gz5
# No bonuses attempted.

from morseCodeMapping import MORSE
from trees import Node

def main():
	encoded = input()
	current = Node.root(('', encoded))
	while current.data[1]:
		startIndex = ord(current.children[-1].data[0][-1]) - ord('a') + 1 if current.children else 0
		for encoding, char in MORSE[startIndex:]:
			if current.data[1].startswith(encoding) and char not in current.data[0]:
				current = current.addChild((current.data[0] + char, current.data[1][len(encoding):]))
				break
		else:
			current = current.parent
	print(current.data[0])

if __name__ == '__main__':
	main()

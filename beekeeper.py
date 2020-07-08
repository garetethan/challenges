'''
My solution to Beekeeper by Nicholas Sharp.
https://open.kattis.com/problems/beekeeper
'''

import re

def main():
	# Get input.
	cases = []
	n = int(input())
	while n:
		words = set()
		for i in range(n):
			words.add(input())
		cases.append(words)
		n = int(input())
	
	for case in cases:
		bestCount = 0
		bestWord = ''
		for word in case:
			count = sum(1 for match in re.finditer(r'([aeiouy])\1', word))
			if count > bestCount:
				bestCount = count
				bestWord = word
		print(bestWord)
	
if __name__ == '__main__':
	main()

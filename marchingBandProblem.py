'''
My solution to the Marching Band Problem by Matt Parker, using a prime factorization implementation I found online (https://stackoverflow.com/a/22808285/5231183).
http://think-maths.co.uk/marchingband
https://www.youtube.com/watch?v=5GZ5IqxAt30
'''

from math import ceil, sqrt

RECTANGLE_COUNT_TARGET = 64

def main():
	i = RECTANGLE_COUNT_TARGET
	rectangleCount = countRectangles(i)
	while rectangleCount < RECTANGLE_COUNT_TARGET:
		i += 1
		rectangleCount = countRectangles(i)
	print(f'{i} band players allows {rectangleCount} different configurations.')

def countRectangles(n):
	'''Return the number of ways n objects can be arranged in a rectangle (counting different orientations). Eg 12 has 6 ways: 1 × 12, 2 × 6, 3 × 4, 4 × 3, 6 × 2, and 12 × 1. Squares (eg 2 × 2 for 4) are counted once.'''
	if not isinstance(n, int) or n <= 0:
		raise ValueError(f'Unable to factorize {n}.')
	# 1 × n and n × 1 must be valid rectangles.
	factorPairCount = 2
	for i in range(2, ceil(sqrt(n))):
		if n % i == 0:
			# i and n / i are both factors.
			factorPairCount += 2
	if sqrt(n) % 1 == 0:
		factorPairCount += 1
	return factorPairCount

if __name__ == '__main__':
	main()

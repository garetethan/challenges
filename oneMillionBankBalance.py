'''
My solution to the 1 Million Bank Balance Puzzle by Matt Parker.
https://www.think-maths.co.uk/BankBalance
https://www.youtube.com/watch?v=ILrqPpLpwpE
'''

TARGET = 10 ** 6
MAX = 3000
failures = 0

for i in range(1, MAX + 1):
	for j in range(1, MAX + 1):
		lastBalance = i
		balance = j
		days = 2
		while balance < TARGET:
			newBalance = lastBalance + balance
			lastBalance = balance
			balance = newBalance
			days += 1

		if balance == TARGET:
			print(f'Score: {days}. Starting pair: ({i}, {j}).')
		else:
			failures += 1

print(f'Failures: {failures}.')

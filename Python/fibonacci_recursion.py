# Return n fibonacci numbers. Use recursion (do not use iteration).
# Fibonacci series: Sum of previous 2 numbers...
# e.g. 0 1 1 2 3 5 8 13 21 34 55 89 144 233
def fibonacci(n, a = 0, b = 1, fibs = [0]):
	if(len(fibs) >= n):
		print(fibs)
		return fibs
	else:
		c = a + b
		fibs.append(c)
		a = b
		b = c
		fibonacci(n, a, b, fibs)

fibonacci(11)

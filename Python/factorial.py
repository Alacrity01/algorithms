# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(9)
 

# factorial of 9  -> factorial(9)
# prod = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 
# return prod

# def factorial(n, prod=0):
def factorial(n, sum=0):
	if n == 1:
		return sum

		# prod = prod * n-1
		# factorial(n-1, prod)
	if sum == 0:
		sum = n
	
	sum = sum * n-1
	n -= 1
	factorial(n, sum)

print(factorial(5))

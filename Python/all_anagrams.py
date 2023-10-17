#  Permutations with Repetition: n^r


#  Permutations without Repetition: n!
def factorial(str):	# without recursion
	x = len(str)
	n = x - 1
	while n > 0:
		x *= n
		n -= 1

	return(x)

# str = "melodiependras"
# str = "Tom Marvolo Riddle"

# print(factorial(str))


def check(s1,s2):
	s1 = s1.replace(" ","")
	s2 = s2.replace(" ","")
	s1 = sorted(s1.casefold())
	s2 = sorted(s2.casefold())
	if s1 == s2:
		print("these are anagrams")
	else:
		print("these are not anagrams")


s1 = "Tom Marvolo Riddle"
s2 = "I am Lord Voldemort"
check(s1,s2)
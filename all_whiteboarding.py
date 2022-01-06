#*************************** Whiteboarding Questions 1 ***************************
# # Easy:
# 1. Write a method that returns an array of every number from 1 to 100. 
def a100():
	return list(range(1,101))
# print(a100())

# 2. Write a method that returns an array of every other number from 1 to 100. (That is, 1, 3, 5, 7 … 99).
def odds100():
	return list(range(1,100,2))
# print(odds100())

# 3. Write a method that returns an array of all numbers from 1 to 1000 that are divisible by 3.
def mults_of_3():
	return list(a for a in range(1,1001) if a % 3 == 0)
# print(mults_of_3())

# 4. Write a method that accepts one argument - an array of numbers - and returns an array of all numbers from that original array that are greater than 7. For example, if the input is [5, 8, 1, 7, 9, 10], the function should return [8, 9, 10].
def greater_7(nums):
	return list(a for a in nums if a > 7)
# test_arr = [5, 8, 1, 7, 9, 10]
# print(greater_7(test_arr))

# 5. Write a method that accepts an array of numbers as a parameter, and returns the number of how many 55’s there are in the array. For example, if the input is [55, 4, 7, 55, 9, 1, 55, 2, 3, 55, 0], the output should be 4. NOTE: DO NOT USE RUBY’s built-in “count” method.

# 6. Write a method that accepts an array of numbers and returns the sum of the numbers. For example, if the input is [1, 5, 7, 9, 2, 0], the output should be 24. Don’t use any of the built in “sum” methods that Ruby comes with.

# Medium:
# 1. Write a method that accepts an array and returns it as a hash. For example, [“a”, “b”, “c] should turn into {0 => “a”, 1 => “b”, 2 => “c”}

# 2. Write a method that accepts a string and returns whether it’s a palindrome. (without using the reverse method)

# Advanced:
# 1. Write a method to generate/print/store the first "n" prime numbers.

# 2. Given an array of randomly sorted numbers, write a method that sorts them in descending order (without using any sort function built into the language.)

# 3. Given a tic-tac-toe board (matrix of 3 x 3), write a method that can check to see whether X or O won.




#*************************** Whiteboarding Questions 2 ***************************
# 1.	Be sure to follow the process outlined in the Whiteboarding cheat sheet!
# 2.	After you’ve written your code, identify how many steps your algorithm takes relative to N.

# i.	Write a function that accepts an array of strings and returns a new array containing every other string from the original array. For example, if the input is [“a”, “b”, “c”, “d”, “e”, “f”], the output should be [“a”, “c”, “e”].

# ii.	Write a method that accepts an array of strings and returns a new array that has the string “awesomesauce” inserted between every string. For example, if the initial array is [“a”, “b”, “c”, “d”, “e”], then the returned array should be [“a”, “awesomesauce”, “b”,  “awesomesauce”, “c”,  “awesomesauce”, “d”,  “awesomesauce”, “e”].

# iii.	Write a method that accepts one argument - an array of numbers. The method should return the greatest number. For example, if the input is [5, 4, 8, 1, 2], the output should be 8.

# iv.	Write a method that accepts a number and returns its factorial. For example, the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.

# v.	Write a method that accepts one argument - an array of numbers that are in ascending order. The method that returns a new array with the same values in descending order. However, do not use the “reverse” method built in to Ruby.

# vi.	Write a method that accepts two arrays of numbers, and returns an array of every sum of every combination of single numbers from first and second array. For example, if the method receives [1, 5, 10] and [100, 500, 1000], the method should return this array: [101, 501, 1001, 105, 505, 1005, 110, 510, 1010].

# Bonus: Research recursive functions. Then solve the factorial question using recursion instead of a loop!

# (If you're done early, here are some more array questions, some are fairly difficult: http://javarevisited.blogspot.com/2015/06/top-20-array-interview-questions-and-answers.html)

# *************************** Whiteboarding Questions 3 ***************************
# A.	Be sure to follow the process outlined in the Whiteboarding cheat sheet!
# B.	Everyone should pair up to take turns whiteboarding the following problems and identifying the efficiency of each algorithm in terms of Big O Notation.

# 1. Write a function that reverses a string. Don’t use the “reverse” method!

# 2. Write a function that accepts a string and returns the number of times that the letter “a” occurs in it.

# 3. Write a method that accepts two arguments. The first argument is an array of numbers that are in ascending order. The second argument is a number to search for within in the array. The method should do a linear search and return the index at which this value is found, or it should return nil if the value is not found. See if there’s a way in which you can optimize this method to keep its number of steps to a minimum! Note: Do not use the “index” method!

# 4. Write a method that accepts two arguments. The first argument is an array of numbers that are in ascending order. The second argument is a new number that is not yet in the array. The method should return a new array with the new number inserted in the proper place. Do not use the “sort” method!

# 5. Write a method that accepts two arguments. The first argument is an array of numbers that are in ascending order. The second argument is a number that is contained within the array. The method should return the string “lower” if the value is found in the lower half of the array, and it should return “higher” if the value is found within the greater half of the array. Try to optimize this algorithm so that it takes a minimum number of steps!

# 6. Work on this one together: Write a method that does binary search. Specifically, it should accept two arguments. The first argument is an array of numbers that are in ascending order. The second argument is a number that may or may not be contained within the array. The method should perform binary search to find the index at which this second value is found within the array. If the value cannot be found within the array, the method should return nil. 

# 7. Write a method that accepts two arrays, and returns a new array that does a “riffle shuffle” between them. That is, if the first array is [1, 3, 5, 7, 9], and the second array is [10, 8, 6, 4, 2], the returned array should be [1, 10, 3, 8, 5, 6, 7, 4, 9, 2].

# BONUS: Read about and implement the following sorting algorithms that sort an array of numbers. Be sure to identify the Big O efficiency of each algorithm! 
# * Bubble sort
# * Insertion sort
# * Selection sort
# * Merge sort
# * Quick sort
# * Heap sort 

# *************************** Whiteboarding Questions 4 ***************************
# Everyone should pair up to take turns whiteboarding the following problems and identifying the efficiency of each algorithm in terms of Big O Notation. (Take turns on doing each one.)

# 1. Write a function that accepts an array as a parameter and returns true or false depending on whether there are any duplicate values. Use the *nested loops approach* as described in the slides.

# 2.  Write a function that accepts an array as a parameter and returns true or false depending on whether there are any duplicate values. Use the *hash approach* as described in the slides.

# 3. Write a method that accepts a string as a parameter and returns an array containing each character as a separate value, but the character must also be capitalized.

# 4. Write a method that accepts an array of numbers and returns the sum of all odd numbers.

# 5. (If you didn’t get to it last week) Write a method that accepts two arrays, and returns a new array that does a “riffle shuffle” between them. That is, if the first array is [1, 3, 5, 7, 9], and the second array is [2, 4, 6, 8, 10], the returned array should be [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

# BONUS: You can use your computer for this last section. Read about and implement the following sorting algorithms that sort an array of numbers. Be sure to identify the Big O efficiency of each algorithm! 
# * Bubble sort
# * Insertion sort
# * Selection sort
# * Merge sort
# * Quick sort
# * Heap sort 


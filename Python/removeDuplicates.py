
# 26. Remove Duplicates from Sorted Array
# Easy
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }

# def removeDuplicates(nums):  # Not in place solution, will fail judge's test
#     nums = list({n: True for (n) in nums}.keys())
#     print(nums)
#     return len(nums)

# def removeDuplicates(nums):  # in place solution, very slow
#     i = len(nums)-1
#     while i >= 0:
#         a = nums.index(nums[i])
#         if i != a:
#             nums.pop(i)
#         i -= 1
#     # print(nums)
#     return len(nums)

def removeDuplicates(nums):  # Optimal solution: Time beats 74.4%, memory beats 97.5%
    keys = list({n: True for (n) in nums}.keys())
    i = 0
    for k in keys:
        nums[i] = k
        i += 1
    r = len(nums) - len(keys)
    x = len(nums) - 1
    for i in range(r):
        nums.pop(x)
        x -= 1
    return len(nums)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums))

nums = [1, 1, 2]
print(removeDuplicates(nums))

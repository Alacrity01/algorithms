# https://leetcode.com/problems/rotate-array/
# 189. Rotate Array
    # Medium
    # Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
        # Example 1:
            # Input: nums = [1,2,3,4,5,6,7], k = 3
            # Output: [5,6,7,1,2,3,4]
            # Explanation:
            # rotate 1 steps to the right: [7,1,2,3,4,5,6]
            # rotate 2 steps to the right: [6,7,1,2,3,4,5]
            # rotate 3 steps to the right: [5,6,7,1,2,3,4]
        # Example 2:
            # Input: nums = [-1,-100,3,99], k = 2
            # Output: [3,99,-1,-100]
            # Explanation: 
            # rotate 1 steps to the right: [99,-1,-100,3]
            # rotate 2 steps to the right: [3,99,-1,-100]
        
        # Constraints:
        # 1 <= nums.length <= 105
        # -231 <= nums[i] <= 231 - 1

    # Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
    # Could you do it in-place with O(1) extra space?

def rotateArray(nums, k): # Solution 1: Runtime Beats 93.41%, Memory Beats 48.67% of users with Python3
    base = len(nums)
    for i in range(base):
        nums.append(nums[(i - k) % base])
    del nums[:base]

# def rotateArray(nums, k): # Solution 2: Time limit exceeded on large test case
#     base = len(nums)
#     d = {i+1:nums[(i-k) % base] for i in range(base)}
#     for i in range(base):
#         nums[i] = list(d.values())[i]

def rotateArray(nums, k): # Solution 3
    base = len(nums)
    [nums.append(nums[(i - k) % base]) for i in range(base)]
    del nums[:base]
    # [print(i) for i in range(base)]

nums = [1,2,3,4,5,6,7]; k = 3
rotateArray(nums,k)
print(nums)

nums = [-1,-100,3,99]; k = 2
rotateArray(nums,k)
print(nums)

nums = [-1]; k = 2
rotateArray(nums,k)
# print(nums)


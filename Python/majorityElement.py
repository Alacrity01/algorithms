# https://leetcode.com/problems/majority-element/
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# Efficiency: Runtime Beats 85.28%, Memory Beats 42.34% of users with Python3
def majorityElement(nums):
    d = {n: 0 for n in nums}
    for k, v in d.items():
        d[k] = nums.count(k)

    maj = max(d, key=d.get)
    return maj


nums = [3, 2, 3]
print(majorityElement(nums))

nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))

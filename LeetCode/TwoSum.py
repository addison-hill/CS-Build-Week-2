"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # Understand - find values that add to target. Return indexes
#         # Plan
#         # loop through list
#         # val = target - nums[i]
#         # if val in nums:
#         # return (i, nums.index(val))
#         for i in range(0, len(nums)):
#             val = target - nums[i]
#             if val in nums[:i:]:
#                 return [i, nums.index(val)]

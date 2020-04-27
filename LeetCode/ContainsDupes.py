"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
Input: [1,2,3,1]
Output: true

Input: [1,2,3,4]
Output: false
"""

# Linear Search - loop through nums see if there is a dupe -- fails time limit
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            if nums.count(num) > 1:
                return True
            
        return False
"""

# Creating a cache, still has for loop -- fails time limit
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        cache = []
        for i in nums:
            if i not in cache:    
                cache.append(i)
            else:
                return True
        
        return False
"""

# Sorting will allow the duplicates to be right next to each other so loop through nums if nums[i] == nums[i+1] return true -- PASS
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
"""

# sets do not contain duplicates so if len(set(nums)) < len(nums) there is a dupe!! -- PASS

"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) < len(nums):
            return True
        else:
            return False

"""

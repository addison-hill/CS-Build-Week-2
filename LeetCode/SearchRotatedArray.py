"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Understand - search thru list find target value in Ologn time
        # Plan - Binary Search!
        # initiate a start pointer and end pointer
        # take the mid index and if target = mid return mid
        # if target is located in non-rotated array go left: end = mid - 1 else go right
        # then do binary search again
        # keep cutting it in half until eventually your mid will equal the target
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[end]:  # Left side of mid is sorted
                if nums[start] <= target and target < nums[mid]:  # Target in the left side
                    end = mid - 1
                else:  # in right side
                    start = mid + 1
            else:  # Right side is sorted
                if nums[mid] < target and target <= nums[end]:  # Target in the right side
                    start = mid + 1
                else:  # in left side
                    end = mid - 1
        return -1

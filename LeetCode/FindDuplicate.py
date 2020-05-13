class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Understand - given an array of nums containing n +1 integers, where each integer is between 1 and n inclusive. Prove there is a duplicate. There will be a dupe because there are more spaces in the array then integers to place in the array so has to be a dupe.

        # Plan - cant modify the array so you cant sort :(
        # Loop thru array, if count is greater than 1 return that num -- passes but can do better
        # for i in nums:
        # if nums.count(nums[i]) > 1:
        # return nums[i]

        # Use a set such as visited to check each element and return if one is already in - passes good speed
        visited = set()
        for i in nums:
            if i in visited:
                return i
            visited.add(i)

        # Cycle detection - Tortiose and Hare
        # Given a linked list, return the node where the cycle begins
        # f(x) = nums[x]
        # each new element in the sequence is an elemetn in nums at the index of the previous element
        # the duplicate node is a cycle entrance
        # given array [2, 6, 4, 1, 3, 1, 5]
        """
        start from 2
        nums[2] = 4
        nums[4] = 3
        nums[3] = 1 --- CYCLE
        nums[1] = 6
        nums[6] = 5
        nums[5] = 1 --- CYCLE
        """
        # so we need to find the intersection point of the two runners
        # and then find the entrance to the cycle
#         tortoise = hare = nums[0]
#         while True:
#             tortoise = nums[tortoise]
#             hare = nums[nums[hare]]
#             if tortoise == hare:
#                 break

#             # find the entrance to the cycle
#             tortoise = nums[0]
#             while tortoise != hare:
#                 tortoise = nums[tortoise]
#                 hare = nums[hare]

#             return hare

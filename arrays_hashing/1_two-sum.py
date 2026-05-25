
"""
Problem: 1. Two Sum
Pattern: Hash Map
Difficulty: Easy

Key Idea:
- Store visited numbers in a hashmap
- Check if complement already exists
- Return indices immediately once found

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def twoSum(self, nums, target):
        index = {}

        for i, num in enumerate(nums):
            n = target - num

            if n in index:
                return [index[n], i]

            index[num] = i
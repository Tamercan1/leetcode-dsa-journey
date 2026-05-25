
"""
Problem: 1. Contains Duplicate
Pattern: Hash Map, Array
Difficulty: Easy

Key Idea:
- Store visited numbers in a hashmap
- Check if complement already exists
- Return True if already exist

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
        
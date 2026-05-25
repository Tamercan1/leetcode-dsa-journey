"""
Problem: 704. Binary Search
Pattern: Binary Search
Difficulty: Easy

Key Idea:
- Compare middle element with target
- Eliminate half of the search space
- Repeat until target found or pointers cross

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

        
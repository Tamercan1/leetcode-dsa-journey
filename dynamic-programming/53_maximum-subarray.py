"""
Problem: 53. Maximum Subarray
Pattern: Kadane’s Algorithm / Dynamic Programming
Difficulty: Medium

Key Idea:
- Track the current subarray sum
- If current sum becomes negative, reset it
- A negative sum would only hurt future subarrays
- Continuously update the maximum subarray sum found

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def maxSubArray(self, nums):
        
        max_sum = nums[0]
        curr_sum = 0

        for num in nums:

            if curr_sum < 0:
                curr_sum = 0
            
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
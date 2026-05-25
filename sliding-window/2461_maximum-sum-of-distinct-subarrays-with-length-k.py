"""
Problem: 2461. Maximum Sum of Distinct Subarrays With Length K
Pattern: Fixed Sliding Window
Difficulty: Medium

Key Idea:
- Maintain window of size k
- Track distinct elements using hashmap/set
- Update maximum sum if all elements are distinct

Time Complexity: O(n)
Space Complexity: O(k)
"""

class Solution(object):
    def maximumSubarraySum(self, nums, k):
        left = 0
        arr_sum = 0
        max_sum = 0
        seen = set()

        for r in range(len(nums)):
            
            while nums[r] in seen:
                seen.remove(nums[left])
                arr_sum -= nums[left]
                left += 1

            seen.add(nums[r])
            arr_sum += nums[r]

            if r - left + 1 == k:
                max_sum = max(max_sum, arr_sum)
                seen.remove(nums[left])
                arr_sum -= nums[left]
                left += 1

        return max_sum

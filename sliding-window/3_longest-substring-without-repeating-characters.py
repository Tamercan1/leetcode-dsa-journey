"""
Problem: 3. Longest Substring Without Repeating Characters
Pattern: Sliding Window
Difficulty: Medium

Key Idea:
- Expand window while characters are unique
- Shrink window when duplicate appears
- Track maximum window size

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        left = 0
        seen = set()
        length = 0

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            length = max(length, right - left + 1)
        
        return length
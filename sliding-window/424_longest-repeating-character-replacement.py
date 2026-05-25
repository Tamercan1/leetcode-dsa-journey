"""
Problem: 424. Longest Repeating Character Replacement
Pattern: Sliding Window
Difficulty: Medium

Key Idea:
- Track most frequent character in window
- Window is valid if replacements needed <= k
- Shrink window when invalid

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        left = 0
        freq = Counter()
        
        ans = 0
        max_freq = 0

        for right in range(len(s)):
            
            freq[s[right]] += 1

            max_freq = max(max_freq, freq[s[right]])

            while not (right - left + 1) - max_freq <= k:
                freq[s[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans
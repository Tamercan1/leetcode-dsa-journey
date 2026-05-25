"""
Problem: 242. Valid Anagram
Pattern: Hash Map / Frequency Count
Difficulty: Easy

Key Idea:
- Count frequency of characters
- Compare both frequency maps
- Strings are anagrams if counts match

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False

        freq_s = {}
        freq_t = {}

        for i in range(len(s)):
            freq_s[s[i]] = freq_s.get(s[i], 0) + 1
            freq_t[t[i]] = freq_t.get(t[i], 0) + 1
            
        for ch in freq_s:
            if freq_s[ch] != freq_t.get(ch, 0): 
                return False

        return True

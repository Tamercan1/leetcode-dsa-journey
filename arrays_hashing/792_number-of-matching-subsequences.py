"""
Problem: 121. Best Time to Buy and Sell Stock
Pattern: Sliding Window / Two Pointers
Difficulty: Easy

Key Idea:
- Track minimum buying price
- Calculate profit at each step
- Keep maximum profit found

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        pos = defaultdict(list)

        for i, ch in enumerate(s):
            pos[ch].append(i)
        
        def is_valid(word):

            prev = -1

            for ch in word:

                if ch not in pos:
                    return False

                lst = pos[ch]

                j = bisect.bisect_right(lst, prev)

                if j == len(lst):
                    return False
                
                prev = lst[j]
            
            return True
        
        return sum(is_valid(w) for w in words)
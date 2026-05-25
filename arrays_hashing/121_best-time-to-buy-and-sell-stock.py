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
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        max_profit = 0
        buy = prices[0]

        for i in range(1, len(prices)):
            
            if prices[i] < buy:
                buy = prices[i]

            current_profit = prices[i] - buy
            max_profit = max(max_profit, current_profit)

        return max_profit
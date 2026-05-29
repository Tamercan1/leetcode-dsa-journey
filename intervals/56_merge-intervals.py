"""
Problem: 56. Merge Intervals
Pattern: Intervals / Sorting + Greedy
Difficulty: Medium

Key Idea:
- Sort intervals by start time
- Keep a "previous interval" tracker
- If current interval overlaps with previous:
  → merge them by updating end boundary
- If no overlap:
  → push previous to result and move forward
- Always ensure last interval is added at the end

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort()
        
        result = []
        prev = intervals[0]

        for i in range(1, len(intervals)):

            current = intervals[i]

            if prev[1] < current[0]:
                result.append(prev)
                prev = current
            else:
                prev = [min(prev[0], current[0]), max(prev[1], current[1])]
        
        result.append(prev)
        return result

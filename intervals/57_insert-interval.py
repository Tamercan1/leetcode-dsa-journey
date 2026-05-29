"""
Problem: 57. Insert Interval
Pattern: Intervals / Greedy
Difficulty: Medium

Key Idea:
- Traverse intervals in order
- Three cases:
  1. Current interval is completely before newInterval
     → add it to result
  2. Current interval is completely after newInterval
     → insert newInterval and return remaining intervals
  3. Overlapping intervals
     → merge by updating newInterval boundaries
- Return final merged list

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        result = []

        for i in range(len(intervals)):

            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            
        result.append(newInterval)
        return result
        
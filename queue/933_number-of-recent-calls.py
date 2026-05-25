"""
Problem: 933. Number of Recent Calls
Pattern: Queue
Difficulty: Easy

Key Idea:
- Store request timestamps in queue
- Remove timestamps older than 3000ms
- Queue size represents valid requests

Time Complexity: O(1) amortized
Space Complexity: O(n)
"""

from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.q = deque()

    def ping(self, t):
        self.q.append(t)

        while self.q and self.q[0] < t - 3000:
            self.q.popleft()

        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
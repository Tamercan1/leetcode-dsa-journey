import heapq

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        q = []
        result = []

        for x, y in points:
            dist = (x**2) + (y**2)
            q.append([dist, x, y])
        
        heapq.heapify(q)

        for _ in range(k):
            dist, x, y = heapq.heappop(q)
            result.append([x, y])

        return result

# Another short solution

class Solution(object):
    def kClosest(self, points, k):
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        return points[:k]

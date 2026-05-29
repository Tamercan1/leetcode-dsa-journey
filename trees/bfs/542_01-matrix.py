"""
Problem: 542. 01 Matrix (Update Matrix)
Pattern: Multi-source BFS (Graph / Grid)
Difficulty: Medium

Key Idea:
- Treat all 0 cells as starting points (multi-source BFS)
- Initialize queue with all 0 positions
- Mark all 1s as unvisited (-1)
- Expand level by level using BFS
- First time reaching a cell guarantees shortest distance
- Update distance = previous cell distance + 1

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

from collections import deque

class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        
        rows, cols = len(mat), len(mat[0])
        q = deque()

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    q.append((row, col))
                else:
                    mat[row][col] = -1

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if mat[nr][nc] == -1:
                        mat[nr][nc] = mat[r][c] + 1
                        q.append((nr, nc))

        return mat
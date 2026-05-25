"""
Problem: 200. Number of Islands
Pattern: DFS / Graph Traversal
Difficulty: Medium

Key Idea:
- Traverse connected land cells
- Mark visited cells
- Count connected components

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        islands = 0
        len_rows = len(grid)
        len_cols = len(grid[0])

        def dfs(row, col):

            if row < 0 or row >= len_rows or col < 0 or col >= len_cols:
                return
            
            if grid[row][col] == "0": return

            grid[row][col] = "0"

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for i in range(len_rows):
            for j in range(len_cols):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)

        return islands
        
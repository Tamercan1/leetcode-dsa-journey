"""
Problem: 733. Flood Fill
Pattern: DFS / Graph Traversal
Difficulty: Easy

Key Idea:
- Traverse connected cells
- Avoid revisiting
- Change color during traversal

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        origcolor = image[sr][sc]
        
        if origcolor == color: return image

        len_rows = len(image)
        len_cols = len(image[0])

        def fill(row, col):

            if row < 0 or row >= len_rows or col < 0 or col >= len_cols:
                return

            if image[row][col] != origcolor:
                return

            image[row][col] = color

            fill(row, col + 1)
            fill(row, col - 1)
            fill(row + 1, col)
            fill(row - 1, col)

        fill(sr, sc)

        return image
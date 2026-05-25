"""
Problem: 102. Binary Tree Level Order Traversal
Pattern: Tree BFS
Difficulty: Medium

Key Idea:
- Use queue for level-by-level traversal
- Process nodes layer by layer
- Store values for each level separately

Time Complexity: O(n)
Space Complexity: O(n)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque

class Solution(object):
    def levelOrder(self, root):
        ans = []

        if root is None:
            return ans

        q = deque()
        q.append(root)

        while q:
            level = []

            for _ in range(len(q)):
                pop = q.popleft()
                level.append(pop.val)

                if pop.left: q.append(pop.left)
                if pop.right: q.append(pop.right)

            ans.append(level)

        return ans

        
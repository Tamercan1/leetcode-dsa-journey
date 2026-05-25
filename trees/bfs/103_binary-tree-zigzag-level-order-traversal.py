"""
Problem: 103. Binary Tree Zigzag Level Order Traversal
Pattern: Tree BFS
Difficulty: Medium

Key Idea:
- Perform level-order traversal
- Alternate traversal direction each level
- Reverse values when needed

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
    def zigzagLevelOrder(self, root):
        ans = []

        if root is None: return ans

        q = deque([root])
        ltr = True

        while q:
            level = deque()

            for _ in range(len(q)):
                pop = q.popleft()
                if ltr:
                    level.append(pop.val)
                else:
                    level.appendleft(pop.val)

                if pop.left: q.append(pop.left)
                if pop.right: q.append(pop.right)

            ans.append(list(level))
            ltr = not ltr

        return ans

        
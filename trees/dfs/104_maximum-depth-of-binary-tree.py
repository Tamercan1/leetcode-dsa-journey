"""
Problem: 104. Maximum Depth of Binary Tree
Pattern: Tree DFS (Recursion)
Difficulty: Easy

Key Idea:
- Depth of a node = 1 + max(depth of left subtree, depth of right subtree)
- Use post-order recursion (left → right → root)
- Base case: null node has depth 0

Time Complexity: O(n)
Space Complexity: O(h) where h = height of tree (recursion stack)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)
        
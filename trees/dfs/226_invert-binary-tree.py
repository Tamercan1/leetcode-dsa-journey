"""
Problem: 226. Invert Binary Tree
Pattern: Tree DFS
Difficulty: Easy

Key Idea:
- Swap left and right children
- Recursively traverse subtrees
- DFS traversal naturally processes all nodes

Time Complexity: O(n)
Space Complexity: O(h)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        if not root:
            return None

        self.invertTree(root.left)
        self.invertTree(root.right)

        temp = root.left
        root.left = root.right
        root.right = temp

        return root

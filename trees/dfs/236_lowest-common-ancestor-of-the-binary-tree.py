"""
Problem: 235. Lowest Common Ancestor of the Binary Tree
Pattern: Tree DFS
Difficulty: Medium

Key Idea:
- Traverse the tree recursively using DFS
- If current node is p or q, return it immediately
- Recursively search left and right subtrees
- If both left and right return non-null values,
  the current node is the Lowest Common Ancestor
- If only one side returns a node,
  propagate that node upward

Time Complexity: O(n)
Space Complexity: O(h)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if root is None:
            return None
        
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        
        return left if left else right
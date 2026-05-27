"""
Problem: 235. Lowest Common Ancestor of the Binary Search Tree
Pattern: Tree DFS
Difficulty: Medium

Key Idea:
- Use BST property to guide traversal
- If both p and q are smaller than current,
  move left
- If both p and q are greater than current,
  move right
- Otherwise, current node splits p and q,
  making it the Lowest Common Ancestor

Time Complexity: O(n)
Space Complexity: O(1)
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
        
        current = root

        while current:
            
            if p.val < current.val and q.val < current.val:
                current = current.left
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else:
                return current
"""
Problem: 617. Merge Two Binary Trees
Pattern: Tree DFS (Recursion) / Tree Construction
Difficulty: Easy

Key Idea:
- Recursively merge corresponding nodes from both trees
- If one node is null, return the other node
- Otherwise:
  - sum the values
  - recursively merge left children
  - recursively merge right children

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
    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        def merge(p, q):
            
            if not p: return q
            if not q: return p

            p.left = merge(p.left, q.left)
            p.right = merge(p.right, q.right)

            p.val += q.val

            return p
        
        return merge(root1, root2)
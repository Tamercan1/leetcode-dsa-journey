# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(root):

            if root is None:
                return [True, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)

            isbal = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            height = 1 + max(left[1], right[1])

            return [isbal, height]

        return dfs(root)[0]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True
        def tree_height(node):
            nonlocal ans
            if not node:
                return 0
            left = tree_height(node.left)
            right = tree_height(node.right)
            if abs(left - right) > 1:
                ans = False
            return max(left, right) + 1
        tree_height(root)
        return ans
        
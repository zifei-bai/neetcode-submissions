# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # ans = True
        def tree_height(node):
            # nonlocal ans
            if not node:
                return 0
            left = tree_height(node.left)
            if left == -1:
                return -1
            right = tree_height(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        # tree_height(root)
        return tree_height(root) != -1
        
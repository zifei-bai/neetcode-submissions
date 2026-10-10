# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def f(node):
            nonlocal ans
            if not node:
                return -1
            left_h = f(node.left) + 1
            right_h = f(node.right) + 1
            ans = max(ans, left_h + right_h)
            return max(left_h, right_h)
        f(root)
        return ans
        
        
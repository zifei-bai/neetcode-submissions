# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if root == p:
            return root
        if root == q:
            return root
        
        left_report = self.lowestCommonAncestor(root.left, p, q)
        right_report = self.lowestCommonAncestor(root.right, p, q)

        if left_report and right_report:
            return root
        if left_report and (not right_report):
            return left_report
        if right_report and (not left_report):
            return right_report
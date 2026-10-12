# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 比较两棵树是否完全相同
        def same(node, sub):
            if node is None or sub is None:
                return node is None and sub is None

            return (
                node.val == sub.val
                and same(node.left, sub.left)
                and same(node.right, sub.right)
            )

        # 在大树里寻找匹配起点
        def search(node):
            if node is None:
                return False

            return (
                same(node, subRoot)
                or search(node.left)
                or search(node.right)
            )

        if subRoot is None:
            return True

        return search(root)
        


               
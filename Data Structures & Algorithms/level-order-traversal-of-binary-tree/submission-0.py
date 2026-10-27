# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = deque([root])
        res = []
        if not root:
            return res
        while dq:
            level_len = len(dq)
            sub_list = []
            for i in range(level_len):
                node = dq.popleft()
                sub_list.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(sub_list)
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        dq = deque()
        dq.append(root)
        ans = []
        if not root:
            return ans
        while len(dq) != 0:
            level_size = len(dq)
            for i in range(level_size):
                popped = dq.popleft()
                if popped.left:
                    dq.append(popped.left)
                if popped.right:
                    dq.append(popped.right)
                if i == level_size - 1:
                    ans.append(popped.val)
        return ans
            
            

        
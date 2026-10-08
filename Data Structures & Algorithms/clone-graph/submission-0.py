"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldNew = {}
        if not node:
            return None
        def dfs(nd):
            if nd in oldNew:
                return oldNew[nd]
            copy = Node(nd.val)
            oldNew[nd] = copy
            for nei in nd.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        return dfs(node)

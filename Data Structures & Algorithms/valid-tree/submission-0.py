class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        visited = set()
        isTree = True

        def dfs(parent, vertex):
            nonlocal isTree
            visited.add(vertex)
            for u in g[vertex]:
                if u in visited:
                    if u != parent:
                        isTree = False
                        return
                else:
                    dfs(vertex, u)

        dfs(None, 0)

        return isTree and len(visited) == n

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        visited = set()
        
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        def bfs(vertex):
            dq = deque([vertex])
            while dq:
                node = dq.popleft()
                visited.add(node)
                for vx in g[node]:
                    if vx not in visited:
                        dq.append(vx)
        
        count = 1
        bfs(0)
        # print(visited, len(visited))
        while len(visited) < n:
            for x in range(n):
                if x not in visited:
                    bfs(x)
                    break
            count += 1
        return count
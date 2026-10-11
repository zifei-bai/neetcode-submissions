class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        g = [[] for _ in range(n)]

        for u, v in edges:
            g[u-1].append(v)
            g[v-1].append(u)
        
        def check_connect(vertex):
            visited = set([vertex])
            dq = deque([vertex])
            # visited.add(vertex)
            while dq:
                node = dq.popleft()
                for vx in g[node-1]:
                    if vx not in visited:
                        dq.append(vx)
                        visited.add(vx)
                        
            # print(len(visited) == n)
            return len(visited) == n

        for u, v in reversed(edges):
            index_u = g[v-1].index(u)
            index_v = g[u-1].index(v)
            del g[v-1][index_u]
            del g[u-1][index_v]
            if check_connect(1):
                return [u, v]
            else:
                g[v-1].append(u)
                g[u-1].append(v)
 
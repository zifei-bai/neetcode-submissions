class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v in connections:
            g[u].append((v, 1))
            g[v].append((u, 0))

        dq = deque([0])
        visited = set([0])
        flipped = 0
        while dq:
            curr_node = dq.popleft()
            for nei in g[curr_node]:
                if nei[0] in visited:
                    continue
                flipped += nei[1]
                visited.add(nei[0])
                dq.append(nei[0])

        return flipped

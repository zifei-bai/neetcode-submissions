class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        g = [[] for _ in range(len(points))]
        for i in range(len(points)):
            x = points[i]
            for j in range(i + 1, len(points)):
                y = points[j]
                g[i].append((abs(x[0] - y[0]) + abs(x[1] - y[1]), j))
                g[j].append((abs(x[0] - y[0]) + abs(x[1] - y[1]), i))
        
        visited = set()
        start = 0
        heap = []
        ans = 0
        visited.add(start)
        for w, vx in g[start]:
            heapq.heappush(heap, (w, vx))
        while heap:
            wei, vertex = heapq.heappop(heap)
            if vertex not in visited:
                visited.add(vertex)
                ans += wei
                for w, nei in g[vertex]:
                    heapq.heappush(heap, (w, nei))
        return ans

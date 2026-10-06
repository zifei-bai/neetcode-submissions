class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[] for _ in range(n)]
        for t in times:
            g[t[0]-1].append((t[1], t[2]))
        dist = [float("inf")] * n
        dist[k-1] = 0
        heap = [(0, k)]
        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node-1]:
                continue
            else:
                for x, w in g[node-1]:
                    nd = d + w
                    if nd < dist[x-1]:
                        dist[x-1] = nd
                        heapq.heappush(heap, (nd, x))
        if any(x == float("inf") for x in dist):
            return -1
        return max(dist)

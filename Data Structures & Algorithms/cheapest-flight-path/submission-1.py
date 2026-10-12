class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        cost = [INF] * n
        cost[src] = 0
        for _ in range(k + 1):
            nxt = cost[:]
            for u, v, w in flights:
                if cost[u] != INF:
                    nxt[v] = min(nxt[v], cost[u] + w)
            cost = nxt
        print(cost)
        return cost[dst] if cost[dst] != INF else -1
        
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0] * n
        for u, v in edges:
            indegree[v] += 1
        champion = []
        for i, x in enumerate(indegree):
            if x == 0:
                champion.append(i)
        return champion[0] if len(champion) == 1 else -1
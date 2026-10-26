from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        out_deg = [0] * len(graph)
        reverse_graph = [[] for _ in range(len(graph))]
        for i, out_nodes in enumerate(graph):
            for u in out_nodes:
                out_deg[i] += 1
                reverse_graph[u].append(i)
        
        safe_nodes  = []
        for i, deg in enumerate(out_deg):
            if deg == 0:
                safe_nodes.append(i)
        
        # visited = set(safe_nodes)
        # print(visited)
        dq = deque(safe_nodes)
        while dq:
            curr_node = dq.popleft()
            for v in reverse_graph[curr_node]:
                out_deg[v] -= 1
                if out_deg[v] == 0:
                    dq.append(v)
        ans = []
        for i, x in enumerate(out_deg):
            if x == 0:
                ans.append(i)
        return ans

        
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])
        
        starts = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    starts.append((r, c))
        # print(starts)
        if len(starts) == 0:
            return
        def bfs(starts):
            dq = deque(starts)
            visited = set(starts[0])
            while dq:
                node_r, node_c = dq.popleft()
                # print(node)
                for ur, uc in directions:
                    if node_r+ur < 0 or node_r+ur >= rows or node_c+uc < 0 or node_c+uc >= cols:
                        continue
                    if (node_r+ur, node_c+uc) in visited:
                        continue
                    else:
                        grid[node_r+ur][node_c+uc] = min(
                            grid[node_r][node_c] + 1, 
                            grid[node_r+ur][node_c+uc])
                        visited.add((node_r+ur, node_c+uc))
                        if grid[node_r+ur][node_c+uc] != -1:
                            dq.append((node_r+ur, node_c+uc))
        
        bfs(starts)
        
        


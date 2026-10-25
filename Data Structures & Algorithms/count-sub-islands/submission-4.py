class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        rows = len(grid2)
        cols = len(grid2[0])
        num_island = 0
        for i in range(rows):
            for j in range(cols):
                if (i, j) in visited or grid2[i][j] == 0:
                    continue
                valid = True
                num_island += 1
                dq = deque([(i, j)])
                visited.add((i, j))
                while dq:
                    r, c = dq.popleft()
                    if grid1[r][c] == 0:
                        valid = False
                    for ur, uc in directions:
                        nr = r + ur
                        nc = c + uc
                        if not (0 <= nr < rows and 0 <= nc < cols) or (nr, nc) in visited:
                            continue
                        visited.add((nr, nc))
                        if grid2[nr][nc] == 1:
                            dq.append((nr, nc))
                if not valid:
                    num_island -= 1

        return num_island                
                
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def dfs(r, c):
            nonlocal temp
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] == 0:
                return
            if grid[r][c] == 1:
                temp += 1
                grid[r][c] = 0
                for nr, nc in directions:
                    dfs(r+nr, c+nc)

        for r in range(rows):
            for c in range(cols):
                temp = 0
                dfs(r, c)
                ans = max(ans, temp)
        return ans
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        reachable = [[[False, False] for _ in range(cols)] for _ in range(rows)]
      
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        ans = []
        def dfs(r, c, ocean):
            if reachable[r][c][ocean]:
                return
            reachable[r][c][ocean] = True

            for ur, uc in directions:
                new_r, new_c = r + ur, c + uc
                if not (0 <= new_r < rows and 0 <= new_c < cols):
                    continue
                if heights[new_r][new_c] < heights[r][c]:
                    continue
                dfs(new_r, new_c, ocean)
        
        for r in range(rows):
            dfs(r, 0, 0)
            dfs(r, cols - 1, 1)
        for c in range(cols):
            dfs(0, c, 0)
            dfs(rows - 1, c, 1)
        ans = []
        for r in range(rows):
            for c in range(cols):
                if reachable[r][c] == [True, True]:
                    ans.append([r, c])
        return ans


            


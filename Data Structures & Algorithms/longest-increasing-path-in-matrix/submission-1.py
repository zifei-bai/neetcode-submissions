from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        @cache
        def dfs(r, c):
            longest = 1
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            curr_height = matrix[r][c]
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    neighbor_height = matrix[nr][nc]
                    if neighbor_height - curr_height > 0:
                        longest = max(longest, 1 + dfs(nr, nc))
            return longest
        
        ans = max(
            dfs(r, c)
            for r in range(rows)
            for c in range(cols)
        )
        return ans
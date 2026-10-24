from collections import deque
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def bfs(r, c):

            if grid[r][c] == 0:
                return 0

            visited = set()
            dq = deque([(r, c)])
            max_fish = grid[r][c]
            visited.add((r, c))
            while dq:
                r, c = dq.popleft()
                for ur, uc in directions:
                    if not (0 <= r + ur < rows) or not (0 <= c + uc < cols):
                        continue
                    elif (r + ur, c + uc) in visited:
                        continue
                    elif grid[r + ur][c + uc] == 0:
                        visited.add((r + ur, c + uc))
                        continue
                    else:
                        max_fish += grid[r + ur][c + uc]
                        visited.add((r + ur, c + uc))
                        dq.append((r + ur, c + uc))
            return max_fish
        
        ans = 0
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, bfs(i, j))
                # print(f'{i}, {j}, bfs: {ans}')
        return ans

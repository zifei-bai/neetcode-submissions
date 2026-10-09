class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        rottens = []
        visited = set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rottens.append((r, c))
                    visited.add((r, c))
                if grid[r][c] == 0:
                    visited.add((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        if len(rottens) == 0:
            if fresh == 0:
                return 0
            else:
                return -1
        dq = deque(rottens)
        count = 0
        num_ro = len(dq)
        while dq:
            if num_ro == 0:
                num_ro = len(dq)
                count += 1
            ro_banana_r, ro_banana_c = dq.popleft()
            num_ro -= 1
            for ur, uc in directions:
                new_r, new_c = ro_banana_r + ur, ro_banana_c + uc
                if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                   continue
                if (new_r, new_c) in visited:
                    continue
                else:
                    if grid[new_r][new_c] == 1:
                        grid[new_r][new_c] == 2
                        dq.append((new_r, new_c))
                        visited.add((new_r, new_c))
        
        if len(visited) < rows * cols:
            return -1
        return count

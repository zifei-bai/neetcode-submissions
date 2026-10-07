class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        sub_w = ""
        rows = len(board)
        cols = len(board[0])
        visited = set()
        def dfs(r, c):
            nonlocal sub_w
            if (r, c) in visited:
                return
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if sub_w + board[r][c] == word:
                return True
            if sub_w + board[r][c] == word[:len(sub_w)+1]:
                sub_w = sub_w + board[r][c]
                visited.add((r, c))
                for nr, nc in directions:
                    if dfs(r+nr, c+nc):
                        return True
                sub_w = sub_w[:-1]
                visited.remove((r, c))
            else:
                return
        
        for r in range(rows):
            for c in range(cols):
                ans = dfs(r, c)
                if ans:
                    return True
        return False
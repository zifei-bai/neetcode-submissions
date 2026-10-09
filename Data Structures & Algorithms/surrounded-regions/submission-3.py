class Solution:
    def solve(self, board: List[List[str]]) -> None:
        starts = set()
        rows = len(board)
        cols = len(board[0])
        for r in range(rows):
            if board[r][0] == 'O':
                starts.add((r, 0))
            if board[r][cols - 1] == 'O':
                starts.add((r, cols - 1))
        for c in range(cols):
            if board[0][c] == 'O':
                starts.add((0, c))
            if board[rows - 1][c] == 'O':
                starts.add((rows - 1, c))

        starts = list(starts)
        # if len(starts) == 0:
        #     return
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def dfs(r, c):
            
            board[r][c] = '#'
            for ur, uc in directions:
                new_r, new_c = r + ur, c + uc
                if not (0 <= new_r < rows and 0 <= new_c < cols):
                    continue
                if board[new_r][new_c] == 'X':
                    continue
                if board[new_r][new_c] == '#':
                    continue
                else:
                    dfs(new_r, new_c)

        for r, c in starts:
            dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == '#':
                    board[r][c] = 'O'
        


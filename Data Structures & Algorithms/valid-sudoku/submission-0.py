class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        boxes = defaultdict(list)
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == '.':
                    continue
                else:
                    rows[row].append(board[row][col])
                    cols[col].append(board[row][col])
                    if row < 3:
                        if col < 3:
                            boxes[0].append(board[row][col])
                        elif col >= 3 and col < 6:
                            boxes[1].append(board[row][col])
                        else:
                            boxes[2].append(board[row][col])
                    elif row >=3 and row < 6:
                        if col < 3:
                            boxes[3].append(board[row][col])
                        elif col >= 3 and col < 6:
                            boxes[4].append(board[row][col])
                        else:
                            boxes[5].append(board[row][col])
                    else:
                        if col < 3:
                            boxes[6].append(board[row][col])
                        elif col >= 3 and col < 6:
                            boxes[7].append(board[row][col])
                        else:
                            boxes[8].append(board[row][col])

        for k, v in rows.items():
            set_v = set(v)
            if len(set_v) != len(v):
                return False
        for k, v in cols.items():
            set_v = set(v)
            if len(set_v) != len(v):
                return False
        for k, v in boxes.items():
            set_v = set(v)
            if len(set_v) != len(v):
                return False
        return True

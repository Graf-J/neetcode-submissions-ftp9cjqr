class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for row_idx in range(len(board)):
            for col_idx in range(len(board)):
                value = board[row_idx][col_idx]
                if value == '.':
                    continue

                if value in rows[row_idx]:
                    return False
                if value in cols[col_idx]:
                    return False
                if value in boxes[row_idx // 3][col_idx // 3]:
                    return False

                rows[row_idx].add(value)
                cols[col_idx].add(value)
                boxes[row_idx // 3][col_idx // 3].add(value)

        return True
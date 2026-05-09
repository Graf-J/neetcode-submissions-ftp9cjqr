class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = [0] * 9, [0] * 9, [[0] * 3 for _ in range(3)]
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                # Check if number already exists in row, column or box
                b = 1 << int(board[r][c])
                if (
                    rows[r] & b or
                    cols[c] & b or
                    boxes[r // 3][c // 3] & b
                ):
                    return False

                # Update state
                rows[r] |= b
                cols[c] |= b
                boxes[r // 3][c // 3] |= b

        return True

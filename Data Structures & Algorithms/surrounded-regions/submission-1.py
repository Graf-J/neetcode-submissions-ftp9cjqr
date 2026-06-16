# Like with previous Problem -> Sometimes it is smarter to thing "the other way round"

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        safe = set()

        def dfs(row, col):
            if (
                row < 0 or row == ROWS or
                col < 0 or col == COLS or
                board[row][col] == "X" or
                (row, col) in safe
            ):
                return

            safe.add((row, col))
            for nr, nc in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                dfs(nr, nc)

        for row in range(ROWS):
            for col in range(COLS):
                if (
                    row == 0 or row == ROWS - 1 or
                    col == 0 or col == COLS - 1
                ) and board[row][col] == "O":
                    dfs(row, col)

        for row in range(1, ROWS - 1):
            for col in range(1, COLS - 1):
                if board[row][col] == "O" and (row, col) not in safe:
                    board[row][col] = "X"


        

            

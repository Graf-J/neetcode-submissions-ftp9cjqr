class Solution:
    def set_row_attacked(self, attacked, row, val):
        for i in range(len(attacked)):
            attacked[row][i] += val

    def set_col_attacked(self, attacked, col, val):
        for row in attacked:
            row[col] += val

    def set_pos_diag_attacked(self, attacked, row, col, val):
        # Move up
        ctr = 0
        while row - ctr >= 0 and col + ctr < len(attacked):
            attacked[row - ctr][col + ctr] += val
            ctr += 1

        # Move down
        ctr = 0
        while row + ctr < len(attacked) and col - ctr >= 0:
            attacked[row + ctr][col - ctr] += val
            ctr += 1

    def set_neg_diag_attacked(self, attacked, row, col, val):
        # Move up
        ctr = 0
        while row - ctr >= 0 and col - ctr >= 0:
            attacked[row - ctr][col - ctr] += val
            ctr += 1

        # Move down
        ctr = 0
        while row + ctr < len(attacked) and col + ctr < len(attacked):
            attacked[row + ctr][col + ctr] += val
            ctr += 1

    def update_attacked(self, attacked, row, col, val):
        self.set_row_attacked(attacked, row, val)
        self.set_col_attacked(attacked, col, val)
        self.set_pos_diag_attacked(attacked, row, col, val)
        self.set_neg_diag_attacked(attacked, row, col, val)
        attacked[row][col] -= 5 * val


    def solveNQueens(self, n: int) -> List[List[str]]:
        # Explore all valid Boards
        result = []
        def dfs(row: int, attacked: List[List[int]], path: List[Tuple[int, int]]) -> None:
            if row == len(attacked):
                result.append(path.copy())
                return

            for col, is_field_attacked in enumerate(attacked[row]):
                if not is_field_attacked:
                    self.update_attacked(attacked, row, col, 1)
                    path.append((row, col))
                    dfs(row + 1, attacked, path)
                    self.update_attacked(attacked, row, col, -1)
                    path.pop()

        dfs(0, [[0 for _ in range(n)] for _ in range(n)], [])

        # Construct Final Boards
        valid_boards = []
        for path in result:
            board = ["."*n for _ in range(n)]
            for queen_row, queen_col in path:
                board[queen_row] = board[queen_row][:queen_col] + "Q" + board[queen_row][queen_col+1:]
            valid_boards.append(board)

        return valid_boards


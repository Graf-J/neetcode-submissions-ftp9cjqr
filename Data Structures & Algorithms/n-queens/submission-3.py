class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]
        cols, diag_pos, diag_neg = set(), set(), set()
        def dfs(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col not in cols and row + col not in diag_pos and row - col not in diag_neg:
                    cols.add(col)
                    diag_pos.add(row + col)
                    diag_neg.add(row - col)
                    board[row][col] = "Q"
                    dfs(row + 1)
                    cols.remove(col)
                    diag_pos.remove(row + col)
                    diag_neg.remove(row - col)
                    board[row][col] = "."

        dfs(0)
        return result



# 0, 1, 2, 3
# 1, 2, 3, 4
# 2, 3, 4, 5
# 3, 4, 5, 6

# 0, -1, -2, -3
# 1,  0, -1, -2
# 2,  1,  0, -1
# 3,  2,  1,  0

# [0, 0], [0, 1], [0, 2], [0, 3]
# [1, 0], [1, 1], [1, 2], [1, 3]
# [2, 0], [2, 1], [2, 2], [2, 3]
# [3, 0], [3, 1], [3, 2], [3, 3]




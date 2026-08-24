import sys
sys.setrecursionlimit(10000)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        is_first_row_zero = any(matrix[0][c] == 0 for c in range(COLS))
        is_first_col_zero = any(matrix[r][0] == 0 for r in range(ROWS))

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if is_first_row_zero:
            for c in range(COLS):
                matrix[0][c] = 0

        if is_first_col_zero:
            for r in range(ROWS):
                matrix[r][0] = 0
        
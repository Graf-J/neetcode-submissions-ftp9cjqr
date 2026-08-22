class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        for i in range(ROWS):
            for j in range(COLS):
                matrix[i][j] = None if matrix[i][j] == 0 else matrix[i][j]

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] is not None:
                    continue

                for row in range(ROWS):
                    matrix[row][j] = None if matrix[row][j] is None else 0
                for col in range(COLS):
                    matrix[i][col] = None if matrix[i][col] is None else 0

        for i in range(ROWS):
            for j in range(COLS):
                matrix[i][j] = 0 if matrix[i][j] is None else matrix[i][j]
        
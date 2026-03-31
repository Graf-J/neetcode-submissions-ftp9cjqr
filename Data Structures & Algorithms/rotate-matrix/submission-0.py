class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Transpose Matrix
        for row_idx in range(0, len(matrix) - 1):
            for col_idx in range(1 + row_idx, len(matrix)):
                temp = matrix[row_idx][col_idx]
                matrix[row_idx][col_idx] = matrix[col_idx][row_idx]
                matrix[col_idx][row_idx] = temp

        # Switch Columns
        left_col_idx = 0
        right_col_idx = len(matrix) - 1
        while left_col_idx < right_col_idx:
            for row_idx in range(len(matrix)):
                temp = matrix[row_idx][left_col_idx]
                matrix[row_idx][left_col_idx] = matrix[row_idx][right_col_idx]
                matrix[row_idx][right_col_idx] = temp
            
            # Move Cursors
            left_col_idx += 1
            right_col_idx -= 1

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) * len(matrix[0])
        while l < r:
            m = (l + r) // 2
            row, col = m // len(matrix[0]), m % len(matrix[0])
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = m + 1
            else:
                r = m
        return False
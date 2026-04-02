class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        dim_0, dim_1 = len(matrix), len(matrix[0])
        l, r = 0, (dim_0 * dim_1) - 1
        while l <= r:
            m = l + (r - l) // 2
            row = m // dim_1
            col = m % dim_1

            if target < (element := matrix[row][col]):
                r = m - 1
            elif target > element:
                l = m + 1
            else:
                return True

        return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width, height = len(matrix[0]), len(matrix)
        l, r = 0, width * height
        while l < r:
            m = (l + r) // 2
            row, col = m // width, m % width
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = m + 1
            else:
                r = m

        return False


# [
#     [1,  2,  4,  8],
#     [10, 11, 12, 13],
#     [14, 20, 30, 40]
# ]
# target = 10

# width = 4
# height = 3

# l = 4
# r = 5

# m = 4
# row = 1
# col = 0

# -> 10
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top_idx = 0
        bottom_idx = len(matrix) - 1
        left_idx = 0
        right_idx = len(matrix[0]) - 1

        result = []
        while top_idx <= bottom_idx and left_idx <= right_idx:
            for idx in range(left_idx, right_idx + 1):
                result.append(matrix[top_idx][idx])

            for idx in range(top_idx + 1, bottom_idx + 1):
                result.append(matrix[idx][right_idx])

            if bottom_idx - top_idx > 0:
                for idx in range(right_idx - 1, left_idx - 1, -1):
                    result.append(matrix[bottom_idx][idx])

            if right_idx - left_idx > 0:
                for idx in range(bottom_idx - 1, top_idx, -1):
                    result.append(matrix[idx][left_idx])

            # Update Indices
            top_idx += 1
            bottom_idx -= 1
            left_idx += 1
            right_idx -= 1

        return result

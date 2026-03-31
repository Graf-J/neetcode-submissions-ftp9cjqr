class Solution:
    def trap(self, height: List[int]) -> int:
        max_right = height[-1]
        max_right_vals = deque([max_right])
        for i in range(2, len(height) + 1):
            max_right = max(height[-i], max_right)
            max_right_vals.appendleft(max_right)

        result = 0
        max_left = height[0]
        for i in range(1, len(height)):
            result += max(0, min(max_left, max_right_vals[i]) - height[i])
            max_left = max(height[i], max_left)

        return result
        
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for current_idx, current_height in enumerate(heights):
            iterated = False
            while len(stack) > 0 and current_height < stack[-1][1]:
                iterated = True
                left_idx, left_height = stack.pop()
                max_area = max(max_area, left_height * (current_idx - left_idx))

            if iterated:
                stack.append((left_idx, current_height))
            else:
                stack.append((current_idx, current_height))

        while len(stack) > 0:
            idx, height = stack.pop()
            max_area = max(max_area, height * (len(heights) - idx))

        return max_area
from collections import namedtuple

Rect = namedtuple("Rect", ["start", "height"])

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_rect = 0
        stack = []
        for idx, height in enumerate(heights):
            # If current height is bigger than top of stack
            if not stack or height > stack[-1].height:
                stack.append(Rect(idx, height))

            # If current height is smaller than top of stack
            last_start = None
            while stack and height < stack[-1].height:
                rect = stack.pop()
                max_rect = max(max_rect, (idx - rect.start) * rect.height)
                last_start = rect.start

            if last_start is not None:
                stack.append(Rect(last_start, height))
        
        # Cleanup Stack
        for rect in stack:
            max_rect = max(max_rect, (len(heights) - rect.start) * rect.height)

        return max_rect

            
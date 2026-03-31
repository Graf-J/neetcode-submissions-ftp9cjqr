class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, 1
        total_area = 0
        area = 0
        while r < len(height):
            if height[r] < height[l]:
                area += height[l] - height[r]
                r += 1
            else:
                total_area += area
                area = 0
                l = r
                r = l + 1

        area = 0
        r -= 1
        n = r - 1
        while n > l:
            if height[n] < height[r]:
                area += height[r] - height[n]
                n -= 1
            else:
                total_area += area
                area = 0
                r = n
                n = r - 1

        return total_area + area

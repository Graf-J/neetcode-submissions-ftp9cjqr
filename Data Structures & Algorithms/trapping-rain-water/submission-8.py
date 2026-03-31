class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        while l < r:
            if height[l] < height[r]:
                l += 1
                max_l = max(height[l], max_l)
                result += max_l - height[l]
            else:
                r -= 1
                max_r = max(height[r], max_r)
                result += max_r - height[r]
        
        return result
        
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        while l < r:
            if height[l] < height[r]:
                l += 1
                value = min(max_l, max_r) - height[l]
                water += max(0, value)
                max_l = max(height[l], max_l)
            else:
                r -= 1
                value = min(max_l, max_r) - height[r]
                water += max(0, value)
                max_r = max(height[r],max_r)
        
        return water
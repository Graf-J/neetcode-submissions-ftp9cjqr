class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [height[0]]
        for i in range(1, len(height)):
            prefix.append(max(height[i], prefix[-1]))

        postfix = [0] * (len(height) - 1) + [height[-1]]
        for i in range(len(height) - 2, -1, -1):
            postfix[i] = max(height[i], postfix[i + 1])

        trapped_water = 0
        for i in range(len(height)):
            trapped_water += min(prefix[i], postfix[i]) - height[i]

        return trapped_water
        
        

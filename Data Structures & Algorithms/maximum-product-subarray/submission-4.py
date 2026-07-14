class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [None] * len(nums)
        dp[len(nums) - 1] = (nums[-1], nums[-1])
        for i in range(len(nums) - 2, -1, -1):
            dp[i] = (
                min(nums[i], nums[i] * dp[i + 1][0], nums[i] * dp[i + 1][1]),
                max(nums[i], nums[i] * dp[i + 1][0], nums[i] * dp[i + 1][1]),
            )

        return max(x[1] for x in dp)
        



# nums = [2, 4, -3, 5]

#                         O
#         2           4           -3      5
#         2*4         4*(-3)      -3*5    x     
#         2*4*(-3)    4*(-3)*5     x
#         2*4*(-3)*5  x
#         x


# dp = [None, None, None, (5, 5)]
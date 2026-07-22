class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = [[0] * len(nums) for _ in range(len(nums))]
        for l in range(len(nums) - 2, 0, -1):
            for r in range(l, len(nums) - 1):
                for i in range(l, r + 1):
                    dp[l][r] = max(dp[l][r], dp[l][i-1] + nums[l-1]*nums[i]*nums[r+1] + dp[i+1][r])

        return dp[1][len(nums) - 2]






# dp[l][r] = (
#     max
#     for i in range(l, r + 1):
#         max(max, dp[l][i - 1] + nums[l-1] * nums[i] * nums[r + 1] + dp[i + 1][r])
# )


# nums = [1 | 4, 2, 3, 7 | 1]


# # Base Case
#     r:d r:0 r:1 r:2 r:3 r:d
# l:d    
# l:0  0   
# l:1  0   0
# l:2  0   0   0
# l:3  0   0   0   0
# l:d  0   0   0   0   0


# DP: Bottom-Up
class Solution:
    def jump(self, nums: List[int]) -> int:
        target = len(nums) - 1
        dp = [float("inf")] * len(nums)
        dp[target] = 0
        for i in range(target - 1, -1, -1):
            end = min(i + nums[i] + 1, len(nums))
            current_min = float("inf")
            for i_next in range(i + 1, end):
                current_min = min(current_min, dp[i_next])
            dp[i] = 1 + current_min

        return dp[0]



# dp[i] = 1 + min(dp[i + 1], ..., dp[i + nums[i]])

#      [2,4,1,1,1,1]
# dp = [0,0,0,0,0,0]
# dp = [2,1,3,2,1,0]







#                             (0)
#             (1)                             (2)
# (2)     (3)     (4)     (5)                 (3)
#                                             (4)
#                                             (5)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if target > total or target < -total:
            return 0

        dp = [[0] * (2 * total + 1) for _ in range(len(nums) + 1)]
        dp[-1][target + total] = 1
        for i in range(len(nums) - 1, -1, -1):
            for s in range(2 * total + 1):
                left = dp[i + 1][s + nums[i]] if s + nums[i] < (2 * total + 1) else 0
                right = dp[i + 1][s - nums[i]] if s - nums[i] >= 0 else 0
                dp[i][s] = left + right

        return dp[0][total]



# dp[i][s] = dp[i + 1][s + num] + dp[i + 1][s - num]


#     -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6  (s)
# 0:2        1          3       3         
# 1:2              1        2       1
# 2:2                   1       1
# d                         1
# (i)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total:
            return 0

        dp = [0] * (2 * total + 1)
        dp[target + total] = 1
        for i in range(len(nums) - 1, -1, -1):
            dp_next = [0] * (2 * total + 1)
            for s in range(2 * total + 1):
                left = dp[s + nums[i]] if s + nums[i] < (2 * total + 1) else 0
                right = dp[s - nums[i]] if s - nums[i] >= 0 else 0
                dp_next[s] = left + right
            dp = dp_next

        return dp[total]



# dp[i][s] = dp[i + 1][s + num] + dp[i + 1][s - num]


#     -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6  (s)
# 0:2        1          3       3         
# 1:2              1        2       1
# 2:2                   1       1
# d                         1
# (i)
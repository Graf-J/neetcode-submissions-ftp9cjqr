class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for r in range(target, num - 1, -1):
                dp[r] |= dp[r - num]

        return dp[target]

###############
## Optimized ##
###############
# Only keep right-most array which is enough since we only need i + 1 and nothing further to the right

# nums = [1,2,3,4]

# dp[remaining][i] = dp[remaining][i + 1] or dp[remaining - nums[i]][i + 1]
# Can handle remaining with numbers at i or later = (
#     Can handle remaining with numbers at i + 1 or later (if can handle later I can also handle here) or
#     If I add the current number at i than at i + 1 I have to be able to handle remaining - 1 to solve problem
# )

#     0  1  2  3    (i)
# 0   F  F  F  F    (dummy to make indexing easy)
# 1   ?  ?  ?  F
# 2   ?  ?  ?  F
# 3   ?  ?  ?  F
# 4   T  T  T  T
# 5   ?  ?  ?  F

# (r remaining)